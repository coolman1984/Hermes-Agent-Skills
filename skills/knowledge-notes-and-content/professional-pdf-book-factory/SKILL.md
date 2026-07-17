---
name: professional-pdf-book-factory
description: Use when producing, redesigning, auditing, or upgrading professional Arabic-first PDF books with a publishing-grade HTML/CSS to PDF pipeline, visual page review, and iterative quality gates.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  tags: [pdf, book-production, weasyprint, arabic, publishing, visual-qa, design-system]
  related_skills: [ocr-and-documents, powerpoint, mohamed-arabic-content-style]
---

# Professional PDF Book Factory

## Overview

This skill turns book production into a repeatable publishing pipeline, not ad-hoc writing in a document editor.

Canonical flow:

`structured content -> page templates -> design system -> PDF export -> render pages to images -> visual QA -> revise -> final export`

Use it to create books that feel closer to digital publishing houses: consistent pages, professional Arabic typography, clean tables, controlled whitespace, and content that earns every page.

## Installed Toolchain on Mohamed's Environment

A dedicated virtual environment was created here:

`/root/.venvs/pdf-book-factory`

Installed Python packages:

- `weasyprint` for fast HTML/CSS draft export.
- `pymupdf` for rendering PDF pages into images and inspecting pages.
- `pypdf` for page count and metadata checks.
- `beautifulsoup4` for HTML post-processing and cleanup.
- `jinja2` for reusable templates.
- `pillow` for contact sheets and visual previews.
- `fonttools`, `tinycss2`, `cssselect2`, `html5lib` for font/CSS/document support.

Production publishing tools now installed on the system path:

- `prince` 16.2 for final publishing-grade HTML/CSS to PDF output when a commercial-quality renderer matters.
- `verapdf` 1.30.1 for PDF/A and PDF/UA-oriented validation gates.
- `qpdf` for structural checking, inspection, repair-friendly transformations, and linearization.
- `gs` / Ghostscript for post-export variants such as ebook, printer, and prepress files.
- `tesseract` with Arabic language data for scanned/OCR workflows.
- `pdftoppm` / Poppler for rendering and raster inspection fallbacks.
- `pandoc` for Markdown/document conversion when needed.

Optional/conditional tools:

- `PDFreactor` remains a licensed/commercial alternative renderer; use it when a license or service endpoint is available.
- `Antenna House Formatter` remains a premium enterprise alternative; use it only when available on the target machine.
- `typst` 0.14.2 is installed from the official `aarch64-unknown-linux-musl` binary at `/usr/local/bin/typst`; use it as the alternate template-driven typesetting path for books authored from scratch.
- `pagedjs` / Vivliostyle browser preview tools are optional only; npm installation hung silently in this Android/PRoot environment, so do not depend on them unless re-tested.

Installed Arabic fonts:

`/root/.local/share/fonts/pdf-book-factory/`

- Noto Naskh Arabic Regular and Bold.
- Noto Sans Arabic Regular and Bold.

Run with:

```bash
/root/.venvs/pdf-book-factory/bin/python <script.py>
```

## When to Use

Use this skill when Mohamed asks to:

- Create a professional PDF book.
- Turn notes, chapters, or a course into a book.
- Redesign a rough PDF into a publishing-grade edition.
- Review a PDF like a global publisher.
- Produce Arabic-first finance, accounting, training, or business books.
- Build a repeatable template for books, guides, reports, or paid digital products.
- Render pages as images and visually audit the book.

Do not use this for one-page quick notes, raw extraction-only tasks, or casual summaries.

## Core Philosophy

Treat the book as a product, not a text file.

Every page must justify itself with at least one of:

- a new concept
- a relationship between concepts
- a numerical example
- a warning or common mistake
- a managerial insight
- an accounting or operational link
- a practical interview-ready answer
- a decision framework

If a page does not provide value, rewrite, merge, or delete it.

## Production Pipeline

### 1. Define the Reader Promise

Before writing, state the promise in one sharp sentence:

- Who is the reader?
- What can they do after reading?
- What situation will this help them win?

Bad promise:

`Understand cost accounting.`

Better promise:

`Give a factory accountant the logic, language, and examples needed to explain product cost changes to finance and operations management.`

### 2. Build the Content Architecture First

Do not start with design.

Create a content outline with:

- cover
- professional note and usage rights
- table of contents
- introduction
- how to use the book
- chapters
- case studies
- numerical examples
- review checklists
- interview answers
- conclusion
- appendix

For each chapter define:

1. real-world scene
2. core idea
3. operational movement
4. accounting effect
5. numerical example
6. summary table
7. managerial insight
8. interview answer
9. common mistake

### 3. Separate Content from Layout

