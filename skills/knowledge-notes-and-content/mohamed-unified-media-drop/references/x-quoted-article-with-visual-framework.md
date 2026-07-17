# X quoted article with visual framework pattern

Use when Mohamed sends an X status where the root tweet is short but quotes another X article, and the media image contains a framework/diagram that carries part of the argument.

## Durable lesson

For X posts, the root tweet is often not the whole source. A quoted tweet may contain an internal X article with structured blocks, and the root image may contain a summary framework. Treat tweet text, quoted article blocks, and image text as one source package before writing the Arabic note.

## Extraction sequence

1. Parse the tweet id from the URL.
2. Fetch the mirror JSON:

```text
https://api.fxtwitter.com/i/status/<tweet_id>
```

3. Save the full JSON to a temporary file before parsing. Do not rely on truncated terminal output.
4. Check these locations in order:
   - `tweet.article.content.blocks[]`
   - `tweet.quote.article.content.blocks[]`
   - `tweet.quoted_tweet.article.content.blocks[]`
5. If article blocks exist, normalize them into a temporary Markdown source while preserving order:
   - `header-one` → `## heading`
   - `header-two` → `### heading`
   - `unordered-list-item` → bullet
   - `ordered-list-item` → numbered item
   - `blockquote` → quote
   - otherwise paragraph
6. If the tweet or quoted tweet includes images, run vision on the original media URL and extract the visible text/structure. Include the image as source material when it adds concepts, diagrams, or labels that are not in the article text.
7. Use mirrors and vision as provenance in section 1. Do not imply direct live X access when the source came through mirrors.

## Writing pattern

For Mohamed's default source-only mode:

- Use the tweet text as the social framing.
- Use the quoted article blocks as the long-form source body.
- Use the image as conceptual support when it contains a framework.
- Label unverified product/pricing/performance claims clearly rather than researching them automatically.
- Convert the combined source into the normal 14-section Arabic note.

## Vault bridge pattern

If the X source teaches an agent, memory, workflow, business, or decision lens:

1. Create the Downloads media note.
2. Create or update one idea-vault note.
3. Register both paths in `06 - Media Source Map.md`.
4. Update `00 - Index.md`, `02 - Categories.md`, `03 - Connections.md`, and `05 - Review Queue.md` only when the connection is real and useful.
5. Verify the media note with the verifier script using the idea note and source map as optional arguments.

## Failure discipline

If the mirror exposes only a preview and the article blocks are absent, say the source is partial and do not fabricate the article. Try the existing r.jina and Camoufox fallbacks before giving up.
