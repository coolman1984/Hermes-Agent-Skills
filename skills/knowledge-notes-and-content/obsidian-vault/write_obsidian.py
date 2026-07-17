#!/usr/bin/env python3
"""
write_obsidian.py — Create Obsidian Topic and Research files from fetched sources.
Usage: python3 write_obsidian.py [--topic "Topic Name"] [--question "Research question"]
Reads from Knowledge/Sources/_sources_meta.json
"""
import sys
import json
import re
import argparse
from pathlib import Path
from datetime import datetime

SOURCES_DIR = Path("Knowledge/Sources")
TOPICS_DIR = Path("Knowledge/Topics")
RESEARCH_DIR = Path("Knowledge/Research")

def load_sources():
    meta_file = SOURCES_DIR / "_sources_meta.json"
    if not meta_file.exists():
        print(f"❌ No metadata found. Run yt_transcript.py first.")
        print(f"   Expected: {meta_file}")
        sys.exit(1)
    with open(meta_file) as f:
        return json.load(f)

def extract_topics_from_sources(sources):
    """Auto-detect topics from video titles."""
    topics = {}
    for src in sources:
        title = src.get("title", "")
        # Split by common separators
        parts = re.split(r"[:\-\"\"|\[\]()", title)
        words = []
        for part in parts:
            # Filter for significant words
            cleaned = " ".join(
                w for w in part.split()
                if len(w) > 3
                and w.lower() not in {
                    "the", "and", "for", "with", "this", "that", "from",
                    "your", "what", "how", "why", "when", "about",
                }
            ).strip()
            if cleaned and len(cleaned) > 2:
                words.append(cleaned)

        # Use first 2-3 significant words as topic candidates
        if words:
            topic_candidate = words[0]
            if topic_candidate not in topics:
                topics[topic_candidate] = []
            topics[topic_candidate].append(src)

    return topics

def write_topic_files(sources):
    """Create one Topic file per detected topic, linking all relevant sources."""
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)

    topics = extract_topics_from_sources(sources)
    written = []

    for topic_name, related_sources in topics.items():
        safe = re.sub(r'[^\w\s-]', '', topic_name)[:60].strip()
        safe = "-".join(safe.split()) or "topic"
        topic_file = TOPICS_DIR / f"Topic-{safe}.md"

        lines = [
            f"# {topic_name}",
            "",
            f"> Created: {datetime.now().strftime('%Y-%m-%d')}",
            "",
            "## Overview",
            "",
            "*(Add your overview here)*",
            "",
            "## Key Insights",
            "",
            "*(Add insights from sources)*",
            "",
            "## Related Sources",
            "",
        ]

        for src in related_sources:
            title = src.get("title", "Untitled")
            channel = src.get("channel", "")
            url = src.get("url", "")
            mins = src.get("duration_mins", 0)
            file_name = Path(src.get("file", "")).name

            lines.extend([
                f"- [[{file_name[:-3]}]]",
                f"  - {channel} | {mins} min",
                f"  - [{title}]({url})",
                "",
            ])

        lines.extend([
            "## Notes",
            "",
            "*(Add your notes)*",
            "",
            f"**Tags:** #topic #{safe}",
        ])

        with open(topic_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        written.append(topic_file.name)
        print(f"  📌 Topic: {topic_file.name}")

    return written

def write_research_file(question, answer, citations, sources):
    """Create a Research file from an answered question."""
    RESEARCH_DIR.mkdir(parents=True, exist_ok=True)

    # Build safe filename from question
    safe_q = re.sub(r'[^\w\s]', '', question)[:60].strip()
    safe_q = "-".join(safe_q.split()) or "research"
    date_str = datetime.now().strftime("%Y-%m-%d")
    research_file = RESEARCH_DIR / f"Research-{date_str}-{safe_q}.md"

    lines = [
        f"# {question}",
        "",
        f"> **Asked:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Answer",
        "",
        answer,
        "",
        "## Key Citations",
        "",
    ]

    for i, cite in enumerate(citations, 1):
        src = next((s for s in sources if s["vid"] == cite.get("vid")), {})
        ts = cite.get("timestamp", "?")
        text = cite.get("text", "")[:200]
        url = src.get("url", "")
        title = src.get("title", "Source")
        file_name = Path(src.get("file", "")).name

        lines.extend([
            f"**[{i}]** [[{file_name[:-3]}]] — {ts}",
            f"> {text}...",
            f"[Watch at {ts}]({url}&t={cite.get('seconds', 0)}s)",
            "",
        ])

    lines.extend([
        "## Raw Sources",
        "",
    ])
    for src in sources:
        lines.append(f"- [[{Path(src.get('file','?')).name[:-3]}]] — {src['channel']}")

    lines.extend([
        "",
        f"**Tags:** #research",
    ])

    with open(research_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n  📄 Research file: {research_file.name}")
    return research_file

def build_index():
    """Create or update a master index file."""
    index_file = Path("Knowledge") / "INDEX.md"
    lines = [
        "# Knowledge Base",
        "",
        f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Sources",
        f"Total: {len(list(SOURCES_DIR.glob('Source-*.md')))} videos",
        "",
        "## Topics",
        f"Total: {len(list(TOPICS_DIR.glob('Topic-*.md'))} topics",
        "",
        "## Recent Research",
    ]

    for rf in sorted(RESEARCH_DIR.glob("Research-*.md"), reverse=True)[:10]:
        mtime = datetime.fromtimestamp(rf.stat().st_mtime).strftime("%Y-%m-%d")
        lines.append(f"- [[{rf.stem}]] — {mtime}")

    lines.extend(["", "## Quick Links", "", " [[Topic-All Topics]]", " [[Research-All Research]]"])

    with open(index_file, "w") as f:
        f.write("\n".join(lines))

    print(f"  📋 Index: {index_file.name}")
    return index_file

def main():
    parser = argparse.ArgumentParser(description="Create Obsidian Topic and Research files")
    parser.add_argument("--topic", dest="topic", help="Topic name to create")
    parser.add_argument("--question", dest="question", help="Research question")
    parser.add_argument("--answer", dest="answer", help="Answer text")
    parser.add_argument("--citations", dest="citations_file", help="JSON file with citations")
    args = parser.parse_args()

    sources = load_sources()
    print(f"\n📚 Found {len(sources)} sources\n")

    # Write topic files for all detected topics
    print("Creating Topic files...")
    write_topic_files(sources)

    # Build index
    build_index()

    print("\n✅ Obsidian vault updated!")

if __name__ == "__main__":
    main()
