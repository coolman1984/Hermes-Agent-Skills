# Resources and Leads

| Area | URL | Best use |
|---|---|---|
| HTTP | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview | protocol basics |
| HTTPX | https://www.python-httpx.org/ | modern HTTP clients |
| BeautifulSoup | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | static parsing |
| Playwright | https://playwright.dev/python/docs/intro | dynamic/browser tasks |
| Scrapy | https://docs.scrapy.org/ | large crawling |
| arXiv | https://info.arxiv.org/help/api/ | paper metadata/PDF links |
| OpenAlex | https://docs.openalex.org/ | scholarly graph |
| GitHub REST | https://docs.github.com/en/rest | repo/issues/releases |
| Reddit | https://www.reddit.com/dev/api/ | compliant Reddit access |
| Mastodon | https://docs.joinmastodon.org/api/ | federated public APIs |

Top traps: scraping before API; ignoring robots; no manifest; no backoff; no dedup; browser before XHR; collecting personal data without basis; treating CAPTCHA as challenge; no cache; no handoff boundary.

Usage image: choose authorized source, collect raw, manifest it, then hand off.
