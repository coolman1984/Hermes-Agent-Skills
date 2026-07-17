# X quoted article extraction note

Use this when Mohamed sends an `x.com/i/status/<id>` link and the useful long-form content is not in the visible post text.

## Pattern observed

Some X posts are short repost/commentary posts that quote another X post containing an internal X article. In mirror JSON, the root tweet may have no `article` field, while the quoted tweet has:

- `tweet.quote.article.title`
- `tweet.quote.article.preview_text`
- `tweet.quote.article.content.blocks[]`
- `tweet.quote.article.content.entityMap[]`

The root post can still contain useful framing, media, author metrics, and canonical URL.

## Recommended extraction sequence

1. Fetch structured mirror JSON:
   - `https://api.fxtwitter.com/i/status/<tweet_id>`
2. Parse root tweet metadata:
   - root URL
   - author
   - date
   - visible text
   - media URLs when relevant
3. Check article locations in this order:
   - `tweet.article.content.blocks[]`
   - `tweet.quote.article.content.blocks[]`
   - `tweet.quoted_tweet.article.content.blocks[]`
4. Convert text blocks in original order.
5. Preserve meaningful markdown snippets from `entityMap` only conceptually unless the task explicitly needs templates/code.
6. Cross-check readable rendering with:
   - `https://r.jina.ai/http://x.com/i/status/<tweet_id>`
7. If `web_extract` truncates the mirror JSON, use a deterministic `curl` plus Python JSON parser through terminal, writing the response to `/tmp` before parsing.

## What to avoid

- Do not finalize from the visible post only when a quoted internal article exists.
- Do not imply direct live X access if the content came from mirrors.
- Do not dump raw code/template blocks into Mohamed's Arabic note unless they are the point of the source. Explain their operational meaning.
- Do not force the source into the book factory unless the reusable lesson is genuinely about writing, publishing, reader psychology, or author distribution.

## Verification targets

- Media note includes both original URL and extraction sources.
- If a vault bridge is created, the source map contains both the Downloads note path and the idea-vault note path.
- The final Arabic body should not mix English terms inside Arabic lines; URLs and standalone English titles are acceptable.
