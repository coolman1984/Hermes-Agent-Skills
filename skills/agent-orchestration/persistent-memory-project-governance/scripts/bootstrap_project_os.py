#!/usr/bin/env python3
"""Bootstrap Mohamed's file-based project operating system.

Usage:
  python bootstrap_project_os.py /path/to/project
  python bootstrap_project_os.py /path/to/project --force
"""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

DIRS = [
    "00_control",
    "01_inputs/raw_files",
    "01_inputs/user_notes",
    "01_inputs/references",
    "02_understanding",
    "03_design",
    "04_execution/working_files",
    "04_execution/code",
    "04_execution/configs",
    "04_execution/generated_outputs",
    "04_execution/temporary_outputs",
    "05_validation/tests",
    "06_final_outputs/final_files",
    "07_archive/old_attempts",
    "07_archive/rejected_paths",
    "07_archive/previous_versions",
    "07_archive/obsolete_rules",
]

FILES = {
    "00_control/mission.md": "# Mission\n\n## Current mission\n\n## Practical objective\n\n## Why it matters\n",
    "00_control/project_scope.md": "# Project Scope\n\n## In scope\n\n## Out of scope\n\n## Boundaries\n",
    "00_control/success_contract.md": "# Success Contract\n\n## Mission\n\n## Required deliverables\n\n## Acceptance criteria\n\n- [ ] \n\n## Quality criteria\n\n## Data requirements\n\n## Technical constraints\n\n## Formatting constraints\n\n## Naming rules\n\n## Validation method\n\n## Evidence required\n\n## Failure conditions\n\n## Human approval points\n\n## Final handover format\n",
    "00_control/task_queue.md": "# Task Queue\n\n| Task ID | Task name | Role | Status | Priority | Input files | Output files | Dependency | Validation | Evidence | Notes |\n|---|---|---|---|---|---|---|---|---|---|---|\n",
    "00_control/progress.md": "# Progress\n\n## Current state\n\n## Last completed task\n\n## Current pending task\n\n## Validation performed\n\n## Problems found\n\n## Next task\n\n## Confidence level\n",
    "00_control/decisions.md": "# Decisions\n\n## Decision template\n\n- Decision ID:\n- Date:\n- Decision:\n- Reason:\n- Alternatives considered:\n- Evidence:\n- Impact:\n- Risk:\n- Status:\n",
    "00_control/assumptions.md": "# Assumptions\n\n| ID | Date | Assumption | Reason | Risk level | How to verify | Impact if wrong | Status |\n|---|---|---|---|---|---|---|---|\n",
    "00_control/risks.md": "# Risks\n\n| Risk ID | Date | Risk | Cause | Impact | Probability | Mitigation | Owner | Status |\n|---|---|---|---|---|---|---|---|---|\n",
    "00_control/bottlenecks.md": "# Bottlenecks\n\n| ID | Date | Type | Description | Evidence | Smallest removal action | Status |\n|---|---|---|---|---|---|---|\n",
    "00_control/run_log.md": "# Run Log\n\n## Entry template\n\n- Timestamp:\n- Action:\n- Reason:\n- Inputs read:\n- Outputs changed:\n- Result:\n- Evidence:\n- Next step:\n",
    "00_control/evidence_log.md": "# Evidence Log\n\n| Evidence ID | Date | Claim | Evidence type | Evidence location | Verification method | Result | Confidence |\n|---|---|---|---|---|---|---|---|\n",
    "00_control/evaluation_report.md": "# Evaluation Report\n\n## Rubric scores\n\n| Criterion | Score | Notes |\n|---|---:|---|\n| Completeness |  |  |\n| Correctness |  |  |\n| Practical usefulness |  |  |\n| Clarity |  |  |\n| Robustness |  |  |\n| Simplicity |  |  |\n| Restartability |  |  |\n| Evidence quality |  |  |\n| User fit |  |  |\n| Professional quality |  |  |\n\n## Decision\n",
    "00_control/restart_notes.md": "# Restart Notes\n\n## Current mission\n\n## Current project state\n\n## Completed work\n\n## Pending work\n\n## Active constraints\n\n## Active assumptions\n\n## Known risks\n\n## Current bottleneck\n\n## Next best action\n\n## Source-of-truth files\n",
    "00_control/memory_index.md": "# Memory Index\n\n## Compressed summary\n\n## Durable project memory\n\n| Date | Category | Source | Fact or decision | Why it matters | Evidence | Related files | Status | Next action |\n|---|---|---|---|---|---|---|---|---|\n",
    "00_control/open_questions.md": "# Open Questions\n\n| ID | Question | Why it matters | Owner | Status |\n|---|---|---|---|---|\n",
    "01_inputs/source_inventory.md": "# Source Inventory\n\n| Source ID | Path/source | Purpose | Type | Read-only? | Confidence | Notes |\n|---|---|---|---|---|---|---|\n",
    "02_understanding/extracted_requirements.md": "# Extracted Requirements\n\n## Explicit requirements\n\n## Implied requirements\n\n## Missing information\n\n## Operational requirements\n\n## Hidden risks\n",
    "02_understanding/workflow_map.md": "# Workflow Map\n\n## Steps\n\n## Inputs and outputs\n\n## Dependencies\n",
    "02_understanding/logic_map.md": "# Logic Map\n\n## Rules\n\n## Calculations\n\n## Decision logic\n",
    "02_understanding/data_map.md": "# Data Map\n\n## Dataset contract template\n\n- Dataset name:\n- Source file:\n- Purpose:\n- Required columns:\n- Optional columns:\n- Key fields:\n- Expected data types:\n- Row-level meaning:\n- Known issues:\n- Validation rules:\n- Transformation rules:\n- Output mapping:\n",
    "02_understanding/terminology.md": "# Terminology\n\n| Term | Meaning | Source | Notes |\n|---|---|---|---|\n",
    "02_understanding/constraints.md": "# Constraints\n\n## Technical\n\n## Data\n\n## User\n\n## Safety\n",
    "03_design/architecture.md": "# Architecture\n\n## System/workflow design\n\n## File flow\n\n## Interfaces\n",
    "03_design/implementation_plan.md": "# Implementation Plan\n\n## Phases\n\n## Slices\n\n## Dependencies\n",
    "03_design/validation_plan.md": "# Validation Plan\n\n## Gates\n\n## Commands/checks\n\n## Evidence needed\n",
    "03_design/rollback_plan.md": "# Rollback Plan\n\n## Restart triggers\n\n## What to preserve\n\n## What to discard\n\n## Archive locations\n",
    "05_validation/test_results.md": "# Test Results\n\n| Date | Test/check | Result | Evidence | Notes |\n|---|---|---|---|---|\n",
    "05_validation/quality_checks.md": "# Quality Checks\n\n## Gate status\n\n- [ ] Mission clarity\n- [ ] Success contract exists\n- [ ] Inputs inventoried\n- [ ] Assumptions recorded\n- [ ] Output exists\n- [ ] Validation performed\n- [ ] Evidence recorded\n- [ ] Memory updated\n- [ ] Handover complete\n",
    "05_validation/error_log.md": "# Error Log\n\n| Date | What failed | Where | Likely reason | Evidence | Fix attempted | Result | Next action |\n|---|---|---|---|---|---|---|---|\n",
    "05_validation/issue_tracker.md": "# Issue Tracker\n\n| Issue ID | Date | Issue | Severity | Owner | Status | Next action |\n|---|---|---|---|---|---|---|\n",
    "06_final_outputs/final_report.md": "# Final Report\n\n## Summary\n\n## Outputs\n\n## Validation\n\n## Remaining risks\n",
    "06_final_outputs/handover_notes.md": "# Handover Notes\n\n## What was completed\n\n## Final outputs\n\n## Inputs used\n\n## Assumptions made\n\n## Validated items\n\n## Evidence\n\n## Remaining risks\n\n## Optional improvements\n\n## Recommended next action\n",
    "06_final_outputs/proof_of_completion.md": "# Proof of Completion\n\n## Success contract result\n\n## Evidence map\n\n## Validation results\n\n## Final status\n",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a restartable file-based project OS.")
    parser.add_argument("project", nargs="?", default=".", help="Project root directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    root = Path(args.project).resolve()
    root.mkdir(parents=True, exist_ok=True)
    for rel in DIRS:
        (root / rel).mkdir(parents=True, exist_ok=True)

    created = []
    skipped = []
    now = datetime.now().isoformat(timespec="seconds")
    for rel, body in FILES.items():
        path = root / rel
        if path.exists() and not args.force:
            skipped.append(rel)
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        if rel == "00_control/run_log.md":
            body += f"\n## Bootstrap\n\n- Timestamp: {now}\n- Action: Created project OS skeleton\n- Result: Structure initialized\n"
        path.write_text(body, encoding="utf-8")
        created.append(rel)

    print(f"project_root={root}")
    print(f"created_files={len(created)}")
    print(f"skipped_files={len(skipped)}")
    for rel in created:
        print(f"created: {rel}")
    for rel in skipped:
        print(f"skipped: {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
