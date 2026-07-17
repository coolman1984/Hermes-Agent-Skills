# Web Article Extraction Notes

Use this for official web articles, engineering blogs, product posts, research announcements, and other non-video/non-social source links Mohamed drops for durable analysis.

## Trigger

- Bare URL from an official site or blog.
- Source has reusable value for Mohamed's systems: agents, workflows, business, market, automation, investing, content, writing, or strategy.
- Mohamed did not ask for a quick chat-only summary.

## Extraction Pattern

1. Try `web_extract(<url>)` first.
2. Check whether the returned content is complete enough:
   - contains the main title;
   - includes all section headings or a coherent article body;
   - is not visibly truncated before the conclusion;
   - includes enough metadata or page context to cite the source honestly.
3. If content is truncated, incomplete, or blocked, fetch a readable markdown fallback with `r.jina.ai` and save it to a temporary file before synthesis. Example pattern:

```bash
mkdir -p /tmp/source_slug
curl -L --max-time 90 'https://r.jina.ai/http://r.jina.ai/http://https://example.com/path/' -o /tmp/source_slug/article.md
wc -c /tmp/source_slug/article.md
```

4. Read the saved markdown in pages if needed, then synthesize from the full saved source rather than from a truncated tool result.
5. If direct terminal fetch returns an access error but the readable fallback works, describe the extraction method neutrally in the source metadata. Do not claim direct live-site extraction.

## Output Path

Use:

`/storage/emulated/0/Download/media-notes/web/<site-or-publisher>/<safe-title> - <YYYY-MM-DD>.md`

Examples:

`/storage/emulated/0/Download/media-notes/web/openai/harness-engineering-agent-first-world-2026-06-13.md`

## Report Requirements

Use the normal 14-section unified media note format:

1. Source metadata
2. Long Arabic summary
3. Professional opinion on practical value
4. Full Arabic presentation in source order
5. 10 practical use cases
6. Main idea
7. Point-by-point argument breakdown
8. Practical concept explanations
9. Link-by-link explanation
10. Strengths
11. Weaknesses / reservations
12. How Mohamed can apply it
13. Business intelligence extraction
14. Executive conclusion

## Intelligence Vault Bridge

Create/update an intelligence-vault note when the article contains business, product, workflow, automation, agent, investing, strategy, or market signals. Update the mandatory source map with:

- source URL;
- Downloads media note path;
- idea-vault note path;
- reason for the link.

Update index/category/connection/review files only when the connection is real and useful.

## Verification Pitfalls

- The verifier rejects Arabic lines with embedded Latin tokens. Translate stray technical words where possible, or put unavoidable English terms on standalone lines.
- Do not put absolute Obsidian paths inside Arabic report prose; record paths in the source map and final chat response.
- Run `verify_media_note.py <media-note> [idea-note] [source-map]` and patch exact failing lines before delivery.
- Do not run blind global replacements; they can corrupt names, links, and source titles.
