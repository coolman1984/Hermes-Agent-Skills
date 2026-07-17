---
name: database-mastery
description: Use whenever the user mentions databases, SQL, queries, DuckDB, Postgres, SQLite, data cleaning, ETL, pipelines, variance analysis, dashboards, APIs over data, Excel/CSV ingestion, reporting, or wants data extracted, calculated, modeled, validated, or presented — even if they do not say database.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [database, sql, duckdb, postgres, sqlite, etl, dashboards, fastapi, data-engineering, analytics]
    related_skills: [robust-file-extraction, senior-software-engineer]
---

# Database Mastery

## Overview

This skill routes end-to-end database and data-stack work: storage, ingestion, modeling, SQL, performance, backend APIs, dashboards, files, and governance. It is optimized for Mohamed's practical stack: messy Excel/CSV → DuckDB/Python → validated queries → dashboards/reports/APIs.

## Mandatory Start

1. Read `ERRORS.md` before touching data or writing SQL.
2. Identify the job type: ingestion, modeling, query, performance, API, dashboard, file output, or governance.
3. Profile the source data before modeling it.
4. Write the smallest safe query first, then validate row counts and control totals.
5. Present a usable artifact, not just SQL text.

## Iron Rules

- Parameterized queries always. Never interpolate user input into SQL.
- Before `UPDATE`, `DELETE`, `DROP`, `TRUNCATE`, or overwrite: run a `SELECT` preview and get explicit confirmation.
- After every load: validate row counts, null counts for key fields, duplicate keys, and control totals.
- Treat Excel/CSV as untrusted: encodings, merged headers, Arabic text, dates, formulas, and blank rows can break assumptions.
- One row grain per table. If the grain is unclear, stop and define it before aggregating.
- Never trust a dashboard number until the source query has a reconciliation check.
- Use DuckDB for local analytics and file-first workflows; use Postgres for production multi-user services; use SQLite for embedded local apps.
- Record every new pitfall in `ERRORS.md`.

## Router

| Task signal | First reference to read | Default move |
|---|---|---|
| Advanced SQL, CTEs, windows, joins | `references/sql-advanced.md` | Build a small test query and compare totals |
| Slow query, indexes, plan reading | `references/sql-performance.md` | Run `EXPLAIN`, measure baseline, change one thing |
| CSV, Excel, Parquet, local analytics | `references/duckdb.md` | Use DuckDB and profile first |
| Production DB, roles, backups, JSON | `references/postgres.md` | Define access, backup, restore, and migration path |
| Schema design or warehouse model | `references/data-modeling.md` | Define grain, keys, facts, dimensions, constraints |
| ETL/ELT, incremental loads | `references/etl-pipelines.md` | Stage raw, clean typed, validate, load idempotently |
| Finance variance, PVM, cohorts | `references/finance-calculations.md` | Confirm formula and grain before SQL |
| Dashboards and charts | `references/dashboards.md` | Query → validate → JSON → chart/table |
| FastAPI or REST over data | `references/backend-api.md` | Parameterize, paginate, shape JSON for UI |
| React/Next data app | `references/frontend-data.md` | Fetch state, loading/error states, table/chart separation |
| Security, destructive ops, reconciliation | `references/safety-governance.md` | Preview, approve, reconcile, backup |
| Source list and search map | `references/resources-and-leads.md` | Start from official docs |

## Default Workflow

1. **Understand:** What decision or artifact is needed? What data sources exist? What is the grain?
2. **Profile:** Use `scripts/profile_table.sql` or DuckDB profiling queries. Check rows, nulls, duplicates, ranges, totals.
3. **Model:** Choose OLTP, OLAP star, or flat analytical staging. Keep raw data immutable.
4. **Query:** Build with CTEs. Validate each step. Prefer window functions over procedural loops when the logic is set-based.
5. **Validate:** Reconcile totals against input, detect row explosions, compare distinct business keys.
6. **Present:** Create dashboard, API, Excel, PDF, Markdown, or concise decision memo.
7. **Improve:** If the skill missed a pattern, update the relevant reference or `ERRORS.md` immediately.

## Excel-to-Database Reporting Pipelines

When Mohamed asks about automating recurring Excel extraction into a database, running queries, and producing Excel reports again, use `references/excel-to-duckdb-reporting-pipeline.md` before designing the system. The durable pattern is:

```text
inspect real Excel samples → raw extraction with provenance → validation/reconciliation → clean modeled tables → SQL query files → formatted Excel report
```

Do not start with dashboards, schedulers, or a web app until the local pipeline proves trusted numbers with traceability.

## Command Recipes

Create a sample database:

```bash
python scripts/setup_sample_db.py --out /tmp/dbmastery/demo.duckdb
```

Explain a query:

```bash
python scripts/explain_helper.py /tmp/dbmastery/demo.duckdb "select * from sales where region = 'Cairo'"
```

Build a dashboard:

```bash
python scripts/db_to_dashboard.py /tmp/dbmastery/demo.duckdb /tmp/dbmastery/dashboard.html
```

## Verification Checklist

- [ ] `ERRORS.md` read.
- [ ] Data grain stated.
- [ ] Row counts and totals reconciled.
- [ ] SQL is parameterized where inputs exist.
- [ ] Destructive statements were previewed and approved.
- [ ] Dashboard/API/file output was opened or tested.
- [ ] New lesson or error was written back into the skill package.
