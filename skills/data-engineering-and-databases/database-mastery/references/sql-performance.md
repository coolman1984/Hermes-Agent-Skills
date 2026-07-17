# SQL Performance and Query Plans

## Table of Contents
- Plan reading
- Index design
- Anti-patterns
- Partitioning and statistics
- Measurement workflow

## Plan reading

PostgreSQL explains that a plan is a tree of nodes: scans at the bottom, joins/aggregates/sorts above, with estimated cost, rows, and width. Source: https://www.postgresql.org/docs/current/using-explain.html

DuckDB uses `EXPLAIN` and `EXPLAIN ANALYZE` for physical plans and timings.

Read in this order:
1. Actual row count vs expected row count.
2. Full scan vs index/zone-map pruning.
3. Join algorithm and join order.
4. Sort/hash/aggregate memory pressure.
5. Filters applied early or late.

## Index design

Use indexes for selective filters, joins, and order-by patterns. Do not index every column.

Rules:
- Equality columns first, then range columns.
- Covering index can avoid table lookup when the engine supports it.
- Functions on indexed columns can prevent index use unless an expression index exists.
- Low-cardinality indexes can be poor in row stores but useful as bitmap indexes in some engines.

## Anti-patterns

- `SELECT *` in APIs or dashboards.
- N+1 queries from backend loops.
- Applying functions to filter columns: `date(order_ts) = ...`.
- Leading wildcard: `like '%abc'`.
- Joining before filtering or pre-aggregating.
- Correlated subquery that should be a join/window.
- Missing stats after large loads.

## Partitioning and statistics

Partition when pruning large data by date/tenant is common. Do not partition small tables. Update stats after bulk loads.

## Measurement workflow

1. Capture baseline wall time and plan.
2. Change one thing.
3. Re-run with same parameters.
4. Save before/after plan in notes.
5. Reject improvements that break totals.

Usage image: use performance work when a query is slow or a dashboard times out. Watch estimated vs actual rows. Avoid optimizing without a measured baseline.
