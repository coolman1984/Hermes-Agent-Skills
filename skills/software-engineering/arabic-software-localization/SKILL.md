---
name: arabic-software-localization
description: "Use when adding or fixing Arabic (RTL) support in a full-stack web application — i18n architecture, browser QA, PDF rendering, Excel RTL, and localization pitfalls. Covers the dual-layer dictionary+regex pattern from Company-Dashboard and ReportLab Arabic font/shaping mechanics."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [arabic, i18n, rtl, localization, pdf, reportlab, browser-qa]
    related_skills: [senior-software-engineer, mohamed-arabic-content-style, code-review]
---

# Arabic Software Localization

## Overview

Patterns and pitfalls for Arabic-first localization in full-stack web apps — learned from the Company-Dashboard project. Covers i18n architecture, browser QA, PDF/Excel rendering, and RTL layout.

Arabic localization is not just translation. It requires:
- **Bidirectional-aware layout** (RTL for Arabic, LTR fallback for English)
- **Text shaping** (Arabic letters connect differently based on position)
- **Dual-layer translation** (static dictionary + dynamic regex patterns)
- **Font handling** (system fonts for web, vendored fonts for PDF)

## When to Use

- Adding Arabic translations to an existing web app
- Fixing untranslated or mis-rendered Arabic text
- Generating Arabic PDF reports (ReportLab)
- Generating Arabic Excel reports (openpyxl)
- QA pass for Arabic RTL UI
- Setting up i18n for a new Arabic-first project

## Architecture: Dual-Layer i18n

The most effective pattern (used in Company-Dashboard) combines two layers:

### Layer 1: Static Dictionary (`DICT`)

For fixed, known strings. Fast, predictable, easy to audit.

```javascript
var DICT = {
    "ar": {
        "Revenue": "الإيرادات",
        "Gross Margin": "هامش الربح الإجمالي",
        "Save": "حفظ",
    }
};

function t(key) {
    var lang = getLang();
    return (DICT[lang] && DICT[lang][key] !== undefined) ? DICT[lang][key] : undefined;
}
```

Use for: UI labels, navigation, button text, static headings.

### Layer 2: Regex Patterns (`translateText`)

For **dynamically generated** strings that contain variables (year numbers, counts, region names). Applied AFTER the dictionary lookup fails.

```javascript
function translateText(text) {
    if (!langIsAr) return text;
    var direct = t(text);           // Try dictionary first
    if (direct !== undefined) return direct;
    
    // Then try regex patterns
    return text
        .replace(/^Revenue: \$(.*)M$/, "الإيرادات: $1 مليون دولار")
        .replace(/^FY(\d{4}) revenue$/, "إيرادات السنة المالية $1")
        .replace(/^Change vs FY(\d{4})$/, "التغير مقابل السنة المالية $1");
}
```

Use for: generated headings (e.g. "FY2026 revenue"), status messages with counts, table headers with year references, executive summary copy text.

### How they work together

```
User-facing string → t(key) [dictionary] → hit? return translation
                                          → miss? translateText(text) [regex patterns] → return translation or original
```

### Pitfall: Case Sensitivity

Dictionary keys are **exact match**. `t("Revenue")` ≠ `t("REVENUE")` ≠ `t("revenue")`. Always add both case variants for programmatically-generated strings, or normalize the key before lookup.

```javascript
// BAD — misses uppercase variant
DICT["ar"]["Revenue"] = "الإيرادات";
tr("REVENUE");  // returns "REVENUE" (untranslated)

// GOOD — add both
DICT["ar"]["Revenue"] = "الإيرادات";
DICT["ar"]["REVENUE"] = "الإيرادات";
```

## Browser QA Workflow for Arabic

1. **Seed Arabic data** — if your seed script supports it (`--locale ar`), use it so names/regions appear in Arabic
2. **Start the server** and open the app
3. **Check console** — zero errors is the bar. Any red means something broke silently
4. **Scan for English** — walk the DOM text nodes and flag any string starting with `[A-Za-z]` longer than ~12 chars that isn't a number/date/technical abbreviation

```javascript
// Quick English-text scanner for browser console
var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
var eng = [];
while (walker.nextNode()) {
    var t = walker.currentNode.textContent.trim();
    if (t.length > 12 && /^[A-Za-z]/.test(t) && 
        !t.match(/^[\d,.+\-%$£€\s()MKB×]+$/) &&
        !t.includes('SQLite') && !t.includes('FY')) {
        eng.push(t);
    }
}
console.log(eng);
```

5. **Click every tab** — dynamic content loads differently; what's translated on tab 1 may not be on tab 4
6. **Toggle between Arabic and English** — verify the toggle works and doesn't leak one language into the other

### Pitfall: MutationObserver Timing

If your i18n system uses a `MutationObserver` to translate dynamically-injected DOM text, it may miss content that arrives in the initial page load before the observer is attached. Always call `apply()` on DOMContentLoaded AND THEN start the observer.

