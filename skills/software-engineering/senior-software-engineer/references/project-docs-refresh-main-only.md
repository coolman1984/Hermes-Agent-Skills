# Main-only project documentation refresh pattern

Use when Mohamed asks to review what is on GitHub `main`, update docs to match the current code, and push back to `main`.

## Branch discipline

- Treat “main only” literally.
- Start from:

```bash
git checkout main
git pull --ff-only origin main
git status --short --branch
git rev-parse --short HEAD
```

- Do not inspect, merge, or rely on other branches unless required to identify a safety issue.

## Audit shape

1. Inventory user-facing capabilities from README/ROADMAP and code.
2. Run the app or artifact, not just tests.
3. Inspect actual behavior in the important modes. For Mohamed’s dashboard work, include Arabic desktop, Arabic mobile, and English toggle checks.
4. Compare docs, handoff notes, CI config, requirements files, tests, and code.
5. Patch stale docs and small code defects discovered by the audit.
6. Add/strengthen tests when a docs claim depends on behavior not previously asserted.

## Dynamic UI translation gotcha

Browser-rendered text can bypass static translation maps when inserted by app code after load. After changing translation maps:

- Reload the app in Arabic mode.
- Query visible headings/buttons/table cells for remaining English text.
- If text still appears, either route the source string through the app translation helper or add a regex/exact dynamic rule that the mutation observer will catch.

## Completion gate

Before saying it is done:

```bash
npm test
python3 -m extractor.test_arabic
python3 -m extractor.test_extractor
python3 test_map_raw_to_db.py
python3 -m reports.test_reports
python3 -m reports.test_render
python3 -m reports.test_scenario
python3 -m brain.test_brain
python3 -m brain.cli --check
git diff --check
git status --short --branch
```

Then commit on `main`, push, and verify the GitHub Actions run for the pushed SHA.

If interrupted before push, report: changes are local only; not uploaded; list remaining steps.