---
name: codebase-memory-workflow
description: "Use when working on any codebase with 20+ files — index the repo first, query the graph before reading files randomly, then act on targeted context. Reduces token waste and missed relationships in coding agent tasks."
version: 1.0.0
author: Hermes Agent + Mohamed
license: MIT
metadata:
  hermes:
    tags: [codebase, memory, indexing, repo-graph, agent-context, tools]
    related_skills: [senior-software-engineer, mohamed-coding-team, hermes-agent]
---

# Codebase Memory Workflow

## Overview

Before any coding agent reads files one by one, it should index the repository into a queryable graph of functions, calls, imports, and dependencies. One indexing pass replaces dozens of random file reads. This skill defines the standard workflow for all Hermes profiles — default and worker — when touching any non-trivial codebase.

## When to Use

- **Any coding task on a repo with 20+ files** — index first, ask questions later.
- **Before assigning a coding agent (worker profile) to a task** — give it the graph, not the whole file tree.
- **Before refactoring, adding features, or debugging** — know the call paths and hotspots first.
- **When a new agent starts on an existing project** — the graph is its onboarding map.

**Don't use for:**
- Single-file fixes (just read the file).
- Repos under 5 files (overhead exceeds benefit).
- Read-only research that won't touch code (use regular search).

## The Workflow

### Step 0: Prerequisites

The indexing tool lives at:

```
/root/tools/codebase-memory-test/node_modules/.bin/codebase-memory-mcp
```

The local index builder script:

```
/root/.hermes/scripts/build_codebase_memory_index.py
```

The vault output folder:

```
/root/Documents/Obsidian Vault/Projects/Codebase Memory
```

### Step 1: Index the repository

Run the MCP indexer on the target repo:

```bash
cd /root/tools/codebase-memory-test && ./node_modules/.bin/codebase-memory-mcp cli index_repository '{"repo_path":"<REPO_PATH>","project_name":"<PROJECT_NAME>"}'
```

This produces a graph with:
- **Nodes:** Functions, Methods, Classes, Variables, Files, Modules, Routes, Folders, Packages
- **Edges:** CALLS, DEFINES, USAGE, WRITES, IMPORTS, TESTS, CONTAINS, DEPENDS_ON, SEMANTICALLY_RELATED, SIMILAR_TO, FILE_CHANGES_WITH, INHERITS, DECORATES
- **Metadata:** Entry points, hotspots (high fan-in), packages, languages, file tree

### Step 2: Build the local detailed index (for vault and agents)

```bash
python3 /root/.hermes/scripts/build_codebase_memory_index.py
```

This reads all repos under the roots list, extracts AST-level info per file (functions, classes, routes, tables, headings, imports), computes cross-file name mentions, and writes:

- `Codebase Memory — Detailed Index YYYY-MM-DD.md` — human-readable catalog
- `codebase-memory-index-YYYY-MM-DD.json` — full machine-readable data for agents

### Step 3: Query before you read

Instead of opening files randomly, query the graph:

```bash
# Get architecture overview
./node_modules/.bin/codebase-memory-mcp cli get_architecture '{"project":"<PROJECT_NAME>","aspects":["all"]}'

# Search for specific functions/symbols
./node_modules/.bin/codebase-memory-mcp cli search_graph '{"project":"<PROJECT_NAME>","query":"<SEARCH_TERMS>","limit":20}'

# Search code content
./node_modules/.bin/codebase-memory-mcp cli search_code '{"project":"<PROJECT_NAME>","query":"<PATTERN>","limit":20}'

# Trace a call path
./node_modules/.bin/codebase-memory-mcp cli trace_path '{"project":"<PROJECT_NAME>","source":"<fn_a>","target":"<fn_b>"}'

# Get a code snippet
./node_modules/.bin/codebase-memory-mcp cli get_code_snippet '{"project":"<PROJECT_NAME>","qualified_name":"<QUALIFIED_NAME>"}'

# Check if files changed since last index
./node_modules/.bin/codebase-memory-mcp cli detect_changes '{"project":"<PROJECT_NAME>"}'

# List all indexed projects
./node_modules/.bin/codebase-memory-mcp cli list_projects '{}'
```

### Step 4: Read only the files the graph points to

Based on the query results:
1. Read the entry-point files for the area you're touching
2. Read the hotspot files (high fan-in = many callers depend on them)
3. Read the test files for that area
4. Skip everything else unless the graph reveals a dependency you didn't expect

### Step 5: After significant changes, re-index

```bash
./node_modules/.bin/codebase-memory-mcp cli detect_changes '{"project":"<PROJECT_NAME>"}'
# If changes detected:
./node_modules/.bin/codebase-memory-mcp cli index_repository '{"repo_path":"<REPO_PATH>","project_name":"<PROJECT_NAME>"}'
```

## Current indexed repos (as of 2026-06-27)

| Project name | Repo path | Nodes | Edges |
|---|---|---:|---:|
| `root-Company-Dashboard` | `/root/Company-Dashboard` | 2716 | 9652 |
| `root-llm-wiki-agent` | `/root/llm-wiki-agent` | 649 | 916 |
| `root-company-data-command-center` | `/root/company-data-command-center` | 101 | 101 |
| `root-GenericAgent` | `/root/GenericAgent` | 1377 | 3662 |

Vault index files:

