# ADR: Excel-to-Database Reporting Pipeline

- Status: accepted
- Context: recurring Excel reports need traceable trusted numbers.
- Decision: local modular monolith using DuckDB, immutable raw table, clean tables, SQL reports, Excel output.
- Options considered: spreadsheet macros, direct Excel formulas, Postgres web service.
- Trade-offs: DuckDB is simple/local but not multi-user; Postgres later when concurrent access matters.
- Consequences: faster delivery, provenance, easy audits, limited collaboration until server phase.
- Security/reliability: no secrets in files, validation gates, source row provenance.
- Revisit trigger: multiple simultaneous users or report runtime exceeds target.
