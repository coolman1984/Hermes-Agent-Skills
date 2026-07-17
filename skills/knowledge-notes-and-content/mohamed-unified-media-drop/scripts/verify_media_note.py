#!/usr/bin/env python3
"""Verify Mohamed unified media-drop Markdown outputs.

Usage:
  python scripts/verify_media_note.py /path/to/media-note.md [idea-note.md] [source-map.md]

Checks are intentionally deterministic and conservative:
- file exists and is non-empty
- required unified headings are present
- exactly 10 numbered use cases in section 5
- no obvious placeholders
- Arabic body lines do not contain embedded Latin words
- required enrichment provenance labels are present
- optional idea note and source-map bridge paths exist/link back when supplied
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = [
    "## 1)",
    "## 2)",
    "## 3)",
    "## 4)",
    "## 5)",
    "## 6)",
    "## 7)",
    "## 8)",
    "## 9)",
    "## 10)",
    "## 11)",
    "## 12)",
    "## 13)",
    "## 14)",
]

REQUIRED_ENRICHMENT_MARKERS = [
    "من المصدر مباشرة",
    "من البحث الإضافي",
    "قراءة عملية لمحمد",
    "ما يزال غير مؤكد",
]

ARABIC = re.compile(r"[\u0600-\u06FF]")
LATIN = re.compile(r"[A-Za-z]")
PLACEHOLDER = re.compile(r"TODO|PLACEHOLDER|\[\]|<[^>]+>")
STANDALONE_LATIN = re.compile(r"[A-Za-z0-9_ @().:/\-]+")


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def mixed_arabic_latin_lines(text: str) -> list[tuple[int, str]]:
    bad: list[tuple[int, str]] = []
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("http") or STANDALONE_LATIN.fullmatch(s):
            continue
        if ARABIC.search(s) and LATIN.search(s):
            bad.append((i, s[:180]))
    return bad


def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3, 4}:
        print(__doc__.strip())
        return 2

    media = Path(argv[1])
    if not media.exists():
        fail(f"media note missing: {media}")
    if media.stat().st_size <= 0:
        fail(f"media note empty: {media}")

    text = media.read_text(encoding="utf-8")
    missing = [h for h in REQUIRED_HEADINGS if h not in text]
    if missing:
        fail(f"missing headings: {missing}")

    if PLACEHOLDER.search(text):
        fail("placeholder-like token found")

    missing_markers = [m for m in REQUIRED_ENRICHMENT_MARKERS if m not in text]
    if missing_markers:
        fail(f"missing enrichment provenance markers: {missing_markers}")

    try:
        section_5 = text.split("## 6)", 1)[0].split("## 5)", 1)[1]
    except IndexError:
        fail("could not isolate use-case section")
    use_cases = re.findall(r"^\d+\. ", section_5, flags=re.M)
    if len(use_cases) != 10:
        fail(f"expected 10 use cases, found {len(use_cases)}")

    mixed = mixed_arabic_latin_lines(text)
    if mixed:
        print("Mixed Arabic/Latin lines:")
        for line_no, sample in mixed[:30]:
            print(f"  {line_no}: {sample}")
        fail(f"found {len(mixed)} mixed Arabic/Latin lines")

    if len(argv) >= 3:
        idea = Path(argv[2])
        if not idea.exists() or idea.stat().st_size <= 0:
            fail(f"idea note missing or empty: {idea}")

    if len(argv) == 4:
        source_map = Path(argv[3])
        if not source_map.exists() or source_map.stat().st_size <= 0:
            fail(f"source map missing or empty: {source_map}")
        sm_text = source_map.read_text(encoding="utf-8")
        if str(media) not in sm_text:
            fail("source map does not contain media note path")
        if len(argv) >= 3 and str(Path(argv[2])) not in sm_text:
            fail("source map does not contain idea note path")

    print("OK")
    print(f"media_size={media.stat().st_size}")
    if len(argv) >= 3:
        print(f"idea_size={Path(argv[2]).stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