```
/root/Documents/Obsidian Vault/Projects/Codebase Memory/
├── Codebase Memory — Detailed Index 2026-06-27.md
├── codebase-memory-index-2026-06-27.json
├── Codebase Memory MCP Architecture Snapshots 2026-06-27.md
└── DeepSeek Fast — Codebase Memory Review 2026-06-27.md
```

## Worker profile integration

When the orchestrator dispatches a coding task to a worker profile (deepseek-pro, deepseek-fast, kimi-code, glm-go, minimax-go):

1. **Orchestrator** queries the graph first and includes relevant node/edge info in the task prompt.
2. **Worker** can also query the graph directly using the CLI commands above — the tool is installed system-wide, not per-profile.
3. **Worker** must report which files it read and why the graph pointed to them.
4. **Orchestrator** verifies the worker touched the right files by checking the graph.

Example worker dispatch prompt shape:

```
TASK: <specific coding task>
REPO: /root/Company-Dashboard
PROJECT_NAME: root-Company-Dashboard

GRAPH CONTEXT (pre-queried by orchestrator):
- Entry points: <list>
- Hotspots: <list>
- Relevant files: <list from search_graph>
- Call path: <from trace_path if applicable>

INSTRUCTIONS:
1. Read only the files listed above plus any the graph reveals as dependencies.
2. Do NOT randomly browse the repo.
3. Make the change.
4. Run tests.
5. Report: files read, files changed, test result.
```

## MCP server mode (for long-running agent sessions)

For agents that stay alive and need repeated queries:

```bash
# Run as MCP server on stdio (for Claude Code, Codex, etc.)
/root/tools/codebase-memory-test/node_modules/.bin/codebase-memory-mcp

# Enable HTTP graph visualization UI
/root/tools/codebase-memory-test/node_modules/.bin/codebase-memory-mcp --ui=true --port=9749
```

When the MCP server is running, agents can call these tools directly:
- `index_repository` — index or re-index a repo
- `search_graph` — BM25 search over the graph
- `query_graph` — structured graph queries
- `trace_path` — find call paths between two symbols
- `get_code_snippet` — get a specific function's code
- `get_architecture` — architectural overview
- `get_graph_schema` — schema of the graph
- `detect_changes` — check if re-indexing needed
- `list_projects` — list all indexed projects

## Common Pitfalls

1. **Indexing with wrong project name.** The project name becomes the namespace. Always prefix with `root-` (e.g., `root-Company-Dashboard`). The tool auto-prefixes if you don't.

2. **Forgetting to re-index after large changes.** The graph is a snapshot. After significant refactoring, run `detect_changes` and re-index.

3. **Treating the graph as ground truth for editing.** The graph tells you WHERE things are and HOW they connect. It does NOT replace reading the actual file before editing. Always read the file before modifying it.

4. **Over-indexing.** Don't index every tiny repo. The tool works best on repos with 20+ files. For smaller repos, just read the files.

5. **Node modules and venv pollution.** The tool auto-excludes `.git`, `node_modules`, `.venv`, `__pycache__`, but verify the excluded count in the output. If a repo has unusual vendored dirs, they may slip in.

6. **Binary files in the graph.** The tool skips files it can't parse (images, compiled binaries), but may still create File nodes for them. These are structural only — no AST data.

7. **GenericAgent documentation is in Chinese.** The graph indexes structure, not meaning. Chinese variable names and SOPs will be present but may not be useful for Arabic/English reasoning.

8. **Worker profiles do not share skill state.** Each profile has its own copy of skills. When this skill is updated in the default profile, it must be re-copied to all worker profiles (see maintenance below).

## Maintenance: updating the skill across profiles

When this skill is patched or updated in the default profile:

```bash
for p in deepseek-fast deepseek-pro kimi-code glm-go minimax-go; do
  src="/root/.hermes/skills/software-development/codebase-memory-workflow"
  dst="/root/.hermes/profiles/$p/skills/software-development/codebase-memory-workflow"
  rm -rf "$dst"
  cp -a "$src" "$dst"
done
```

Verify each copy:

```bash
for p in deepseek-fast deepseek-pro kimi-code glm-go minimax-go; do
  echo "$p: $(wc -c < /root/.hermes/profiles/$p/skills/software-development/codebase-memory-workflow/SKILL.md) bytes"
done
```

## Verification Checklist

- [ ] The tool is installed at `/root/tools/codebase-memory-test/node_modules/.bin/codebase-memory-mcp`
- [ ] `codebase-memory-mcp --help` returns usage info
- [ ] Target repo is indexed (run `list_projects` to confirm)
- [ ] `get_architecture` returns node/edge counts
- [ ] `search_graph` returns relevant results for a known function name
- [ ] The vault index files exist under `Projects/Codebase Memory/`
- [ ] Worker profiles have this skill in `skills/software-development/codebase-memory-workflow/`
- [ ] Each worker profile's SKILL.md matches the default profile's copy (same byte count)

## aarch64 PRoot limitations

On aarch64 PRoot/Termux environments, heavy ML-based document tools (full Docling pipeline) may hang or timeout during import due to torch + transformers + model loading. Use `docling-core` types for document representation only, and rely on existing Company-Dashboard extractors (pdfplumber + tesseract) for actual file parsing. Full Docling is viable on x86_64 servers with GPU. See `references/docling-installation-aarch64.md` for the detailed installation log and dependency list.