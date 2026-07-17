# Source Capture: llm-wiki-agent README

Source URL: https://github.com/SamurAIGPT/llm-wiki-agent
Captured: 2026-04-17

## Capture Notes
- Practical GitHub implementation of the Karpathy pattern.
- Repository layout: `raw/`, `wiki/`, `graph/`, `tools/`.
- Main workflows: ingest, query, lint, build graph.
- Ingest writes source pages, updates `index.md`, `overview.md`, entity pages, concept pages, and `log.md`.
- Query selects relevant pages from the index, synthesizes an answer, and can save it as a synthesis page.
- Lint checks for orphan pages, broken links, missing entity pages, contradictions, and data gaps.
- Graph build turns wikilinks into explicit edges and can infer relationships for visualization.

## Why this matters
This is the closest working implementation I found. It turns the idea into an operational wiki engine rather than a concept note.