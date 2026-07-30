#!/usr/bin/env python3
"""Validate Domain development session evidence and reject stale evaluations."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_research import validate_ledger

IGNORED_NAMES = {".DS_Store", "__pycache__"}
DIMENSION_WEIGHTS = {
    "contract": 20,
    "professional": 20,
    "boundaries": 15,
    "executability": 15,
    "verifiability": 15,
    "architecture": 10,
    "maintainability": 5,
}
HARD_GATES = {
    "schema_passed",
    "references_resolved",
    "professional_sources_traceable",
    "no_invented_authority",
    "kernel_constraints_preserved",
    "owner_facts_authoritative",
}


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


def hash_artifact(path: Path) -> str:
    if path.is_file():
        return hashlib.sha256(path.read_bytes()).hexdigest()
    digest = hashlib.sha256()
    files = sorted(
        item
        for item in path.rglob("*")
        if item.is_file()
        and not any(part in IGNORED_NAMES for part in item.relative_to(path).parts)
        and item.suffix != ".pyc"
    )
    for item in files:
        digest.update(item.relative_to(path).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def production_artifacts(domain_root: Path) -> set[str]:
    return {
        item.relative_to(domain_root).as_posix()
        for item in domain_root.rglob("*")
        if item.is_file()
        and item.name != ".gitkeep"
        and not item.name.startswith(".")
        and not any(part in IGNORED_NAMES for part in item.relative_to(domain_root).parts)
        and item.suffix != ".pyc"
    }


def find_domain_path(root: Path, domain_id: str, issues: list[str]) -> Path | None:
    registry = load_json(root / "registry" / "domains.json", issues)
    entries = registry.get("domains")
    if not isinstance(entries, list):
        issues.append("Registry domains must be an array")
        return None
    matches = [
        item for item in entries
        if isinstance(item, dict) and item.get("id") == domain_id
    ]
    if len(matches) != 1:
        issues.append(f"Expected one registry entry for {domain_id}, found {len(matches)}")
        return None
    relative = matches[0].get("path")
    if not isinstance(relative, str):
        issues.append(f"Registry path is invalid for {domain_id}")
        return None
    return (root / relative).resolve()


def validate_evaluation(
    evaluation_path: Path,
    artifact_path: Path,
    expected_label: str,
    issues: list[str],
    require_current_pass: bool,
    available_source_ids: set[str],
) -> float | None:
    evaluation = load_json(evaluation_path, issues)
    if not evaluation:
        return None
    if evaluation.get("schema_version") != "1.0":
        issues.append(f"{evaluation_path}: schema_version must be 1.0")
    if evaluation.get("artifact") != expected_label:
        issues.append(f"{evaluation_path}: artifact label does not match {expected_label}")
    if not artifact_path.exists():
        issues.append(f"Missing artifact: {expected_label}")
        return None
    digest = evaluation.get("artifact_sha256")
    if (
        not isinstance(digest, str)
        or len(digest) != 64
        or any(character not in "0123456789abcdef" for character in digest)
    ):
        issues.append(f"{evaluation_path}: artifact_sha256 is invalid")
    elif require_current_pass and digest != hash_artifact(artifact_path):
        issues.append(f"{evaluation_path}: stale artifact digest for {expected_label}")
    if not isinstance(evaluation.get("evaluator"), str) or not evaluation["evaluator"].strip():
        issues.append(f"{evaluation_path}: evaluator must be non-empty")
    iteration = evaluation.get("iteration")
    if not isinstance(iteration, int) or isinstance(iteration, bool) or iteration < 1:
        issues.append(f"{evaluation_path}: iteration must be a positive integer")
    if (
        not isinstance(evaluation.get("evaluated_at"), str)
        or not evaluation["evaluated_at"].strip()
    ):
        issues.append(f"{evaluation_path}: evaluated_at must be non-empty")

    dimensions = evaluation.get("dimensions")
    if not isinstance(dimensions, dict) or set(dimensions) != set(DIMENSION_WEIGHTS):
        issues.append(f"{evaluation_path}: dimensions are incomplete")
        computed_score = None
    elif any(
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not math.isfinite(float(value))
        or value < 0
        or value > 100
        for value in dimensions.values()
    ):
        issues.append(f"{evaluation_path}: dimension scores must be between 0 and 100")
        computed_score = None
    else:
        computed_score = round(
            sum(
                float(dimensions[name]) * weight
                for name, weight in DIMENSION_WEIGHTS.items()
            )
            / 100,
            2,
        )
    if evaluation.get("weights") != DIMENSION_WEIGHTS:
        issues.append(f"{evaluation_path}: weights do not match the scoring contract")

    source_ids = evaluation.get("source_ids")
    if (
        not isinstance(source_ids, list)
        or not source_ids
        or any(not isinstance(item, str) or not item.strip() for item in source_ids)
        or len(set(source_ids)) != len(source_ids)
    ):
        issues.append(f"{evaluation_path}: source_ids must be unique and non-empty")
    elif any(source_id not in available_source_ids for source_id in source_ids):
        issues.append(f"{evaluation_path}: source_ids reference the wrong research ledger")

    score = evaluation.get("overall_score")
    if (
        isinstance(score, bool)
        or not isinstance(score, (int, float))
        or not math.isfinite(float(score))
    ):
        issues.append(f"{evaluation_path}: overall_score must be numeric")
        score_value = None
    else:
        score_value = float(score)
        if computed_score is not None and score_value != computed_score:
            issues.append(f"{evaluation_path}: overall_score does not match dimensions")

    gates = evaluation.get("hard_gates")
    if (
        not isinstance(gates, dict)
        or set(gates) != HARD_GATES
        or any(not isinstance(value, bool) for value in gates.values())
    ):
        issues.append(f"{evaluation_path}: hard gates are incomplete or invalid")
    findings = evaluation.get("findings")
    if not isinstance(findings, list):
        issues.append(f"{evaluation_path}: findings must be an array")
        findings = []
    elif any(
        not isinstance(item, dict)
        or set(item) != {"severity", "summary", "evidence"}
        or item.get("severity") not in {"p0", "p1", "p2", "p3"}
        or not isinstance(item.get("summary"), str)
        or not item["summary"].strip()
        or not isinstance(item.get("evidence"), str)
        or not item["evidence"].strip()
        for item in findings
    ):
        issues.append(f"{evaluation_path}: findings are malformed")
    blocked_reasons = evaluation.get("blocked_reasons")
    if (
        not isinstance(blocked_reasons, list)
        or any(not isinstance(item, str) or not item.strip() for item in blocked_reasons)
    ):
        issues.append(f"{evaluation_path}: blocked_reasons are malformed")
        blocked_reasons = []

    severe = any(
        isinstance(item, dict) and item.get("severity") in {"p0", "p1"}
        for item in findings
    )
    if blocked_reasons:
        expected_verdict = "blocked"
    elif (
        score_value is not None
        and score_value > 90
        and isinstance(gates, dict)
        and set(gates) == HARD_GATES
        and all(value is True for value in gates.values())
        and not severe
    ):
        expected_verdict = "pass"
    else:
        expected_verdict = "fail"
    if evaluation.get("verdict") != expected_verdict:
        issues.append(f"{evaluation_path}: verdict does not match normalized evidence")

    if require_current_pass:
        if evaluation.get("verdict") != "pass":
            issues.append(f"{evaluation_path}: verdict is not pass")
        if score_value is None or score_value <= 90:
            issues.append(f"{evaluation_path}: score must be greater than 90")
        if (
            not isinstance(gates, dict)
            or set(gates) != HARD_GATES
            or not all(value is True for value in gates.values())
        ):
            issues.append(f"{evaluation_path}: hard gates do not all pass")
        if severe:
            issues.append(f"{evaluation_path}: contains a P0 or P1 finding")
        if blocked_reasons:
            issues.append(f"{evaluation_path}: contains blocked reasons")
    return score_value


def validate_session(root: Path, session_path: Path, require_final: bool = False) -> dict:
    root = root.resolve()
    session_path = session_path.resolve()
    issues: list[str] = []
    session = load_json(session_path, issues)
    domain_id = session.get("domain_id")
    if session.get("schema_version") != "1.0":
        issues.append("Session schema_version must be 1.0")
    if not isinstance(domain_id, str) or not domain_id:
        issues.append("Session domain_id must be a non-empty string")
        domain_root = None
    else:
        domain_root = find_domain_path(root, domain_id, issues)

    ledger_relative = session.get("research_ledger")
    available_source_ids: set[str] = set()
    if not isinstance(ledger_relative, str) or not ledger_relative:
        issues.append("Session research_ledger must be a non-empty path")
    elif not isinstance(domain_id, str) or not domain_id:
        issues.append("Research ledger cannot be validated without domain_id")
    else:
        ledger_path = (session_path.parent / ledger_relative).resolve()
        if (
            session_path.parent != ledger_path
            and session_path.parent not in ledger_path.parents
        ):
            issues.append(f"Research ledger escapes change directory: {ledger_relative}")
        else:
            ledger_errors, available_source_ids = validate_ledger(
                root, ledger_path, domain_id
            )
            issues.extend(f"Research ledger: {error}" for error in ledger_errors)

    artifact_budget = session.get("max_artifact_iterations")
    pack_budget = session.get("max_pack_iterations")
    if not isinstance(artifact_budget, int) or not 1 <= artifact_budget <= 5:
        issues.append("max_artifact_iterations must be between 1 and 5")
    if not isinstance(pack_budget, int) or not 1 <= pack_budget <= 3:
        issues.append("max_pack_iterations must be between 1 and 3")

    artifacts = session.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        issues.append("Session artifacts must be a non-empty array")
        artifacts = []
    seen: set[str] = set()
    for index, item in enumerate(artifacts):
        if not isinstance(item, dict):
            issues.append(f"artifacts[{index}] must be an object")
            continue
        label = item.get("path")
        evaluations = item.get("evaluations")
        if not isinstance(label, str) or not label:
            issues.append(f"artifacts[{index}].path must be non-empty")
            continue
        if label in seen:
            issues.append(f"Duplicate artifact path: {label}")
        seen.add(label)
        if domain_root is None:
            continue
        artifact_path = (domain_root / label).resolve()
        if domain_root != artifact_path and domain_root not in artifact_path.parents:
            issues.append(f"Artifact escapes Domain root: {label}")
            continue
        if not isinstance(evaluations, list) or not evaluations:
            issues.append(f"No evaluations recorded for {label}")
            continue
        if isinstance(artifact_budget, int) and len(evaluations) > artifact_budget:
            issues.append(f"Artifact iteration budget exceeded for {label}")
        scores: list[float] = []
        latest_evaluation: dict = {}
        for evaluation_index, relative in enumerate(evaluations):
            if not isinstance(relative, str) or not relative:
                issues.append(f"Invalid evaluation path for {label}")
                continue
            evaluation_path = (session_path.parent / relative).resolve()
            if session_path.parent != evaluation_path and session_path.parent not in evaluation_path.parents:
                issues.append(f"Evaluation escapes change directory: {relative}")
                continue
            if evaluation_index == len(evaluations) - 1:
                latest_evaluation = load_json(evaluation_path, [])
            score = validate_evaluation(
                evaluation_path,
                artifact_path,
                label,
                issues,
                require_current_pass=evaluation_index == len(evaluations) - 1,
                available_source_ids=available_source_ids,
            )
            if score is not None:
                scores.append(score)
        if len(scores) >= 3 and scores[-1] <= 90:
            if scores[-1] - scores[-2] < 2 and scores[-2] - scores[-3] < 2:
                issues.append(f"Non-converging evaluation history for {label}")
        if (
            isinstance(artifact_budget, int)
            and len(evaluations) == artifact_budget
            and latest_evaluation.get("verdict") != "pass"
        ):
            issues.append(f"Artifact iteration budget exhausted for {label}")

    if require_final and domain_root is not None:
        missing = sorted(production_artifacts(domain_root) - seen)
        for relative in missing:
            issues.append(f"Production artifact is not declared in session: {relative}")

    final_records = session.get("final_evaluations", [])
    if not isinstance(final_records, list):
        issues.append("final_evaluations must be an array")
        final_records = []
    if require_final and not final_records:
        issues.append("A final Pack evaluation is required")
    if isinstance(pack_budget, int) and len(final_records) > pack_budget:
        issues.append("Pack iteration budget exceeded")
    if final_records and domain_root is not None:
        latest_final: dict = {}
        for final_index, relative in enumerate(final_records):
            if not isinstance(relative, str) or not relative:
                issues.append("Final evaluation path is invalid")
                continue
            evaluation_path = (session_path.parent / relative).resolve()
            if (
                session_path.parent != evaluation_path
                and session_path.parent not in evaluation_path.parents
            ):
                issues.append(f"Final evaluation escapes change directory: {relative}")
            else:
                validate_evaluation(
                    evaluation_path,
                    domain_root,
                    ".",
                    issues,
                    require_current_pass=final_index == len(final_records) - 1,
                    available_source_ids=available_source_ids,
                )
                if final_index == len(final_records) - 1:
                    latest_final = load_json(evaluation_path, [])
        if (
            isinstance(pack_budget, int)
            and len(final_records) == pack_budget
            and latest_final.get("verdict") != "pass"
        ):
            issues.append("Pack iteration budget exhausted")

    return {
        "schema_version": "1.0",
        "domain_id": domain_id,
        "session": str(session_path),
        "valid": not issues,
        "issues": issues,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--session", type=Path, required=True)
    parser.add_argument("--require-final", action="store_true")
    args = parser.parse_args(argv)
    result = validate_session(args.root, args.session, args.require_final)
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
