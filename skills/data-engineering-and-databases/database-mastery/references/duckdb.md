# DuckDB Reference

## Table of Contents
- When DuckDB wins
- File ingestion
- Python API
- Excel/CSV/Parquet
- Larger-than-RAM handling
- Validation patterns

## When DuckDB wins

DuckDB is an embedded analytical database. It is strongest for local analytics over CSV, Parquet, Excel-derived tables, and Python workflows. Use it when Mohamed has files and needs reliable analysis without setting up a database server.

Source URLs:
- https://duckdb.org/docs
- https://duckdb.org/docs/stable/data/csv/overview.html
- https://duckdb.org/docs/stable/data/parquet/overview.html
- https://duckdb.org/docs/stable/clients/python/overview.html

## File ingestion

```sql
select * from read_csv_auto('sales.csv');
select * from read_parquet('*.parquet');
copy (select * from cleaned_sales) to 'out.parquet' (format parquet);
```

When to use: fast local query over files.
When NOT to use: many concurrent writers or a public multi-user app.

## Python API

Use Python to orchestrate file cleanup and DuckDB for set-based transformations.

```python
import duckdb
con = duckdb.connect('demo.duckdb')
con.execute('create table sales as select * from read_csv_auto(?)', ['sales.csv'])
rows = con.execute('select count(*) from sales').fetchone()[0]
```

## Excel handling

For messy Excel, pandas/openpyxl can read sheets first, then register dataframes in DuckDB. This gives better control over merged headers, Arabic text, and invalid rows.

## Memory and bigger-than-RAM

Set memory and temp directory when needed:

```sql
set memory_limit='2GB';
set temp_directory='/tmp/duckdb_spill';
```

## Validation patterns

```sql
select count(*) rows, sum(amount) amount_total from raw_sales;
select business_key, count(*) from clean_sales group by 1 having count(*) > 1;
select count(*) from clean_sales where product is null or order_date is null;
```

Usage image: use DuckDB as the local truth engine. Watch for type inference mistakes and row explosion after joins. Avoid treating raw file load as clean data.
