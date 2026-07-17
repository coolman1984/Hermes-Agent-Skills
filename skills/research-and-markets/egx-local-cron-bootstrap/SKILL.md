---
name: egx-local-cron-bootstrap
description: "Bootstrap and harden a local-only EGX workflow in Hermes: fail-loud daily report generation, JSON sidecar output, decision memo gating, and cron setup on Android/Proot without systemd conflicts."
---

# egx-local-cron-bootstrap

## When to use
Use this skill when you need to stand up or harden a local-only EGX workflow that:
- reads only local Obsidian files
- writes a daily Markdown report plus a JSON sidecar
- emits a clear ERROR report on parsing/input failures
- generates a separate decision memo from the daily output
- schedules the workflow with Hermes cron
- runs in environments where `market gateway start` can fail because systemd is unavailable

## What this skill is for
This skill captures the stable pattern learned from iterating on the EGX system:
- keep analysis local-only until external data is intentionally added later
- treat empty or suspicious parsed output as a failure, not something to patch manually
- make the daily report and decision memo two separate steps
- prefer a human-review gate in rules before any actual execution
- verify cron state after creation

## Required files
Typical local inputs:
- /root/Documents/Obsidian Vault/egx_system/portfolio/positions.csv
- /root/Documents/Obsidian Vault/egx_system/portfolio/watchlist.txt
- /root/Documents/Obsidian Vault/egx_system/portfolio/rules.md
- /root/Documents/Obsidian Vault/egx_system/playbook/investment_constitution.md
- /root/Documents/Obsidian Vault/egx_system/playbook/sector_map.md
- /root/Documents/Obsidian Vault/egx_system/playbook/workflow.md

Typical outputs:
- /root/Documents/Obsidian Vault/egx_system/reports/daily/daily-local-review-YYYY-MM-DD.md
- /root/Documents/Obsidian Vault/egx_system/reports/daily/daily-local-review-YYYY-MM-DD.json
- /root/Documents/Obsidian Vault/egx_system/reports/daily/daily-local-review-YYYY-MM-DD-ERROR.md
- /root/Documents/Obsidian Vault/egx_system/reports/daily/decision-local-review-YYYY-MM-DD.md
- /root/Documents/Obsidian Vault/egx_system/reports/daily/decision-local-review-YYYY-MM-DD-ERROR.md

## Core workflow
1. Verify the input files exist and are readable.
2. Parse `positions.csv` fully; parse `watchlist.txt` fully.
3. Build counts and buckets:
   - positions_count
   - status_counts
   - core_positions
   - review_positions
   - reduce_positions
   - exit_positions
   - rule_violations
   - missing_data
4. Fail loudly if parsing is suspicious:
   - positions_count <= 0
   - status counts do not sum to positions_count
   - core_positions is empty
   - key sections cannot be built
   - watchlist is missing or unreadable
5. If parsing is valid, write:
   - a Markdown report with a strict header
   - a JSON sidecar containing only the allowed fields
6. If parsing fails, write an ERROR Markdown report instead of a normal report.
7. Run a separate decision-gate step on the latest valid daily Markdown + JSON.
8. Create a human-review gate in rules so local reports are not treated as execution authority.
9. Create cron jobs only after the outputs are stable.

## Strict daily Markdown header
The daily Markdown should always start with:
- date
- creation time
- analysis mode: local-only
- web available: no
- avg_cost: complete / missing
- data source
- signature / run label

## Required daily sections
If the run is valid, the daily report should include:
- summary
- core positions
- review positions
- reduce positions
- exit positions
- rule violations
- proposed decision
- confidence
- missing data

## Required JSON fields
The JSON sidecar should contain only these fields:
- date
- positions_count
- watchlist_count
- status_counts
- core_positions
- review_positions
- reduce_positions
- exit_positions
- rule_violations
- confidence
- missing_data
- analysis_mode
- report_path

## Decision memo workflow
The decision-gate step should:
1. Read the latest daily Markdown and matching JSON.
2. Verify that the pair is valid and dates match.
3. Compare the result against portfolio rules and the investment constitution.
4. Write a short decision memo or an ERROR memo.

## Decision memo sections
A valid decision memo should include:
- summary of decision
- whether the core stays as-is
- review positions
- reduce priorities
- exit priorities
- rule/constitution violations
- final decision: hold / incremental add / reduce / monitor / no action
- confidence
- blockers to higher confidence
- later data needed

## Cron bootstrap on Android / Proot
Important: `market gateway start` may fail if it tries to use systemd.

Preferred pattern:
1. Check `market` exists.
2. Start the gateway with `market gateway run` if `market gateway start` fails.
3. Confirm it is still running with `market cron status` or process polling.
4. Create only the minimal jobs needed.
5. Verify the job list after creation.
6. Make sure the profile model/provider is actually authenticated; a stale provider selection can break cron jobs even when the gateway is up.

Example local-only jobs:
- daily refresh
- decision memo
- weekly review

Cron weekday ranges use standard cron numbering: `1-5` for Mon-Fri. Do not use `0-4` unless you explicitly want Sunday-Thursday drift.

## Cron creation pattern
Use Hermes cron create with:
- a clear `--name`
- `--deliver local`
- attached skills as needed
- a self-contained prompt

Keep jobs simple. Do not create cron recursively from cron.

## Pitfalls
- Do not trust a report that looks formatted but parsed to zero rows.
- Do not silently fix parsing errors by hand inside the skill.
- Do not use web until the local-only workflow is stable.
- Do not assume `market gateway start` works in Proot/Android; it may require `market gateway run`.
- Do not treat decision memos as execution authority; require a human-review rule.
- Do not guess `avg_cost` values if they are not available from a real source.
- If the decision step returns `[SILENT]`, verify whether it actually wrote a new memo or merely detected no new content; do not assume the file was updated.

## Verification
Before considering the setup complete:
- `market cron list` shows the expected jobs only
- `market cron status` shows the scheduler running
- the latest daily report exists and has a matching JSON sidecar
- the decision memo exists and matches the daily pair
- the rules file includes a human-review gate

## Reuse notes
This skill is reusable whenever you need a hardened local-only reporting pipeline with:
- fail-loud parsing
- JSON sidecars
- separate decision gating
- cron scheduling
- Android/Proot Hermes gateway startup quirks