Use separate files:

```text
book_project/
  content/
    chapter_01.md
    chapter_02.md
  templates/
    book.html.j2
  assets/
    style.css
    fonts/
  build/
    book.html
    book.pdf
    pages/
    contact-sheet.png
  scripts/
    create_book.py
    render_review.py
```

The HTML should contain semantic sections:

```html
<section class="cover">...</section>
<section class="frontmatter">...</section>
<section class="chapter">...</section>
<div class="expert-note">...</div>
<table class="comparison">...</table>
```

### 4. Design System Rules

Use a controlled visual identity:

- A4 by default unless the user requests another size.
- Comfortable margins; avoid cheap narrow margins.
- One body font and one heading font.
- A calm background, usually warm off-white for business books.
- Dark professional heading color.
- One accent color, not many decorative colors.
- Tables must have consistent header color, padding, borders, and alignment.
- Footers and page numbers must be consistent.
- Avoid childish fonts for finance, accounting, and executive audiences.

Recommended Arabic font stack:

```css
body {
  font-family: "Noto Naskh Arabic", "Noto Sans Arabic", serif;
  direction: rtl;
  font-size: 10.8pt;
  line-height: 1.66;
}

h1, h2, th {
  font-family: "Noto Sans Arabic", "Noto Naskh Arabic", sans-serif;
}
```

### 5. HTML to PDF Export

Use the right renderer for the stage:

1. Use WeasyPrint for fast drafts and iteration.
2. Use Prince for final serious editions when layout fidelity matters.
3. Use PDFreactor or Antenna House only if the licensed tool is available.
4. Use Typst as a separate authoring path for books written from scratch, not as a universal replacement for the HTML pipeline.

WeasyPrint draft export:

```python
from weasyprint import HTML
HTML(filename="build/book.html").write_pdf("build/book-draft.pdf")
```

Prince final export:

```bash
prince build/book.html -o build/book-final.pdf
```

Use CSS paged-media features:

```css
@page {
  size: A4;
  margin: 16mm;
  background: #fffdf7;
  @bottom-center {
    content: counter(page);
    color: #6f5f43;
    font-size: 9pt;
  }
}
```

### 6. Render Every Page to Images

Never trust the PDF blindly.

Use PyMuPDF to render pages and Pillow to create a contact sheet. Look for:

- broken tables
- orphan headings
- huge empty spaces
- over-compressed pages
- inconsistent backgrounds
- bad page breaks
- wrong page numbers
- cut text
- weak hierarchy
- visual fatigue

### 7. Iterate Like a Publisher

Expect multiple rounds:

1. content-first draft
2. first designed PDF
3. visual review sheet
4. layout fixes
5. content density fixes
6. table and example fixes
7. final proofreading
8. export final edition

The book is not done when the PDF exports. It is done when the visual review and content review both pass.

## Arabic Book Quality Rules for Mohamed

- Arabic body lines must not contain embedded English words.
- Translate generic technical terms where possible.
- Necessary English terms go on standalone lines.
- URLs go on standalone lines.
- Do not use line-by-line robotic formatting unless explicitly requested.
- Use professional Arabic prose suitable for managers, accountants, and executives.
- For finance/accounting books, avoid casual slang and avoid decorative softness.

### Egyptian Professional Official Style Gate

Apply this writing gate before final export:

1. Style is formal, clear, simple, and direct.
2. Use modern easy Fusha that Egyptian readers absorb quickly.
3. Avoid colloquial slang in deliverables unless Mohamed explicitly requests it.
4. Avoid bureaucratic inflation like "نحيط سيادتكم علمًا" when a direct phrasing works.
5. Prefer sentence flow: idea -> concise explanation -> actionable conclusion.
6. Keep sentence length controlled and avoid paragraph overcrowding.
7. Remove padding, repetition, and ornamental expressions.
8. Keep terminology consistent across chapters and tables.
9. Ensure each paragraph serves one clear purpose.
10. Replace vague wording with precise operational language.

### English Professional Style Gate (Only When Requested)

If Mohamed requests an English edition, apply the same rigor in English:

1. Professional, clear, simple, formal business English.
2. One core idea per sentence; one purpose per paragraph.
3. Paragraph sequence: point -> explanation -> practical takeaway.
4. No fluffy marketing language or bureaucratic overstatement.
5. Keep wording precise, operational, and reader-friendly.
6. Keep chapter vocabulary consistent and definitions stable.
7. Use concise headings and explicit transitions.
8. Optimize readability for mixed-seniority business readers.
9. Keep examples practical and decision-oriented.
10. Remove any paragraph that adds no decision value.

## Content Depth Gate

For every chapter, ask:

