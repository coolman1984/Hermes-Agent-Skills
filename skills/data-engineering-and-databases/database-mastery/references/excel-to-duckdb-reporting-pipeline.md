# Excel → DuckDB → SQL → Excel Reporting Pipeline

Use this when Mohamed wants to automate recurring Excel files into a database, run queries, and produce Excel reports again.

## Core Mental Model

```text
Excel input folder
→ raw extraction with provenance
→ validation and reconciliation
→ DuckDB database
→ clean modeled tables
→ SQL query files
→ formatted Excel report
```

The objective is not “read Excel”. The objective is trusted numbers with traceability: every report figure should be traceable back to source file, sheet, row, load time, validation checks, and SQL query.

## Build Order With AI

1. **Inspect samples first**
   - Use 3–5 real messy Excel files.
   - Identify sheets, headers, merged cells, blank rows, formulas, totals, repeated sections, required fields.
   - Output `data_map.md` before writing final extraction logic.

2. **Define grain and schema**
   - State table grain explicitly, e.g. “one row in `clean_sales` = one invoice line”.
   - Keep raw tables separate from clean modeled tables.

3. **Extract to raw table only**
   - Read files from `input/`.
   - Store `source_file`, `sheet_name`, `row_number`, `extracted_at` with every row.
   - Do not build reports yet.

4. **Add validation**
   - Required columns, date parsing, numeric amounts, duplicates, blank rows, total reconciliation.
   - Write `validation_errors` table and a validation Markdown report.

5. **Transform to clean tables**
   - Normalize dates, numbers, customer/product names, and business columns.
   - Preserve provenance columns in clean records.

6. **Create SQL query files**
   - Store queries under `queries/` such as `monthly_sales.sql`, `top_customers.sql`, `reconciliation.sql`.
   - Reconcile totals before trusting the output.

7. **Build Excel report output**
   - Use `openpyxl` or `xlsxwriter` to create sheets such as Summary, Monthly Sales, Top Customers, Validation, Source Files.

8. **One command pipeline**
   - Final command should run extract → validate → load → query → report and print files processed, rows loaded, validation errors, and report path.

## Recommended Project Skeleton

```text
excel-report-pipeline/
├── input/
├── data/reports.duckdb
├── output/reports/
├── output/validation/
├── queries/
├── src/
│   ├── extract_excel.py
│   ├── validate.py
│   ├── load_database.py
│   ├── run_queries.py
│   ├── build_excel_report.py
│   └── pipeline.py
├── config.yaml
└── README.md
```

## Pitfalls

- Building the final report before validating extraction.
- Mixing raw and clean data in one table.
- Losing source file/sheet/row provenance.
- Writing SQL directly inside Python instead of keeping reusable query files.
- Trusting a beautiful Excel report without reconciliation.
- Starting with a dashboard/web app before the local pipeline is proven.

## Good AI Prompt Sequence

```text
Phase 1 only: inspect all Excel files in input/, produce data_map.md, propose raw and clean schema. Do not write final extraction logic yet.
```

```text
Phase 2: implement extraction into raw_excel_rows with source_file, sheet_name, row_number, extracted_at.
```

```text
Phase 3: implement validation and reconciliation, writing validation_errors and a Markdown validation report.
```

```text
Phase 4: implement clean modeled tables and SQL query files.
```

```text
Phase 5: generate a formatted Excel report from the SQL outputs.
```

Usage image: use this reference when the user describes Excel automation, management reports, recurring spreadsheet consolidation, or “Excel to database then report back to Excel”.
