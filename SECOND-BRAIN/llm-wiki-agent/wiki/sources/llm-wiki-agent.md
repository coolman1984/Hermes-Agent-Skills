---
title: "LLM Wiki Agent"
type: source
tags: [github, implementation, workflow]
date: 2026-04-17
source_file: raw/llm-wiki-agent.md
last_updated: 2026-04-17
---

# LLM Wiki Agent

## Summary

`llm-wiki-agent` is the strongest working GitHub implementation found for the LLM Wiki pattern. It provides a clear repository layout, explicit workflows, and Python tools for ingesting sources, querying the wiki, linting for health issues, and building a graph visualization.

## Key Claims

- The repo is organized around `raw/`, `wiki/`, `graph/`, and `tools/`.
- Ingest creates source pages and updates index, overview, entities, concepts, and log entries.
- Query selects relevant pages from the index, synthesizes an answer, and can save it back as a synthesis page.
- Lint catches orphans, broken links, missing entities, contradictions, and data gaps.
- Graph generation turns wikilinks into explicit edges and can infer relationships for visualization.

## Key Quotes

> "Drop source documents into `raw/` and tell the agent to ingest them"

> "Every new source makes the wiki richer"

## Connections

- [[SamurAIGPT]] — maintainer of the repository
- [[LLMWikiPattern]] — the pattern implemented here
- [[AndrejKarpathy]] — inspiration for the repo

## Contradictions

- None found in the current seed set.