# X Article Block Normalization Pattern

Use this when an `x.com/i/status/<id>` link resolves to a long-form X article via mirror JSON.

## Durable pattern

1. Fetch the mirror JSON to a temporary file, not just truncated stdout:
   - `https://api.fxtwitter.com/i/status/<tweet_id>`
2. Prefer article blocks in this order:
   - `tweet.article.content.blocks[]`
   - `tweet.quote.article.content.blocks[]`
   - `tweet.quoted_tweet.article.content.blocks[]`
3. Convert blocks into a clean intermediate Markdown file before synthesis:
   - `header-one`, `header-two`, and similar block types become Markdown headings.
   - `unordered-list-item` becomes a bullet or a prose list item.
   - `blockquote` remains quoted/marked as a highlighted source note.
   - empty `atomic` blocks are skipped unless media captions or meaningful metadata are attached.
4. Preserve the original logical order of blocks; do not reorder by perceived importance.
5. Use the normalized article text as the main source for the Arabic presentation section.
6. Keep the extraction source explicit in metadata: mirror JSON, canonical X status, and any readable rendering cross-check if used.

## Why this matters

Long-form X articles often have an empty root tweet text and all useful content inside `article.content.blocks`. A normalized intermediate file makes it easier to verify sequence, headings, and completeness before producing the unified Arabic note.

## Verification additions

Before final delivery, check:

- number of non-empty text blocks extracted
- article title and author from JSON
- output note includes all mandatory unified sections
- source-map entry contains both the Downloads media note path and the idea-vault note path when a bridge note is created
