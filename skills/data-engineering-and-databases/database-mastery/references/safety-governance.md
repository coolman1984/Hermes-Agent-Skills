# Safety and Governance

## Table of Contents
- SQL injection
- Destructive operations
- Backups
- Reconciliation
- Approval gates

## SQL injection

Use parameterized queries for all user values. Do not build SQL with string interpolation.

## Destructive operations

Before destructive SQL:
1. Run a `SELECT` preview with the same `WHERE`.
2. Show row count and sample rows.
3. Confirm backup/rollback path.
4. Ask explicit approval.

## Backups

For Postgres: backup plus restore drill. For DuckDB/SQLite: copy file only after closing connections or using backup APIs where applicable.

## Reconciliation

After every load: compare input rows vs loaded rows, source total vs table total, invalid row count, duplicates.

## Approval gates

Human approval required for destructive operations, credential changes, production migrations, and publishing reports with financial consequences.

Usage image: use this whenever data can be lost, corrupted, or misreported. Watch silent partial loads. Avoid trusting success messages without totals.
