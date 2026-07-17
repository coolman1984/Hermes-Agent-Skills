---
name: research-collection-mastery
description: Use whenever the user wants to collect, gather, scrape, crawl, harvest, or research data from the web, research papers, arXiv, GitHub, social media, forums, news, or any online source — even if they just say find me data on X or get everything about Y. Covers APIs, scraping, headless browsers, hidden JSON APIs, feeds, academic APIs, GitHub APIs, social APIs, and large-scale crawling.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [research, collection, crawling, scraping, api, arxiv, github, social-media, feeds, playwright, scrapy]
    related_skills: [data-acquisition-mastery, data-extraction-mastery, database-mastery]
---

# Research Collection Mastery

## Mission

Find and collect raw research/data payloads from authorized online sources with senior-engineer discipline: API first, legal basis recorded, polite collection, raw payload manifest, then handoff to `data-extraction-mastery` and `database-mastery`.

## Mandatory Start

1. Read `ERRORS.md`.
2. Choose authorized path: official API/dump/feed/export before scraping.
3. Check robots.txt, terms, license, privacy, rate limits, and authentication scope.
4. Inspect network/XHR before using browser automation.
5. Throttle, cache, identify politely, and never hammer.
6. Save raw payloads and manifest before parsing.
7. Hand raw payloads to `data-extraction-mastery`; analysis belongs in `database-mastery`.

## Iron Rules

- API/data dump/feed before scraping.
- CAPTCHA/hard block means slow down, stop, or seek authorized access — never brute-force.
- Do not bypass login, paywalls, authentication, or access controls.
- Rotate identity only for legitimately public data and never to evade explicit prohibition.
- Respect robots.txt, terms, licenses, copyright, privacy, and rate limits.
- Distributed crawling requires frontier, dedup, politeness, retries, and kill switches.
- Every run emits a manifest: URL, timestamp, legal basis, checksum, status, cache path.
- Log every block, empty payload, malformed response, or source-specific gotcha in `ERRORS.md`.

## Router

| Signal | Reference | Default move |
|---|---|---|
| HTTP, retries, async, sessions | `references/http-foundations.md` | `scripts/fetch.py` with manifest |
| CSS/XPath, HTML parsing | `references/parsing-selectors.md` | stable selectors, save raw HTML |
| Dynamic site, hidden JSON, infinite scroll | `references/dynamic-sites.md` | network/XHR first, then browser only if needed |
| Anti-bot, CAPTCHA, stop signals | `references/anti-bot.md` | ethics checklist and refusal if needed |
| Large crawl | `references/scrapy-at-scale.md` | frontier + dedup + politeness |
| Academic papers | `references/academic-sources.md` | arXiv/OpenAlex/Crossref/PubMed/Unpaywall |
| GitHub/code | `references/github-sources.md` | GitHub REST/GraphQL/archive |
| Social/forums/news | `references/social-media.md` | official APIs/RSS/exports first |
| Search/discovery | `references/feeds-and-discovery.md` | RSS/sitemaps/JSON-LD/search decomposition |
| Law/ethics | `references/legality-ethics.md` | stop checklist |
| Sources/tools | `references/resources-and-leads.md` | official docs map |

## Scripts

```bash
python scripts/fetch.py URL --out /tmp/run
python scripts/find_hidden_api.py URL_OR_HTML --out /tmp/run
python scripts/render_and_collect.py URL --out /tmp/run
python scripts/arxiv_harvest.py 'cat:cs.AI' --out /tmp/run --max-results 50 --pdf-limit 5
python scripts/github_collect.py owner/repo --out /tmp/run --issues
python scripts/collect_with_manifest.py sources.txt --out /tmp/run
```

## Handoff

Raw payloads, PDFs, HTML, JSON, CSV, feeds, and manifests go to `data-extraction-mastery`. Structured tables/databases then go to `database-mastery`.
