# Data Modeling

## Table of Contents
- Grain
- OLTP normalization
- OLAP dimensional modeling
- Slowly changing dimensions
- Data Vault basics

## Grain

The grain is the exact meaning of one row. No model is safe until grain is written.

Examples:
- order line: one row per order/product line
- daily inventory: one row per product/location/day
- monthly budget: one row per product/region/month

## OLTP normalization

Normalize when writing data: one fact in one place, keys and constraints protect correctness. 1NF removes repeating groups; 2NF removes partial dependency; 3NF removes transitive dependency; BCNF tightens determinant rules.

## OLAP dimensional modeling

Use star schemas when reading data: fact tables store measurements at a grain; dimensions provide descriptive context. Kimball Group is a primary reference: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/

## Slowly changing dimensions

- Type 1: overwrite attribute.
- Type 2: add new version with effective dates.
- Type 3: keep limited previous attribute column.

## Data Vault basics

Hubs store business keys, links store relationships, satellites store history/descriptive attributes. Useful for audit-heavy, multi-source integration, but often too heavy for small projects.

Usage image: model when repeated analysis or production usage is expected. Watch grain mismatch. Avoid star schemas for tiny one-off files unless dashboard reuse is likely.
