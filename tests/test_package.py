import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_manifest_identity(self):
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(
            manifest["$schema"],
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        )
        self.assertEqual(manifest["name"], "remote-sensing-vlm-paper-reader")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(manifest["license"], "MIT")

    def test_compatibility_manifest_matches_portable_identity(self):
        portable = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        compatibility = json.loads(
            (ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(compatibility["name"], portable["name"])
        self.assertEqual(compatibility["version"], portable["version"])

    def test_required_root_files(self):
        for relative in (
            "plugin.json",
            ".codex-plugin/plugin.json",
            "LICENSE",
            "README.md",
            "README_zh-CN.md",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_skill_entrypoint_and_references(self):
        skill = ROOT / "skills" / "remote-sensing-vlm-paper-reader"
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: remote-sensing-vlm-paper-reader", text)
        self.assertIn("description: Use when", text)
        self.assertIn("Paper Pilot", text)
        self.assertIn("local PDF", text)
        for name in (
            "deep-reading-protocol.md",
            "remote-sensing-vlm-framework.md",
            "paper-note-schema.md",
            "research-ledger-schema.md",
            "update-policy.md",
        ):
            self.assertTrue((skill / "references" / name).is_file(), name)
            self.assertIn(f"references/{name}", text)


if __name__ == "__main__":
    unittest.main()
