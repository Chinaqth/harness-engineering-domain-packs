#!/usr/bin/env python3
"""Activate a content-complete draft Domain Pack as one rollback-safe transaction."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import tempfile
from pathlib import Path


class FinalizationError(ValueError):
    """Raised when a Domain Pack cannot be activated safely."""


def _load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise FinalizationError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise FinalizationError(f"Expected a JSON object in {path}")
    return value


def _load_pack_checker(root: Path):
    path = root / ".agents" / "skills" / "evaluate-domain-pack" / "scripts" / "check_pack.py"
    spec = importlib.util.spec_from_file_location("domain_pack_finalization_check", path)
    if spec is None or spec.loader is None:
        raise FinalizationError(f"Cannot load Pack checker from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _load_session_validator(root: Path):
    path = root / ".agents" / "skills" / "complete-domain-pack" / "scripts" / "validate_session.py"
    spec = importlib.util.spec_from_file_location("domain_pack_finalization_session", path)
    if spec is None or spec.loader is None:
        raise FinalizationError(f"Cannot load session validator from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _serialize(value: dict) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def _replace_bytes(path: Path, value: bytes) -> None:
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def finalize_domain(
    root: Path,
    domain_id: str,
    ledger: Path,
    session: Path,
    dry_run: bool = False,
) -> Path:
    root = root.resolve()
    registry_path = root / "registry" / "domains.json"
    registry = _load_json(registry_path)
    entries = [
        item
        for item in registry.get("domains", [])
        if isinstance(item, dict) and item.get("id") == domain_id
    ]
    if len(entries) != 1:
        raise FinalizationError(f"Expected exactly one registry entry for {domain_id}")

    domain_path = root / str(entries[0].get("path", ""))
    manifest_path = domain_path / "domain.json"
    manifest = _load_json(manifest_path)
    if entries[0].get("status") != "draft" or manifest.get("status") != "draft":
        raise FinalizationError("Automatic finalization accepts only synchronized draft Packs")

    resolved_session = session.resolve() if session.is_absolute() else (root / session).resolve()
    session_result = _load_session_validator(root).validate_session(
        root, resolved_session, require_final=True
    )
    if not session_result.get("valid"):
        issues = session_result.get("issues") or []
        raise FinalizationError(
            "Completion session is not final and passing: "
            + "; ".join(str(item) for item in issues)
        )

    checker = _load_pack_checker(root)
    result = checker.check_pack(root, domain_id, ledger)
    if result.get("content_state") != "content-complete" or result.get("verdict") != "pass":
        issues = result.get("content_issues") or result.get("issues") or []
        raise FinalizationError(
            "Domain Pack is not content-complete: " + "; ".join(str(item) for item in issues)
        )

    next_registry = json.loads(json.dumps(registry))
    next_entry = next(
        item for item in next_registry["domains"] if item.get("id") == domain_id
    )
    next_entry["status"] = "active"
    next_manifest = dict(manifest)
    next_manifest["status"] = "active"

    if dry_run:
        print(f"Would activate {domain_id} in registry and manifest")
        return domain_path

    original_registry = registry_path.read_bytes()
    original_manifest = manifest_path.read_bytes()
    try:
        _replace_bytes(manifest_path, _serialize(next_manifest))
        _replace_bytes(registry_path, _serialize(next_registry))
    except Exception as exc:
        rollback_errors: list[str] = []
        for path, value in (
            (manifest_path, original_manifest),
            (registry_path, original_registry),
        ):
            try:
                _replace_bytes(path, value)
            except Exception as rollback_exc:
                rollback_errors.append(f"{path}: {rollback_exc}")
        suffix = f"; rollback errors: {rollback_errors}" if rollback_errors else ""
        raise FinalizationError(f"Activation was rolled back: {exc}{suffix}") from exc

    print(f"Activated {domain_id}; registry and manifest now report active")
    return domain_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--domain-id", required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--session", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        finalize_domain(
            args.root, args.domain_id, args.ledger, args.session, args.dry_run
        )
    except FinalizationError as exc:
        print(f"Finalization failed: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
