from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / ".agents"
    / "skills"
    / "complete-domain-pack"
    / "scripts"
    / "finalize_domain_pack.py"
)
SPEC = importlib.util.spec_from_file_location("finalize_domain_pack", SCRIPT)
FINALIZER = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(FINALIZER)


class AutoActivationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.domain = self.root / "domains" / "engineering" / "web"
        self.domain.mkdir(parents=True)
        (self.root / "registry").mkdir()
        self.registry_path = self.root / "registry" / "domains.json"
        self.registry_path.write_text(
            json.dumps({
                "schema_version": "1.0",
                "domains": [{
                    "id": "engineering.web",
                    "path": "domains/engineering/web",
                    "version": "0.1.0",
                    "status": "draft",
                    "owner": "platform-web",
                }],
            }),
            encoding="utf-8",
        )
        (self.domain / "domain.json").write_text(
            json.dumps({"id": "engineering.web", "status": "draft"}),
            encoding="utf-8",
        )
        self.ledger = self.root / "sources.json"
        self.ledger.write_text("{}\n", encoding="utf-8")
        self.session = self.root / "session.json"
        self.session.write_text("{}\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def checker(self, complete: bool = True) -> SimpleNamespace:
        result = {
            "content_state": "content-complete" if complete else "incomplete",
            "verdict": "pass" if complete else "fail",
            "content_issues": [] if complete else ["routes missing"],
        }
        return SimpleNamespace(check_pack=lambda root, domain_id, ledger: result)

    def session_validator(self, valid: bool = True) -> SimpleNamespace:
        result = {"valid": valid, "issues": [] if valid else ["final evaluation missing"]}
        return SimpleNamespace(
            validate_session=lambda root, session, require_final=False: result
        )

    def test_content_complete_draft_is_activated_in_both_documents(self) -> None:
        with (
            mock.patch.object(FINALIZER, "_load_pack_checker", return_value=self.checker()),
            mock.patch.object(
                FINALIZER, "_load_session_validator", return_value=self.session_validator()
            ),
        ):
            FINALIZER.finalize_domain(
                self.root, "engineering.web", self.ledger, self.session
            )
        registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        manifest = json.loads((self.domain / "domain.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["domains"][0]["status"], "active")
        self.assertEqual(manifest["status"], "active")

    def test_incomplete_draft_is_not_activated(self) -> None:
        with mock.patch.object(
            FINALIZER, "_load_pack_checker", return_value=self.checker(complete=False)
        ), mock.patch.object(
            FINALIZER, "_load_session_validator", return_value=self.session_validator()
        ):
            with self.assertRaises(FINALIZER.FinalizationError):
                FINALIZER.finalize_domain(
                    self.root, "engineering.web", self.ledger, self.session
                )
        registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        self.assertEqual(registry["domains"][0]["status"], "draft")

    def test_dry_run_does_not_change_lifecycle(self) -> None:
        with mock.patch.object(
            FINALIZER, "_load_pack_checker", return_value=self.checker()
        ), mock.patch.object(
            FINALIZER, "_load_session_validator", return_value=self.session_validator()
        ):
            FINALIZER.finalize_domain(
                self.root, "engineering.web", self.ledger, self.session, dry_run=True
            )
        manifest = json.loads((self.domain / "domain.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["status"], "draft")

    def test_only_synchronized_drafts_can_be_finalized(self) -> None:
        manifest_path = self.domain / "domain.json"
        manifest_path.write_text(
            json.dumps({"id": "engineering.web", "status": "active"}),
            encoding="utf-8",
        )
        with self.assertRaises(FINALIZER.FinalizationError):
            FINALIZER.finalize_domain(
                self.root, "engineering.web", self.ledger, self.session
            )

    def test_missing_final_evaluation_blocks_activation(self) -> None:
        with (
            mock.patch.object(FINALIZER, "_load_pack_checker", return_value=self.checker()),
            mock.patch.object(
                FINALIZER,
                "_load_session_validator",
                return_value=self.session_validator(valid=False),
            ),
        ):
            with self.assertRaises(FINALIZER.FinalizationError):
                FINALIZER.finalize_domain(
                    self.root, "engineering.web", self.ledger, self.session
                )
        registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        self.assertEqual(registry["domains"][0]["status"], "draft")

    def test_second_write_failure_restores_both_documents(self) -> None:
        original_replace = FINALIZER._replace_bytes
        calls = 0

        def fail_registry_once(path: Path, value: bytes) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated registry replacement failure")
            original_replace(path, value)

        with (
            mock.patch.object(FINALIZER, "_load_pack_checker", return_value=self.checker()),
            mock.patch.object(
                FINALIZER, "_load_session_validator", return_value=self.session_validator()
            ),
            mock.patch.object(FINALIZER, "_replace_bytes", side_effect=fail_registry_once),
        ):
            with self.assertRaises(FINALIZER.FinalizationError):
                FINALIZER.finalize_domain(
                    self.root, "engineering.web", self.ledger, self.session
                )

        registry = json.loads(self.registry_path.read_text(encoding="utf-8"))
        manifest = json.loads((self.domain / "domain.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["domains"][0]["status"], "draft")
        self.assertEqual(manifest["status"], "draft")


if __name__ == "__main__":
    unittest.main()
