# Resources and Leads

## Authoritative sources

| Source | URL | Best for |
|---|---|---|
| DuckDB docs | https://duckdb.org/docs | File-first analytics, SQL, Python API |
| PostgreSQL docs | https://www.postgresql.org/docs/current/ | Production database behavior, EXPLAIN, roles, backups |
| SQLite docs | https://www.sqlite.org/docs.html | Embedded database behavior and WAL |
| SQLite WAL | https://www.sqlite.org/wal.html | WAL advantages, limitations, checkpointing |
| FastAPI SQL databases | https://fastapi.tiangolo.com/tutorial/sql-databases/ | API patterns over SQL databases |
| React Learn | https://react.dev/learn | Data-app UI fundamentals |
| Kimball Group | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/ | Dimensional modeling |
| dbt docs | https://docs.getdbt.com/docs/build/projects | Staging/marts project structure |
| Use The Index, Luke | https://use-the-index-luke.com/ | SQL indexing and performance mental models |
| Modern SQL | https://modern-sql.com/ | Modern SQL features and dialect differences |
| Postgres wiki Don't Do This | https://wiki.postgresql.org/wiki/Don%27t_Do_This | Production anti-patterns |

## Search phrasing that works

- `site:postgresql.org/docs EXPLAIN ANALYZE rows width cost`
- `site:duckdb.org/docs read_csv_auto python parameterized query`
- `site:sqlite.org WAL checkpoint busy`
- `Kimball slowly changing dimension type 2`
- `FastAPI SQLModel pagination filtering`

## Junior mistakes seniors avoid

1. Aggregating before defining grain.
2. Joining tables at different grains.
3. Trusting Excel types.
4. No control totals.
5. Unbounded API endpoints.
6. SQL string interpolation.
7. Dashboards with no reconciliation.
8. Indexing blindly.
9. No restore drill.
10. Treating a report as done before a stakeholder can act on it.
