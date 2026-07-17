#!/usr/bin/env python3
"""
free_search.py — Unified free web search for OpenClaw
Supports: DuckDuckGo text, news, images + web fetching + YouTube + Nitter RSS
"""
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

try:
    from duckduckgo_search import DDCGS as DDGS
    HAS_DDGS = True
except ImportError:
    HAS_DDGS = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    import feedparser
    HAS_FEEDPARSER = True
except ImportError:
    HAS_FEEDPARSER = False

try:
    import scrapetube
    HAS_SCRAPETUBE = True
except ImportError:
    HAS_SCRAPETUBE = False

NITTER_INSTANCES = [
    "nitter.net",
    "nitter.privacydev.net",
    "xcancel.com",
]

def duckduckgo_text(query, max_results=20):
    """Web search — returns title, href, body."""
    if not HAS_DDGS:
        return [{"error": "duckduckgo_search not installed"}]
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("href", ""),
                "snippet": r.get("body", ""),
                "source": "duckduckgo"
            })
    return results

def duckduckgo_news(query, max_results=10):
    """News search."""
    if not HAS_DDGS:
        return [{"error": "duckduckgo_search not installed"}]
    results = []
    with DDGS() as ddgs:
        for r in ddgs.news(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "date": r.get("date", ""),
                "snippet": r.get("body", ""),
                "source": "duckduckgo-news"
            })
    return results

def duckduckgo_images(query, max_results=10):
    """Image search."""
    if not HAS_DDGS:
        return [{"error": "duckduckgo_search not installed"}]
    results = []
    with DDGS() as ddgs:
        for r in ddgs.images(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("image", ""),
                "thumbnail": r.get("thumbnail", ""),
                "source": "duckduckgo-images"
            })
    return results

def fetch_url(url, timeout=10):
    """Fetch a URL and return basic info."""
    if not HAS_REQUESTS:
        return {"error": "requests not installed"}
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
        return {
            "url": url,
            "status": r.status_code,
            "content_type": r.headers.get("content-type", ""),
            "length": len(r.text),
            "snippet": r.text[:500],
        }
    except Exception as e:
        return {"url": url, "error": str(e)}

def nitter_rss(username):
    """Get tweets from a Twitter user via Nitter RSS."""
    if not HAS_FEEDPARSER:
        return [{"error": "feedparser not installed"}]
    for inst in NITTER_INSTANCES:
        try:
            url = f"https://{inst}/{username}/rss"
            import requests as req
            r = req.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code != 200:
                continue
            feed = feedparser.parse(r.text)
            tweets = []
            for entry in feed.entries[:20]:
                tweets.append({
                    "title": entry.get("title", ""),
                    "link": entry.get("link", ""),
                    "published": entry.get("published", ""),
                    "source": f"nitter-{inst}"
                })
            return tweets
        except Exception:
            continue
    return [{"error": "All Nitter instances failed"}]

def youtube_search(query, max_results=10):
    """Search YouTube via scrapetube."""
    if not HAS_SCRAPETUBE:
        return [{"error": "scrapetube not installed"}]
    results = []
    for v in scrapetube.get_search(query, limit=max_results):
        try:
            title = (v.get("title", {}).get("runs", [{}])[0].get("text", "N/A")
            vid = v.get("videoId", "N/A")
            channel = (v.get("longBylineText", {}).get("runs", [{}])[0].get("text", "N/A")
            results.append({
                "title": title,
                "url": f"https://youtube.com/watch?v={vid}",
                "video_id": vid,
                "channel": channel,
                "source": "youtube"
            })
        except Exception:
            continue
    return results

def format_results(results, style="brief"):
    """Format search results for display."""
    if not results:
        return "No results found."
    if "error" in results[0]:
        return f"Error: {results[0]['error']}"

    lines = []
    for i, r in enumerate(results, 1):
        if style == "brief":
            lines.append(f"{i}. {r.get('title', 'N/A')[:70]}")
            lines.append(f"   {r.get('url', r.get('href', ''))[:80]}")
            if r.get("snippet"):
                lines.append(f"   {r.get('snippet', '')[:120]}")
        elif style == "news":
            lines.append(f"{i}. {r.get('title', '')[:70]}")
            lines.append(f"   {r.get('date', '')} | {r.get('url', '')}[:80]}")
        elif style == "compact":
            lines.append(f"{i}. {r.get('title', '')[:70]} — {r.get('url', '')}[:80]}")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Free unified search")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--type", default="text", choices=["text", "news", "images", "nitter", "youtube", "fetch", "all"])
    parser.add_argument("--max", type=int, default=10, help="Max results")
    parser.add_argument("--username", dest="username", help="Nitter username")
    parser.add_argument("--url", help="URL to fetch")
    parser.add_argument("--format", default="brief", choices=["brief", "news", "compact"])
    args = parser.parse_args()

    results = []

    if args.type == "text":
        results = duckduckgo_text(args.query, args.max)
    elif args.type == "news":
        results = duckduckgo_news(args.query, args.max)
    elif args.type == "images":
        results = duckduckgo_images(args.query, args.max)
    elif args.type == "nitter":
        if not args.username:
            print("Error: --username required for nitter search")
            sys.exit(1)
        results = nitter_rss(args.username)
    elif args.type == "youtube":
        results = youtube_search(args.query, args.max)
    elif args.type == "fetch":
        if not args.url:
            print("Error: --url required for fetch")
            sys.exit(1)
        results = [fetch_url(args.url)]
    elif args.type == "all":
        # Run all, return combined
        text_results = duckduckgo_text(args.query, min(5, args.max))
        yt_results = youtube_search(args.query, min(3, args.max))
        results = text_results + yt_results

    print(format_results(results, args.format))

    # Also print as JSON for OpenClaw parsing
    print(f"\n--- JSON ---")
    print(json.dumps(results[:5], indent=2))

if __name__ == "__main__":
    main()
