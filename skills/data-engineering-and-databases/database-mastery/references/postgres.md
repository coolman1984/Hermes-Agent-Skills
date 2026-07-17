# PostgreSQL Production Patterns

## Table of Contents
- When Postgres wins
- Roles and least privilege
- Backups and restore drills
- JSONB and full-text search
- Extensions
- Operations checklist

## When Postgres wins

Use PostgreSQL for production systems with concurrent users, transactions, permissions, API backends, scheduled jobs, and durable operations.

Official docs: https://www.postgresql.org/docs/current/

## Roles and least privilege

Create separate roles: owner, migrator, app read-write, read-only reporting. The API should not connect as a superuser.

## Backups and restore drills

A backup is only real after restore testing. Use `pg_dump` for logical backups and managed physical backups for larger production.

## JSONB and full-text search

Use JSONB for semi-structured attributes, not as a substitute for obvious relational columns. Use GIN indexes when querying JSONB keys heavily.

## Extensions

Common: `pg_stat_statements`, `uuid-ossp` or native UUID, `pg_trgm`, PostGIS where spatial is real.

## Operations checklist

- migrations are versioned
- backups exist
- restore was tested
- app role is least privilege
- slow queries observable
- destructive changes have preview and rollback plan

Usage image: choose Postgres when correctness, users, and operations matter. Watch: role drift and missing restore drills. Avoid: using JSONB to dodge data modeling.
