# X internal article extraction note

Use this when Mohamed sends an `x.com/i/status/<id>` link whose useful content is an internal long-form X article attached to the same status.

## Pattern observed

The root tweet can have an empty or nearly empty visible text field while the full article lives directly under:

- `tweet.article.title`
- `tweet.article.preview_text`
- `tweet.article.content.blocks[]`
- `tweet.article.content.entityMap[]`

This is different from the quoted-article pattern where the long-form article lives under `tweet.quote.article` or `tweet.quoted_tweet.article`.

## Recommended extraction sequence

1. Fetch structured mirror JSON:
   - `https://api.fxtwitter.com/i/status/<tweet_id>`
2. Parse root tweet metadata:
   - canonical URL
   - author handle and display name
   - created date
   - views and engagement when useful
3. Check article locations in the standard order:
   - `tweet.article.content.blocks[]`
   - `tweet.quote.article.content.blocks[]`
   - `tweet.quoted_tweet.article.content.blocks[]`
4. For root article blocks, preserve original order and map common block types:
   - `header-two` and similar header blocks become Markdown headings.
   - `unordered-list-item` becomes bullet points.
   - `unstyled` becomes paragraphs.
   - empty `atomic` spacer blocks can be skipped.
5. Save the extracted normalized article to `/tmp` when it is long, then read it back in chunks before writing Mohamed's Arabic note.
6. Cross-check readable rendering with:
   - `https://r.jina.ai/http://x.com/i/status/<tweet_id>`
7. If the readable cross-check fails but `api.fxtwitter.com` returns complete root `tweet.article.content.blocks[]`, it is acceptable to proceed from the structured mirror only. Preserve the original block order, label the readable cross-check failure in metadata/final notes, and do not imply direct live X access. Use Camoufox only when the structured mirror is incomplete, blocked, or the article body cannot be reconstructed from the JSON.
8. In the media note metadata, say clearly that extraction came from mirrors and readable cross-checks when available, not direct live X browsing.

## Writing guidance for Mohamed

- Do not translate the root article as numbered fragments.
- Present it as a coherent professional Arabic article in the original logical order.
- Explain tool names conceptually when they are not central.
- If the article is about workflows, agents, automation, market signals, products, or services, create an intelligence-vault bridge note and source-map entry.

## Verification targets

- Media note includes original URL, canonical URL when available, mirror source, and readable cross-check source.
- The article body in the note is coherent prose, not raw block dumps.
- Exactly ten use cases are present in the unified format.
- Source map includes both the Downloads media note path and the idea-vault note path when a bridge was created.
