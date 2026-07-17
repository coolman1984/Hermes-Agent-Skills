# PDF OCR

Use OCR only after text test shows low/no extractable text. Tesseract with `ara+eng` handles Arabic and English; OCRmyPDF is preferred for producing searchable PDFs when available. Render pages to images, OCR, preserve page number and image path. For Arabic scans, use a page segmentation mode such as `--psm 6` for uniform text blocks and retry alternate render scales before declaring OCR empty.

Sources: https://tesseract-ocr.github.io/tessdoc/ ; pytesseract docs.

When to use: scanned PDFs, image-only pages. When it fails: low resolution, handwriting, skewed pages, poor fonts. Watch: Arabic text quality and numeric fidelity separately.

Usage image: detect, preserve structure, validate, and only then normalize/load.