```javascript
document.addEventListener("DOMContentLoaded", function () {
    apply();              // Translate existing DOM
    observeDynamicText(); // Start watching for new content
});
```

## ReportLab Arabic PDF Rendering

ReportLab does NOT support Arabic out of the box. Three things must happen, in this exact order:

### 1. Register the Font (once, globally)

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

_ARABIC_FONT_PATH = "fonts/NotoNaskhArabic.ttf"

def _register_arabic_font():
    if not os.path.exists(_ARABIC_FONT_PATH):
        return
    pdfmetrics.registerFont(TTFont("Arabic", _ARABIC_FONT_PATH))
```

**Critical:** This must be called BEFORE any Paragraph that uses the font. If you have a cover page before the first report, register the font at the start of the cover function, not inside a per-report function.

### 2. Shape the Text

Arabic letters need reshaping (they connect differently based on position in a word) and bidirectional reordering (English numbers embedded in Arabic text flow LTR).

```python
import arabic_reshaper
from bidi.algorithm import get_display

config = arabic_reshaper.config_for_true_type_font(
    _ARABIC_FONT_PATH, arabic_reshaper.ENABLE_ALL_LIGATURES
)
reshaper = arabic_reshaper.ArabicReshaper(configuration=config)

def _shape_arabic(text):
    if not text or not _has_arabic(text):
        return text
    return get_display(reshaper.reshape(text))
```

**Pitfall:** `_shape_arabic()` produces correctly-shaped Unicode characters, but ReportLab's default Helvetica font has no glyphs for Arabic. The shaped text renders as empty boxes (`nnnn`) unless you tell the Paragraph to use the Arabic font.

### 3. Wrap in `<font>` XML Tag

ReportLab's `Paragraph` class respects a subset of HTML tags. To use the registered Arabic font, wrap shaped text in:

```python
title_xml = f'<font face="Arabic">{_shape_arabic(ar_title)}</font>'
Paragraph(title_xml, styles["Title"])
```

**Without the `<font>` tag:** Arabic text renders as `nnnn` (empty glyphs) even if the font is registered and text is shaped.

**With the `<font>` tag:** Arabic renders correctly.

### 4. The `force_arabic` Pattern

When building a board pack with an Arabic title, propagate Arabic rendering to ALL child reports even if their individual data (column names, values) is English. The user chose Arabic for the pack — honor it throughout.

```python
def render_pdf_pack(envelopes, out_path, title="Board Pack"):
    is_arabic_pack = _has_arabic(title)
    
    if is_arabic_pack:
        _register_arabic_font()  # EARLY — before any rendering
    
    for env in envelopes:
        # Reports use force_arabic=True when pack title is Arabic
        flowables = _pdf_report_flowables(env, styles, doc.width, force_arabic=is_arabic_pack)
```

### Full Rendering Checklist

- [ ] Arabic font file exists at the path (vendored, not system-dependent)
- [ ] Font registered BEFORE any Paragraph that uses it
- [ ] Text shaped via arabic_reshaper + bidi BEFORE wrapping
- [ ] Shaped text wrapped in `<font face="Arabic">...</font>` XML
- [ ] Cover page rendered with Arabic font (register early!)
- [ ] Meta text (date, source, row count) translated and shaped
- [ ] Report titles and descriptions translated via dictionary
- [ ] Column headers translated (in the envelope layer, not the renderer)

## Excel RTL for Arabic

openpyxl supports worksheet-level RTL:

```python
from openpyxl import Workbook
ws = wb.active
ws.sheet_view.rightToLeft = True  # Arabic sheets flow RTL
```

For column formatting, use `#,##0` patterns (same as LTR) — Excel handles digit display based on the sheet locale.

## Known Pitfalls

1. **Case-sensitive dictionary keys** — `t("Revenue")` ≠ `t("REVENUE")`. Add both or normalize.
2. **MutationObserver misses initial load** — call `apply()` before `observeDynamicText()`.
3. **ReportLab font registration order** — register before any Paragraph, not inside a per-report function that may run too late.
4. **Missing `<font>` tag** — shaped text without `<font face="Arabic">` renders as blank boxes.
5. **Arabic seed data changes API queries** — if `seed_db.py --locale ar` changes region names from "Africa" to "أفريقيا", API queries using English region names (`?region=Africa`) will return empty results.
6. **Regex must handle FY prefix variants** — "Share of FY2026 outlook" and "Share of 2026 outlook" may both appear; add patterns for both.
7. **Dynamic strings in JS need `tr()` wrapper** — don't hardcode English in template literals that will be injected into the DOM. Use `tr('Change vs FY' + year)` so the translation layer can catch it.

## Reference Files

- `references/company-dashboard-arabic-qa.md` — session log: which files changed, which texts were found, regexes added
