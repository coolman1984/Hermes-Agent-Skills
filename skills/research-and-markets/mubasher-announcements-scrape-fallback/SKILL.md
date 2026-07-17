---
name: mubasher-announcements-scrape-fallback
description: Reliable fallback for extracting recent EGX/Mubasher announcements when web search/extract tools are blocked or return generic wrappers.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [egypt, egx, mubasher, scraping, announcements, research]
---

# Mubasher Announcements Scrape Fallback

Use this skill when you need recent EGX announcements/news for Egyptian stocks and the normal web tools are blocked, rate-limited, or return wrapper text.

## When to use
- web_search returns errors or empty results
- web_extract returns generic wrappers / unreadable article bodies
- Mubasher pages are accessible in browser/terminal but not via extract tools
- You need fast headline-level verification for a ticker

## Reliable method
1. Fetch the announcements page directly with `requests` in terminal or a Python script.
2. Parse with `BeautifulSoup`.
3. On Mubasher announcements pages, the useful structure is usually:
   - `div.mi-announcement`
   - `.mi-announcement__date`
   - `.mi-announcement__source`
   - nested `<a>` for the headline and link
4. Keep only the visible metadata and headline text. Do not invent article details if the body is blocked.
5. Prioritize recent timestamped items such as:
   - treasury stock releases
   - AGM/EGM invites and minutes
   - board decisions
   - results releases
   - regulatory/FRA disclosures

## Practical page targets
- `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/announcements/`
- `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/`
- `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/profile/`
- `https://english.mubasher.info/markets/EGX/stocks/{TICKER}/volume-statistics/`

## Output rules
- Label anything recovered only from headline/date as headline-derived.
- If the stock page has little or no numeric quote block, switch to announcements immediately.
- If the timestamp does not clearly look like a market-session time, downgrade confidence.
- Never treat a wrapper page or generic shell as a factual article source.

## Practical failure mode observed
- In some Hermes runs, `web_search` can fail consistently with HTTP 432 against the Tavily backend.
- When that happens, do **not** keep retrying broad web search for EGX/Mubasher facts.
- Go directly to `requests` in terminal or a Python script and parse the Mubasher HTML with `BeautifulSoup`.
- For Egyptian stock monitoring, the most useful fallback is usually still the announcements page, because it often exposes static headline/date/source metadata even when article bodies are blocked.

## Example extraction pattern
- Headline: use the anchor text
- Date: use `.mi-announcement__date`
- Source: use `.mi-announcement__source`
- Link: use the anchor href

## Why this works
Mubasher often exposes announcement metadata in static HTML even when the full article body or search extraction is blocked. That makes it a strong operational fallback for Egyptian equity monitoring.
