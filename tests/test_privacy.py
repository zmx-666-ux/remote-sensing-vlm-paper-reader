import re
import subprocess
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".json", ".yaml", ".yml", ".py", ".txt", ".gitignore"}
FORBIDDEN = [
    re.compile(r"C:\\Users\\12890", re.I),
    re.compile(r"zhangmuxin2021@163\.com", re.I),
    re.compile(r"github_pat_[A-Za-z0-9_]+"),
    re.compile(r"ghp_[A-Za-z0-9]+"),
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
]


def release_files():
    """Yield tracked and non-ignored candidate files, never ignored local QA data."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    for raw_name in result.stdout.split(b"\0"):
        if raw_name:
            yield ROOT / raw_name.decode("utf-8")


def iter_text():
    for path in release_files():
        if not path.is_file():
            continue
        label = str(path.relative_to(ROOT))
        if path.suffix.lower() in TEXT_EXTENSIONS:
            yield label, path.read_text(encoding="utf-8", errors="ignore")
        elif path.suffix.lower() in {".docx", ".xlsx"}:
            with zipfile.ZipFile(path) as archive:
                for name in archive.namelist():
                    if name.endswith(".xml"):
                        content = archive.read(name).decode("utf-8", errors="ignore")
                        yield f"{label}::{name}", content


class PrivacyTests(unittest.TestCase):
    def test_no_pdf_files(self):
        pdfs = [str(path.relative_to(ROOT)) for path in release_files() if path.suffix.lower() == ".pdf"]
        self.assertEqual(pdfs, [])

    def test_no_private_markers(self):
        failures = []
        for source, content in iter_text():
            for pattern in FORBIDDEN:
                if pattern.search(content):
                    failures.append(f"{source}: {pattern.pattern}")
        self.assertEqual(failures, [])
