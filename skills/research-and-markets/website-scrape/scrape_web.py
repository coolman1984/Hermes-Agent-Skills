#!/usr/bin/env python3
"""
scrape_web.py — Website scraping toolkit for OpenClaw
Supports: static HTML (requests+BeautifulSoup) and dynamic JS (playwright when available)
"""
import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime

import requests
from bs4 import BeautifulSoup

HAS_PLAYWRIGHT = False
try:
    from playwright.async_api import async_playwright
    HAS_PLAYWRIGHT = True
except ImportError:
    pass


def scrape_static(url, selectors=None, timeout=15):
    """
    Scrape a static HTML page with BeautifulSoup.
    Returns: title, text, links, metadata, selected elements.
    """
    try:
        r = requests.get(url, timeout=timeout, headers={
            "User-Agent": "Mozilla/5.0 (compatible; OpenClaw/1.0)"
        })
        r.raise_for_status()
    except Exception as e:
        return {"url": url, "error": f"Request failed: {e}"}

    soup = BeautifulSoup(r.text, "html.parser")

    # Extract title
    title = ""
    if soup.title:
        title = soup.title.string.strip()
    elif soup.find("h1"):
        title = soup.find("h1").get_text().strip()

    # Extract meta description
    meta_desc = ""
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        meta_desc = meta.get("content", "")

    # Extract all text
    # Remove script, style, nav, header, footer
    for tag in soup(["script", "style", "nav", "header", "footer", "aside", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Extract links
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        link_text = a.get_text(strip=True)
        if href.startswith("http"):
            links.append({"url": href, "text": link_text})

    # Extract selected elements if selectors provided
    selected = {}
    if selectors:
        for sel, name in selectors.items():
            els = soup.select(sel)
            selected[name] = [e.get_text(strip=True) for e in els[:20]]

    # Count words
    word_count = len(text.split())

    return {
        "url": url,
        "status": r.status_code,
        "title": title,
        "meta_description": meta_desc,
        "text": text[:5000],  # First 5000 chars
        "word_count": word_count,
        "links_found": len(links),
        "links": links[:50],
        "selected": selected,
        "fetched_at": datetime.now().isoformat(),
    }


async def scrape_dynamic(url, timeout=30):
    """
    Scrape a JavaScript-heavy page with Playwright.
    Handles SPAs, infinite scroll, login walls.
    """
    if not HAS_PLAYWRIGHT:
        return {"url": url, "error": "Playwright not available"}

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle", timeout=timeout * 1000)
            # Wait extra for JS to settle
            await page.wait_for_timeout(2000)
            content = await page.content()
            await browser.close()

        soup = BeautifulSoup(content, "html.parser")
        text = re.sub(r"<script.*?</script>", "", content, flags=re.DOTALL)
        text = re.sub(r"<style.*?</style>", "", text, flags=re.DOTALL)
        text = BeautifulSoup(text, "html.parser").get_text(separator="\n", strip=True)
        text = re.sub(r"\n{3,}", "\n\n", text)

        return {
            "url": url,
            "title": soup.title.string.strip() if soup.title else "",
            "text": text[:5000],
            "dynamic": True,
        }
    except Exception as e:
        return {"url": url, "error": str(e)}


def scrape_with_fallback(url, selectors=None):
    """Try static first, fall back to dynamic if needed."""
    result = scrape_static(url, selectors)
    if "error" in result:
        if HAS_PLAYWRIGHT:
            import asyncio
            return asyncio.run(scrape_dynamic(url))
    return result


def extract_structured(soup, schema_type=None):
    """Extract structured data: articles, products, reviews, etc."""
    items = []

    if schema_type in (None, "article"):
        for art in soup.find_all("article"):
            title = art.find(["h1", "h2", "h3"])
            body = art.get_text("\n", strip=True)
            items.append({"type": "article", "title": title.text if title else "", "body": body[:500]})

    if schema_type in (None, "product"):
        for prod in soup.find_all("div", class_=re.compile(r"product|item|card", re.I)):
            title = prod.find(["h2", "h3", "span"])
            price = prod.find(attrs={"itemprop": "price"}) or prod.find(class_=re.compile(r"price"))
            items.append({
                "type": "product",
                "title": title.text if title else "",
                "price": price.text if price else "",
            })

    return items[:20]


def main():
    parser = argparse.ArgumentParser(description="Scrape websites with BeautifulSoup")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--select", action="append", help="CSS selector to extract (format: selector:name)")
    parser.add_argument("--dynamic", action="store_true", help="Use Playwright for JS sites")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--text-only", action="store_true", help="Output text only")
    parser.add_argument("--links", action="store_true", help="Output links only")
    args = parser.parse_args()

    selectors = {}
    if args.select:
        for s in args.select:
            if ":" in s:
                sel, name = s.split(":", 1)
                selectors[sel] = name

    if args.dynamic and HAS_PLAYWRIGHT:
        import asyncio
        result = asyncio.run(scrape_dynamic(args.url))
    else:
        result = scrape_with_fallback(args.url, selectors)

    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    if args.text_only:
        print(result.get("text", ""))
    elif args.links:
        for link in result.get("links", []):
            print(f"{link['text'][:50]:<50} {link['url']}")
    elif args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"URL: {result['url']}")
        print(f"Title: {result['title']}")
        print(f"Words: {result['word_count']}")
        print(f"Links: {result['links_found']}")
        print(f"\n--- Text Preview ---")
        print(result.get("text", "")[:1000])


if __name__ == "__main__":
    main()
