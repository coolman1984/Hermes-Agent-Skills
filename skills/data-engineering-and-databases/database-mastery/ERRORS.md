# Database Mastery Error Log

Use this file as first-read operational memory for database tasks.

## 2026-07-07 — Row explosion from joining facts at different grains

- Symptom: Budget-vs-actual totals became too high after joining sales lines to a monthly budget table.
- Root cause: The fact table was at order-line grain while budget was at product-month grain; joining without pre-aggregating multiplied budget rows.
- Fix: Aggregate sales to the same month/product/region grain before joining budget, then reconcile row counts and totals.
- Prevention rule: State table grain before every join. If grains differ, aggregate or bridge first.

## 2026-07-07 — Dashboard script failed on DuckDB file lock

- Symptom: `db_to_dashboard.py` failed with a DuckDB conflicting lock while validation still had an open connection.
- Root cause: The dashboard generator opened the database in default read-write mode, which conflicts with another process holding the file.
- Fix: Open dashboard connections with `duckdb.connect(path, read_only=True)` and close write connections before external scripts when possible.
- Prevention rule: Read-only reporting scripts should open DuckDB in read-only mode.

## 2026-07-07 — Dashboard SQL failed on ambiguous alias

- Symptom: DuckDB parser failed near `month` in dashboard query.
- Root cause: The script used `month` as a bare alias after an expression; this can collide with parser expectations and is less portable.
- Fix: Use explicit `as month_label` and explicit aliases for aggregate columns.
- Prevention rule: Generated SQL examples should use explicit `AS` aliases, avoiding reserved or function-like names.

## 2026-07-07 — Skill initially missed FastAPI test dependency boundary

- Symptom: API validation can fail in a clean environment if FastAPI/httpx are not installed.
- Root cause: Scripts assumed backend libraries existed globally.
- Fix: Validation uses an isolated virtual environment and records dependencies in the backend reference.
- Prevention rule: Every runnable example must declare imports and installation needs.

## 2026-07-07 — Excel control totals can silently include bad rows

- Symptom: A messy workbook contained a negative quantity and a blank row; totals still looked plausible.
- Root cause: Control totals only checked total sales, not invalid business rules.
- Fix: Add validation for non-negative quantity/price, required product/date, and duplicate row identifiers.
- Prevention rule: Reconcile both arithmetic totals and business-validity counts.
