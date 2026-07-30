#!/usr/bin/env python3
"""Normalize a Domain artifact evaluation and derive its immutable verdict."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path

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
SEVERITIES = {"p0", "p1", "p2", "p3"}
IGNORED_NAMES = {".DS_Store", "__pycache__"}


class EvaluationError(ValueError):
    """Raised when an evaluation cannot be normalized safely."""


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvaluationError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise EvaluationError(f"Expected a JSON object in {path}")
    return value


def hash_artifact(path: Path) -> str:
    path = path.resolve()
    if path.is_file():
        return hashlib.sha256(path.read_bytes()).hexdigest()
    if not path.is_dir():
        raise EvaluationError(f"Artifact does not exist: {path}")

    digest = hashlib.sha256()
    files = sorted(
        item
        for item in path.rglob("*")
        if item.is_file()
        and not any(part in IGNORED_NAMES for part in item.relative_to(path).parts)
        and item.suffix != ".pyc"
    )
    for item in files:
        relative = item.relative_to(path).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def validate_score(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise EvaluationError(f"{label} must be a number")
    score = float(value)
    if not math.isfinite(score) or score < 0 or score > 100:
        raise EvaluationError(f"{label} must be between 0 and 100")
    return score


def normalize(raw: dict, artifact: Path, artifact_label: str | None = None) -> dict:
    if raw.get("schema_version") != "1.0":
        raise EvaluationError("Unsupported evaluation schema_version")
    evaluator = raw.get("evaluator")
    if not isinstance(evaluator, str) or not evaluator.strip():
        raise EvaluationError("evaluator must be a non-empty string")
    iteration = raw.get("iteration")
    if not isinstance(iteration, int) or isinstance(iteration, bool) or iteration < 1:
        raise EvaluationError("iteration must be a positive integer")
    evaluated_at = raw.get("evaluated_at")
    if not isinstance(evaluated_at, str) or not evaluated_at.strip():
        raise EvaluationError("evaluated_at must be a non-empty string")

    dimensions = raw.get("dimensions")
    if not isinstance(dimensions, dict) or set(dimensions) != set(DIMENSION_WEIGHTS):
        raise EvaluationError(
            "dimensions must contain exactly: "
            + ", ".join(sorted(DIMENSION_WEIGHTS))
        )
    normalized_dimensions = {
        name: validate_score(dimensions[name], f"dimensions.{name}")
        for name in DIMENSION_WEIGHTS
    }

    hard_gates = raw.get("hard_gates")
    if not isinstance(hard_gates, dict) or set(hard_gates) != HARD_GATES:
        raise EvaluationError(
            "hard_gates must contain exactly: " + ", ".join(sorted(HARD_GATES))
        )
    if any(not isinstance(value, bool) for value in hard_gates.values()):
        raise EvaluationError("every hard gate must be boolean")

    source_ids = raw.get("source_ids")
    if (
        not isinstance(source_ids, list)
        or not source_ids
        or any(not isinstance(item, str) or not item.strip() for item in source_ids)
        or len(set(source_ids)) != len(source_ids)
    ):
        raise EvaluationError("source_ids must be a unique non-empty array of source IDs")

    findings = raw.get("findings")
    if not isinstance(findings, list):
        raise EvaluationError("findings must be an array")
    normalized_findings = []
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            raise EvaluationError(f"findings[{index}] must be an object")
        if set(finding) != {"severity", "summary", "evidence"}:
            raise EvaluationError(
                f"findings[{index}] must contain severity, summary, and evidence"
            )
        if finding["severity"] not in SEVERITIES:
            raise EvaluationError(f"findings[{index}].severity is invalid")
        if not isinstance(finding["summary"], str) or not finding["summary"].strip():
            raise EvaluationError(f"findings[{index}].summary must be non-empty")
        if not isinstance(finding["evidence"], str) or not finding["evidence"].strip():
            raise EvaluationError(f"findings[{index}].evidence must be non-empty")
        normalized_findings.append(finding)

    blocked_reasons = raw.get("blocked_reasons")
    if (
        not isinstance(blocked_reasons, list)
        or any(not isinstance(item, str) or not item.strip() for item in blocked_reasons)
    ):
        raise EvaluationError("blocked_reasons must be an array of non-empty strings")

    overall_score = round(
        sum(
            normalized_dimensions[name] * weight
            for name, weight in DIMENSION_WEIGHTS.items()
        )
        / 100,
        2,
    )
    severe = any(item["severity"] in {"p0", "p1"} for item in normalized_findings)
    if blocked_reasons:
        verdict = "blocked"
    elif overall_score > 90 and all(hard_gates.values()) and not severe:
        verdict = "pass"
    else:
        verdict = "fail"

    return {
        "schema_version": "1.0",
        "artifact": artifact_label or str(artifact),
        "artifact_sha256": hash_artifact(artifact),
        "evaluator": evaluator.strip(),
        "iteration": iteration,
        "evaluated_at": evaluated_at.strip(),
        "dimensions": normalized_dimensions,
        "weights": DIMENSION_WEIGHTS,
        "hard_gates": hard_gates,
        "source_ids": source_ids,
        "findings": normalized_findings,
        "blocked_reasons": blocked_reasons,
        "overall_score": overall_score,
        "verdict": verdict,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--artifact-label", required=True)
    args = parser.parse_args(argv)
    try:
        result = normalize(
            load_json(args.input),
            args.artifact,
            artifact_label=args.artifact_label,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except EvaluationError as exc:
        print(f"Evaluation normalization failed: {exc}", file=sys.stderr)
        return 1
    print(
        f"{result['verdict'].upper()} {result['overall_score']:.2f} "
        f"{result['artifact']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
