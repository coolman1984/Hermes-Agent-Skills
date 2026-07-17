---
title: "Karpathy LLM Wiki"
type: source
tags: [karpathy, llm-wiki, knowledge-base]
date: 2026-04-02
source_file: raw/karpathy-llm-wiki.md
last_updated: 2026-04-17
---

# Karpathy LLM Wiki

## Summary

Andrej Karpathy's idea file describes a persistent wiki that is compiled from raw source documents and maintained by an LLM over time. Instead of using the model only for one-shot retrieval, the wiki keeps accumulating summaries, backlinks, concept pages, entity pages, and a living synthesis.

## Key Claims

- Raw sources should be immutable and separate from the wiki.
- The LLM should maintain the wiki, not just answer queries from it.
- Knowledge should be compiled once and kept current.
- Query outputs can be filed back into the wiki so they compound.
- Linting and graphing are part of the workflow, not optional extras.

## Key Quotes

> "the wiki is a persistent, compounding artifact"

> "the LLM does all the grunt work"

## Connections

- [[AndrejKarpathy]] — originator of the pattern
- [[LLMWikiPattern]] — the concept described by the source
- [[llm-wiki-agent]] — practical implementation inspired by the idea

## Contradictions

- None found in the current seed set.