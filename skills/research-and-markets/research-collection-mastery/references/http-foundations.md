# HTTP Foundations

Use timeouts, retries with exponential backoff and jitter, sessions/cookies, redirects, cache validators, and clear User-Agent. Prefer httpx for sync/async; requests remains simple and reliable.

Sources: MDN HTTP https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview ; RFC 9110 https://www.rfc-editor.org/rfc/rfc9110.html ; HTTPX https://www.python-httpx.org/ ; requests https://requests.readthedocs.io/

When to use: every web/API pull. When it fails: forbidden, auth required, CAPTCHA, malformed response.

Usage image: choose authorized source, collect raw, manifest it, then hand off.
