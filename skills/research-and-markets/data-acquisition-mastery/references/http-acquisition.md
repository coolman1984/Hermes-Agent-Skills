# HTTP Acquisition

Core concepts: methods, headers, cookies, sessions, redirects, status codes, retries, timeout, TLS, compression, cache validators, and content negotiation. Prefer `httpx` for modern sync/async clients and `requests` for simple scripts. Use exponential backoff with jitter for transient 429/5xx.

Sources: MDN HTTP overview https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview ; RFC 9110 https://www.rfc-editor.org/rfc/rfc9110.html ; requests docs https://requests.readthedocs.io/ ; HTTPX docs https://www.python-httpx.org/

When to use: any web/API pull. When it fails: auth required, blocked, CAPTCHA, forbidden automation. Watch: status codes and retry-after headers.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
