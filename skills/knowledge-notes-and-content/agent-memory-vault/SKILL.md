---
name: agent-memory-vault
description: Design and implement a local-first, typed Obsidian-style memory vault
  for Hermes/OpenClaw agents with provenance, confidence, expiry, conflict tracking,
  and compaction snapshots.
tags: [memory, vault, obsidian, second-brain, continuity, local-first]
---

# Agent Memory Vault

Use this skill when the user wants a better agent memory system than a flat note dump: a local-first vault, structured memory, durable continuity, and a workflow that avoids stale facts, duplicates, and context bloat.

## When to use
- User asks to improve Hermes/OpenClaw memory or “second brain” behavior
- User wants an Obsidian-based memory system for agents
- User wants a Google Drive, Docs, or external cloud second brain connected to agent workflows
- User wants a shared workspace for multiple agents with durable notes
- User wants a better design than simple daily logs or a single archive folder

## Core approach
Do not treat the vault as a pile of notes.
Treat it as a typed memory system with these layers:

1. Raw inbox
2. Daily episodic logs
3. Stable facts
4. Decisions
5. Procedures
6. Errors and lessons
7. Conflicts / contradictions
8. Shared workspace
9. Archived cold storage

## Agentic adoption order
When improving an agent system around memory, do not jump straight to autonomy.
Use this order instead:

1. Context
2. Rules
3. Memory
4. Verification
5. Automation
6. Independence

This matters because a strong agent on top of weak context or weak memory only creates fast confusion.

The key rule: raw input is not durable memory until it is sorted, verified, and promoted.

## Recommended workflow

### 1) Research first
Before changing the system, inspect the current vault, config, and related files.
Look for:
- existing vault path
- current daily log
- active project notes
- current snapshot / continuity file
- any existing rules or templates

### 2) Design the memory flow
Use a strict lifecycle:

Raw -> Sort -> Verify -> Store -> Consolidate -> Invalidate or Promote

### 3) Use typed memory records
Every durable record should include:
- title
- type
- source
- timestamp
- confidence
- validity / expiry
- status
- links to related records
- brief summary

### 4) Separate memory by purpose
Avoid mixing these in one place:
- temporary working context
- stable truth
- decisions
- procedures
- mistakes
- contradictions
- shared cross-agent notes

### 5) Add conflict tracking
Never silently overwrite contradictory facts.
Record both sides, confidence, source, and current preference.

### 6) Add compaction survival
Maintain a short continuity snapshot with:
- current goal
- what changed
- open hypotheses
- irreversible decisions
- what must not be lost

### 7) Consolidate regularly
Use periodic review to:
- merge duplicates
- promote repeated facts into stable facts
- demote stale notes
- archive dead content
- refresh confidence and expiry

## Suggested vault structure

```text
VAULT/
├── VAULT-INDEX.md
├── START-HERE.md
├── CURRENT-SNAPSHOT.md
├── INBOX/
├── DAILY/
├── FACTS/
├── DECISIONS/
├── PROCEDURES/
├── PROJECTS/
├── ERRORS/
├── CONFLICTS/
├── SHARED/
├── ARCHIVE/
└── TEMPLATES/
```

## Important design rules
- Do not promote text to durable memory without a source
- Do not keep the same fact duplicated as separate canonical truth
- Do not let old facts live forever without expiry or review
- Do not let shared memory become an ungoverned dump
- Prefer human-readable files over black-box storage
- Prefer retrieval by type and intent, not only similarity search
- If the user's second brain is on Google Drive or another external store, treat it as a separate canonical knowledge base: start read-only, preserve file links/IDs/provenance, and only mirror/cache locally unless the user explicitly asks to migrate or write back.

## Practical implementation steps

### A. Create the vault
If no vault exists, create a local vault folder and seed it with:
- index file
- start-here file
- current snapshot file
- daily template
- fact template
- decision template
- procedure template
- error template
- conflict template
- shared template
- project template

### B. Seed the first live files
Create at least:
- today’s daily note
- core facts note
- core decisions note
- core errors note
- open conflicts note
- active projects note

### C. Verify the structure
Check that:
- the folders exist
- the templates exist
- the index points to the right places
- the current snapshot exists
- the daily note for today exists

### D. Only then integrate with the agent
Update the agent’s startup behavior or documentation so it reads:
- index
- current snapshot
- today’s daily note
- active project note
- conflict log if needed

## Pitfalls discovered
- Do not auto-edit protected config files if the environment blocks them; document the manual step instead and continue with the vault build
- Do not store everything in the daily log and call it memory
- Do not rely on search alone; you need typed sections and canonical records
- Do not make shared memory unrestricted
- Do not treat archived content as deleted truth
- If the user corrects ownership of a routine or workflow, revert any vault changes that exposed it, keep assistant-internal habits out of the user vault unless explicitly requested, and record the lesson separately

## Verification checklist
Before finishing, confirm:
- vault path is known
- folder structure exists
- templates exist
- live starter files exist
- snapshot exists
- structure is readable and browsable
- no critical config write was silently skipped

## Output style for this skill
When using this skill, deliver:
- a short diagnosis of the current state
- a smarter design than the initial one
- the exact folder/file structure
- the implementation steps
- the verification result

## Notes
If the user wants continuous improvement, keep revisiting the memory design and prefer the smallest system that preserves provenance, confidence, and recoverability.
