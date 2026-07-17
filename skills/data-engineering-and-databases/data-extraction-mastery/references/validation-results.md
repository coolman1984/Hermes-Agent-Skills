# Data Extraction Mastery Validation Results

| Task | Result | Evidence | Fix applied |
|---|---|---|---|
| 1 report-formatted .xlsm merged/junk/totals → clean records | PASS | rows=2; merged=['A1:D1'] |  |
| 2 scanned Arabic PDF → OCR searchable text with numbers intact | PASS | ocr_pages=1; text_sample='فاتورة رقم 12345 المبلغ 6789' |  |
| 3 PDF table spanning 3 pages → reassembled text/table lines | PASS | pages_headers=3; has_last=True |  |
| 4 email with xlsx/pdf attachments → body + attachment manifest | PASS | attachments=2; body_chars=19 | True Outlook .msg parsing is supported by reference via extract-msg, but validation used standard .eml because generating valid proprietary .msg locally is not reliable. |
| 5 web page data table → landed into DuckDB | PASS | tables=[{'index': 1, 'rows': 2, 'cols': 4, 'output': '/tmp/extractmastery_validation/out_web/table_1.jsonl'}]; duckdb_rows=2 | Validation used post-rendered HTML; Playwright route is documented for live JS pages. |
| 6 folder of 20 mixed files + corrupt → DB + extraction report | PASS | files=20; ok=19; needs_review=1; db=/tmp/extractmastery_validation/out_batch/extraction_report.sqlite |  |
