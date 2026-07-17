#!/usr/bin/env python3
"""Bootstrap a Mohamed Agent Loop state folder.

Usage:
  python bootstrap_agent_loop.py /path/to/project --level minimal
  python bootstrap_agent_loop.py /path/to/project --level full
"""
from __future__ import annotations

import argparse
from pathlib import Path

TEMPLATE_MAP = {
    "minimal": [
        ("brief-contract.md", "brief-contract.md"),
        ("progress.md", "progress.md"),
        ("run-log.md", "run-log.md"),
    ],
    "full": [
        ("brief-contract.md", "brief-contract.md"),
        ("progress.md", "progress.md"),
        ("run-log.md", "run-log.md"),
        ("evaluator-findings.md", "evaluator-findings.md"),
        ("quality-rubric.md", "quality-rubric.md"),
        ("scaffolding-review.md", "scaffolding-review.md"),
        ("bottleneck-log.md", "bottleneck-log.md"),
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create .agent-loop state files from templates.")
    parser.add_argument("project", nargs="?", default=".", help="Project directory")
    parser.add_argument("--level", choices=sorted(TEMPLATE_MAP), default="minimal")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    skill_dir = script_dir.parent
    template_dir = skill_dir / "templates"
    project = Path(args.project).resolve()
    loop_dir = project / ".agent-loop"
    loop_dir.mkdir(parents=True, exist_ok=True)

    created = []
    skipped = []
    for template_name, output_name in TEMPLATE_MAP[args.level]:
        src = template_dir / template_name
        dst = loop_dir / output_name
        if dst.exists() and not args.force:
            skipped.append(str(dst))
            continue
        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        created.append(str(dst))

    print(f"loop_dir={loop_dir}")
    print(f"level={args.level}")
    print(f"created={len(created)}")
    for item in created:
        print(f"created: {item}")
    print(f"skipped={len(skipped)}")
    for item in skipped:
        print(f"skipped: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
