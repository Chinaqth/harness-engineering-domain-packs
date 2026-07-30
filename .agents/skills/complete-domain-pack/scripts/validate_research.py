#!/usr/bin/env python3
"""Validate a source-traceable profession research ledger."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

AUTHORITIES = {"primary", "standards-body", "professional-body", "repository-fact"}
KINDS = {"web", "repository"}


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot read valid JSON from {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path}: expected a JSON object")
        return {}
    return value


def validate_ledger(root: Path, ledger_path: Path, domain_id: str) -> tuple[list[str], set[str]]:
    root = root.resolve()
    ledger_path = ledger_path.resolve()
    errors: list[str] = []
    ledger = load_json(ledger_path, errors)
    supporting_outputs: dict[str, str] = {}
    for supporting_name in ("capability-map.md", "responsibility-boundaries.md"):
        supporting_path = ledger_path.parent / supporting_name
        try:
            supporting_text = supporting_path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"Missing research output {supporting_path}: {exc}")
        else:
            if not supporting_text.strip():
                errors.append(f"Research output must be non-empty: {supporting_path}")
            else:
                supporting_outputs[supporting_name] = supporting_text
    if ledger.get("schema_version") != "1.0":
        errors.append("Research ledger schema_version must be 1.0")
    if ledger.get("domain_id") != domain_id:
        errors.append(f"Research ledger domain_id must be {domain_id}")
    if not isinstance(ledger.get("generated_at"), str) or not ledger["generated_at"].strip():
        errors.append("Research ledger generated_at must be non-empty")

    sources = ledger.get("sources")
    if not isinstance(sources, list):
        errors.append("Research ledger sources must be an array")
        sources = []
    source_ids: set[str] = set()
    professional_source_ids: set[str] = set()
    locators: set[str] = set()
    authoritative_web = 0
    repository_facts = 0
    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label} must be an object")
            continue
        required = {"id", "kind", "title", "publisher", "locator", "authority", "retrieved_at", "claims"}
        if set(source) != required:
            errors.append(f"{label} must contain exactly {', '.join(sorted(required))}")
            continue
        source_id = source["id"]
        if not isinstance(source_id, str) or not source_id.strip():
            errors.append(f"{label}.id must be non-empty")
        elif source_id in source_ids:
            errors.append(f"Duplicate source ID: {source_id}")
        else:
            source_ids.add(source_id)
        if source["kind"] not in KINDS:
            errors.append(f"{label}.kind is invalid")
        if source["authority"] not in AUTHORITIES:
            errors.append(f"{label}.authority is invalid")
        for field in ("title", "publisher", "locator", "retrieved_at"):
            if not isinstance(source[field], str) or not source[field].strip():
                errors.append(f"{label}.{field} must be non-empty")
        claims = source["claims"]
        if (
            not isinstance(claims, list)
            or not claims
            or any(not isinstance(item, str) or not item.strip() for item in claims)
        ):
            errors.append(f"{label}.claims must contain non-empty strings")
        locator = source["locator"]
        if isinstance(locator, str) and locator:
            if locator in locators:
                errors.append(f"Duplicate source locator: {locator}")
            locators.add(locator)
            if source["kind"] == "web":
                parsed = urlparse(locator)
                if parsed.scheme != "https" or not parsed.netloc:
                    errors.append(f"{label}.locator must be an HTTPS URL")
                elif source["authority"] in {"primary", "standards-body", "professional-body"}:
                    authoritative_web += 1
                    if isinstance(source_id, str) and source_id.strip():
                        professional_source_ids.add(source_id)
            elif source["kind"] == "repository":
                path = (root / locator).resolve()
                if root != path and root not in path.parents:
                    errors.append(f"{label}.locator escapes repository root")
                elif not path.is_file():
                    errors.append(f"{label}.locator does not exist: {locator}")
                if source["authority"] != "repository-fact":
                    errors.append(f"{label}: repository source authority must be repository-fact")
                else:
                    repository_facts += 1

    if authoritative_web < 2:
        errors.append("Research ledger requires at least two authoritative HTTPS sources")
    if repository_facts < 1:
        errors.append("Research ledger requires at least one repository identity source")
    for supporting_name, supporting_text in supporting_outputs.items():
        if not any(source_id in supporting_text for source_id in professional_source_ids):
            errors.append(
                f"Research output {supporting_name} must cite an authoritative source ID"
            )

    hypotheses = ledger.get("capability_hypotheses")
    if not isinstance(hypotheses, list) or not hypotheses:
        errors.append("capability_hypotheses must be a non-empty array")
        hypotheses = []
    hypothesis_ids: set[str] = set()
    for index, item in enumerate(hypotheses):
        label = f"capability_hypotheses[{index}]"
        if not isinstance(item, dict) or set(item) != {"id", "description", "source_ids"}:
            errors.append(f"{label} must contain id, description, and source_ids")
            continue
        if not isinstance(item["id"], str) or not item["id"].strip():
            errors.append(f"{label}.id must be non-empty")
        elif item["id"] in hypothesis_ids:
            errors.append(f"Duplicate capability hypothesis ID: {item['id']}")
        else:
            hypothesis_ids.add(item["id"])
        if not isinstance(item["description"], str) or not item["description"].strip():
            errors.append(f"{label}.description must be non-empty")
        cited = item["source_ids"]
        if not isinstance(cited, list) or not cited:
            errors.append(f"{label}.source_ids must be non-empty")
        elif any(source_id not in source_ids for source_id in cited):
            errors.append(f"{label} references an unknown source ID")
        elif not set(cited).intersection(professional_source_ids):
            errors.append(f"{label} must cite an authoritative professional web source")

    gaps = ledger.get("organizational_gaps")
    if not isinstance(gaps, list):
        errors.append("organizational_gaps must be an array")
        gaps = []
    gap_ids: set[str] = set()
    for index, gap in enumerate(gaps):
        label = f"organizational_gaps[{index}]"
        if not isinstance(gap, dict) or set(gap) != {"id", "description", "required_for_activation"}:
            errors.append(f"{label} must contain id, description, and required_for_activation")
            continue
        if not isinstance(gap["id"], str) or not gap["id"].strip():
            errors.append(f"{label}.id must be non-empty")
        elif gap["id"] in gap_ids:
            errors.append(f"Duplicate organizational gap ID: {gap['id']}")
        else:
            gap_ids.add(gap["id"])
        if not isinstance(gap["description"], str) or not gap["description"].strip():
            errors.append(f"{label}.description must be non-empty")
        if not isinstance(gap["required_for_activation"], bool):
            errors.append(f"{label}.required_for_activation must be boolean")
    return errors, source_ids


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--domain-id", required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args(argv)
    errors, source_ids = validate_ledger(args.root, args.ledger, args.domain_id)
    result = {
        "schema_version": "1.0",
        "domain_id": args.domain_id,
        "valid": not errors,
        "source_ids": sorted(source_ids),
        "errors": errors,
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
