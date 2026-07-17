---
name: website-scrape
description: "Scrape websites with scrape_web.py: BeautifulSoup for static HTML, Playwright for JavaScript-heavy SPAs, with text-only and selector extraction options. Use when the user wants page content, tables, or structured data pulled from a URL."
tags: [scraping, beautifulsoup, playwright, web, extraction]
---

# Website Scraping Skill

Scrape static HTML sites with BeautifulSoup, or JavaScript-heavy SPAs with Playwright when available.

## Quick Reference

```bash
# Basic scrape
python3 skills/website-scrape/scrape_web.py "https://example.com"

# Text only
python3 skills/website-scrape/scrape_web.py "https://news.ycombinator.com" --text-only

# Links only
python3 skills/website-scrape/scrape_web.py "https://example.com" --links

# JSON output
python3 skills/website-scrape/scrape_web.py "https://example.com" --json

# Extract specific elements
python3 skills/website-scrape/scrape_web.py "https://example.com" \
    --select "article:h3" --select "p:paragraphs"

# JavaScript-heavy site
python3 skills/website-scrape/scrape_web.py "https://example.com" --dynamic
```

## In Python

```python
from skills.website-scrape.scrape_web import scrape_static, scrape_with_fallback

# Static site
result = scrape_static("https://example.com")
print(result["title"])
print(result["text"])
print(result["links"][:5])

# Auto-detect (static first, dynamic if needed)
result = scrape_with_fallback("https://example.com")
```

## Methods

| Method | Use Case |
|--------|---------|
| `scrape_static()` | Fast, best for most sites |
| `scrape_dynamic()` | JS-heavy SPAs, React, Vue |
| `scrape_with_fallback()` | Auto-detect: try static, use dynamic if needed |
| `extract_structured()` | Articles, products, reviews |

## What Gets Extracted

- **Title** — page title or first H1
- **Meta description** — SEO description
- **Text** — clean text, scripts/styles removed
- **Links** — all external links with anchor text
- **Word count** — for content analysis
- **Selected elements** — via CSS selectors

## CSS Selector Examples

```
article:h3          → Extract all h3 inside article tags
.main p              → Paragraphs inside .main
.product .price      → Price elements inside .product
blockquote           → All blockquotes
.meta .author        → Author inside .meta
```

## JavaScript Sites

```python
# Playwright for dynamic sites
from scrape_web import scrape_dynamic
import asyncio
result = asyncio.run(scrape_dynamic("https://example.com"))
```

Note: Playwright needs browser binaries. If not available, falls back to static.

## When to Use Scraping vs Web Fetch

| Task | Tool |
|-------|------|
| Quick page content | `scrape_web.py` |
| Full page with JS | `scrape_web.py --dynamic` |
| Clean text extraction | `scrape_web.py --text-only` |
| Find all links | `scrape_web.py --links` |
| Specific elements | `--select "css:selector"` |
| No JS needed | `requests` directly |

## Tips

- Always check `robots.txt` before scraping
- Add delays between requests for polite scraping
- Use `--select` to get exactly what you need, not the whole page
- For search results, use DuckDuckGo instead of scraping search engines
