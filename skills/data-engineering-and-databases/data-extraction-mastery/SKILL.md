---
name: data-extraction-mastery
description: Use whenever the user mentions extracting, reading, parsing, or pulling data from any PDF, Word, Excel (xlsx/xlsm/xlsb/xls), CSV, email (eml/msg/pst/Outlook), web page, or any file — even if they just say get the data out of this or read this file. Also triggers on OCR, scanned documents, Arabic text extraction, attachments, batch file ingestion, and landing extracted data into a database.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [data-extraction, files, pdf, ocr, excel, word, email, web-scraping, arabic, duckdb]
    related_skills: [database-mastery, robust-file-extraction]
---

# Data Extraction Mastery

## Mission

Extract data faithfully from files and sources, preserve structure and provenance, validate what was extracted, then hand clean records to `database-mastery` for querying, calculations, dashboards, and reporting.

## Mandatory Start

1. Read `ERRORS.md`.
2. Detect actual file type; do not trust extension alone.
3. Choose extractor by type and failure mode.
4. Preserve provenance: source path, sheet/page/attachment/url, extraction time.
5. Validate counts, samples, skipped content, and warnings.
6. Land structured output into DuckDB/SQLite/Postgres when analysis is needed, then load `database-mastery`.

## Iron Rules

- Detect type before choosing a tool.
- Test-for-text before OCR; never OCR a searchable PDF blindly.
- Every extraction ends with counts, sample spot-check, and skipped/warnings note.
- If the exact proprietary format cannot be generated or obtained locally (for example real Outlook `.msg`), validate the closest standards-based path, state the substitution explicitly, and mark the exact format as next real-sample work — never overclaim it as fully validated.
- Batch extraction must not crash on one bad file; log it and continue.
- Arabic/RTL is first-class: keep UTF-8, try cp1256 fallback for CSV/email, preserve numbers.
- Do not silently drop tables, attachments, hidden sheets, merged-cell context, or PDF pages.
- Password-protected, corrupt, or unsupported files go to human review with a clear reason.
- Handoff point to `database-mastery`: once records/tables are landed with provenance into a database.

## Router

| Signal | Reference | Default tool |
|---|---|---|
| xlsx/xlsm/templates/csv/tsv/xls/xlsb | `references/spreadsheets.md` | openpyxl/pandas/csv; pyxlsb/xlrd when available |
| docx/doc/rtf/txt/md/html fragment | `references/documents.md` | python-docx, LibreOffice fallback, plain parsers |
| text PDF/tables/forms/passwords | `references/pdf.md` | PyMuPDF/pdfplumber/pypdf |
| scanned PDF/image PDF/Arabic OCR | `references/pdf-ocr.md` | Tesseract/OCRmyPDF; test text first |
| eml/msg/pst/attachments | `references/email.md` | Python email, extract-msg, readpst fallback |
| web page/table/API/feed | `references/web-scraping.md` | requests+BeautifulSoup, pandas.read_html, Playwright if JS |
| type/date/number/Arabic cleanup | `references/normalization.md` | normalize before load |
| load to DB/report | `references/loading.md` | DuckDB first, then database-mastery |
| source lookup | `references/resources-and-leads.md` | official docs first |

## Default Flow

```text
detect → route → extract → normalize → validate → load with provenance → handoff to database-mastery
```

## Scripts

```bash
python scripts/detect_and_route.py FILE --out /tmp/extracted
python scripts/batch_extract.py FOLDER --out /tmp/extraction_run
python scripts/extract_excel.py workbook.xlsm --out /tmp/extracted
python scripts/extract_pdf.py file.pdf --out /tmp/extracted
python scripts/extract_email.py message.eml --out /tmp/extracted
python scripts/scrape_page.py URL_OR_HTML_FILE --out /tmp/extracted
```

## Completion Checklist

- [ ] Actual type detected.
- [ ] Extraction warnings recorded.
- [ ] Counts and spot-check sample produced.
- [ ] Skipped pages/sheets/attachments listed.
- [ ] Provenance present in every output table/record.
- [ ] Bad files logged without killing the batch.
- [ ] Landed data handed to `database-mastery` when analysis starts.
