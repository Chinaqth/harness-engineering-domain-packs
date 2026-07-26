from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_registry.py"
REGISTER_PATH = (
    ROOT
    / ".agents"
    / "skills"
    / "register-domain-pack"
    / "scripts"
    / "register_domain_pack.py"
)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_module("validate_registry", VALIDATOR_PATH)
REGISTER = load_module("register_domain_pack_for_registry", REGISTER_PATH)


class RegistryValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "domains", self.root / "domains")
        shutil.copytree(ROOT / "schemas", self.root / "schemas")
        shutil.copytree(ROOT / "registry", self.root / "registry")
        self.domain = REGISTER.register_domain(
            self.root,
            "engineering.ios",
            "iOS Engineering",
            "ios-platform-team",
            "Owns reusable iOS delivery practice and evaluation.",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, value: dict) -> None:
        (self.domain / relative).write_text(
            json.dumps(value, indent=2) + "\n", encoding="utf-8"
        )

    def activate_registry_and_manifest(self) -> dict:
        registry_path = self.root / "registry" / "domains.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["domains"][0]["status"] = "active"
        registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

        manifest_path = self.domain / "domain.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["status"] = "active"
        manifest["compatibility"]["statement"] = "Compatible with Kernel protocol 1.0."
        manifest["activation"]["evidence"] = ["tests/activation-evidence.md"]
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        return manifest

    def test_schema_invalid_active_pack_is_rejected(self) -> None:
        self.activate_registry_and_manifest()
        self.write(
            "routes.json",
            {
                "schema_version": "1.0",
                "domain_id": "engineering.ios",
                "routes": [{"id": "feature", "capabilities": ["delivery"]}],
            },
        )
        self.write(
            "capabilities.json",
            {
                "schema_version": "1.0",
                "domain_id": "engineering.ios",
                "capabilities": [{"id": "delivery"}],
            },
        )
        self.write(
            "owners.json",
            {
                "schema_version": "1.0",
                "domain_id": "engineering.ios",
                "primary_owner": "ios-platform-team",
                "reviewers": ["mobile-architecture"],
            },
        )
        errors = VALIDATOR.validate(self.root)
        self.assertTrue(any("missing required property" in error for error in errors))
        self.assertTrue(any("must define evaluators" in error for error in errors))

    def test_complete_active_pack_passes(self) -> None:
        self.activate_registry_and_manifest()
        self.write(
            "routes.json",
            {
                "schema_version": "1.0",
                "domain_id": "engineering.ios",
                "routes": [
                    {
                        "id": "feature",
                        "priority": 100,
                        "task_types": ["feature"],
                        "signals": ["swift"],
                        "capabilities": ["delivery"],
                    }
                ],
            },
        )
        self.write(
            "capabilities.json",
            {
                "schema_version": "1.0",
                "domain_id": "engineering.ios",
                "capabilities": [
                    {
                        "id": "delivery",
                        "description": "Deliver an iOS feature.",
                        "task_types": ["feature"],
                        "workflows": ["WORKFLOW.md"],
                        "skills": [],
                        "tools": [],
                        "evaluators": ["EVALUATOR.md"],
                        "permissions": [],
                        "dependencies": [],
                    }
                ],
            },
        )
        self.write(
            "owners.json",
            {
                "schema_version": "1.0",
                "domain_id": "engineering.ios",
                "primary_owner": "ios-platform-team",
                "reviewers": ["mobile-architecture"],
            },
        )
        self.assertEqual(VALIDATOR.validate(self.root), [])

    def test_unknown_dependency_is_rejected(self) -> None:
        capabilities_path = self.domain / "capabilities.json"
        capabilities = json.loads(capabilities_path.read_text(encoding="utf-8"))
        capabilities["capabilities"] = [
            {
                "id": "delivery",
                "description": "Deliver an iOS feature.",
                "task_types": ["feature"],
                "workflows": [],
                "skills": [],
                "tools": [],
                "evaluators": [],
                "permissions": [],
                "dependencies": ["security.review"],
            }
        ]
        capabilities_path.write_text(
            json.dumps(capabilities, indent=2) + "\n", encoding="utf-8"
        )
        self.assertTrue(
            any("unknown dependency" in error for error in VALIDATOR.validate(self.root))
        )


if __name__ == "__main__":
    unittest.main()
