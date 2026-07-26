#!/usr/bin/env python3
"""Validate the Domain Pack registry and its filesystem contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

DOMAIN_ID = re.compile(r"^[a-z0-9][a-z0-9-]*(\.[a-z0-9][a-z0-9-]*)+$")
REQUIRED_FILES = ("DOMAIN.md", "domain.json", "routes.json", "capabilities.json", "owners.json")
REQUIRED_DIRS = ("rules", "workflows", "evaluators", "templates", "skills")
ALLOWED_STATES = {"draft", "active", "deprecated", "retired"}


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path}: top-level JSON value must be an object")
        return {}
    return value


def unique_ids(items: object, label: str, errors: list[str]) -> set[str]:
    if not isinstance(items, list):
        errors.append(f"{label}: expected an array")
        return set()
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            errors.append(f"{label}: every item must have a string ID")
            continue
        item_id = item["id"]
        if item_id in seen:
            errors.append(f"{label}: duplicate ID {item_id}")
        seen.add(item_id)
    return seen


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    registry_path = root / "registry" / "domains.json"
    template_path = root / "domains" / "_template"

    for required in REQUIRED_FILES:
        if not (template_path / required).is_file():
            errors.append(f"Template missing file: domains/_template/{required}")
    for required in REQUIRED_DIRS:
        if not (template_path / required).is_dir():
            errors.append(f"Template missing directory: domains/_template/{required}")

    registry = load_json(registry_path, errors)
    if registry.get("schema_version") != "1.0":
        errors.append("registry/domains.json: schema_version must be 1.0")
    entries = registry.get("domains")
    if not isinstance(entries, list):
        errors.append("registry/domains.json: domains must be an array")
        return errors

    seen: set[str] = set()
    sorted_entries = sorted(
        entries, key=lambda item: item.get("id", "") if isinstance(item, dict) else ""
    )
    if entries != sorted_entries:
        errors.append("registry/domains.json: domains must be sorted by ID")

    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("registry/domains.json: every entry must be an object")
            continue
        domain_id = entry.get("id")
        if not isinstance(domain_id, str) or not DOMAIN_ID.fullmatch(domain_id):
            errors.append(f"Registry entry has invalid ID: {domain_id!r}")
            continue
        if domain_id in seen:
            errors.append(f"Registry contains duplicate Domain ID: {domain_id}")
        seen.add(domain_id)

        expected_relative = "domains/" + "/".join(domain_id.split("."))
        if entry.get("path") != expected_relative:
            errors.append(f"{domain_id}: path must be {expected_relative}")
        domain_path = root / expected_relative
        for required in REQUIRED_FILES:
            if not (domain_path / required).is_file():
                errors.append(f"{domain_id}: missing {required}")
        for required in REQUIRED_DIRS:
            if not (domain_path / required).is_dir():
                errors.append(f"{domain_id}: missing {required}/")
        if not domain_path.is_dir():
            continue

        manifest = load_json(domain_path / "domain.json", errors)
        for key in ("id", "version", "status", "owner"):
            if manifest.get(key) != entry.get(key):
                errors.append(f"{domain_id}: manifest and registry disagree on {key}")
        if manifest.get("status") not in ALLOWED_STATES:
            errors.append(f"{domain_id}: unsupported lifecycle state")

        routes = load_json(domain_path / "routes.json", errors)
        capabilities = load_json(domain_path / "capabilities.json", errors)
        owners = load_json(domain_path / "owners.json", errors)
        for label, document in (
            ("routes", routes),
            ("capabilities", capabilities),
            ("owners", owners),
        ):
            if document.get("domain_id") != domain_id:
                errors.append(f"{domain_id}: {label}.json has the wrong domain_id")

        unique_ids(routes.get("routes"), f"{domain_id} routes", errors)
        capability_ids = unique_ids(
            capabilities.get("capabilities"), f"{domain_id} capabilities", errors
        )
        for route in routes.get("routes", []):
            if not isinstance(route, dict):
                continue
            for capability_id in route.get("capabilities", []):
                if capability_id not in capability_ids:
                    errors.append(
                        f"{domain_id}: route references unknown capability {capability_id}"
                    )

        for capability in capabilities.get("capabilities", []):
            if not isinstance(capability, dict):
                continue
            for key, directory in (
                ("workflows", "workflows"),
                ("skills", "skills"),
                ("evaluators", "evaluators"),
            ):
                values = capability.get(key, [])
                if not isinstance(values, list):
                    errors.append(
                        f"{domain_id}: capability {capability.get('id')} {key} must be an array"
                    )
                    continue
                for relative in values:
                    if not (domain_path / directory / relative).exists():
                        errors.append(
                            f"{domain_id}: capability {capability.get('id')} "
                            f"references missing {directory}/{relative}"
                        )

        skills_path = domain_path / "skills"
        if skills_path.is_dir():
            for child in skills_path.iterdir():
                if child.name.startswith("."):
                    continue
                if child.is_dir() and not (child / "SKILL.md").is_file():
                    errors.append(f"{domain_id}: Skill {child.name} is missing SKILL.md")

        if manifest.get("status") == "active":
            if not routes.get("routes"):
                errors.append(f"{domain_id}: active Domain must define at least one route")
            if not capabilities.get("capabilities"):
                errors.append(f"{domain_id}: active Domain must define at least one capability")
            if not owners.get("reviewers"):
                errors.append(f"{domain_id}: active Domain must define at least one reviewer")

    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Domain registry validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
