# Company-Dashboard Mapping Review Tool Notes

Use this when implementing or reviewing Phase 2 real-data onboarding work in `Company-Dashboard`, especially mapping generation between `raw/*.raw.json` spreadsheet captures and `schema.sql`.

## Durable lessons

- The mapping tool belongs to the extraction/load layer, not presentation. If it is a canonical root tool, add it to `test_project_structure.py` root allow-list in the same commit.
- Keep it dependency-light. CI did not install `pytest` for project tests, so new root tests should use stdlib `unittest` unless CI is intentionally updated to install a test framework.
- Treat generated mapping files as drafts. Low-confidence matches should be omitted, not guessed into `columns`; the operator must review required fields and constants before running `map_raw_to_db.py`.
- Raw spreadsheet captures store rows under `content.sheets[].cells`; the first row is typically the header. Do not invent a `headers` key in tests unless the extractor actually emits one.
- For bilingual matching, combine:
  1. exact source header to schema column,
  2. known bilingual patterns,
  3. `extractor.arabic.match_key()` for Arabic spelling variants,
  4. conservative substring matching after normalizing underscores/spaces on both sides.
- If adding a new project gate, update all three places together: `.github/workflows/ci.yml`, `AGENTS.md` rule 4, and any structure guard allow-list.

## Verification pattern

Run focused checks first:

```bash
python3 test_mapping_tool.py
python3 test_project_structure.py
```

Then run a real dry-run fixture:

```bash
tmp=$(mktemp -d)
mkdir -p "$tmp/raw"
# create a spreadsheet raw JSON fixture with Year/Version/Period + metrics
python3 mapping_tool.py --raw "$tmp/raw" --output "$tmp/mapping.json" --report "$tmp/review.html"
python3 map_raw_to_db.py --mapping "$tmp/mapping.json" --raw "$tmp/raw" --db "$tmp/pl_detail.db" --dry-run
```

Then run the full project gate before merge/push.

## Push/main safety

When Mohamed explicitly asks to merge/push to `main`, prefer a non-destructive sequence:

```bash
git fetch origin
git checkout main
git pull --ff-only origin main
git merge --ff-only <feature-branch>
git push origin main
```

Avoid bundling `git reset --hard` into the same command unless the user explicitly approves discarding local main state; approval gates may block it as destructive.