#!/usr/bin/env python3
"""Create a draft Domain Pack from the canonical repository template."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

DOMAIN_ID = re.compile(r"^[a-z0-9][a-z0-9-]*(\.[a-z0-9][a-z0-9-]*)+$")


class RegistrationError(ValueError):
    """Raised when a Domain cannot be registered safely."""


def _load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistrationError(f"Cannot read valid JSON from {path}: {exc}") from exc


def _replace_tokens(path: Path, values: dict[str, str]) -> None:
    if not path.is_file() or path.name == ".gitkeep":
        return
    text = path.read_text(encoding="utf-8")
    for token, value in values.items():
        text = text.replace(token, value)
    path.write_text(text, encoding="utf-8")


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
    template_path = root / "domains" / "_template"

    if not DOMAIN_ID.fullmatch(domain_id):
        raise RegistrationError(
            "Domain ID must contain two or more lowercase dotted segments; "
            "example: engineering.ios"
        )
    for label, value in (
        ("display name", display_name),
        ("owner", owner),
        ("description", description),
    ):
        if not value.strip():
            raise RegistrationError(f"{label.capitalize()} cannot be empty")
    if not registry_path.is_file() or not template_path.is_dir():
        raise RegistrationError(
            "The root must contain registry/domains.json and domains/_template/"
        )

    registry = _load_json(registry_path)
    entries = registry.get("domains")
    if registry.get("schema_version") != "1.0" or not isinstance(entries, list):
        raise RegistrationError("registry/domains.json has an unsupported structure")

    domain_path = root / "domains" / Path(*domain_id.split("."))
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
        "owner": owner.strip(),
    }
    next_entries = sorted([*entries, entry], key=lambda item: item["id"])

    if dry_run:
        print(f"Would create {relative_path}/")
        print(f"Would register {domain_id} as draft version 0.1.0")
        return domain_path

    domain_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template_path, domain_path)
    values = {
        "{{DOMAIN_ID}}": domain_id,
        "{{DISPLAY_NAME}}": display_name.strip(),
        "{{OWNER}}": owner.strip(),
        "{{DESCRIPTION}}": description.strip(),
    }
    for file_path in domain_path.rglob("*"):
        _replace_tokens(file_path, values)

    registry["domains"] = next_entries
    registry_path.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
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
