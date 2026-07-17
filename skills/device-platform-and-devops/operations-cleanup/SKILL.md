---
name: operations-cleanup
description: Operations and cleanup for OpenClaw workspace hygiene, maintainability,
  clutter reduction, safe reversible cleanup, duplication removal, and cost/load reduction.
  Use when inspecting waste, reducing clutter, logging meaningful changes, or proposing
  cleanup actions.
tags: [cleanup, operations, maintenance, declutter, housekeeping]
---

# Operations / Cleanup

## Use this skill
Use when the goal is to keep the system lean, organized, and healthy.

## Operating model
1. Inspect the area for clutter, waste, duplication, and stale artifacts.
2. Identify what is safe to remove, consolidate, or keep.
3. Prefer reversible cleanup actions.
4. Explain impact before major cleanup.
5. Record meaningful changes.

## Cleanup rules
- Preserve safety first.
- Do not remove critical assets casually.
- Prefer the smallest cleanup that reduces waste.
- Call out duplicated config, stale files, and unused wrappers.
- Keep logs of meaningful changes.

## Output format
Always return:
- Area inspected
- Problems found
- Recommended actions
- Risk level
- Cleanup log

## Use the references
- Read `references/cleanup-playbook.md` for the default inspection checklist when you need a more specific cleanup pass.
- Read `references/hermes-proot-performance-audit.md` when Mohamed asks to inspect assistant/system performance in Hermes/OpenClaw, especially in Android PRoot/no-systemd environments.

## Hermes/OpenClaw performance cleanup notes
When cleaning the live assistant system:
- Trust process lists, logs, and state files over service status in PRoot/no-systemd setups.
- Look for long-lived stale tool processes before blaming the model or Telegram.
- Move stale gateway state files to a backup directory if their PID is gone; do not delete blindly.
- Clean only old, low-risk temporary artifacts, never broad-delete `/tmp`.
- Do not start secondary profile gateways casually because they may reuse the Telegram bot token.
