# Dashboards and Presentation

## Table of Contents
- Dashboard principles
- Static HTML
- Chart choices
- Streamlit vs frontend
- Validation before presentation

## Dashboard principles

A good dashboard answers one decision. Start with KPI cards, then trend, then breakdown, then detail table. Keep filters visible.

## Static HTML

For file handoff, generate self-contained HTML with embedded JSON and Chart.js or ECharts CDN when internet is available. For offline, use plain SVG/canvas or bundle assets.

## Chart choices

- KPI cards: current state
- line: trend over time
- bar: category comparison
- stacked bar: composition
- table: audit and drill-down

## Streamlit vs static HTML vs real frontend

- Static HTML: easiest handoff.
- Streamlit: quick internal app.
- React/Next: production frontend with state, routing, auth.

## Validation before presentation

Every displayed number must map to a query and a reconciliation check.

Usage image: use dashboards when Mohamed needs to see and decide. Watch chart/table mismatch. Avoid fancy visuals before trustworthy totals.
