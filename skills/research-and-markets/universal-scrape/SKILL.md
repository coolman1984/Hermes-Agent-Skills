---
name: universal-scrape
description: "Three-layer web scraping with no browser or system packages — Jina Reader for JS-heavy SPAs, curl + Cheerio for static HTML, plus fallbacks — designed to work on Android ARM64 / Termux / PRoot. Use when scraping pages in constrained environments where Playwright or headless Chrome cannot run."
tags: [scraping, jina, cheerio, termux, android, no-browser]
---

# Universal Scrape Skill

No browser, no binary, no system packages needed. Works on Android ARM64 / Termux / PRoot.

## How It Works

Three layers, each better for different jobs:

| Layer | Tool | Best For |
|-------|------|----------|
| 1 | **Jina Reader** (`r.jina.ai`) | JavaScript-heavy sites, SPAs, complex pages |
| 2 | **Curl + Cheerio** | Static HTML sites, fast parsing |
| 3 | **YouTube Innertube API** | YouTube search, video details |

## Quick Start

```bash
cd skills/universal-scrape

# Any URL → clean Markdown (JS sites included!)
node universal_scrape.js jina "https://news.ycombinator.com"
node universal_scrape.js jina "https://twitter.com/user/status/123"

# Static site → parsed HTML
node universal_scrape.js scrape "https://example.com"

# YouTube search (no browser)
node universal_scrape.js yt-search "AI agents 2026"

# YouTube video details
node universal_scrape.js yt-video dQw4w9WgXcQ
```

## In Python Code

```python
import subprocess
result = subprocess.run(
    ["node", "skills/universal-scrape/universal_scrape.js", "jina", url],
    capture_output=True, text=True, timeout=30
)
print(result.stdout)  # Clean Markdown
```

## In Another Node.js Script

```javascript
import { youtubeSearch, jinaRead } from './universal_scrape.js';
const results = await youtubeSearch('AI agents');
const page = await jinaRead('https://news.ycombinator.com');
```

## What Each Layer Returns

### Jina Reader
```javascript
// Input: URL
// Output: Clean Markdown text (server-side rendered)
// Handles: Twitter, HN, LinkedIn, Reddit, any JS-heavy site
// Rate limit: ~100 requests/day (free tier)
```

### Curl + Cheerio
```javascript
// Input: URL
// Output: { url, title, text, links, meta }
// Handles: Static sites, fast parsing
```

### YouTube API
```javascript
// Input: query string
// Output: [{ id, title, channel, duration, views, url }, ...]
// Rate limit: Very high (uses YouTube's own API)
```

## SSL Workaround

The PRoot environment has broken CA certificates. All HTTPS requests use `curl -sk` to bypass verification. This is safe for scraping — never for authentication.

## Limitations

- **Jina rate limits** (~100 req/day free) — use it for JS-heavy sites only
- **Login-required sites** (NotebookLM, X.com cookies) — need browser bridge
- **Rate limiting** — add delays between requests

## Testing

```bash
node universal_scrape.js jina "https://example.com"
node universal_scrape.js scrape "https://example.com"  
node universal_scrape.js yt-search "test"
```
