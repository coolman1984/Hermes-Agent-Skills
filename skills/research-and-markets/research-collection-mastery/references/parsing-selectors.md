# Parsing and Selectors

Use BeautifulSoup/lxml/parsel. Pick stable selectors: semantic tags, IDs, data attributes, table headers, JSON-LD. Avoid brittle nth-child layout selectors. Save raw before parse.

Sources: BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/ ; lxml https://lxml.de/ ; parsel https://parsel.readthedocs.io/

When to use: static authorized HTML. When it fails: JS-rendered content or unstable markup.

Usage image: choose authorized source, collect raw, manifest it, then hand off.
