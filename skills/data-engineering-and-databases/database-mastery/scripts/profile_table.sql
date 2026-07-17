-- Replace {table} before running. DuckDB generic profile.
select
  count(*) as row_count,
  count(*) - count(*) filter (where true) as impossible_check
from {table};

-- Column-level profiling is best generated dynamically because SQL needs column names.
-- Template checks:
-- select count(*) rows, count(distinct business_key) distinct_keys from {table};
-- select min(date_col), max(date_col) from {table};
-- select sum(amount_col) control_total from {table};
