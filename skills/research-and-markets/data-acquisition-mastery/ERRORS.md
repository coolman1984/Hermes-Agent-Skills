# Data Acquisition Mastery Error Log

## 2026-07-08 — Web extraction tool unavailable due missing Tavily key
- Symptom: web extraction calls returned `TAVILY_API_KEY environment variable not set`.
- Root cause: configured extraction backend required a missing API key.
- Fix: use direct HTTP libraries or built-in browser/file tools; record source URLs manually when official docs are known.
- Prevention rule: acquisition skill must include fallback collectors independent of a single web-search provider.

## 2026-07-08 — Over-eager network terminal check blocked
- Symptom: a terminal network status probe was blocked by safety gating.
- Root cause: environment/user-consent policy treated the command as needing confirmation.
- Fix: do not retry the same network probe; continue with local validation sources and documented official URLs.
- Prevention rule: validation must not depend solely on external live sites.

## 2026-07-08 — Hidden API beats scraping dynamic HTML
- Symptom: a dynamic page can display rows only after JavaScript, while raw HTML is empty.
- Root cause: data lives behind an XHR JSON endpoint.
- Fix: inspect network and hit the JSON endpoint directly when authorized.
- Prevention rule: always inspect network/API before browser automation.

## 2026-07-08 — One bad source must not kill a batch acquisition
- Symptom: corrupt URL/file/source can abort a multi-source run.
- Root cause: exceptions were not isolated per source.
- Fix: per-source try/except and manifest status `needs_review`.
- Prevention rule: batch acquisition is partial-success by design.
