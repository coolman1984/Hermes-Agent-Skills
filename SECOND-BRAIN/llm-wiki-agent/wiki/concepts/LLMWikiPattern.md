---
title: "LLM Wiki Pattern"
type: concept
tags: [knowledge-base, markdown, workflow]
sources: [karpathy-llm-wiki, llm-wiki-agent]
last_updated: "2026-04-17"
---

# LLM Wiki Pattern

The LLM Wiki Pattern is a persistent, compounding knowledge base built from markdown files. Raw sources are read once, compiled into a structured wiki, and then maintained over time rather than re-derived on every question.

## Core layers

- Raw sources: immutable capture of articles, papers, notes, and transcripts.
- Wiki: agent-maintained markdown pages for sources, entities, concepts, and syntheses.
- Schema: instructions and conventions that keep the wiki coherent.

## Core behaviors

- Ingest new sources into the wiki.
- Update the overview and index as knowledge grows.
- Create or update entity and concept pages when they become important.
- Flag contradictions instead of silently overwriting them.
- File valuable answers back into the wiki so they compound.
- Run linting and graph generation to keep the structure healthy.

## Why it works

The tedious part of knowledge management is bookkeeping, not thinking. The pattern delegates the bookkeeping to the LLM so the human can focus on choosing sources, asking better questions, and deciding what matters.

## Related pages

- [[AndrejKarpathy]]
- [[SamurAIGPT]]
- [[llm-wiki-agent]]