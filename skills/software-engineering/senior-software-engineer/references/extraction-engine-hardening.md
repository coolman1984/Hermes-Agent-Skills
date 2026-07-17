# Extraction Engine Hardening Pattern

## When to Use
When Mohamed asks to "harden," "strengthen," or "add edge case handling" to file extractors, parsers, or data ingestion code.

## The Pattern (proven in Company-Dashboard, 2026-06-15)

Apply these guards systematically to every extractor:

### 1. File Integrity Guards
```python
# File size limit (adjust per type: Excel 50-100MB, CSV 100MB, PDF 200MB)
file_size = os.path.getsize(path)
if file_size > 100 * 1024 * 1024:
    warnings.append(f"File is very large ({file_size / (1024*1024):.1f} MB). "
                    "Extraction may be slow or incomplete.")

# Empty file detection
if file_size == 0:
    warnings.append("File is empty (0 bytes).")
    return {"sheets": []}, warnings

# Corrupt file detection
try:
    workbook = open_workbook(path)
except Exception as exc:
    raise ValueError(
        f"Cannot open workbook: {exc}. File may be corrupt, encrypted, "
        "or not a valid Excel file."
    ) from exc

# Binary content detection (for CSV/text)
def _looks_binary(raw_bytes: bytes) -> bool:
    sample = raw_bytes[:10240]
    non_printable = sum(
        1 for byte in sample
        if byte < 32 and byte not in (9, 10, 13)  # tab, newline, carriage return
    )
    return (non_printable / len(sample)) > 0.1 if sample else False
```

### 2. Content-Level Error Handling

**Excel formula errors:**
```python
def _clean(value):
    """Convert formula errors (#REF!, #DIV/0!) to null with warnings."""
    if isinstance(value, str) and value.startswith("#"):
        error_markers = ("#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#NULL!", "#N/A", "#NUM!")
        if value in error_markers:
            return None, True  # Convert to null, flag as error
    # ... rest of cleaning
    return value, False

# Track error count per sheet
error_cells = 0
for row_idx, row in enumerate(ws.iter_rows(values_only=True), start=1):
    for cell in values:
        clean_val, had_error = _clean(cell)
        if had_error:
            error_cells += 1

if error_cells > 0:
    warnings.append(f"Sheet '{sheet_name}': {error_cells} cell(s) contained "
                    "formula errors - converted to null.")
```

**PDF encrypted/password-protected:**
```python
try:
    pdf = pdfplumber.open(path)
except Exception as exc:
    error_msg = str(exc).lower()
    if "password" in error_msg or "encrypt" in error_msg:
        raise ValueError(
            f"PDF is password-protected or encrypted. "
            f"Cannot extract without password. Error: {exc}"
        ) from exc
    raise ValueError(
        f"Cannot open PDF: {exc}. File may be corrupt or not a valid PDF."
    ) from exc
```

### 3. Per-Element Error Tracking

**Key principle:** Never abort the entire extraction for one bad element.

```python
# Excel: per-sheet isolation
for sheet_name in workbook.sheets:
    try:
        # ... extract sheet
    except Exception as exc:
        warnings.append(f"Sheet '{sheet_name}': could not read ({exc})")
        # Continue with next sheet

# PDF: per-page isolation
for index, page in enumerate(pdf.pages, start=1):
    try:
        text = page.extract_text() or ""
        pages.append({"number": index, "text": text})
    except Exception as exc:
        parse_errors += 1
        if parse_errors <= 5:  # Don't spam warnings
            warnings.append(f"Page {index}: extraction error ({exc}). Page skipped.")
        pages.append({"number": index, "text": ""})  # Placeholder

if parse_errors > 5:
    warnings.append(f"... and {parse_errors - 5} more extraction errors")

# CSV: per-line error tracking
parse_errors = 0
for line_num, row in enumerate(reader, start=1):
    try:
        cleaned = [_clean(v) for v in row]
        rows.append(cleaned)
    except Exception as exc:
        parse_errors += 1
        if parse_errors <= 5:
            warnings.append(f"Line {line_num}: parse error ({exc})")
```

### 4. Graceful Degradation

**Never crash on partial failure:**
- Sheet-level errors don't abort the workbook
- Page-level errors don't abort the document
- Paragraph-level errors don't abort the document
- Row-level errors don't abort the sheet

**Contextual warnings:**
```python
# PDF: distinguish scanned vs digital
if empty_pages:
    if empty_pages == total_pages:
        warnings.append(f"ALL {empty_pages} page(s) had no selectable text - "
                        "this is likely a scanned PDF. Route to the OCR stage.")
    elif empty_pages > total_pages * 0.5:
        warnings.append(f"{empty_pages} of {total_pages} page(s) had no selectable text - "
                        "many pages may be scanned. Consider OCR for better results.")
    else:
        warnings.append(f"{empty_pages} page(s) had no selectable text - likely scanned; "
                        "route to the OCR stage.")
```

### 5. Encoding and Format Detection (CSV)

```python
def _decode(raw_bytes: bytes):
    """Try encodings in order: BOM -> UTF-8 -> Windows-1256 -> Latin-1"""
    if raw_bytes.startswith(b"\xef\xbb\xbf"):
        return raw_bytes.decode("utf-8-sig"), "utf-8-sig"
    if raw_bytes[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw_bytes.decode("utf-16"), "utf-16"
    try:
        return raw_bytes.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass
    try:
        return raw_bytes.decode("cp1256"), "cp1256"  # Arabic legacy
    except UnicodeDecodeError:
        return raw_bytes.decode("latin-1"), "latin-1"  # Last resort
```

## Pitfalls

1. **Don't use `os.replace()` for backups** - it moves the file, not copies it. Use `shutil.copy2()` so the backup remains available for repeated rollbacks.

2. **Don't check `.exists()` before `write_text()`** - `write_text()` creates the file. The check prevents writing when the file doesn't exist yet.

3. **ISO timestamp formatting** - don't use string manipulation on run IDs. Parse the run ID format explicitly:
   ```python
   # run_id format: run-YYYYMMDD-HHMMSS-microseconds
   parts = run_id.split("-")
   date_part, time_part, micro_part = parts[1], parts[2], parts[3]
   iso_ts = f"{date_part[:4]}-{date_part[4:6]}-{date_part[6:8]}T{time_part[:2]}:{time_part[2:4]}:{time_part[4:6]}.{micro_part}"
   ```

4. **Pyright false positives** - `wb.active` after `Workbook()` is typed as `Optional[Worksheet]` but is never None in practice. Add `# type: ignore` if needed, but verify at runtime.

## Verification

After hardening, run comprehensive tests:
```bash
python3 -m extractor.test_extractor
python3 -m extractor.test_arabic
python3 test_map_raw_to_db.py
```

Test edge cases explicitly:
- Empty files (0 bytes)
- Corrupt files (invalid format)
- Binary content in text files
- Formula errors in Excel
- Encrypted PDFs
- Large files (>100MB)
- Encoding variants (UTF-8, Windows-1256, UTF-16)
