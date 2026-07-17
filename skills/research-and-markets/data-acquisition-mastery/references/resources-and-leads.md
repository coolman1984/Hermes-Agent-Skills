# Resources and Leads

| Source | URL | Best for |
|---|---|---|
| MDN HTTP | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview | HTTP concepts |
| RFC 9110 | https://www.rfc-editor.org/rfc/rfc9110.html | HTTP semantics |
| requests | https://requests.readthedocs.io/ | simple HTTP |
| HTTPX | https://www.python-httpx.org/ | sync/async HTTP |
| BeautifulSoup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | HTML parsing |
| Playwright | https://playwright.dev/python/docs/intro | browser automation |
| robotparser | https://docs.python.org/3/library/urllib.robotparser.html | robots.txt checks |
| pandas read_html | https://pandas.pydata.org/docs/reference/api/pandas.read_html.html | HTML tables |

Top traps: scraping before checking API; ignoring robots/terms; no user-agent; no timeouts; no retries; no cache; no manifest; browser automation when XHR JSON exists; treating CAPTCHA as a puzzle; collecting personal data without basis.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
