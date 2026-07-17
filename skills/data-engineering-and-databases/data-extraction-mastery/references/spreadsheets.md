# Spreadsheets

Use openpyxl for xlsx/xlsm/xltx/xltm cells, merged ranges, comments, hidden sheets/rows, and formulas vs cached values. Use pandas for tabular reads after the real data region is found. Use pyxlsb for xlsb; openpyxl cannot read xlsb. Use xlrd only for legacy xls. CSV/TSV require encoding fallback: utf-8-sig, utf-8, cp1256, latin-1.

Sources: https://openpyxl.readthedocs.io/ ; https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html ; Python csv docs.

Pattern: detect workbook, inspect sheets, find header row, forward-fill merged cells, drop totals rows only after capturing them for reconciliation, output CSV/JSON with `_source_file` and `_source_sheet`.

When to use: Excel/CSV business exports. When it fails: encrypted/corrupt files, unsupported xlsb/xls without dependency. Watch: formulas without cached values, hidden rows, Arabic cp1256 CSV, multi-row headers.

Usage image: detect, preserve structure, validate, and only then normalize/load.
