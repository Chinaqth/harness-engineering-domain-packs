#!/usr/bin/env python3
"""Validate project-scoped Codex Custom Agent configuration."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path

REQUIRED_AGENTS = {
    "domain_pack_builder": "workspace-write",
    "domain_profession_researcher": "read-only",
    "domain_artifact_author": "workspace-write",
    "domain_artifact_evaluator": "read-only",
    "domain_pack_evaluator": "read-only",
}


def load_toml(path: Path, errors: list[str]) -> dict:
    try:
        value = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"{path}: invalid TOML: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path}: expected a TOML table")
        return {}
    return value


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    config = load_toml(root / ".codex" / "config.toml", errors)
    agents_config = config.get("agents")
    if not isinstance(agents_config, dict):
        errors.append(".codex/config.toml: missing [agents]")
    else:
        if agents_config.get("enabled") is not True:
            errors.append(".codex/config.toml: agents.enabled must be true")
        concurrency = agents_config.get("max_concurrent_threads_per_session")
        if not isinstance(concurrency, int) or isinstance(concurrency, bool) or concurrency < 4:
            errors.append(
                ".codex/config.toml: max_concurrent_threads_per_session must be at least 4"
            )

    agents_root = root / ".codex" / "agents"
    found: dict[str, dict] = {}
    for path in sorted(agents_root.glob("*.toml")):
        agent = load_toml(path, errors)
        name = agent.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{path}: name must be non-empty")
            continue
        if name in found:
            errors.append(f"Duplicate Agent name: {name}")
        found[name] = agent
        for field in ("description", "developer_instructions"):
            if not isinstance(agent.get(field), str) or not agent[field].strip():
                errors.append(f"{path}: {field} must be non-empty")
        expected_sandbox = REQUIRED_AGENTS.get(name)
        if expected_sandbox and agent.get("sandbox_mode") != expected_sandbox:
            errors.append(f"{path}: sandbox_mode must be {expected_sandbox}")

    missing = sorted(set(REQUIRED_AGENTS) - set(found))
    if missing:
        errors.append("Missing required Agents: " + ", ".join(missing))
    unexpected = sorted(set(found) - set(REQUIRED_AGENTS))
    if unexpected:
        errors.append("Unexpected project Agents: " + ", ".join(unexpected))

    builder = found.get("domain_pack_builder", {})
    instructions = builder.get("developer_instructions", "")
    for dependency in (
        "$complete-domain-pack",
        "domain_profession_researcher",
        "domain_artifact_author",
        "domain_artifact_evaluator",
        "domain_pack_evaluator",
    ):
        if dependency not in instructions:
            errors.append(f"domain_pack_builder does not reference {dependency}")

    researcher_instructions = found.get("domain_profession_researcher", {}).get(
        "developer_instructions", ""
    )
    for handoff_field in (
        "sources_json",
        "capability_map_markdown",
        "responsibility_boundaries_markdown",
    ):
        if handoff_field not in researcher_instructions:
            errors.append(
                f"domain_profession_researcher does not require {handoff_field}"
            )
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Project Custom Agent validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
