# Arabic Full-Book Upgrade Playbook (PDF Source -> Pro Publishing PDF)

## When to use
- User sends an existing Arabic PDF and asks for full professional upgrade (not only 4-page sample).

## Proven workflow
1. Extract text page-by-page with PyMuPDF from the source PDF.
2. Clean extraction artifacts before layout:
   - spacing artifacts around diacritics
   - OCR-like token issues (example: "مالحظة" -> "ملاحظة")
   - remove footer line noise and bullet leftovers
3. Rebuild into structured HTML with consistent sections:
   - professional cover
   - unified internal page system
   - chapter/appendix markers
4. Export with Prince.
5. Run technical QA:
   - `qpdf --check`
   - `verapdf` for archival profile
6. For global archival delivery, produce a dedicated profile build:
   - `prince --pdf-profile=pdf/a-3b input.html -o output_pdfa3b.pdf`
   - verify with `verapdf` expecting PASS 3b.
7. Run visual QA contact sheet and inspect for:
   - blank/near-blank pages
   - inconsistent page rhythm
   - broken RTL readability

## Critical pitfalls found
- Forcing `.section { page-break-after: always; }` can create blank or near-blank pages in long Arabic books.
  - Fix: use auto flow and chapter separators instead of hard break on every section.
- Verify there are no accidental English tokens inside Arabic body lines.
  - Use an automated scan for `[A-Za-z]` in extracted text from the final PDF.
- A PDF can pass `qpdf` but fail archival compliance if not built with a PDF/A profile.
  - If archival/global publication is requested, export explicit `pdf/a-3b` and validate with veraPDF.

## Delivery set used successfully
- Main file: PDF/A-3b master
- Additional derivatives: linearized, ebook, printer, prepress
- QA artifacts: finish report + visual contact sheet
