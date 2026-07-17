# Brave Search Fallback via curl + Python

When `web_search` (Tavily), `web_extract`, `x_search`, Exa MCP, DuckDuckGo, and Playwright browser are all unavailable or blocked, Brave Search HTML via `curl` + Python parsing is a reliable zero-key fallback.

## Proven pattern (2026-07-12, Hermes aarch64 PRoot)

All tools failed:
- `web_search` / `web_extract` → `TAVILY_API_KEY not set`
- `x_search` → XAI credits exhausted
- Exa MCP → not configured
- DuckDuckGo → CAPTCHA bot-detection
- Playwright → browser not installed
- Google → blocked/empty

Brave Search was the only path that returned real results.

## The pattern

```python
import urllib.request, re, urllib.parse

def brave_search(query: str, max_snippets: int = 10) -> list[dict]:
    """Search Brave and return {title, snippet} dicts. No API key needed."""
    qe = urllib.parse.quote(query)
    req = urllib.request.Request(
        f'https://search.brave.com/search?q={qe}&source=web',
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Accept': 'text/html'
        }
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        body = r.read().decode('utf-8', errors='replace')
    
    results = []
    # Extract title + snippet pairs
    snippets = re.findall(
        r'<div[^>]*class="[^"]*snippet[^"]*"[^>]*>(.*?)</div>',
        body, re.DOTALL
    )
    for s in snippets[:max_snippets]:
        text = re.sub(r'<[^>]+>', '', s).strip()
        text = re.sub(r'&amp;', '&', text)
        text = re.sub(r'&#x27;', "'", text)
        text = re.sub(r'&quot;', '"', text)
        if len(text) > 50:
            results.append({'snippet': text[:400]})
    return results
```

## Key observations

- Brave does not block curl when a standard User-Agent is set.
- Results are returned as HTML (not JSON) — parse with regex.
- The `class="snippet"` divs carry the richest content.
- Title extraction is fragile (varies with Brave's markup); snippets are the reliable payload.
- Searches can be chained: run 3–5 queries in sequence to triangulate a topic.
- Always `timeout=15` per request to avoid hanging.

## When to use vs other tools

| Tool | When available | Fallback when not |
|---|---|---|
| `web_search` (Tavily) | First choice | Skip |
| `web_extract` (Tavily) | For known URLs | Skip |
| `x_search` | X/Twitter topics | Skip |
| Exa MCP | Free AI search | Skip |
| DuckDuckGo curl | Good fallback | Often CAPTCHA-blocked |
| **Brave curl** | **Reliable fallback** | **Use this** |
| Google curl | Last resort | Often blocked/empty |

## Pitfalls

- Brave may eventually CAPTCHA or rate-limit, but at ~10 req/min it has been reliable.
- Do not use this for authenticated or paywalled content.
- Snippet text is truncated — use it to identify which URLs to fetch next, not as final source.
- The page HTML structure can change; if snippets stop matching, inspect with `print(body[:2000])` and adapt the regex.
