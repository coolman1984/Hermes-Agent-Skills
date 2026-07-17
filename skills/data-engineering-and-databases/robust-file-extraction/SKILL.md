---
name: robust-file-extraction
version: 1.0.0
description: Patterns for building resilient file/data extraction from messy real-world sources (Excel, CSV, PDF, Word, email). Covers edge case handling, graceful degradation, error tracking, and encoding detection.
triggers:
  - "extraction engine"
  - "file ingestion"
  - "data import"
  - "parse messy files"
  - "handle corrupt files"
  - "edge cases in file reading"
  - "robust data extraction"
---

# Robust File Extraction

**When to use:** Building or hardening any system that reads untrusted/messy files from real users (Excel exports, CSV dumps, PDF reports, Word docs, email archives).

Real-world client files are **never clean**. They're corrupt, encrypted, empty, huge, use wrong encodings, contain formula errors, or are just plain weird. This skill encodes the defensive patterns that keep extraction pipelines from crashing on the 47th file of a 500-file batch.

---

## The Five Guards (apply to every extractor)

### 1. File Integrity Guards
Check **before** attempting to parse:

```python
# Size limit (tune per format)
file_size = os.path.getsize(path)
if file_size > 100 * 1024 * 1024:  # 100MB
    warnings.append(f"File very large ({file_size / (1024*1024):.1f} MB). Extraction may be slow.")

# Empty file
if file_size == 0:
    warnings.append("File is empty (0 bytes).")
    return empty_result_structure, warnings

# Corrupt/unreadable
try:
    doc = library.open(path)
except Exception as exc:
    raise ValueError(
        f"Cannot open file: {exc}. File may be corrupt, encrypted, or invalid."
    ) from exc
```

**Why:** A single corrupt file must not abort a batch. Catch early, warn clearly, continue.

### 2. Content-Level Error Handling
Track errors **per unit** (row, page, paragraph, cell):

```python
errors = 0
for row_idx, row in enumerate(rows, start=1):
    try:
        cleaned = process(row)
        result.append(cleaned)
    except Exception as exc:
        errors += 1
        if errors <= 3:  # Limit warnings
            warnings.append(f"Row {row_idx}: {exc}")

if errors > 3:
    warnings.append(f"... and {errors - 3} more errors")
```

**Why:** Don't spam 10,000 warnings. Show first few, summarize the rest.

### 3. Graceful Degradation
Never all-or-nothing. If a sheet fails, return the other sheets. If a page fails, return the other pages.

```python
sheets = []
for sheet_name in workbook.sheets:
    try:
        data = read_sheet(sheet_name)
        sheets.append(data)
    except Exception as exc:
        warnings.append(f"Sheet '{sheet_name}': could not read ({exc})")
        # Continue to next sheet
```

**Why:** Partial data is better than no data. The human can review warnings.

### 4. Format-Specific Defenses

**Excel:**
- Formula errors (#REF!, #DIV/0!, #VALUE!, #NAME?, #NULL!, #N/A, #NUM!) → convert to `null` + warn
- Encrypted workbooks → detect and fail with clear message
- Hidden rows/columns → preserve but note in warnings if relevant

**CSV:**
- Encoding fallback chain: BOM → UTF-8 → Windows-1256 → Latin-1
- Binary content heuristic: if >10% non-printable bytes, warn "may be binary"
- Delimiter sniffing with fallback to comma
- Quoted field edge cases (embedded newlines, escaped quotes)

**PDF:**
- Encrypted/password-protected → detect and fail clearly
- Scanned PDFs (no selectable text) → warn "route to OCR stage"
- Page-level errors → continue with remaining pages

**Word:**
- Corrupt .docx → clear error message
- Per-paragraph error tracking
- Per-table error tracking

**Email (.msg/.eml):**
- .eml via stdlib `email` module (no dependency)
- .msg via `extract-msg` library
- Attachment-level error tracking
- Charset detection for body decoding

### 5. Consistent Error Messages
Every error message should suggest next steps:

```python
# Good
"Cannot open workbook: Invalid file signature. File may be corrupt, encrypted, or not a valid Excel file."

# Bad
"Error: ZipFile error"
```

---

## Testing Edge Cases

Every extractor needs tests for:

1. **Empty file** (0 bytes) → should warn, not crash
2. **Corrupt file** (invalid format) → should raise clear ValueError
3. **Partial failure** (one bad row/page/sheet) → should extract rest + warn
4. **Encoding issues** (wrong charset, BOM, binary content) → should detect and warn
5. **Size limits** (huge files) → should warn about performance

Example test structure:

```python
def test_csv_edge_cases():
    # Empty file
    empty_path = write_file("empty.csv", b"")
    content, warnings = extractor.extract(empty_path)
    assert content["n_rows"] == 0
    assert any("empty" in w.lower() for w in warnings)
    
    # Binary content
    binary_path = write_file("binary.csv", b"\x00" * 1000 + b"a,b,c\n")
    content, warnings = extractor.extract(binary_path)
    assert any("binary" in w.lower() for w in warnings)
    
    # Corrupt file
    corrupt_path = write_file("corrupt.csv", b"\xff\xfe" * 100)
    try:
        extractor.extract(corrupt_path)
        assert False, "should have raised"
    except ValueError as exc:
        assert "corrupt" in str(exc).lower()
```

---

## Pitfalls

1. **Don't catch BaseException** — catch `Exception` so KeyboardInterrupt/SystemExit still work
2. **Don't leak file handles** — use context managers (`with open(...)`) or explicit `try/finally`
3. **Don't assume encoding** — always detect or try fallback chain
4. **Don't truncate warnings** — limit count but summarize ("... and N more")
5. **Don't fail silently** — every error path must log or warn
6. **Don't mix stdout/stderr** — warnings go to structured output (JSON), errors to stderr
7. **Don't hardcode limits** — make file size limits configurable or at least documented

---

## When This Skill Does NOT Apply

- Trusted internal data (you control the format)
- Single-file manual imports (not batch processing)
- Real-time streaming (different error model)
- APIs with strict schemas (validation happens at schema level)

This skill is for **batch extraction from untrusted user-generated files** where partial success is better than total failure.
