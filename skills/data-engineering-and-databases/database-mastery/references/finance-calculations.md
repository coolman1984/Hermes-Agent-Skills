# Finance and Analytical Calculations

## Table of Contents
- Budget vs actual
- Price Volume Mix
- Cohorts and retention
- Weighted averages
- Allocations
- FX translation

## Budget vs actual

Always align grain first: month/product/region, etc.

```sql
with actual as (
  select month, product, region, sum(qty) qty, sum(revenue) revenue
  from sales_monthly group by 1,2,3
)
select a.*, b.budget_revenue, a.revenue - b.budget_revenue as variance
from actual a
join budget b using (month, product, region);
```

## Price Volume Mix

At product level:
- price effect = `(actual_price - budget_price) * actual_qty`
- volume effect = `(actual_qty - budget_qty) * budget_price`
- mix is needed when portfolio share changes; define formula with finance owner before using.

## Cohorts and retention

Find first month per customer, then count active customers by cohort and age.

## Weighted averages

Never average averages unless weights are equal.

```sql
sum(rate * balance) / nullif(sum(balance), 0)
```

## Allocations

Use drivers with a control total. The allocated sum must match the source total.

## FX translation

Store transaction currency, functional currency, rate source, and rate date. Reconcile both local and reporting currency.

Usage image: use these patterns when numbers must support decisions. Watch grain mismatch and totals. Avoid formulas that finance has not approved.
