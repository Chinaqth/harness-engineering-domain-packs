#!/usr/bin/env python3
"""Create a draft Domain Pack through a staged, rollback-safe registration."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

DOMAIN_ID = re.compile(r"^[a-z0-9][a-z0-9-]*(\.[a-z0-9][a-z0-9-]*)+$")


class RegistrationError(ValueError):
    """Raised when a Domain cannot be registered safely."""


def _load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistrationError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RegistrationError(f"Expected a JSON object in {path}")
    return value


def _write_json(path: Path, value: dict) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _replace_markdown_tokens(path: Path, values: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    for token, value in values.items():
        text = text.replace(token, value)
    path.write_text(text, encoding="utf-8")


def _prepare_domain(
    domain_path: Path,
    domain_id: str,
    display_name: str,
    owner: str,
    description: str,
) -> None:
    values = {
        "{{DOMAIN_ID}}": domain_id,
        "{{DISPLAY_NAME}}": display_name,
        "{{OWNER}}": owner,
        "{{DESCRIPTION}}": description,
    }
    for markdown in domain_path.rglob("*.md"):
        _replace_markdown_tokens(markdown, values)

    manifest = _load_json(domain_path / "domain.json")
    manifest.update(
        {
            "id": domain_id,
            "display_name": display_name,
            "description": description,
            "owner": owner,
        }
    )
    _write_json(domain_path / "domain.json", manifest)

    routes = _load_json(domain_path / "routes.json")
    routes["domain_id"] = domain_id
    _write_json(domain_path / "routes.json", routes)

    capabilities = _load_json(domain_path / "capabilities.json")
    capabilities["domain_id"] = domain_id
    _write_json(domain_path / "capabilities.json", capabilities)

    owners = _load_json(domain_path / "owners.json")
    owners["domain_id"] = domain_id
    owners["primary_owner"] = owner
    _write_json(domain_path / "owners.json", owners)

    for json_path in domain_path.rglob("*.json"):
        _load_json(json_path)


def _remove_empty_parents(path: Path, stop: Path) -> None:
    while path != stop and stop in path.parents:
        try:
            path.rmdir()
        except OSError:
            return
        path = path.parent


def register_domain(
    root: Path,
    domain_id: str,
    display_name: str,
    owner: str,
    description: str,
    dry_run: bool = False,
) -> Path:
    root = root.resolve()
    registry_path = root / "registry" / "domains.json"
    domains_root = root / "domains"
    template_path = domains_root / "_template"

    if not DOMAIN_ID.fullmatch(domain_id):
        raise RegistrationError(
            "Domain ID must contain two or more lowercase dotted segments; "
            "example: engineering.ios"
        )
    normalized = {
        "display name": display_name.strip(),
        "owner": owner.strip(),
        "description": description.strip(),
    }
    for label, value in normalized.items():
        if not value:
            raise RegistrationError(f"{label.capitalize()} cannot be empty")
    for label in ("display name", "owner"):
        if "\n" in normalized[label] or "\r" in normalized[label]:
            raise RegistrationError(f"{label.capitalize()} must be a single line")
    if not registry_path.is_file() or not template_path.is_dir():
        raise RegistrationError(
            "The root must contain registry/domains.json and domains/_template/"
        )

    registry = _load_json(registry_path)
    entries = registry.get("domains")
    if registry.get("schema_version") != "1.0" or not isinstance(entries, list):
        raise RegistrationError("registry/domains.json has an unsupported structure")

    domain_path = domains_root / Path(*domain_id.split("."))
    if domain_path.exists():
        raise RegistrationError(f"Domain path already exists: {domain_path}")
    if any(entry.get("id") == domain_id for entry in entries if isinstance(entry, dict)):
        raise RegistrationError(f"Domain ID is already registered: {domain_id}")

    relative_path = domain_path.relative_to(root).as_posix()
    entry = {
        "id": domain_id,
        "path": relative_path,
        "version": "0.1.0",
        "status": "draft",
        "owner": normalized["owner"],
    }
    next_registry = dict(registry)
    next_registry["domains"] = sorted([*entries, entry], key=lambda item: item["id"])

    if dry_run:
        print(f"Would create {relative_path}/")
        print(f"Would register {domain_id} as draft version 0.1.0")
        return domain_path

    registry_temp: Path | None = None
    moved_domain = False
    try:
        with tempfile.TemporaryDirectory(prefix=".register-", dir=domains_root) as stage_root:
            staged_domain = Path(stage_root) / "domain"
            shutil.copytree(template_path, staged_domain)
            _prepare_domain(
                staged_domain,
                domain_id,
                normalized["display name"],
                normalized["owner"],
                normalized["description"],
            )

            descriptor, temp_name = tempfile.mkstemp(
                prefix=".domains-", suffix=".json", dir=registry_path.parent
            )
            os.close(descriptor)
            registry_temp = Path(temp_name)
            _write_json(registry_temp, next_registry)
            _load_json(registry_temp)

            domain_path.parent.mkdir(parents=True, exist_ok=True)
            staged_domain.replace(domain_path)
            moved_domain = True
            os.replace(registry_temp, registry_path)
            registry_temp = None
    except (OSError, RegistrationError) as exc:
        if moved_domain and domain_path.exists():
            shutil.rmtree(domain_path)
        _remove_empty_parents(domain_path.parent, domains_root)
        if registry_temp and registry_temp.exists():
            registry_temp.unlink()
        if isinstance(exc, RegistrationError):
            raise
        raise RegistrationError(f"Registration was rolled back: {exc}") from exc

    print(f"Created {relative_path}/")
    print(f"Registered {domain_id} as draft version 0.1.0")
    return domain_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--id", required=True, dest="domain_id")
    parser.add_argument("--display-name", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    try:
        register_domain(
            args.root,
            args.domain_id,
            args.display_name,
            args.owner,
            args.description,
            args.dry_run,
        )
    except RegistrationError as exc:
        print(f"Registration failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
