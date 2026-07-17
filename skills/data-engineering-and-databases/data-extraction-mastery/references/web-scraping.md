# Web and Semi-Structured Extraction

Use requests+BeautifulSoup for static pages. Use `pandas.read_html` for HTML tables; when passing literal HTML already loaded into a string, wrap it with `io.StringIO(html)` so pandas does not treat the string as a path/URL. Use Playwright/Selenium only when JavaScript renders the data. Use APIs/RSS/JSON/XML directly when available. Respect rate limits and terms.

Sources: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ ; https://pandas.pydata.org/docs/reference/api/pandas.read_html.html ; Playwright docs.

When to use: web pages, public tables, feeds. When it fails: blocked pages, login, JS-only data without browser. Watch: pagination and changing markup.

Usage image: detect, preserve structure, validate, and only then normalize/load.
