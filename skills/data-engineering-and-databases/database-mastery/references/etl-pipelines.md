# ETL and ELT Pipelines

## Table of Contents
- Layering
- Messy Excel/CSV handling
- Idempotent loads
- Incremental watermarks
- Validation gates
- Python stack choices

## Layering

Use layers:
1. Raw immutable files/tables.
2. Staging typed and lightly cleaned.
3. Marts shaped for business questions.

This mirrors dbt's staging-to-marts philosophy. Source: https://docs.getdbt.com/docs/build/projects

## Messy Excel/CSV handling

Apply robust extraction: encoding fallback, sheet-level warnings, formula error handling, Arabic text preserved as UTF-8, date parsing with explicit formats where possible.

## Idempotent loads

A load can be safely re-run and produce the same result. Use source file hash, batch id, and merge/upsert rules.

## Incremental loads

Use watermarks such as `updated_at`, monotonically increasing IDs, or file arrival timestamp. Store last successful watermark only after reconciliation passes.

## Validation gates

- row count
- distinct business keys
- null key count
- duplicate key count
- amount/control total
- invalid domain values

## Python stack choices

- pandas: messy row/Excel handling, Python ecosystem
- DuckDB: SQL joins/aggregations over large local files
- Polars: fast dataframe operations when available

Usage image: use ETL when raw files repeat. Watch silent type coercion and bad dates. Avoid overwriting raw inputs.
