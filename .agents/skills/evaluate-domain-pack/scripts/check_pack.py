#!/usr/bin/env python3
"""Produce deterministic structural evidence for one Domain Pack."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


def load_json(path: Path, issues: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        issues.append(f"Cannot read valid JSON from {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"{path}: expected a JSON object")
        return {}
    return value


def load_registry_validator(root: Path):
    path = root / "scripts" / "validate_registry.py"
    spec = importlib.util.spec_from_file_location("domain_pack_registry_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load registry validator from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    spec.loader.exec_module(module)
    return module


def load_research_validator(root: Path):
    path = (
        root
        / ".agents"
        / "skills"
        / "complete-domain-pack"
        / "scripts"
        / "validate_research.py"
    )
    spec = importlib.util.spec_from_file_location("domain_research_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load research validator from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_pack(root: Path, domain_id: str, ledger_path: Path | None = None) -> dict:
    root = root.resolve()
    content_issues: list[str] = []
    activation_issues: list[str] = []
    checks: list[dict] = []

    try:
        registry_issues = load_registry_validator(root).validate(root)
    except Exception as exc:  # validator failures are evaluation evidence
        registry_issues = [f"Registry validator could not run: {exc}"]
    checks.append({
        "name": "repository-registry-validation",
        "scope": "content",
        "passed": not registry_issues,
        "detail": registry_issues,
    })
    content_issues.extend(registry_issues)

    registry = load_json(root / "registry" / "domains.json", content_issues)
    entries = [
        item
        for item in registry.get("domains", [])
        if isinstance(item, dict) and item.get("id") == domain_id
    ]
    checks.append({
        "name": "unique-registry-entry",
        "scope": "content",
        "passed": len(entries) == 1,
        "detail": f"found {len(entries)}",
    })
    if len(entries) != 1:
        content_issues.append(
            f"Expected one registry entry for {domain_id}, found {len(entries)}"
        )
        return {
            "schema_version": "1.0",
            "domain_id": domain_id,
            "state": "fail",
            "content_state": "incomplete",
            "content_verdict": "fail",
            "activation_verdict": "blocked",
            "verdict": "fail",
            "checks": checks,
            "content_issues": content_issues,
            "activation_issues": activation_issues,
            "issues": content_issues,
        }

    domain_root = root / entries[0]["path"]
    manifest = load_json(domain_root / "domain.json", content_issues)
    load_json(domain_root / "owners.json", content_issues)
    routes = load_json(domain_root / "routes.json", content_issues)
    capabilities = load_json(domain_root / "capabilities.json", content_issues)

    organizational_gaps: list[dict] = []
    if ledger_path is None:
        research_issues = ["A validated research ledger is required"]
    else:
        resolved_ledger = (
            ledger_path.resolve()
            if ledger_path.is_absolute()
            else (root / ledger_path).resolve()
        )
        changes_root = (root / "changes").resolve()
        if changes_root != resolved_ledger and changes_root not in resolved_ledger.parents:
            research_issues = ["Research ledger must be stored under changes/"]
            ledger = {}
        else:
            try:
                research_issues, _ = load_research_validator(root).validate_ledger(
                    root, resolved_ledger, domain_id
                )
            except Exception as exc:
                research_issues = [f"Research validator could not run: {exc}"]
            ledger = load_json(resolved_ledger, research_issues)
        gaps = ledger.get("organizational_gaps")
        if isinstance(gaps, list):
            organizational_gaps = [gap for gap in gaps if isinstance(gap, dict)]
    checks.append({
        "name": "validated-research-ledger",
        "scope": "content",
        "passed": not research_issues,
        "detail": research_issues,
    })
    content_issues.extend(f"Research: {issue}" for issue in research_issues)

    content_readiness = {
        "applicability-task-types": bool(
            manifest.get("applicability", {}).get("task_types")
        ),
        "applicability-repository-signals": bool(
            manifest.get("applicability", {}).get("repository_signals")
        ),
        "compatibility-statement": bool(
            str(manifest.get("compatibility", {}).get("statement", "")).strip()
        ),
        "routes": bool(routes.get("routes")),
        "capabilities": bool(capabilities.get("capabilities")),
    }
    for name, passed in content_readiness.items():
        checks.append({"name": name, "scope": "content", "passed": passed, "detail": ""})
        if not passed:
            content_issues.append(f"Content completeness gate failed: {name}")

    for capability in capabilities.get("capabilities", []):
        if not isinstance(capability, dict):
            continue
        capability_id = capability.get("id", "<unknown>")
        for field in ("task_types", "workflows", "evaluators"):
            passed = bool(capability.get(field))
            name = f"capability-{capability_id}-{field}"
            checks.append({
                "name": name,
                "scope": "content",
                "passed": passed,
                "detail": "",
            })
            if not passed:
                content_issues.append(f"Capability {capability_id} must define {field}")

    route_priorities: dict[tuple[str, tuple[str, ...]], list[dict]] = {}
    for route in routes.get("routes", []):
        if not isinstance(route, dict):
            continue
        key = (
            json.dumps(sorted(route.get("task_types", []))),
            tuple(sorted(str(item).lower() for item in route.get("signals", []))),
        )
        route_priorities.setdefault(key, []).append(route)
    for candidates in route_priorities.values():
        priorities = [item.get("priority") for item in candidates]
        if len(candidates) > 1 and len(set(priorities)) != len(priorities):
            ids = ", ".join(str(item.get("id")) for item in candidates)
            content_issues.append(f"Ambiguous routes share signals and priority: {ids}")

    checks.append({
        "name": "route-priority-determinism",
        "scope": "content",
        "passed": not any("Ambiguous routes" in item for item in content_issues),
        "detail": "",
    })
    content_verdict = "pass" if not content_issues else "fail"
    content_state = (
        "content-complete"
        if content_verdict == "pass"
        else "incomplete"
    )
    activation_verdict = "pass" if content_verdict == "pass" else "fail"
    if content_verdict == "fail":
        state = "fail"
    else:
        state = "activation-ready"
    return {
        "schema_version": "1.0",
        "domain_id": domain_id,
        "domain_path": entries[0]["path"],
        "state": state,
        "content_state": content_state,
        "content_verdict": content_verdict,
        "activation_verdict": activation_verdict,
        "verdict": content_verdict,
        "checks": checks,
        "content_issues": content_issues,
        "activation_issues": activation_issues,
        "organizational_gaps": organizational_gaps,
        "organizational_gaps_block_lifecycle": False,
        "issues": [*content_issues, *activation_issues],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--domain-id", required=True)
    parser.add_argument("--ledger", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = check_pack(args.root, args.domain_id, args.ledger)
    serialized = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0 if result["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
