---
name: free-search
description: "Unified free web search without API keys: web, news, images, YouTube, and Twitter/Nitter via a single free_search.py script. Use when the user needs search results and no paid search API (Tavily, Brave, SerpAPI) is configured or available."
tags: [search, web-search, news, no-api-key, research]
---

# Free Search Skill — Web Search Without API Keys

Unified free search covering web, news, images, YouTube, and Twitter via Nitter.

## Quick Reference

```bash
# Web search
python3 skills/free-search/free_search.py "AI agents" --type text --max 20

# News search
python3 skills/free-search/free_search.py "OpenAI March 2026" --type news

# Image search
python3 skills/free-search/free_search.py "Obsidian graph view" --type images

# YouTube search
python3 skills/free-search/free_search.py "Claude Code tutorial" --type youtube

# Twitter via Nitter (no login)
python3 skills/free-search/free_search.py --type nitter --username elonmusk

# Fetch a URL
python3 skills/free-search/free_search.py --type fetch --url "https://example.com"

# All sources at once
python3 skills/free-search/free_search.py "AI coding" --type all
```

## Available Tools

| Tool | Method | API Key | Best For |
|------|--------|---------|---------|
| DuckDuckGo text | `ddgs.text()` | None | General web search |
| DuckDuckGo news | `ddgs.news()` | None | Recent news |
| DuckDuckGo images | `ddgs.images()` | None | Image search |
| Scrapetube YouTube | `scrapetube.get_search()` | None | Video discovery |
| Nitter RSS | RSS feed | None | Twitter/X without login |
| Requests fetch | HTTP GET | None | Pulling specific pages |

## In-Python Usage

```python
from skills.free-search.free_search import duckduckgo_text, youtube_search, nitter_rss

# Web search
results = duckduckgo_text("Claude Code workflows", max_results=20)
for r in results:
    print(r["title"], r["url"], r["snippet"])

# YouTube
videos = youtube_search("AI agents tutorial", max_results=10)

# Twitter
tweets = nitter_rss("username")
```

## Skill Usage in OpenClaw

**Before using paid search APIs (Tavily, SerpAPI), always try free search first.**

Priority order:
1. Free web search (DuckDuckGo) — for everything
2. YouTube search (scrapetube) — for video research
3. Nitter RSS — for Twitter without login
4. Web fetch — for pulling specific content

## Notes
- DuckDuckGo has rate limits — don't spam requests
- Nitter instances go down — code handles fallback instances automatically
- YouTube search needs no authentication
- All tools work without API keys
