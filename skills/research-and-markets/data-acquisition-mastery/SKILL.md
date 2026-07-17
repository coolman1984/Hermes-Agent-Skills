---
name: data-acquisition-mastery
description: Use whenever the user asks to research, collect, monitor, pull, crawl, scrape, fetch, download, acquire, or gather data from any website, API, feed, file listing, repository, public dataset, search result, or online source. Also triggers on hidden JSON APIs, dynamic sites, pagination, rate limits, robots.txt, data manifests, source provenance, and handing raw payloads to data-extraction-mastery.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
metadata:
  hermes:
    tags: [research, data-acquisition, scraping, api, http, playwright, robots, feeds, datasets]
    related_skills: [data-extraction-mastery, database-mastery, web-browsing]
---

# Data Acquisition Mastery

## Mission

Acquire raw data from the cleanest authorized source, preserve provenance and legal basis, save raw payloads and manifests, then hand payloads to `data-extraction-mastery` for parsing and `database-mastery` for analysis.

## Mandatory Start

1. Read `ERRORS.md`.
2. Ask: is there an official API, export, data dump, RSS/feed, or documented endpoint? Use that before scraping.
3. Check legality/ethics: terms, robots.txt, licensing, privacy, rate limits.
4. Choose the least invasive collector: API → feed/file dump → static HTML → hidden XHR JSON → browser automation.
5. Throttle, cache, identify politely, and avoid hammering.
6. Save raw payload, manifest, source URL, retrieval time, status, headers subset, license/legal basis, and warnings.
7. Hand raw files to `data-extraction-mastery` when parsing begins.

## Iron Rules

- API before scraping, always.
- If robots.txt or terms forbid automated access, stop and report the boundary.
- CAPTCHA is a stop/seek-authorized-route signal, not a challenge to defeat.
- Do not collect personal data unlawfully.
- Use exponential backoff with jitter for transient errors.
- Never bypass authentication, paywalls, or access controls.
- Cache raw payloads and avoid repeated fetches.
- Treat 403/429 as signals to slow down, authenticate properly, or stop.
- Record legal basis and source license in the manifest.
- Acquisition is not extraction: save raw first, then hand to `data-extraction-mastery`.

## Router

| Source signal | Reference | Default move |
|---|---|---|
| HTTP/API/headers/status/retries | `references/http-acquisition.md` | requests/httpx with retries, manifest |
| REST/GraphQL/open data portals | `references/apis-and-feeds.md` | documented API, pagination, schema capture |
| Static HTML/table/page | `references/static-html.md` | requests + BeautifulSoup/lxml, selectors |
| Dynamic JS site / infinite scroll | `references/dynamic-sites.md` | inspect network/XHR first, Playwright only if needed |
| Defended site/429/403/CAPTCHA | `references/defenses-ethics.md` | slow/stop/authorized route |
| Files, zips, PDFs, datasets | `references/datasets-files.md` | download raw, checksum, hand to extraction |
| Monitoring recurring sources | `references/monitoring.md` | conditional requests, hashes, cron-friendly manifests |
| Source manifest/provenance | `references/provenance-manifest.md` | JSONL manifest for every payload |
| Tool/source map | `references/resources-and-leads.md` | official docs first |
| No-key web search fallback | `references/brave-search-fallback.md` | Brave Search curl when Tavily/Exa/DuckDuckGo are all blocked |

## Default Flow

```text
source question → authorized path → robots/terms/rate limit check → acquire raw → manifest → extraction handoff → database analysis
```

## Scripts

```bash
python scripts/fetch_url.py URL --out /tmp/acq
python scripts/check_robots.py https://example.com/path
python scripts/api_collect.py URL --out /tmp/acq --paginate next_url
python scripts/scrape_static.py URL_OR_HTML --out /tmp/acq
python scripts/discover_links.py URL --out /tmp/acq
python scripts/batch_acquire.py sources.txt --out /tmp/acq_run
```

## Completion Checklist

- [ ] Authorized path chosen before scraping.
- [ ] Robots/terms/legal basis noted.
- [ ] Rate limit/throttle used.
- [ ] Raw payload saved.
- [ ] Manifest written.
- [ ] Errors/blocks logged.
- [ ] Payload handed to `data-extraction-mastery` when parsing starts.
