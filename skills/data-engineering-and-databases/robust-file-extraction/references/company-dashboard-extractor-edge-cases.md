# Concrete Edge Case Implementations

Real-world implementations from the Company-Dashboard extraction engine (2026-06-15).
These are battle-tested patterns, not theoretical advice.

## Excel Formula Error Detection

```python
def _clean(value):
    """Make cell values JSON-friendly. Returns (cleaned_value, had_error)."""
    import datetime as dt
    
    # Formula errors - openpyxl returns these as strings
    if isinstance(value, str) and value.startswith("#"):
        error_markers = ("#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#NULL!", "#N/A", "#NUM!")
        if value in error_markers:
            return None, True  # Convert to null, flag as error
    
    if isinstance(value, (dt.datetime, dt.date, dt.time)):
        return value.isoformat(), False
    return value, False
```

**Why this works:** openpyxl doesn't crash on formula errors — it returns the error string as the cell value. We detect and convert to null so downstream code doesn't see "#REF!" as valid data.

## CSV Binary Content Detection

```python
def _looks_binary(raw_bytes: bytes) -> bool:
    """Heuristic: detect if file contains too many non-printable bytes."""
    sample = raw_bytes[:10240]  # Sample first 10KB
    if not sample:
        return False
    
    # Count non-printable, non-whitespace bytes
    non_printable = sum(
        1 for byte in sample
        if byte < 32 and byte not in (9, 10, 13)  # tab, newline, CR
    )
    
    # If >10% non-printable, likely binary
    return (non_printable / len(sample)) > 0.1
```

**Why this works:** CSV files are text. If >10% of bytes are control characters (excluding whitespace), it's probably not CSV. Warn the user but don't refuse — sometimes CSVs have embedded nulls that are still parseable.

## CSV Encoding Fallback Chain

```python
def _decode(raw_bytes: bytes):
    """Return (text, encoding_used), trying encodings Arabic CSVs use."""
    if raw_bytes.startswith(b"\xef\xbb\xbf"):
        return raw_bytes.decode("utf-8-sig"), "utf-8-sig"
    if raw_bytes[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return raw_bytes.decode("utf-16"), "utf-16"
    try:
        return raw_bytes.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass
    try:
        return raw_bytes.decode("cp1256"), "cp1256"  # Arabic code page
    except UnicodeDecodeError:
        return raw_bytes.decode("latin-1"), "latin-1"  # Never fails
```

**Why this works:** Arabic CSVs from Windows are often Windows-1256 (not UTF-8). The fallback chain tries UTF-8 first (most common), then cp1256 (Arabic legacy), then latin-1 (guaranteed to decode anything). Each step warns if it's not UTF-8.

## PDF Encrypted File Detection

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

**Why this works:** pdfplumber raises various exceptions for encrypted PDFs. We detect the "password" or "encrypt" keywords in the error message and give a clearer, actionable error. The user knows they need to provide an unencrypted version.

## Sheet-Level Error Isolation

```python
sheets = []
for sheet_name in workbook.sheets:
    try:
        with workbook.get_sheet(sheet_name) as sheet:
            rows = []
            row_errors = 0
            for row_idx, row in enumerate(sheet.rows(), start=1):
                try:
                    values = [cell.v for cell in row]
                    # ... process row
                    rows.append(cleaned)
                except Exception as exc:
                    row_errors += 1
                    if row_errors <= 3:
                        warnings.append(f"Sheet '{sheet_name}' row {row_idx}: {exc}")
            
            if row_errors > 3:
                warnings.append(f"Sheet '{sheet_name}': ... and {row_errors - 3} more row errors")
            
            sheets.append({"name": sheet_name, "rows": rows})
    except Exception as exc:
        warnings.append(f"Sheet '{sheet_name}': could not read ({exc})")
        # Continue to next sheet
```

**Why this works:** Two levels of isolation — sheet-level errors don't abort the workbook, and row-level errors don't abort the sheet. The 3-error limit prevents warning spam while still giving actionable feedback.

## Testing Empty Files

```python
def test_csv_empty_file():
    extractor = CsvTextExtractor()
    with tempfile.TemporaryDirectory() as tmp:
        empty_path = os.path.join(tmp, "empty.csv")
        with open(empty_path, "wb") as fh:
            pass  # 0 bytes
        content, warnings = extractor.extract_content(empty_path)
        assert content["sheets"][0]["n_rows"] == 0
        assert any("empty" in w.lower() for w in warnings)
```

**Why this works:** Empty files are surprisingly common (failed downloads, zero-byte exports). The extractor should return a valid structure with 0 rows and a warning, not crash or return null.

## Testing Corrupt Files

```python
def test_excel_corrupt_file():
    extractor = ExcelOpenpyxlExtractor()
    with tempfile.TemporaryDirectory() as tmp:
        corrupt_path = os.path.join(tmp, "corrupt.xlsx")
        with open(corrupt_path, "wb") as fh:
            fh.write(b"this is not a valid excel file")
        
        try:
            extractor.extract_content(corrupt_path)
            assert False, "should have raised ValueError"
        except ValueError as exc:
            assert "corrupt" in str(exc).lower() or "cannot open" in str(exc).lower()
```

**Why this works:** Corrupt files should raise `ValueError` with a clear message, not `zipfile.BadZipFile` or other library-specific exceptions. The caller catches one exception type and gets a human-readable message.

## Partial Extraction on Failure

```python
pages = []
parse_errors = 0
for index, page in enumerate(pdf.pages, start=1):
    try:
        text = page.extract_text() or ""
        pages.append({"number": index, "text": text})
    except Exception as exc:
        parse_errors += 1
        if parse_errors <= 5:
            warnings.append(f"Page {index}: extraction error ({exc}). Page skipped.")
        # Add empty placeholder so page numbers stay consistent
        pages.append({"number": index, "text": ""})

if parse_errors > 5:
    warnings.append(f"... and {parse_errors - 5} more extraction errors")
```

**Why this works:** Even if 5 pages fail in a 100-page PDF, we return the other 95 pages. The empty placeholder keeps page numbers aligned (page 47 is still page 47 in the output, not page 42 after skipping 5 errors).
