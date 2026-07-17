# Loading and Handoff

Land extracted tables into DuckDB first for local analysis. Every row gets provenance columns: `_source_file`, `_source_unit` (sheet/page/attachment/url), `_extracted_at`, `_extractor`, `_warnings`.

After load, hand off to `database-mastery` for profiling, modeling, SQL, calculations, dashboards, and APIs.

When to use: any extraction that needs analysis. When it fails: schema drift across files; solve with raw tables + normalized views.

Usage image: detect, preserve structure, validate, and only then normalize/load.
