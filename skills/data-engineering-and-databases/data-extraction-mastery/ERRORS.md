# Data Extraction Mastery Error Log

## 2026-07-08 — Fake extension is not format detection
- Symptom: A file named `.xlsm` can be a normal xlsx zip without macros.
- Root cause: Extension alone was trusted.
- Fix: Inspect file signature and parse capability, then record actual route.
- Prevention rule: always detect actual type before choosing extractor.

## 2026-07-08 — Report-formatted Excel can hide real header row
- Symptom: Junk title rows and merged cells produce unnamed columns or missing data.
- Root cause: Reader assumed first row is header.
- Fix: scan first rows for the best header candidate and forward-fill merged context.
- Prevention rule: for Excel reports, detect data region before treating it as a table.

## 2026-07-08 — OCR can change Arabic text but keep numbers better than letters
- Symptom: Arabic OCR text may be imperfect while numeric amounts survive.
- Root cause: OCR model quality/layout/font issues.
- Fix: validate numbers separately and mark OCR confidence/human review when text quality is low.
- Prevention rule: for Arabic scans, preserve image/page provenance and spot-check numbers.

## 2026-07-08 — pandas.read_html treated literal HTML as a file path
- Symptom: web table extraction produced no `table_1.jsonl` and pandas raised `No such file or directory: <html>...`.
- Root cause: new pandas behavior expects literal HTML to be wrapped in a file-like object.
- Fix: use `pd.read_html(StringIO(html))`.
- Prevention rule: wrap literal HTML strings with `io.StringIO` before `pandas.read_html`.

## 2026-07-08 — Arabic OCR returned blank without page segmentation mode
- Symptom: Tesseract extracted no text from a clean Arabic image PDF, while direct CLI with page segmentation worked.
- Root cause: default layout detection was poor for the synthetic single-line Arabic scan.
- Fix: call Tesseract with `--psm 6` and retry alternate render scales `(2, 1, 3)` when OCR returns blank.
- Prevention rule: expose OCR page segmentation mode and retry render scale before declaring no text.

## 2026-07-08 — Corrupt file in batch must not abort run
- Symptom: invalid bytes in one file can stop a folder extraction.
- Root cause: exception was not isolated per file.
- Fix: batch script catches per-file errors and writes `needs_review` rows.
- Prevention rule: batch extraction is partial-success by design.
