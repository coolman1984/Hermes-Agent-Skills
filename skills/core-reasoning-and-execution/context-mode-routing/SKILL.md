---
name: context-mode-routing
description: Route large file reads, verbose command output, web fetches, logs, and
  browser snapshots through Context Mode sandbox tools to reduce context bloat. Use
  when outputs may exceed a few hundred tokens or when you need index/search/fetch-first
  behavior instead of raw dumps.
tags: [context-mode, sandbox, extraction, large-output, routing]
---

# Context Mode Routing

## Core rule
Prefer Context Mode sandbox tools over raw `read`, shell, or web fetch when the output is likely to be large or noisy.

## Use Context Mode for
- files larger than a quick skim
- logs, traces, and search-heavy text
- web pages that need extraction before analysis
- command output that may be verbose
- browser snapshots and other large structured dumps

## Tool selection
- `ctx_index` — ingest large text into searchable chunks
- `ctx_search` — ask targeted questions against indexed content
- `ctx_fetch_and_index` — fetch a page, convert it, and index it
- `ctx_execute` — run a command when the raw output should stay out of the model context
- `ctx_batch_execute` — run multiple sandboxed commands or searches together
- `ctx_execute_file` — process a file in the sandbox without dumping it raw

## Default workflow
1. Index first.
2. Search specifically.
3. Summarize only the relevant findings.

## Do not use Context Mode for
- short one-line commands
- tiny files that are faster to read directly
- interactive commands that need live streaming

## Prompting pattern
Ask for intent, not raw dumps:
- “Index this log, then search for error spikes.”
- “Fetch and index this page, then search for plan details.”
- “Run the command in Context Mode and return only the relevant result.”

## Verification
If the Context Mode tools are unavailable, fall back to normal tools and state the limitation briefly.

## Reference
Read `references/context-mode-routing.md` for the routing checklist and config notes.
