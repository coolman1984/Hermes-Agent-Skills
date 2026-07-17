# Database Mastery Validation Results

| Task | Result | Evidence | Fix applied |
|---|---|---|---|
| 1 ingest messy multi-sheet Excel, clean, validate totals | PASS | rows=800; expected_rows=800; total=1635764.13; invalid_rows_removed=1 | Added ERRORS.md rule: validate business rules, not only totals. |
| 2 PVM budget-vs-actual with window functions | PASS | rows=54; columns=['month', 'product', 'region', 'actual_qty', 'actual_revenue', 'actual_price', 'budget_qty', 'budget_price'] |  |
| 3 read plan and make query faster | PASS | slow=0.039723s; fast=0.002681s; speedup=14.8x; plan_has=┌───────────────────────────┐ | Reference stresses measured baseline and one-change optimization. |
| 4 FastAPI endpoint serving paginated filtered data | PASS | status=200; returned=5 |  |
| 5 self-contained HTML dashboard | PASS | bytes=2040; has_table=True | Validation exposed DuckDB lock behavior; dashboard script now opens read-only and validation closes writer before report generation. |
| 6 diagnose bad join row explosion | PASS | wrong_rows=4800; right_rows=54; wrong_budget=163036800; right_budget=1879200 | Logged row-grain join explosion in ERRORS.md. |
