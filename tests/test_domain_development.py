from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


SCORER = load_module(
    "score_domain_evaluation",
    ROOT
    / ".agents"
    / "skills"
    / "evaluate-domain-artifact"
    / "scripts"
    / "score_evaluation.py",
)
SESSION = load_module(
    "validate_domain_session",
    ROOT
    / ".agents"
    / "skills"
    / "complete-domain-pack"
    / "scripts"
    / "validate_session.py",
)
RESEARCH = load_module(
    "validate_domain_research",
    ROOT
    / ".agents"
    / "skills"
    / "complete-domain-pack"
    / "scripts"
    / "validate_research.py",
)
PACK = load_module(
    "check_domain_pack",
    ROOT
    / ".agents"
    / "skills"
    / "evaluate-domain-pack"
    / "scripts"
    / "check_pack.py",
)
SKILLS = load_module(
    "validate_repository_skills",
    ROOT / "scripts" / "validate_skills.py",
)
AGENTS = load_module(
    "validate_project_agents",
    ROOT / "scripts" / "validate_agents.py",
)


def raw_evaluation(score: int = 91) -> dict:
    return {
        "schema_version": "1.0",
        "evaluator": "independent-test-evaluator",
        "iteration": 1,
        "evaluated_at": "2026-07-29T00:00:00Z",
        "source_ids": ["android-official"],
        "dimensions": {
            name: score for name in SCORER.DIMENSION_WEIGHTS
        },
        "hard_gates": {
            name: True for name in SCORER.HARD_GATES
        },
        "findings": [],
        "blocked_reasons": [],
    }


class EvaluationScoringTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.artifact = Path(self.temp.name) / "artifact.md"
        self.artifact.write_text("# Artifact\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_score_must_be_strictly_greater_than_ninety(self) -> None:
        passing = SCORER.normalize(raw_evaluation(91), self.artifact, "artifact.md")
        failing = SCORER.normalize(raw_evaluation(90), self.artifact, "artifact.md")
        self.assertEqual(passing["overall_score"], 91)
        self.assertEqual(passing["verdict"], "pass")
        self.assertEqual(failing["overall_score"], 90)
        self.assertEqual(failing["verdict"], "fail")

    def test_p1_finding_overrides_high_score(self) -> None:
        raw = raw_evaluation(100)
        raw["findings"] = [
            {
                "severity": "p1",
                "summary": "Invented owner approval",
                "evidence": "No authoritative owner record was provided.",
            }
        ]
        result = SCORER.normalize(raw, self.artifact, "artifact.md")
        self.assertEqual(result["overall_score"], 100)
        self.assertEqual(result["verdict"], "fail")

    def test_hard_gate_overrides_high_score(self) -> None:
        raw = raw_evaluation(100)
        raw["hard_gates"]["kernel_constraints_preserved"] = False
        result = SCORER.normalize(raw, self.artifact, "artifact.md")
        self.assertEqual(result["verdict"], "fail")

    def test_evaluation_requires_traceable_source_ids(self) -> None:
        raw = raw_evaluation(100)
        raw["source_ids"] = []
        with self.assertRaises(SCORER.EvaluationError):
            SCORER.normalize(raw, self.artifact, "artifact.md")

    def test_cli_requires_explicit_session_artifact_label(self) -> None:
        with mock.patch("sys.stderr", new=io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                SCORER.main(
                    [
                        "--artifact",
                        str(self.artifact),
                        "--input",
                        str(Path(self.temp.name) / "raw.json"),
                        "--output",
                        str(Path(self.temp.name) / "evaluation.json"),
                    ]
                )
        self.assertEqual(raised.exception.code, 2)

    def test_missing_evidence_produces_blocked(self) -> None:
        raw = raw_evaluation(100)
        raw["blocked_reasons"] = ["Domain owner source is unavailable."]
        result = SCORER.normalize(raw, self.artifact, "artifact.md")
        self.assertEqual(result["verdict"], "blocked")


class SessionValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.domain = self.root / "domains" / "engineering" / "android"
        self.domain.mkdir(parents=True)
        (self.root / "registry").mkdir()
        (self.root / "registry" / "domains.json").write_text(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "domains": [
                        {
                            "id": "engineering.android",
                            "path": "domains/engineering/android",
                            "version": "0.1.0",
                            "status": "draft",
                            "owner": "platform-android",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        self.artifact = self.domain / "DOMAIN.md"
        self.artifact.write_text("# Android Engineering\n", encoding="utf-8")
        self.change = self.root / "changes" / "android"
        (self.change / "evaluations").mkdir(parents=True)
        (self.change / "research").mkdir()
        (self.change / "research" / "capability-map.md").write_text(
            "# Capability Map\n\nSource: android-official\n", encoding="utf-8"
        )
        (self.change / "research" / "responsibility-boundaries.md").write_text(
            "# Responsibility Boundaries\n\nSource: android-official\n",
            encoding="utf-8",
        )
        (self.change / "research" / "sources.json").write_text(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "domain_id": "engineering.android",
                    "generated_at": "2026-07-30T00:00:00Z",
                    "sources": [
                        {
                            "id": "android-official",
                            "kind": "web",
                            "title": "Android Developers",
                            "publisher": "Google",
                            "locator": "https://developer.android.com/",
                            "authority": "primary",
                            "retrieved_at": "2026-07-30T00:00:00Z",
                            "claims": ["Android application delivery guidance."],
                        },
                        {
                            "id": "kotlin-official",
                            "kind": "web",
                            "title": "Kotlin Documentation",
                            "publisher": "JetBrains",
                            "locator": "https://kotlinlang.org/docs/home.html",
                            "authority": "primary",
                            "retrieved_at": "2026-07-30T00:00:00Z",
                            "claims": ["Kotlin language guidance."],
                        },
                        {
                            "id": "registry-record",
                            "kind": "repository",
                            "title": "Domain Registry",
                            "publisher": "Harness Domain Packs",
                            "locator": "registry/domains.json",
                            "authority": "repository-fact",
                            "retrieved_at": "2026-07-30T00:00:00Z",
                            "claims": ["Registered identity and owner."],
                        },
                    ],
                    "capability_hypotheses": [
                        {
                            "id": "application-delivery",
                            "description": "Deliver Android application changes.",
                            "source_ids": ["android-official", "kotlin-official"],
                        }
                    ],
                    "organizational_gaps": [],
                }
            ),
            encoding="utf-8",
        )
        artifact_evaluation = SCORER.normalize(
            raw_evaluation(92), self.artifact, "DOMAIN.md"
        )
        (self.change / "evaluations" / "DOMAIN.1.json").write_text(
            json.dumps(artifact_evaluation),
            encoding="utf-8",
        )
        self.session = self.change / "session.json"
        self.session.write_text(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "domain_id": "engineering.android",
                    "research_ledger": "research/sources.json",
                    "max_artifact_iterations": 5,
                    "max_pack_iterations": 3,
                    "artifacts": [
                        {
                            "path": "DOMAIN.md",
                            "evaluations": ["evaluations/DOMAIN.1.json"],
                        }
                    ],
                    "final_evaluations": [],
                }
            ),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_current_passing_artifact_is_valid(self) -> None:
        result = SESSION.validate_session(self.root, self.session)
        self.assertTrue(result["valid"], result["issues"])

    def test_changed_artifact_invalidates_evaluation(self) -> None:
        self.artifact.write_text("# Changed Android Engineering\n", encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session)
        self.assertFalse(result["valid"])
        self.assertTrue(any("stale artifact digest" in item for item in result["issues"]))

    def test_incomplete_normalized_record_is_rejected(self) -> None:
        path = self.change / "evaluations" / "DOMAIN.1.json"
        evaluation = json.loads(path.read_text(encoding="utf-8"))
        del evaluation["dimensions"]
        path.write_text(json.dumps(evaluation), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session)
        self.assertFalse(result["valid"])
        self.assertTrue(any("dimensions are incomplete" in item for item in result["issues"]))

    def test_evaluation_source_must_exist_in_research_ledger(self) -> None:
        path = self.change / "evaluations" / "DOMAIN.1.json"
        evaluation = json.loads(path.read_text(encoding="utf-8"))
        evaluation["source_ids"] = ["invented-source"]
        path.write_text(json.dumps(evaluation), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session)
        self.assertFalse(result["valid"])
        self.assertTrue(
            any("wrong research ledger" in item for item in result["issues"])
        )

    def test_final_evaluation_is_required_on_delivery(self) -> None:
        result = SESSION.validate_session(self.root, self.session, require_final=True)
        self.assertFalse(result["valid"])
        self.assertIn("A final Pack evaluation is required", result["issues"])

    def test_final_evaluation_cannot_escape_change_directory(self) -> None:
        session = json.loads(self.session.read_text(encoding="utf-8"))
        session["final_evaluations"] = ["../../outside.json"]
        self.session.write_text(json.dumps(session), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session, require_final=True)
        self.assertFalse(result["valid"])
        self.assertTrue(
            any("Final evaluation escapes change directory" in item for item in result["issues"])
        )

    def test_current_final_directory_evaluation_is_valid(self) -> None:
        final_evaluation = SCORER.normalize(
            raw_evaluation(94), self.domain, "."
        )
        (self.change / "evaluations" / "final.1.json").write_text(
            json.dumps(final_evaluation),
            encoding="utf-8",
        )
        session = json.loads(self.session.read_text(encoding="utf-8"))
        session["final_evaluations"] = ["evaluations/final.1.json"]
        self.session.write_text(json.dumps(session), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session, require_final=True)
        self.assertTrue(result["valid"], result["issues"])

    def test_final_session_must_declare_every_production_file(self) -> None:
        (self.domain / "domain.json").write_text("{}\n", encoding="utf-8")
        final_evaluation = SCORER.normalize(
            raw_evaluation(94), self.domain, "."
        )
        (self.change / "evaluations" / "final.1.json").write_text(
            json.dumps(final_evaluation),
            encoding="utf-8",
        )
        session = json.loads(self.session.read_text(encoding="utf-8"))
        session["final_evaluations"] = ["evaluations/final.1.json"]
        self.session.write_text(json.dumps(session), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session, require_final=True)
        self.assertFalse(result["valid"])
        self.assertIn(
            "Production artifact is not declared in session: domain.json",
            result["issues"],
        )

    def test_every_final_evaluation_history_record_must_exist(self) -> None:
        final_evaluation = SCORER.normalize(
            raw_evaluation(94), self.domain, "."
        )
        (self.change / "evaluations" / "final.3.json").write_text(
            json.dumps(final_evaluation),
            encoding="utf-8",
        )
        session = json.loads(self.session.read_text(encoding="utf-8"))
        session["final_evaluations"] = [
            "evaluations/missing.1.json",
            "evaluations/missing.2.json",
            "evaluations/final.3.json",
        ]
        self.session.write_text(json.dumps(session), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session, require_final=True)
        self.assertFalse(result["valid"])
        self.assertTrue(
            any("Cannot read valid JSON" in item for item in result["issues"])
        )

    def test_non_converging_low_scores_are_reported(self) -> None:
        evaluation_paths = []
        for iteration, score in enumerate((85, 86, 87), start=1):
            raw = raw_evaluation(score)
            raw["iteration"] = iteration
            evaluation = SCORER.normalize(raw, self.artifact, "DOMAIN.md")
            relative = f"evaluations/DOMAIN.{iteration}.json"
            (self.change / relative).write_text(
                json.dumps(evaluation),
                encoding="utf-8",
            )
            evaluation_paths.append(relative)
        session = json.loads(self.session.read_text(encoding="utf-8"))
        session["artifacts"][0]["evaluations"] = evaluation_paths
        self.session.write_text(json.dumps(session), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session)
        self.assertFalse(result["valid"])
        self.assertTrue(
            any("Non-converging evaluation history" in item for item in result["issues"])
        )

    def test_final_failing_artifact_iteration_exhausts_budget(self) -> None:
        evaluation_paths = []
        for iteration, score in enumerate((80, 82, 84, 86, 88), start=1):
            raw = raw_evaluation(score)
            raw["iteration"] = iteration
            evaluation = SCORER.normalize(raw, self.artifact, "DOMAIN.md")
            relative = f"evaluations/DOMAIN.{iteration}.json"
            (self.change / relative).write_text(
                json.dumps(evaluation),
                encoding="utf-8",
            )
            evaluation_paths.append(relative)
        session = json.loads(self.session.read_text(encoding="utf-8"))
        session["artifacts"][0]["evaluations"] = evaluation_paths
        self.session.write_text(json.dumps(session), encoding="utf-8")
        result = SESSION.validate_session(self.root, self.session)
        self.assertFalse(result["valid"])
        self.assertIn(
            "Artifact iteration budget exhausted for DOMAIN.md",
            result["issues"],
        )


class RepositoryIntegrationTests(unittest.TestCase):
    def test_repository_skills_are_valid(self) -> None:
        self.assertEqual(SKILLS.validate(ROOT), [])

    def test_evaluation_skill_declares_session_artifact_label(self) -> None:
        skill = (
            ROOT
            / ".agents"
            / "skills"
            / "evaluate-domain-artifact"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("--artifact-label <artifact-relative-path>", skill)
        self.assertIn("Use `.` for the whole-Pack evaluation", skill)

    def test_project_agents_are_valid(self) -> None:
        self.assertEqual(AGENTS.validate(ROOT), [])

    def test_draft_android_pack_is_not_activation_ready(self) -> None:
        result = PACK.check_pack(ROOT, "engineering.android")
        self.assertEqual(result["verdict"], "fail")
        self.assertTrue(
            any("Activation readiness gate failed" in item for item in result["issues"])
        )

    def test_activation_evidence_must_resolve_to_a_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertTrue(
                PACK.activation_evidence_issues(root, ["changes/missing/evidence.json"])
            )
            evidence = root / "changes" / "android" / "evidence.json"
            evidence.parent.mkdir(parents=True)
            evidence.write_text("{}\n", encoding="utf-8")
            readme = root / "README.md"
            readme.write_text("# Not activation evidence\n", encoding="utf-8")
            self.assertTrue(PACK.activation_evidence_issues(root, ["README.md"]))
            self.assertTrue(
                PACK.activation_evidence_issues(root, ["changes/../README.md"])
            )
            self.assertEqual(
                PACK.activation_evidence_issues(
                    root, ["changes/android/evidence.json"]
                ),
                [],
            )


class ResearchContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "registry").mkdir()
        (self.root / "registry" / "domains.json").write_text("{}\n", encoding="utf-8")
        self.ledger = self.root / "changes" / "android" / "research" / "sources.json"
        self.ledger.parent.mkdir(parents=True)
        (self.ledger.parent / "capability-map.md").write_text(
            "# Capability Map\n\nSource: android\n", encoding="utf-8"
        )
        (self.ledger.parent / "responsibility-boundaries.md").write_text(
            "# Responsibility Boundaries\n\nSource: android\n", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def valid_ledger(self) -> dict:
        return {
            "schema_version": "1.0",
            "domain_id": "engineering.android",
            "generated_at": "2026-07-30T00:00:00Z",
            "sources": [
                {
                    "id": "android",
                    "kind": "web",
                    "title": "Android Developers",
                    "publisher": "Google",
                    "locator": "https://developer.android.com/",
                    "authority": "primary",
                    "retrieved_at": "2026-07-30T00:00:00Z",
                    "claims": ["Android platform guidance."],
                },
                {
                    "id": "kotlin",
                    "kind": "web",
                    "title": "Kotlin",
                    "publisher": "JetBrains",
                    "locator": "https://kotlinlang.org/docs/home.html",
                    "authority": "primary",
                    "retrieved_at": "2026-07-30T00:00:00Z",
                    "claims": ["Kotlin language guidance."],
                },
                {
                    "id": "registry",
                    "kind": "repository",
                    "title": "Registry",
                    "publisher": "Harness",
                    "locator": "registry/domains.json",
                    "authority": "repository-fact",
                    "retrieved_at": "2026-07-30T00:00:00Z",
                    "claims": ["Registered Domain identity."],
                },
            ],
            "capability_hypotheses": [
                {
                    "id": "delivery",
                    "description": "Deliver Android application changes.",
                    "source_ids": ["android", "kotlin"],
                }
            ],
            "organizational_gaps": [
                {
                    "id": "reviewer",
                    "description": "Required reviewer is unknown.",
                    "required_for_activation": True,
                }
            ],
        }

    def test_valid_research_ledger_passes(self) -> None:
        self.ledger.write_text(json.dumps(self.valid_ledger()), encoding="utf-8")
        errors, source_ids = RESEARCH.validate_ledger(
            self.root, self.ledger, "engineering.android"
        )
        self.assertEqual(errors, [])
        self.assertEqual(source_ids, {"android", "kotlin", "registry"})

    def test_research_requires_supporting_analysis_outputs(self) -> None:
        self.ledger.write_text(json.dumps(self.valid_ledger()), encoding="utf-8")
        (self.ledger.parent / "capability-map.md").unlink()
        errors, _ = RESEARCH.validate_ledger(
            self.root, self.ledger, "engineering.android"
        )
        self.assertTrue(any("Missing research output" in item for item in errors))

    def test_supporting_analysis_must_cite_source_id(self) -> None:
        self.ledger.write_text(json.dumps(self.valid_ledger()), encoding="utf-8")
        (self.ledger.parent / "capability-map.md").write_text(
            "# Capability Map\n\nNo source citation.\n", encoding="utf-8"
        )
        errors, _ = RESEARCH.validate_ledger(
            self.root, self.ledger, "engineering.android"
        )
        self.assertTrue(any("must cite an authoritative source ID" in item for item in errors))

    def test_research_requires_two_authoritative_web_sources(self) -> None:
        ledger = self.valid_ledger()
        ledger["sources"] = ledger["sources"][1:]
        self.ledger.write_text(json.dumps(ledger), encoding="utf-8")
        errors, _ = RESEARCH.validate_ledger(
            self.root, self.ledger, "engineering.android"
        )
        self.assertTrue(any("at least two authoritative HTTPS" in item for item in errors))

    def test_research_requires_repository_identity_source(self) -> None:
        ledger = self.valid_ledger()
        ledger["sources"] = [
            source for source in ledger["sources"] if source["kind"] != "repository"
        ]
        self.ledger.write_text(json.dumps(ledger), encoding="utf-8")
        errors, _ = RESEARCH.validate_ledger(
            self.root, self.ledger, "engineering.android"
        )
        self.assertTrue(any("repository identity source" in item for item in errors))

    def test_capability_hypothesis_requires_professional_source(self) -> None:
        ledger = self.valid_ledger()
        ledger["capability_hypotheses"][0]["source_ids"] = ["registry"]
        self.ledger.write_text(json.dumps(ledger), encoding="utf-8")
        errors, _ = RESEARCH.validate_ledger(
            self.root, self.ledger, "engineering.android"
        )
        self.assertTrue(
            any("authoritative professional web source" in item for item in errors)
        )


class PackStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.domain = self.root / "domains" / "engineering" / "android"
        self.domain.mkdir(parents=True)
        (self.root / "registry").mkdir()
        (self.root / "registry" / "domains.json").write_text(
            json.dumps(
                {
                    "domains": [
                        {
                            "id": "engineering.android",
                            "path": "domains/engineering/android",
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        (self.root / "changes" / "android").mkdir(parents=True)
        self.ledger = self.root / "changes" / "android" / "sources.json"
        self.write_domain(reviewers=[])
        self.write_ledger(with_gap=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_domain(self, reviewers: list[str]) -> None:
        evidence = self.root / "changes" / "android" / "evidence.json"
        evidence.write_text("{}\n", encoding="utf-8")
        (self.domain / "domain.json").write_text(
            json.dumps(
                {
                    "applicability": {
                        "task_types": ["implementation"],
                        "repository_signals": ["AndroidManifest.xml"],
                    },
                    "compatibility": {"statement": "Compatible with protocol 1.0."},
                    "activation": {"evidence": ["changes/android/evidence.json"]},
                }
            ),
            encoding="utf-8",
        )
        (self.domain / "owners.json").write_text(
            json.dumps({"reviewers": reviewers}), encoding="utf-8"
        )
        (self.domain / "routes.json").write_text(
            json.dumps(
                {
                    "routes": [
                        {
                            "id": "delivery",
                            "priority": 100,
                            "task_types": ["implementation"],
                            "signals": ["AndroidManifest.xml"],
                            "capabilities": ["delivery"],
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        (self.domain / "capabilities.json").write_text(
            json.dumps(
                {
                    "capabilities": [
                        {
                            "id": "delivery",
                            "task_types": ["implementation"],
                            "workflows": ["WORKFLOW.md"],
                            "evaluators": ["EVALUATOR.md"],
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )

    def write_ledger(self, with_gap: bool) -> None:
        self.ledger.write_text(
            json.dumps(
                {
                    "organizational_gaps": (
                        [
                            {
                                "id": "reviewer",
                                "description": "Reviewer is unknown.",
                                "required_for_activation": True,
                            }
                        ]
                        if with_gap
                        else []
                    )
                }
            ),
            encoding="utf-8",
        )

    def run_check(self) -> dict:
        registry_validator = SimpleNamespace(validate=lambda root: [])
        research_validator = SimpleNamespace(
            validate_ledger=lambda root, ledger, domain_id: ([], {"source"})
        )
        with (
            mock.patch.object(PACK, "load_registry_validator", return_value=registry_validator),
            mock.patch.object(PACK, "load_research_validator", return_value=research_validator),
        ):
            return PACK.check_pack(
                self.root, "engineering.android", self.ledger
            )

    def test_content_can_pass_while_organization_input_is_missing(self) -> None:
        result = self.run_check()
        self.assertEqual(result["content_state"], "content-complete")
        self.assertEqual(result["content_verdict"], "pass")
        self.assertEqual(result["state"], "needs-org-input")

    def test_activation_ready_requires_no_organization_gaps(self) -> None:
        self.write_domain(reviewers=["mobile-architecture"])
        self.write_ledger(with_gap=False)
        result = self.run_check()
        self.assertEqual(result["content_state"], "content-complete")
        self.assertEqual(result["state"], "activation-ready")


if __name__ == "__main__":
    unittest.main()