1. Does it add a new idea, or repeat a previous one?
2. Does it include a practical example?
3. Does it connect operations to finance?
4. Does it include a common mistake?
5. Does it include a manager-ready explanation?
6. Can the reader use it in an interview tomorrow?
7. Are claims precise enough to be audited?
8. Are definitions and formulas explicit where needed?

Delete or rewrite weak paragraphs.

## Visual Quality Gate

Before final delivery, render pages and inspect:

- cover impact
- table of contents alignment
- heading hierarchy
- text density
- table readability
- page breaks
- margins
- footer consistency
- page number correctness
- background consistency
- typography maturity
- whether each page looks sellable

Rule of thumb:

A professional page is neither stuffed nor empty. It has high value density and controlled breathing space.

## Finance and Accounting Book Scientific Gate

For accounting, costing, finance, and factory books, verify:

- cost flow is logically correct
- inventory versus expense timing is correct
- raw materials, work in process, finished goods, and cost of goods sold are separated
- job-order and process-costing logic is not confused
- overhead drivers are operationally justified
- standard versus actual cost logic is clear
- variances separate price, quantity, efficiency, volume, and overhead effects where relevant
- numerical examples reconcile
- tables do not hide missing assumptions
- managerial conclusions follow from the numbers

If the content is educational, explicitly state simplifications.

## Common Layout Problems and Fixes

### Huge empty spaces

Likely causes:

- forced page breaks before every chapter
- forcing `.section { page-break-after: always; }` across long rebuilt Arabic manuscripts (causes blank/near-blank pages)
- tables set to avoid breaking entirely
- headings kept with too much following content
- content too short for the page

Fixes:

- reduce forced page breaks
- allow logical table splitting
- add useful examples, not filler
- tighten vertical rhythm

### Pages feel crowded

Likely causes:

- font too small
- line height too tight
- too many tables
- weak paragraph breaks

Fixes:

- raise line height
- split long tables
- add section rhythm
- move details to appendix

### Tables break visually

Fixes:

- use clear headers
- reduce columns
- use stacked cards for narrow content
- repeat headers if needed
- avoid tiny font unless unavoidable

### Book feels less premium

Likely causes:

- weak font
- too many colors
- inconsistent spacing
- no page rhythm
- poor cover hierarchy

Fixes:

- use Noto Naskh Arabic for body
- use Noto Sans Arabic for headings
- restrict palette
- standardize boxes and tables
- visually review every page

## Commands and Smoke Test

Check the environment:

```bash
/root/.venvs/pdf-book-factory/bin/python - <<'PY'
import weasyprint, fitz, PIL, bs4, jinja2, pypdf
print('pdf book factory ok')
PY
```

Check fonts:

```bash
fc-match 'Noto Naskh Arabic'
fc-match 'Noto Sans Arabic'
```

Generate a smoke test using the linked script:

```bash
/root/.venvs/pdf-book-factory/bin/python ~/.hermes/skills/productivity/professional-pdf-book-factory/scripts/smoke_test.py
```

Run final finishing and quality checks on any exported book:

```bash
/root/.venvs/pdf-book-factory/bin/python ~/.hermes/skills/productivity/professional-pdf-book-factory/scripts/finish_pdf.py build/book-final.pdf --render
```

When the book is intentionally authored for PDF/A, add:

```bash
/root/.venvs/pdf-book-factory/bin/python ~/.hermes/skills/productivity/professional-pdf-book-factory/scripts/finish_pdf.py build/book-final.pdf --pdfa --render
```

## Deliverable Checklist

Reference for full-source upgrade runs: `references/arabic-full-book-upgrade-playbook.md`.

A professional book deliverable should include:

- final PDF
- generated HTML
- CSS design file
- rendered page images or contact sheet
- short review report
- list of remaining risks if any

## Verification Checklist

- [ ] Content promise is explicit.
- [ ] Every chapter follows a repeatable structure.
- [ ] Weak repeated paragraphs removed.
- [ ] Numerical examples checked.
- [ ] Tables are readable after rendering.
- [ ] PDF page count verified.
- [ ] Every page rendered to image.
- [ ] Contact sheet reviewed.
- [ ] No cut-off text.
- [ ] No huge accidental blank areas.
- [ ] No overcrowded pages.
- [ ] Fonts are professional and embedded/available.
- [ ] Arabic direction is correct.
- [ ] Footer and page numbers are consistent.
- [ ] Final file exists and is non-empty.

## Future Improvements for This Skill

Add later:

- a complete reusable book project scaffold
- multiple visual themes
- automated orphan-heading detection
- automated table-overflow detection
- OCR comparison for rendered pages
- a page scoring report
- finance-book formula validator
- templates for case studies, checklists, and interview boxes
