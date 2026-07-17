#!/usr/bin/env python3
"""Verify a standalone Arabic interactive book-explainer HTML artifact.

Usage:
  python verify_interactive_html.py /path/to/page.html "عنوان مطلوب" "قسم مطلوب"
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
import tempfile


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.skip = False
        self.text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.skip = True

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.skip = False

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.text.append(data.strip())


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: verify_interactive_html.py <html-path> [required text...]")
        return 2

    path = Path(sys.argv[1])
    required = sys.argv[2:]
    if not path.exists():
        print(f"FAIL missing file: {path}")
        return 1
    if path.stat().st_size <= 0:
        print(f"FAIL empty file: {path}")
        return 1

    html = path.read_text(encoding="utf-8")
    missing = [item for item in required if item not in html]
    if missing:
        print("FAIL missing required text:", missing)
        return 1

    if "<style" not in html or "</style>" not in html:
        print("FAIL missing embedded CSS")
        return 1
    if "<script" not in html or "</script>" not in html:
        print("FAIL missing embedded JavaScript")
        return 1

    parser = VisibleTextParser()
    parser.feed(html)
    mixed = []
    for item in parser.text:
        if re.search(r"[\u0600-\u06FF]", item) and re.search(r"[A-Za-z]", item):
            mixed.append(item)
    if mixed:
        print("FAIL visible mixed Arabic/English lines:")
        for item in mixed[:20]:
            print(item)
        return 1

    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.S)
    if scripts:
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as tmp:
            tmp.write("\n".join(scripts))
            tmp_path = tmp.name
        try:
            result = subprocess.run(["node", "--check", tmp_path], text=True, capture_output=True)
            if result.returncode != 0:
                print("FAIL JavaScript syntax check")
                print(result.stdout)
                print(result.stderr)
                return 1
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    print("OK", path, path.stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
