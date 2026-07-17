# Phase Progression Reference — Pilot-Ready to Pilot-Operating

This reference documents the actual progression that happened after the
five deliverables from the SKILL.md landed. It is meant as a worked
example for future projects, not a script to follow blindly.

## Background

The Company-Dashboard project followed the `CLIENT_READINESS_REVIEW.md`
phases:

- **Phase 1** — Pilot-ready polish: no-visible-defects QA, demo script,
  polished Arabic report outputs, client-readable errors, locked scope.
- **Phase 2** — Real-data onboarding: per-client workspaces, mapping
  review, visible validation report, source drill-back.
- **Phase 3** — Decision product: executive narrative, scenario
  comparison, client templates, knowledge-base usefulness.

The five Phase-1 deliverables from this skill were completed and shipped
to `main` (commit `38355da`). Phase 2 #1 (import-run workspace) was
implemented on branch `mohamed/phase-2-import-workspace` immediately
after.

## What Phase 2 #1 looked like in practice

The first Phase-2 deliverable, **import-run workspace**, is the natural
follow-up to deliverable #4 (source traceability). Once a client
challenges a number, the very next question is "show me the import that
produced it" — and at that moment you need a workspace to point at.

Concrete artifacts:

- `import_workspace.py` — directory layout, history persistence with a
  50-entry cap, atomic backup/promote helpers, copy-raw-inputs helper.
- `import_workspace_cli.py` — `history` and `rollback` subcommands.
- `map_raw_to_db.py` — extended with opt-in `--client` and
  `--no-workspace` flags. Legacy behaviour is byte-for-byte equivalent.
- 23 unit tests + 3 integration tests, all green.
- README "Import-run workspaces (Phase 2)" section.
- AGENTS.md journal entry + Task Board In-Progress → Done transition.

## Pitfalls that surfaced and how they were handled

1. **Run-id collision in tight loops.** First implementation used
   second-precision timestamps. Two back-to-back runs in the same second
   silently overwrote each other. Fixed by adding a microsecond suffix
   plus a regression test.

2. **LSP / pyright false positives on `dict(possibly-int)`.**
   `dict(final_validation or {})` triggered a report-only error from
   pyright. Resolved with a `# type: ignore[arg-type]` comment, not by
   restructuring the code. Do not chase type checker noise if the code
   is correct.

3. **SyntaxError from a bad `].` typo.** A copy-paste mistake left
   `mapping["columns"].].values()` in the file. The first `node --check`
   / `python3 -c "import …"` would have caught it; a syntax-check step
   at the start of every edit-block is worth the cost.

4. **Backwards compatibility must be a test, not a promise.** The
   `--client` flag is opt-in. The integration tests include an
   explicit "no client_id keeps legacy behaviour" assertion: no
   `workspaces/` directory, no `import_history.json`, no behavioural
   change.

## How to use this reference

When the next project enters its "pilot demo done, client wants real
data" phase, do not start with the mapping review UI. Start with the
workspace + history + rollback, because:

- It is the smallest unit that lets a second operator repeat the import
  from docs alone.
- It produces artefacts (history, validation.json, backups) that the
  visible validation page in the UI will need anyway.
- It is the only safe foundation under the source drill-back work.

The order that worked: workspace → validation report UI → mapping
review → source drill-back.
