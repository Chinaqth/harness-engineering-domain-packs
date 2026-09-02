from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DomainExecutionPlanConfirmationTests(unittest.TestCase):
    def test_active_mutating_domains_declare_current_kernel_and_checkpoint(self) -> None:
        registry = json.loads((ROOT / "registry" / "domains.json").read_text(encoding="utf-8"))
        for entry in registry["domains"]:
            if entry["status"] != "active":
                continue
            manifest = json.loads(
                (ROOT / entry["path"] / "domain.json").read_text(encoding="utf-8")
            )
            workflow = (ROOT / entry["path"] / "workflows" / "WORKFLOW.md").read_text(
                encoding="utf-8"
            )
            with self.subTest(domain=entry["id"]):
                self.assertEqual(manifest["compatibility"]["kernel_protocol_version"], "3.0")
                self.assertIn("Domain Execution Plan", workflow)
                self.assertIn("changes/<change-id>/task.md", workflow)
                self.assertIn("complete", workflow.lower())
                self.assertIn("digest", workflow.lower())

    def test_every_mutating_published_skill_declares_checkpoint(self) -> None:
        paths = [
            "domains/engineering/harmonyos/skills/harmonyos-engineering/SKILL.md",
            "domains/engineering/harmonyos/skills/hmos-arkts-deprecated-interface-checker/SKILL.md",
            "domains/engineering/harmonyos/skills/hmos-arkts-syntax-checker/SKILL.md",
            "domains/engineering/harmonyos/skills/hmos-arkui-develop-skill/SKILL.md",
            "domains/engineering/harmonyos/skills/hmos-arkui-statemgt-migration/SKILL.md",
            "domains/engineering/harmonyos/skills/hmos-business-module-development/SKILL.md",
            "domains/engineering/harmonyos/skills/hmos-init-business-module/SKILL.md",
            "domains/engineering/web/skills/web-interface-delivery/SKILL.md",
        ]
        for relative in paths:
            text = (ROOT / relative).read_text(encoding="utf-8")
            with self.subTest(skill=relative):
                self.assertIn("Mandatory Domain Execution Plan Checkpoint", text)
                self.assertIn("changes/<change-id>/task.md", text)
                self.assertIn("complete", text.lower())
                self.assertIn("digest", text.lower())


if __name__ == "__main__":
    unittest.main()
