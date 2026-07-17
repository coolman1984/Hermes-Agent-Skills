# Context Mode Routing Checklist

## Routing checklist
- Is the output likely to be large?
- Is the text noisy or search-heavy?
- Would indexing and search be better than raw reading?
- Would a sandboxed command keep the model context smaller?
- Would a web fetch need conversion before analysis?

## Preferred patterns
- large file -> index, then search
- log analysis -> index, then targeted searches
- web page -> fetch and index, then search
- verbose command -> execute in sandbox and summarize
- browser snapshot -> route through sandbox execution

## Fallback rule
If Context Mode is unavailable, use the smallest reliable non-sandbox tool and avoid dumping raw output unless necessary.

## Config note
If you register a Context Mode MCP server, restart the OpenClaw gateway so the tools appear in the next session.
