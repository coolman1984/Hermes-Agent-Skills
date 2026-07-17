#!/usr/bin/env python3
"""
research_pipeline.py — Full YouTube → Obsidian research pipeline.
Usage:
  python3 research_pipeline.py search "query"              Step 1: search + pick
  python3 research_pipeline.py fetch                          Step 2: get transcripts
  python3 research_pipeline.py analyze "question" "answer"    Step 3: create research file
"""
import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

def run(script, *args):
    cmd = [sys.executable, str(SCRIPT_DIR / script), *args]
    result = subprocess.run(cmd)
    return result.returncode

def main():
    if len(sys.argv) < 2:
        print("""
Research Pipeline — YouTube → Obsidian Vault

Usage:
  python3 research_pipeline.py search "query" [--limit 20]
  python3 research_pipeline.py fetch [--urls file.txt]
  python3 research_pipeline.py analyze --question "Q" --answer "A"
  python3 research_pipeline.py full "query" [--limit 20]
""")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "search":
        query = " ".join(sys.argv[2:])
        limit = "--limit"
        if limit in sys.argv:
            idx = sys.argv.index(limit)
            limit_n = sys.argv[idx + 1]
            sys.argv[idx:idx+2] = []
        else:
            limit_n = "20"
        run("yt_search.py", query, "--limit", limit_n, "--save", "selected_urls.txt")

    elif cmd == "fetch":
        urls_file = "selected_urls.txt"
        run("yt_transcript.py", urls_file, "--output", "Knowledge/Sources")

    elif cmd == "analyze":
        # Parse key=value args
        question = answer = citations = None
        for arg in sys.argv[2:]:
            if arg.startswith("--question="):
                question = arg.split("=", 1)[1]
            elif arg.startswith("--answer="):
                answer = arg.split("=", 1)[1]
        if not question:
            print("❌ Provide --question='Your question'")
            sys.exit(1)
        if not answer:
            answer = "*(Add answer here after analysis)*"
        run("write_obsidian.py", "--question", question, "--answer", answer)

    elif cmd == "full":
        # Run all three steps
        query = " ".join(sys.argv[2:])
        print("\n=== STEP 1: Search YouTube ===")
        run("yt_search.py", query, "--save", "selected_urls.txt")

        print("\n=== STEP 2: Fetch Transcripts ===")
        print("(Run again with: python3 research_pipeline.py fetch)")
        print("\nOr manually pick videos from selected_urls.txt, then run:")
        print("  python3 research_pipeline.py fetch")

    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
