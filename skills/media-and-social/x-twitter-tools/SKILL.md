---
name: x-twitter-tools
description: Free X/Twitter retrieval methods, including no-login mirror APIs for
  tweet inspection when direct extraction fails.
version: 1.1.0
author: Hermes Agent
license: MIT
tags: [twitter, x, free, fxtwitter, scraping, no-api-key]
metadata:
  tags:
  - x
  - twitter
  - scraping
  - fxtwitter
  - vxtwitter
  - nitter
---

# X/Twitter Tools Skill — Free Methods Only

No paid API needed. Use these in order from fastest to most robust.

## Available Methods

### 0. FX/VX Twitter API mirrors (fastest for single tweet links)
No login, no cookies. Best when `web_extract` fails on `x.com/.../status/...`.

Endpoints:
- `https://api.fxtwitter.com/{username}/status/{tweet_id}`
- `https://api.vxtwitter.com/Twitter/status/{tweet_id}`

Returns typically include:
- tweet text
- author name/handle
- counts (likes/replies/retweets/views)
- media URLs (video/photo) + metadata

Fallback flow:
1. Parse tweet ID (and username if present) from URL.
2. Try `api.fxtwitter.com` first.
3. If failed/empty, try `api.vxtwitter.com`.
4. Return concise summary and clearly note mirror source.

Caveats:
- Mirror APIs can rate-limit or become unavailable.
- Good for read-only inspection, not compliance-critical evidence.

### 1. Browser cookies + requests (best authenticated free method)
Requires your X.com session cookies from a browser.

How to get cookies:
1. Open X.com in Chrome/Edge.
2. Press F12 → Application → Cookies → x.com.
3. Copy `auth_token`.

What it can do:
- search tweets
- get profiles
- get tweet details
- get bookmarks
- get trending topics

### 2. Nitter (free, no login)
RSS-style frontend.

Endpoints:
- `https://nitter.net/{username}`
- `https://nitter.net/{username}/rss`
- `https://nitter.net/i/search?q={query}`

### 4. Discovery/search fallback via DuckDuckGo HTML
When direct X search or generic web search is blocked, use DuckDuckGo's HTML endpoint to discover recent X URLs and related posts.

Recommended flow:
1. Query `https://html.duckduckgo.com/html/?q=<query>` with a normal browser-like User-Agent.
2. Parse result links and extract the real URL from `uddg=` redirect params.
3. Prefer `x.com/.../status/...` results for direct inspection with FX/VX mirrors.
4. If the query is about a topic rather than a single tweet, use this method to find candidate posts, then inspect the best hits with mirror APIs.

Practical note from field use:
- `web_search` / `web_extract` can return 432 errors on X-heavy queries in this environment.
- DuckDuckGo HTML was more reliable for discovery, especially for recent model-release chatter and trending posts.

### 5. Public page HTML scrape (last resort)
Use normal requests + HTML parsing on public pages.

### 6. X article / tweet-with-article fallback via mirror article blocks and r.jina.ai
Some X links point to `x.com/i/article/...` or a tweet that only contains a short URL to an X article. In these cases:
1. Try the normal X URL if needed, but expect login-wall / unsupported-page behavior.
2. For a tweet/status URL, fetch `https://api.fxtwitter.com/i/status/<tweet_id>` and inspect `tweet.article`. When present, `tweet.article.content.blocks[]` can contain the full structured article body, not just the preview. Parse block `type` values into Markdown (`header-one`, `header-two`, `unordered-list-item`, `ordered-list-item`, `blockquote`, otherwise paragraph) and preserve the original logical order.
3. Also try `https://api.vxtwitter.com/Twitter/status/<tweet_id>` for article metadata and preview if fxtwitter is empty or incomplete.
4. Fetch `https://r.jina.ai/http://x.com/i/status/<tweet_id>` for a readable Markdown rendition and media captions when available. Use it as a cross-check or fallback; it can expose more readable image/card context but may omit or truncate some details.
5. If the tweet only contains a `t.co` link to an X article, expand the short link and then fetch `https://r.jina.ai/http://x.com/i/article/<article_id>`.
6. If r.jina.ai returns "This page is not supported", pivot to the author's profile and inspect the latest X page or article preview text from mirrors.
7. Prefer structured mirror article blocks plus tweet metadata when available rather than pretending the live X article was directly accessible.

Observed pitfall from practice:
- `api.fxtwitter.com` may return a tweet whose text is just a bare article URL, not the article content itself.
- Direct `x.com/i/article/...` browsing often login-walls or shows a generic X splash page in headless mode.
- `r.jina.ai` can still expose the article text for `x.com/i/status/...` even when the live X page is inaccessible.
- `r.jina.ai/http://x.com/i/article/<article_id>` can also fail with empty content even when mirrors expose the article title/preview. In that case, do not stop: use exact-title and author web searches to discover mirrored posts, LinkedIn/Pulse reposts, indexed summaries, and adjacent part IDs, then inspect each discovered X status with FX/VX mirrors.
- If a tweet includes media cards/photos that summarize the content, run `vision_analyze` on the `media.photos[].url` / `mediaURLs[]` image URL to extract the text and structure. This is often the most complete accessible version of X “framework” posts.

- `references/x-article-block-extraction.md`: session-tested recipe for extracting full internal X articles from `api.fxtwitter.com/i/status/<tweet_id>` structured `tweet.article.content.blocks[]`, with r.jina cross-checks.

## Recommended decision flow
1. If any direct X page, X article, or extractor path is blocked/login-walled, run Camoufox immediately and verify the rendered page body before deciding it failed. For Mohamed, this is the first fallback on blocked content.
2. If Camoufox lands on `x.com/i/flow/login` or only shows signup/login chrome, treat that as confirmed login-wall, not as article content.
3. If the user sends a single tweet URL and Camoufox is blocked or unnecessary after verification: use method 0 mirrors (`fxtwitter`, then `vxtwitter`) for tweet text/media/metadata.
4. If the tweet links to an X article, try `r.jina.ai/http://x.com/i/status/<tweet_id>` and/or `r.jina.ai/http://x.com/i/article/<article_id>` after Camoufox confirms the direct article is blocked.
5. If mirrors and r.jina are incomplete: try Nitter, indexed web search, DuckDuckGo HTML discovery, media OCR/vision, and adjacent status IDs.
6. If still blocked and user needs deeper data: use cookie-auth method if available.
7. Always mention uncertainty/source when using mirrors or partial article previews.

## Notes
- Cookies expire; refresh periodically.
- X blocks scraping aggressively; keep multiple fallbacks.
- Fresh automated/remote-browser logins can trigger X’s “Suspicious login prevented” screen. If seen, stop retrying and switch to a trusted existing session path.
- If the user says their X login is in an Android browser such as Comet, do not hunt for saved passwords. Use ADB visual control to operate the trusted browser session, or ask the user to explicitly export only the needed X session cookie if they accept that risk.
- Nitter instances may be down intermittently.
- For discovery/search around X when direct search is blocked, use a warmed `requests.Session()` against DuckDuckGo HTML (`https://html.duckduckgo.com/html/`) and parse result redirects to real `x.com` URLs. In this environment, single-shot `web_search` / `web_extract` often hit 432 errors, while the warmed-session terminal fallback worked.
- Direct `x.com/search` commonly returns sign-in walls, and `r.jina.ai` on search pages is usually just the login page, so prefer indexed discovery via search engines first.