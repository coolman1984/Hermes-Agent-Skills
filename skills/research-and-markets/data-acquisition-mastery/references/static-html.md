# Static HTML

Use requests/httpx + BeautifulSoup/lxml. Choose stable selectors based on semantic tags, ids, data attributes, or table headers. Avoid brittle CSS paths based on layout. Save raw HTML before parsing.

Sources: BeautifulSoup docs https://www.crummy.com/software/BeautifulSoup/bs4/doc/ ; lxml docs https://lxml.de/

When to use: public pages without JS dependency. When it fails: content rendered after JS, bot blocks, markup changes. Watch: duplicate rows, pagination, hidden tables.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
