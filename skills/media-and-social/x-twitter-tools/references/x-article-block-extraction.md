# X Article Structured Block Extraction

Session-tested pattern for X status links that wrap an internal X article.

## When to use

Use this when the input is a single `x.com/i/status/<tweet_id>` or `x.com/<user>/status/<tweet_id>` and the tweet text is empty, a `t.co` link, or an `x.com/i/article/<article_id>` link.

## Fast extraction path

1. Fetch:
   `https://api.fxtwitter.com/i/status/<tweet_id>`
2. Inspect:
   `tweet.article`
3. If present, persist the raw JSON for audit/debug before transforming.
4. Parse:
   `tweet.article.content.blocks[]`
5. Convert blocks in order:
   - `header-one` → `# <text>`
   - `header-two` → `## <text>`
   - `unordered-list-item` → `- <text>`
   - `ordered-list-item` → `1. <text>`
   - `blockquote` → `> <text>`
   - any other non-empty `text` → paragraph
6. Keep metadata from `tweet.article.title`, `preview_text`, `created_at`, author fields, counts, and `tweet.url`.

## Cross-check path

Fetch:
`https://r.jina.ai/http://x.com/i/status/<tweet_id>`

Use it to cross-check article order, media captions, and readable rendering. Do not rely on it alone if the structured mirror contains fuller article blocks.

## Pitfalls

- `api.vxtwitter.com` may expose article metadata and preview but not the full article body.
- Direct live X article URLs often login-wall.
- The tweet text may be just a short URL while the full article lives under `tweet.article.content.blocks`.
- Always label mirror extraction clearly in the final source metadata; do not imply direct authenticated access.
