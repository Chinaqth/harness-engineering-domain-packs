import json, unittest, tempfile, shutil, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_registry import validate

class DomainLifecycleTests(unittest.TestCase):

    def test_active_domains_have_real_stage_skills(self):
        registry = json.loads((ROOT / 'registry/domains.json').read_text())
        names = set()
        for entry in registry['domains']:
            base = ROOT / entry['path']
            manifest = json.loads((base / 'domain.json').read_text())
            self.assertEqual(manifest['compatibility']['kernel_protocol_version'], '4.0')
            binding = json.loads((base / 'lifecycle.json').read_text())
            self.assertEqual(set(binding['stages']), {'prepare', 'execute', 'evaluate', 'summarize'})
            for (stage, relative) in binding['stages'].items():
                text = (base / relative).read_text()
                self.assertIn('context_id', text)
                self.assertNotIn('Mandatory Domain Execution Plan Checkpoint', text)
                name = text.split('name: ', 1)[1].splitlines()[0]
                self.assertNotIn(name, names)
                names.add(name)

    def test_missing_stage_detected_for_activation(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'repo'
            shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns('.git', '__pycache__'))
            p = target / 'domains/engineering/web/lifecycle.json'
            doc = json.loads(p.read_text())
            doc['stages'].pop('evaluate')
            p.write_text(json.dumps(doc))
            self.assertTrue(any(('stage evaluate' in e for e in validate(target))))

    def test_current_activation_evidence_survives_changes_cleanup(self):
        for entry in json.loads((ROOT / 'registry/domains.json').read_text())['domains']:
            base = ROOT / entry['path']
            manifest = json.loads((base / 'domain.json').read_text())
            for relative in manifest['activation']['evidence']:
                self.assertTrue((base / relative).is_file())
if __name__ == '__main__':
    unittest.main()
