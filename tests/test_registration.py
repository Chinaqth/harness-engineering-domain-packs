from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = (
    REPO_ROOT
    / ".agents"
    / "skills"
    / "register-domain-pack"
    / "scripts"
    / "register_domain_pack.py"
)
SPEC = importlib.util.spec_from_file_location("register_domain_pack", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class RegistrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        shutil.copytree(
            REPO_ROOT / "domains" / "_template",
            self.root / "domains" / "_template",
        )
        (self.root / "registry").mkdir()
        shutil.copy2(
            REPO_ROOT / "registry" / "domains.json",
            self.root / "registry" / "domains.json",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def register(self, dry_run: bool = False) -> Path:
        return MODULE.register_domain(
            self.root,
            "engineering.ios",
            "iOS Engineering",
            "ios-platform-team",
            "Owns reusable iOS delivery practice and evaluation.",
            dry_run,
        )

    def test_registration_creates_contract_and_registry_entry(self) -> None:
        domain_path = self.register()
        manifest = json.loads((domain_path / "domain.json").read_text(encoding="utf-8"))
        registry = json.loads(
            (self.root / "registry" / "domains.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["id"], "engineering.ios")
        self.assertEqual(manifest["status"], "draft")
        self.assertEqual(registry["domains"][0]["path"], "domains/engineering/ios")

    def test_duplicate_is_rejected(self) -> None:
        self.register()
        with self.assertRaises(MODULE.RegistrationError):
            self.register()

    def test_dry_run_does_not_write(self) -> None:
        domain_path = self.register(dry_run=True)
        self.assertFalse(domain_path.exists())
        registry = json.loads(
            (self.root / "registry" / "domains.json").read_text(encoding="utf-8")
        )
        self.assertEqual(registry["domains"], [])

    def test_invalid_id_is_rejected(self) -> None:
        with self.assertRaises(MODULE.RegistrationError):
            MODULE.register_domain(
                self.root,
                "iOS",
                "iOS Engineering",
                "ios-platform-team",
                "Description",
            )

    def test_json_sensitive_values_are_encoded_safely(self) -> None:
        domain_path = MODULE.register_domain(
            self.root,
            "engineering.web",
            'Web "Platform"',
            "web-platform-team",
            'Owns "web" delivery.\nIncludes browser evaluation.',
        )
        manifest = json.loads((domain_path / "domain.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["display_name"], 'Web "Platform"')
        self.assertIn("\n", manifest["description"])

    def test_registry_commit_failure_rolls_back_domain(self) -> None:
        registry_before = (
            self.root / "registry" / "domains.json"
        ).read_text(encoding="utf-8")
        with mock.patch.object(MODULE.os, "replace", side_effect=OSError("simulated")):
            with self.assertRaises(MODULE.RegistrationError):
                self.register()
        self.assertFalse((self.root / "domains" / "engineering" / "ios").exists())
        self.assertEqual(
            (self.root / "registry" / "domains.json").read_text(encoding="utf-8"),
            registry_before,
        )

    def test_owner_must_be_single_line(self) -> None:
        with self.assertRaises(MODULE.RegistrationError):
            MODULE.register_domain(
                self.root,
                "engineering.ios",
                "iOS Engineering",
                "ios-team\nother-team",
                "Description",
            )


if __name__ == "__main__":
    unittest.main()
