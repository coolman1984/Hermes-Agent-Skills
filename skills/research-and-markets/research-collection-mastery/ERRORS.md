# Research Collection Mastery Error Log

## 2026-07-08 — Validation must not depend on bypassing external defenses
- Symptom: external sites can block or change during validation.
- Root cause: live web is not deterministic.
- Fix: validate core mechanics on a local authorized server; use real public APIs where stable and permitted.
- Prevention rule: combine controlled tests with real API smoke tests, and label substitutions honestly.

## 2026-07-08 — Hidden JSON API beats rendered scraping
- Symptom: dynamic page has empty HTML list but network JSON contains records.
- Root cause: JavaScript fetches data after load.
- Fix: collect the JSON endpoint directly when authorized.
- Prevention rule: inspect network/XHR before browser automation.

## 2026-07-08 — Hidden API regex accidentally over-escaped
- Symptom: hidden API discovery found no `fetch('/api/...')` candidates in a controlled dynamic page.
- Root cause: regex pattern used `\\(` instead of `\(` after script generation escaping.
- Fix: compile scripts and test regex against a local dynamic page; use single escaped parenthesis in raw regex.
- Prevention rule: every generated collector regex must be tested on a fixture before packaging.

## 2026-07-08 — arXiv API HTTP endpoint redirected with empty body
- Symptom: arXiv harvester failed XML parse because `http://export.arxiv.org` returned 301 with empty content.
- Root cause: script used HTTP instead of HTTPS and did not follow redirect there.
- Fix: use `https://export.arxiv.org/api/query`.
- Prevention rule: academic API collectors must check status/content-type before parsing and prefer HTTPS endpoints.

## 2026-07-08 — GitHub stargazers timestamp endpoint may require auth/richer headers
- Symptom: unauthenticated stargazers request with star timestamp media type returned 401 in validation.
- Root cause: GitHub API access/rate/auth behavior differs by endpoint/media type and environment.
- Fix: keep repo/issues collection working; write an empty stargazers sample plus `star_warning` advising `GITHUB_TOKEN` for richer star history.
- Prevention rule: GitHub collectors must degrade gracefully and record rate/auth limitations in the manifest.

## 2026-07-08 — Mastodon public timeline endpoint required auth on mastodon.social
- Symptom: `/api/v1/timelines/public` returned 422 requiring authenticated user.
- Root cause: instance-specific API policy restricts unauthenticated public timeline access.
- Fix: validation used documented unauthenticated trends statuses endpoint with limit.
- Prevention rule: social collectors must record endpoint-specific auth requirements and prefer documented public endpoints or authenticated official access.

## 2026-07-08 — Robots disallow is a pass condition when refused
- Symptom: source path is disallowed.
- Root cause: robots.txt says no automated access to path.
- Fix: stop, log refusal, propose API/export/permission path.
- Prevention rule: refusal is successful senior behavior when collection is not permitted.
