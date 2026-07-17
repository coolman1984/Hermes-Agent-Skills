# Source Capture: Karpathy LLM Wiki

Source URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Related tweet: https://x.com/i/status/2039805659525644595
Captured: 2026-04-17

## Capture Notes
- Karpathy describes LLM Wiki as a persistent, compounding markdown knowledge base.
- Raw sources stay immutable in `raw/`.
- The LLM compiles those sources into a structured wiki with summaries, backlinks, entity pages, concept pages, and an evolving overview.
- Queries can be filed back into the wiki as durable outputs, so explorations compound over time.
- Linting is part of the loop: contradiction detection, missing links, stale data, and data gaps.

## Core Shape
raw sources -> compiled wiki -> query -> file outputs back into wiki -> lint -> graph

## Why it matters
The point is not RAG alone. The point is a maintained knowledge artifact that keeps getting richer instead of being rediscovered from scratch every time.