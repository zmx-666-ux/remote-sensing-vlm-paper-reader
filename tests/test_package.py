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

    def test_word_template_sections(self):
        from docx import Document

        path = ROOT / "skills" / "remote-sensing-vlm-paper-reader" / "assets" / "paper-note-template.docx"
        doc = Document(path)
        headings = [p.text.strip() for p in doc.paragraphs if p.style.name.startswith("Heading")]
        required = [
            "论文身份信息",
            "一句话问题与核心结论",
            "阅读前置知识",
            "方法流程",
            "关键图表",
            "关键公式",
            "实验与证据",
            "主张、证据与推断",
            "局限与失败条件",
            "对研究台账的影响",
            "主动回忆",
            "PDF页码索引",
        ]
        self.assertEqual(headings, required)

    def test_workbook_structure_and_status_lists(self):
        from openpyxl import load_workbook

        path = ROOT / "skills" / "remote-sensing-vlm-paper-reader" / "assets" / "research-ledger-template.xlsx"
        wb = load_workbook(path)
        visible = [ws.title for ws in wb.worksheets if ws.sheet_state == "visible"]
        self.assertEqual(visible, ["论文索引", "创新假设", "模块方法库", "跨论文对比", "概念术语", "待读问题"])
        self.assertEqual(wb["_配置"].sheet_state, "hidden")
        for name in visible:
            ws = wb[name]
            self.assertEqual(ws.freeze_panes, "A2")
            self.assertTrue(ws.auto_filter.ref)
        innovation_values = [wb["_配置"][f"B{i}"].value for i in range(2, 12)]
        self.assertIn("被已有工作覆盖", innovation_values)
        self.assertIn("已否定", innovation_values)


if __name__ == "__main__":
    unittest.main()
