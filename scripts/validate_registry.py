#!/usr/bin/env python3
"""Validate Domain documents, registry consistency, lifecycle, and references."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from schema_validation import validate_instance

REQUIRED_FILES = ("DOMAIN.md", "domain.json", "routes.json", "capabilities.json", "owners.json")
REQUIRED_DIRS = ("rules", "workflows", "evaluators", "templates", "skills")
SCHEMA_FILES = {
    "registry": "registry.schema.json",
    "manifest": "domain-pack.schema.json",
    "routes": "route.schema.json",
    "capabilities": "capability.schema.json",
    "owners": "owners.schema.json",
}


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
        return set()
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            continue
        item_id = item["id"]
        if item_id in seen:
            errors.append(f"{label}: duplicate ID {item_id}")
        seen.add(item_id)
    return seen


def apply_schema(document: dict, schema: dict, label: str, errors: list[str]) -> None:
    for error in validate_instance(document, schema):
        errors.append(f"{label}: {error}")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    registry_path = root / "registry" / "domains.json"
    template_path = root / "domains" / "_template"
    schemas = {
        key: load_json(root / "schemas" / filename, errors)
        for key, filename in SCHEMA_FILES.items()
    }

    for required in REQUIRED_FILES:
        if not (template_path / required).is_file():
            errors.append(f"Template missing file: domains/_template/{required}")
    for required in REQUIRED_DIRS:
        if not (template_path / required).is_dir():
            errors.append(f"Template missing directory: domains/_template/{required}")

    registry = load_json(registry_path, errors)
    apply_schema(registry, schemas["registry"], "registry/domains.json", errors)
    entries = registry.get("domains")
    if not isinstance(entries, list):
        return errors

    sorted_entries = sorted(
        entries, key=lambda item: item.get("id", "") if isinstance(item, dict) else ""
    )
    if entries != sorted_entries:
        errors.append("registry/domains.json: domains must be sorted by ID")

    seen: set[str] = set()
    records: dict[str, dict] = {}
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
            continue
        domain_id = entry["id"]
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
        routes = load_json(domain_path / "routes.json", errors)
        capabilities = load_json(domain_path / "capabilities.json", errors)
        owners = load_json(domain_path / "owners.json", errors)
        for key, document, filename in (
            ("manifest", manifest, "domain.json"),
            ("routes", routes, "routes.json"),
            ("capabilities", capabilities, "capabilities.json"),
            ("owners", owners, "owners.json"),
        ):
            apply_schema(document, schemas[key], f"{domain_id}/{filename}", errors)

        records[domain_id] = {
            "entry": entry,
            "path": domain_path,
            "manifest": manifest,
            "routes": routes,
            "capabilities": capabilities,
            "owners": owners,
        }

    qualified_capabilities = {
        f"{domain_id}/{capability['id']}"
        for domain_id, record in records.items()
        for capability in record["capabilities"].get("capabilities", [])
        if isinstance(capability, dict) and isinstance(capability.get("id"), str)
    }

    for domain_id, record in records.items():
        entry = record["entry"]
        domain_path = record["path"]
        manifest = record["manifest"]
        routes = record["routes"]
        capabilities = record["capabilities"]
        owners = record["owners"]

        for key in ("id", "version", "status", "owner"):
            if manifest.get(key) != entry.get(key):
                errors.append(f"{domain_id}: manifest and registry disagree on {key}")
        for label, document in (
            ("routes", routes),
            ("capabilities", capabilities),
            ("owners", owners),
        ):
            if document.get("domain_id") != domain_id:
                errors.append(f"{domain_id}: {label}.json has the wrong domain_id")
        if owners.get("primary_owner") != entry.get("owner"):
            errors.append(f"{domain_id}: owners.json and registry disagree on owner")

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
                    continue
                for relative in values:
                    if isinstance(relative, str) and not (domain_path / directory / relative).exists():
                        errors.append(
                            f"{domain_id}: capability {capability.get('id')} "
                            f"references missing {directory}/{relative}"
                        )
            for dependency in capability.get("dependencies", []):
                qualified = (
                    dependency if "/" in dependency else f"{domain_id}/{dependency}"
                )
                if qualified not in qualified_capabilities:
                    errors.append(
                        f"{domain_id}: capability {capability.get('id')} "
                        f"references unknown dependency {dependency}"
                    )

        skills_path = domain_path / "skills"
        if skills_path.is_dir():
            for child in skills_path.iterdir():
                if child.name.startswith("."):
                    continue
                if child.is_dir() and not (child / "SKILL.md").is_file():
                    errors.append(f"{domain_id}: Skill {child.name} is missing SKILL.md")

        if manifest.get("status") == "active":
            route_items = routes.get("routes", [])
            capability_items = capabilities.get("capabilities", [])
            if not route_items:
                errors.append(f"{domain_id}: active Domain must define at least one route")
            if not capability_items:
                errors.append(f"{domain_id}: active Domain must define at least one capability")
            if not owners.get("reviewers"):
                errors.append(f"{domain_id}: active Domain must define at least one reviewer")
            if not manifest.get("compatibility", {}).get("statement", "").strip():
                errors.append(f"{domain_id}: active Domain must define a compatibility statement")
            if not manifest.get("activation", {}).get("evidence"):
                errors.append(f"{domain_id}: active Domain must record activation evidence")
            for capability in capability_items:
                if not isinstance(capability, dict):
                    continue
                capability_id = capability.get("id", "<unknown>")
                for field in ("task_types", "workflows", "evaluators"):
                    if not capability.get(field):
                        errors.append(
                            f"{domain_id}: active capability {capability_id} "
                            f"must define {field}"
                        )

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
