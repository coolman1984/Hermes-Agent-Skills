# Backend APIs Over Data

## Table of Contents
- FastAPI default
- Parameterized query pattern
- Pagination and filters
- Caching
- JSON shaped for charts

## FastAPI default

FastAPI can use any database library; its official SQL tutorial uses SQLModel/SQLAlchemy and SQLite for simple examples, with PostgreSQL suggested for production. Source: https://fastapi.tiangolo.com/tutorial/sql-databases/

## Parameterized query pattern

```python
@app.get('/sales')
def sales(region: str | None = None, limit: int = 100, offset: int = 0):
    where = 'where region = ?' if region else ''
    params = [region] if region else []
    params += [limit, offset]
    return con.execute(f'select * from sales {where} limit ? offset ?', params).fetchall()
```

Only interpolate trusted SQL fragments created by your code, never user values.

## Pagination and filters

Limit every list endpoint. Return `items`, `limit`, `offset`, and optionally `total`.

## Caching

Cache expensive aggregate endpoints if source data is batch-loaded and immutable during a session.

## JSON shaped for charts

Return chart-ready rows: labels, series, values. Avoid making the frontend compute finance logic.

Usage image: build an API when multiple clients need data. Watch N+1 and unbounded result sets. Avoid returning raw database schema directly if the UI needs a stable contract.
