# SQL Advanced Patterns

## Table of Contents
- Window functions
- CTEs and recursive CTEs
- Semi joins and anti joins
- Lateral joins
- Pivoting and grouping sets
- Usage image

## Window functions

Use window functions when a row needs context from neighboring rows or group totals without collapsing the row set.

Tested DuckDB pattern:

```sql
select
  month,
  product,
  revenue,
  revenue - lag(revenue) over (partition by product order by month) as revenue_delta,
  sum(revenue) over (partition by product order by month rows between unbounded preceding and current row) as running_revenue
from monthly_sales;
```

When to use: running totals, moving averages, rank, retention, previous-period comparison.
When NOT to use: when the result grain should collapse to one row per group; use `group by`.
Signal: you need both detail rows and group context.
Mistake to avoid: window functions run after `where` and grouping; filter carefully.

Source: PostgreSQL window tutorial — https://www.postgresql.org/docs/current/tutorial-window.html

## CTEs

Use CTEs to make a calculation auditable step by step. Do not assume a CTE is faster; it is mainly for clarity unless the engine materializes or optimizes it differently.

```sql
with clean as (
  select * from sales where qty > 0 and unit_price >= 0
), monthly as (
  select date_trunc('month', order_date) as month, product, sum(qty * unit_price) as revenue
  from clean
  group by 1, 2
)
select * from monthly;
```

When to use: staged transformations, debugging, reusable sub-results.
When NOT to use: hiding a massive repeated subquery that should be a temp table or model.

## Recursive CTEs

Use for hierarchies such as bill-of-materials, organization trees, chart of accounts.

```sql
with recursive tree(id, parent_id, depth) as (
  select id, parent_id, 0 from accounts where parent_id is null
  union all
  select a.id, a.parent_id, t.depth + 1
  from accounts a join tree t on a.parent_id = t.id
)
select * from tree;
```

## Semi joins and anti joins

Use `exists` for semi-join and `not exists` for anti-join. Avoid `not in` when nulls may appear.

```sql
select c.*
from customers c
where exists (select 1 from orders o where o.customer_id = c.customer_id);

select c.*
from customers c
where not exists (select 1 from orders o where o.customer_id = c.customer_id);
```

## Lateral joins

Use lateral when a subquery depends on the current row, such as top-N per parent.

```sql
select c.customer_id, x.order_id, x.revenue
from customers c
join lateral (
  select order_id, revenue
  from orders o
  where o.customer_id = c.customer_id
  order by revenue desc
  limit 3
) x on true;
```

## Pivoting and grouping sets

DuckDB supports `pivot`; many engines support conditional aggregation everywhere.

```sql
select product,
  sum(case when region = 'Cairo' then revenue else 0 end) as cairo_revenue,
  sum(case when region = 'Alex' then revenue else 0 end) as alex_revenue
from monthly_sales
group by product;
```

Use grouping sets when one query should return multiple subtotal levels.

```sql
select region, product, sum(revenue)
from sales
group by grouping sets ((region, product), (region), ());
```

## Usage image

Ask: what is the row grain before and after this query? Watch: duplicates after joins, null logic in anti-joins, and hidden filters before windows. Avoid: clever one-liners that cannot be reconciled.
