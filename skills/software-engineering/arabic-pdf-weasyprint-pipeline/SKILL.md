---
name: arabic-pdf-weasyprint-pipeline
description: Render professional Arabic/RTL PDFs from report data using HTML/CSS and
  WeasyPrint instead of ReportLab.
tags: [arabic, pdf, weasyprint, rtl, html-css, reports]
title: Arabic PDF Pipeline with HTML/CSS and WeasyPrint
category: software-development
---

# Arabic PDF Pipeline with HTML/CSS and WeasyPrint

## When to use this skill

- You need PDF output with correct connected Arabic glyphs and RTL layout.
- ReportLab or other low-level PDF libraries are producing broken Arabic text.
- You want board-pack-style reports with tables, metadata, and cover pages.

## The core idea

Instead of drawing PDF primitives, build an HTML string with proper Arabic
markup and render it with WeasyPrint.  HTML/CSS already handles:

- Connected Arabic glyph shaping (via the browser-quality rendering engine).
- Right-to-left paragraphs and tables.
- Automatic text wrapping and page breaks.
- Repeating table headers across pages.

## Minimal template

```html
<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <style>
    @page { size: A4 landscape; margin: 14mm; }
    body {
      direction: rtl;
      text-align: right;
      font-family: "Noto Naskh Arabic", "Noto Sans Arabic", serif;
      font-size: 10pt;
    }
    table { width: 100%; border-collapse: collapse; direction: rtl; }
    th { background: #12395a; color: white; padding: 7px; text-align: right; }
    td { padding: 6px; border: 1px solid #d9e2ec; text-align: right; }
    .num { direction: ltr; unicode-bidi: isolate; text-align: left; }
  </style>
</head>
<body>
  <h1>عنوان التقرير</h1>
  <table>
    <thead><tr><th>المنطقة</th><th>المبيعات</th></tr></thead>
    <tbody>
      <tr><td>القاهرة</td><td class="num">1,234,567</td></tr>
    </tbody>
  </table>
</body>
</html>
```

Render with:

```python
from weasyprint import HTML
HTML(string=html).write_pdf("output.pdf")
```

## Translation strategy

- Keep a column-label dictionary mapping internal names to Arabic labels.
- Translate static phrases once, outside the HTML builder.
- Keep numbers as-is and wrap them in a `.num` class so they stay LTR.

## Layout rules that matter

1. **Always** set `<html lang="ar" dir="rtl">`.
2. **Always** set `direction: rtl` on Arabic containers.
3. Use `unicode-bidi: isolate` on mixed-direction text.
4. Use `@page` to control size, orientation, and margins.
5. Test by converting the first pages to PNG and visually inspecting.

## Common pitfalls

- **ReportLab `<font face="...">` does not work**; ReportLab uses `name="..."` and still fails on complex Arabic shaping.
- Numbers inside Arabic sentences can flip direction if not isolated with CSS.
- Without a proper Arabic font family, fallback fonts may render disconnected glyphs.
- Page breaks inside tall tables can be tuned with `page-break-inside: avoid` on rows if needed.

## Verification checklist

- [ ] Generated PDF opens without errors.
- [ ] Arabic text is connected and readable.
- [ ] Text direction is RTL.
- [ ] Numbers are LTR and aligned consistently.
- [ ] Table headers repeat across pages (for multi-page reports).
- [ ] Cover page renders correctly.
