#!/usr/bin/env python3
"""Validate repository Skill packaging without external YAML dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")


def frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if "[TODO" in text or "TODO:" in text:
        errors.append(f"{path}: contains an unresolved TODO")
    if not text.startswith("---\n"):
        errors.append(f"{path}: missing YAML frontmatter")
        return {}
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        errors.append(f"{path}: malformed YAML frontmatter")
        return {}
    values: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path}: malformed frontmatter line {line!r}")
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    if set(values) != {"name", "description"}:
        errors.append(f"{path}: frontmatter must contain only name and description")
    if not values.get("description"):
        errors.append(f"{path}: description must be non-empty")
    return values


def yaml_string(text: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}:\s*\"([^\"]*)\"\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def validate(root: Path) -> list[str]:
    root = root.resolve()
    skills_root = root / ".agents" / "skills"
    errors: list[str] = []
    names: set[str] = set()
    for skill_dir in sorted(item for item in skills_root.iterdir() if item.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        values = frontmatter(skill_file, errors)
        name = values.get("name", "")
        if name != skill_dir.name:
            errors.append(f"{skill_file}: name must match directory {skill_dir.name}")
        if not SKILL_NAME.fullmatch(name):
            errors.append(f"{skill_file}: invalid Skill name {name!r}")
        if name in names:
            errors.append(f"Duplicate Skill name: {name}")
        names.add(name)

        yaml_path = skill_dir / "agents" / "openai.yaml"
        if not yaml_path.is_file():
            errors.append(f"{skill_dir}: missing agents/openai.yaml")
        else:
            yaml = yaml_path.read_text(encoding="utf-8")
            display_name = yaml_string(yaml, "display_name")
            short_description = yaml_string(yaml, "short_description")
            default_prompt = yaml_string(yaml, "default_prompt")
            if not display_name:
                errors.append(f"{yaml_path}: missing quoted display_name")
            if not short_description or not 25 <= len(short_description) <= 64:
                errors.append(f"{yaml_path}: short_description must contain 25-64 characters")
            if not default_prompt or f"${name}" not in default_prompt:
                errors.append(f"{yaml_path}: default_prompt must mention ${name}")

        for extra in ("README.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md"):
            if (skill_dir / extra).exists():
                errors.append(f"{skill_dir}: extraneous Skill file {extra}")

        skill_text = skill_file.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(skill_text):
            if target.startswith(("http://", "https://", "#")):
                continue
            if not (skill_dir / target).exists():
                errors.append(f"{skill_file}: broken local reference {target}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Repository Skill validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

