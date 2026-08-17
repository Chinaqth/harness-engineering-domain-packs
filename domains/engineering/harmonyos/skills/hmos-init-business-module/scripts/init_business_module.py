#!/usr/bin/env python3
"""Create a HarmonyOS business HAR module from the bundled template."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path


MODULE_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
MODULE_TOKEN = "__MODULE_ID__"
DISPLAY_TOKEN = "__DISPLAY_NAME__"
PROVIDER_SUFFIX = "provider"
PROVIDERS_DIRECTORY = Path("providers")

EMPTY_DIRECTORIES = (
    "src/main/ets/api/repository",
    "src/main/ets/components",
    "src/main/ets/dialogs",
    "src/main/ets/models/request",
    "src/main/ets/models/response",
    "src/main/ets/pages",
    "src/main/ets/router",
    "src/main/ets/viewmodels",
    "src/main/resources/base/media",
    "src/main/resources/rawfile",
)

REQUIRED_PATHS = (
    ".gitignore",
    "Index.ets",
    "build-profile.json5",
    "consumer-rules.txt",
    "hvigorfile.ts",
    "obfuscation-rules.txt",
    "oh-package.json5",
    "src/main/module.json5",
    "src/main/resources/base/element/float.json",
    "src/main/resources/base/element/string.json",
    "src/test/List.test.ets",
    "src/test/LocalUnit.test.ets",
    "src/ohosTest/module.json5",
    "src/ohosTest/ets/test/Ability.test.ets",
    "src/ohosTest/ets/test/List.test.ets",
)

EXCLUDED_PATHS = (
    "oh-package-lock.json5",
    "oh_modules",
    "build",
)

PROVIDER_EMPTY_DIRECTORIES = (
    "src/main/ets",
    "src/main/resources/base/media",
    "src/main/resources/rawfile",
)

PROVIDER_REQUIRED_PATHS = (
    ".gitignore",
    "Index.ets",
    "build-profile.json5",
    "consumer-rules.txt",
    "hvigorfile.ts",
    "obfuscation-rules.txt",
    "oh-package.json5",
    "src/main/module.json5",
    "src/main/resources/base/element/float.json",
    "src/main/resources/base/element/string.json",
)


class InitializationError(RuntimeError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a HarmonyOS business HAR module."
    )
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--module-id", required=True)
    parser.add_argument("--display-name")
    parser.add_argument("--modules-dir", default="features", type=Path)
    return parser.parse_args()


def find_array(text: str, key: str) -> tuple[int, int]:
    match = re.search(rf'"{re.escape(key)}"\s*:\s*\[', text)
    if not match:
        raise InitializationError(f'Cannot find top-level "{key}" array')

    start = text.find("[", match.start())
    depth = 0
    in_string = False
    escaped = False
    line_comment = False
    block_comment = False
    index = start

    while index < len(text):
        char = text[index]
        next_char = text[index + 1] if index + 1 < len(text) else ""

        if line_comment:
            if char in "\r\n":
                line_comment = False
            index += 1
            continue

        if block_comment:
            if char == "*" and next_char == "/":
                block_comment = False
                index += 2
            else:
                index += 1
            continue

        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            index += 1
            continue

        if char == "/" and next_char == "/":
            line_comment = True
            index += 2
            continue
        if char == "/" and next_char == "*":
            block_comment = True
            index += 2
            continue
        if char == '"':
            in_string = True
            index += 1
            continue
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return start, index
        index += 1

    raise InitializationError(f'Unclosed "{key}" array')


def update_project_manifest(text: str, module_id: str, module_path: str) -> str:
    start, end = find_array(text, "modules")
    body = text[start + 1 : end]

    if re.search(rf'"name"\s*:\s*"{re.escape(module_id)}"', body):
        raise InitializationError(
            f'Module "{module_id}" already exists in build-profile.json5'
        )

    trailing_match = re.search(r"\s*$", body)
    trailing = trailing_match.group(0) if trailing_match else ""
    core = body[: len(body) - len(trailing)] if trailing else body
    separator = ""
    if core.strip() and not core.rstrip().endswith(","):
        separator = ","

    module_path_literal = json.dumps(f"./{module_path}", ensure_ascii=False)
    entry = (
        "\n    {\n"
        f'      "name": "{module_id}",\n'
        f'      "srcPath": {module_path_literal}\n'
        "    }"
    )
    new_body = core + separator + entry + trailing
    return text[: start + 1] + new_body + text[end:]


def render_templates(module_root: Path, module_id: str, display_name: str) -> None:
    escaped_display_name = json.dumps(display_name, ensure_ascii=False)[1:-1]
    for path in module_root.rglob("*"):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rendered = content.replace(MODULE_TOKEN, module_id).replace(
            DISPLAY_TOKEN, escaped_display_name
        )
        path.write_text(rendered, encoding="utf-8")


def add_local_dependency(
    package_path: Path, dependency_name: str, dependency_path: str
) -> None:
    try:
        package = json.loads(package_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise InitializationError(f"Invalid package manifest: {package_path}") from error
    dependencies = package.get("dependencies")
    if not isinstance(dependencies, dict):
        raise InitializationError(
            f'Package manifest must contain a "dependencies" object: {package_path}'
        )
    if dependency_name in dependencies:
        raise InitializationError(
            f'Dependency "{dependency_name}" already exists in {package_path}'
        )
    dependencies[dependency_name] = f"file:{dependency_path}"
    package_path.write_text(
        json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def write_manifest_atomically(path: Path, content: str) -> None:
    original_mode = path.stat().st_mode
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(content)
        os.chmod(temporary_path, original_mode)
        os.replace(temporary_path, path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def validate_result(
    target: Path,
    provider_target: Path,
    manifest_text: str,
    module_id: str,
    module_path: str,
    provider_id: str,
    provider_path: str,
    provider_dependency_path: str,
) -> None:
    missing = [relative for relative in REQUIRED_PATHS if not (target / relative).is_file()]
    if missing:
        raise InitializationError(f"Missing required files: {', '.join(missing)}")

    missing_directories = [
        relative for relative in EMPTY_DIRECTORIES if not (target / relative).is_dir()
    ]
    if missing_directories:
        raise InitializationError(
            f"Missing required directories: {', '.join(missing_directories)}"
        )

    unexpected = [relative for relative in EXCLUDED_PATHS if (target / relative).exists()]
    if unexpected:
        raise InitializationError(f"Unexpected paths created: {', '.join(unexpected)}")

    missing_provider = [
        relative
        for relative in PROVIDER_REQUIRED_PATHS
        if not (provider_target / relative).is_file()
    ]
    if missing_provider:
        raise InitializationError(
            f"Missing required provider files: {', '.join(missing_provider)}"
        )
    missing_provider_directories = [
        relative
        for relative in PROVIDER_EMPTY_DIRECTORIES
        if not (provider_target / relative).is_dir()
    ]
    if missing_provider_directories:
        raise InitializationError(
            "Missing required provider directories: "
            + ", ".join(missing_provider_directories)
        )
    provider_ets_root = provider_target / "src/main/ets"
    provider_ets_files = [
        str(path.relative_to(provider_target))
        for path in provider_ets_root.rglob("*")
        if path.is_file()
    ]
    if provider_ets_files:
        raise InitializationError(
            f"Provider ETS directory must be empty: {', '.join(provider_ets_files)}"
        )
    provider_unexpected = [
        relative for relative in EXCLUDED_PATHS if (provider_target / relative).exists()
    ]
    if provider_unexpected:
        raise InitializationError(
            f"Unexpected provider paths created: {', '.join(provider_unexpected)}"
        )

    unresolved = []
    for path in target.rglob("*"):
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            if MODULE_TOKEN in content or DISPLAY_TOKEN in content:
                unresolved.append(str(path.relative_to(target)))
    if unresolved:
        raise InitializationError(f"Unresolved template tokens: {', '.join(unresolved)}")

    start, end = find_array(manifest_text, "modules")
    body = manifest_text[start + 1 : end]
    count = len(re.findall(rf'"name"\s*:\s*"{re.escape(module_id)}"', body))
    provider_count = len(
        re.findall(rf'"name"\s*:\s*"{re.escape(provider_id)}"', body)
    )
    expected_path = f'"srcPath": {json.dumps(f"./{module_path}", ensure_ascii=False)}'
    expected_provider_path = (
        f'"srcPath": {json.dumps(f"./{provider_path}", ensure_ascii=False)}'
    )
    if (
        count != 1
        or provider_count != 1
        or expected_path not in body
        or expected_provider_path not in body
    ):
        raise InitializationError("Root module registration validation failed")

    package = json.loads((target / "oh-package.json5").read_text(encoding="utf-8"))
    expected_dependency = f"file:{provider_dependency_path}"
    if package.get("dependencies", {}).get(provider_id) != expected_dependency:
        raise InitializationError("Business-module provider dependency validation failed")


def initialize(
    project_root: Path,
    module_id: str,
    display_name: str,
    modules_dir: Path = Path("features"),
) -> dict[str, object]:
    if not MODULE_ID_RE.fullmatch(module_id):
        raise InitializationError(
            "module_id must start with a lowercase letter and contain only "
            "lowercase letters, digits, or underscores"
        )

    project_root = project_root.expanduser().resolve()
    if modules_dir.is_absolute() or ".." in modules_dir.parts or modules_dir == Path("."):
        raise InitializationError(
            "modules_dir must be a relative project path without parent traversal"
        )

    manifest_path = project_root / "build-profile.json5"
    modules_root = (project_root / modules_dir).resolve()
    try:
        modules_root.relative_to(project_root)
    except ValueError as error:
        raise InitializationError(
            "modules_dir must resolve inside the project root"
        ) from error
    target = modules_root / module_id
    module_path = (modules_dir / module_id).as_posix()
    template_root = Path(__file__).resolve().parent.parent / "assets" / "module-template"
    provider_template_root = (
        Path(__file__).resolve().parent.parent / "assets" / "provider-template"
    )
    providers_root = (project_root / PROVIDERS_DIRECTORY).resolve()
    try:
        providers_root.relative_to(project_root)
    except ValueError as error:
        raise InitializationError(
            "providers directory must resolve inside the project root"
        ) from error
    provider_id = f"{module_id}{PROVIDER_SUFFIX}"
    provider_target = providers_root / provider_id
    provider_path = (PROVIDERS_DIRECTORY / provider_id).as_posix()

    if not manifest_path.is_file():
        raise InitializationError(f"Missing project manifest: {manifest_path}")
    if not modules_root.is_dir():
        raise InitializationError(f"Missing modules directory: {modules_root}")
    if not template_root.is_dir():
        raise InitializationError(f"Missing template directory: {template_root}")
    if not provider_template_root.is_dir():
        raise InitializationError(
            f"Missing provider template directory: {provider_template_root}"
        )
    if target.exists():
        raise InitializationError(f"Target already exists: {target}")
    if provider_target.exists():
        raise InitializationError(f"Provider target already exists: {provider_target}")

    original_manifest = manifest_path.read_text(encoding="utf-8")
    updated_manifest = update_project_manifest(original_manifest, module_id, module_path)
    updated_manifest = update_project_manifest(
        updated_manifest, provider_id, provider_path
    )
    provider_dependency_path = os.path.relpath(provider_target, target).replace(
        os.sep, "/"
    )

    providers_root_created = not providers_root.exists()
    manifest_written = False
    try:
        shutil.copytree(template_root, target)
        providers_root.mkdir(parents=True, exist_ok=True)
        shutil.copytree(provider_template_root, provider_target)
        render_templates(target, module_id, display_name)
        render_templates(provider_target, provider_id, f"{display_name} Provider")
        for relative in EMPTY_DIRECTORIES:
            (target / relative).mkdir(parents=True, exist_ok=True)
        for relative in PROVIDER_EMPTY_DIRECTORIES:
            (provider_target / relative).mkdir(parents=True, exist_ok=True)
        (target / "consumer-rules.txt").write_text("", encoding="utf-8")
        (provider_target / "consumer-rules.txt").write_text("", encoding="utf-8")
        add_local_dependency(
            target / "oh-package.json5", provider_id, provider_dependency_path
        )
        write_manifest_atomically(manifest_path, updated_manifest)
        manifest_written = True
        final_manifest = manifest_path.read_text(encoding="utf-8")
        validate_result(
            target,
            provider_target,
            final_manifest,
            module_id,
            module_path,
            provider_id,
            provider_path,
            provider_dependency_path,
        )
    except Exception:
        try:
            if manifest_written and manifest_path.exists():
                write_manifest_atomically(manifest_path, original_manifest)
        finally:
            if target.exists():
                shutil.rmtree(target)
            if provider_target.exists():
                shutil.rmtree(provider_target)
            if providers_root_created and providers_root.exists():
                try:
                    providers_root.rmdir()
                except OSError:
                    pass
        raise

    created_files = sorted(
        str(path.relative_to(project_root)) for path in target.rglob("*") if path.is_file()
    )
    created_directories = sorted(
        str(path.relative_to(project_root)) for path in target.rglob("*") if path.is_dir()
    )
    provider_created_files = sorted(
        str(path.relative_to(project_root))
        for path in provider_target.rglob("*")
        if path.is_file()
    )
    provider_created_directories = sorted(
        str(path.relative_to(project_root))
        for path in provider_target.rglob("*")
        if path.is_dir()
    )
    return {
        "module_id": module_id,
        "display_name": display_name,
        "modules_dir": modules_dir.as_posix(),
        "module_path": module_path,
        "module_root": str(target),
        "provider_id": provider_id,
        "provider_path": provider_path,
        "provider_root": str(provider_target),
        "provider_dependency": f"file:{provider_dependency_path}",
        "manifest_updated": str(manifest_path),
        "created_files": created_files,
        "created_directories": created_directories,
        "provider_created_files": provider_created_files,
        "provider_created_directories": provider_created_directories,
    }


def main() -> int:
    args = parse_args()
    display_name = args.display_name if args.display_name is not None else args.module_id
    try:
        summary = initialize(
            args.project_root, args.module_id, display_name, args.modules_dir
        )
    except (InitializationError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
