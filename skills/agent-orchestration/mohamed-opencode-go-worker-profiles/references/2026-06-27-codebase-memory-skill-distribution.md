# Codebase Memory Skill Distribution — 2026-06-27

## What was done

Created the skill `codebase-memory-workflow` in the default profile and distributed it to all five worker profiles.

## Skill location

Default profile:

```
/root/.hermes/skills/software-development/codebase-memory-workflow/SKILL.md
```

Worker profiles (identical copies):

```
/root/.hermes/profiles/deepseek-fast/skills/software-development/codebase-memory-workflow/SKILL.md
/root/.hermes/profiles/deepseek-pro/skills/software-development/codebase-memory-workflow/SKILL.md
/root/.hermes/profiles/kimi-code/skills/software-development/codebase-memory-workflow/SKILL.md
/root/.hermes/profiles/glm-go/skills/software-development/codebase-memory-workflow/SKILL.md
/root/.hermes/profiles/minimax-go/skills/software-development/codebase-memory-workflow/SKILL.md
```

## Verification

All six copies (default + 5 workers) match at 10064 bytes.

## What the skill does

Defines the standard workflow for any coding agent (default or worker) when touching a repo with 20+ files:

1. Index the repo with `codebase-memory-mcp`
2. Build the local detailed index with the Python script
3. Query the graph before reading files randomly
4. Read only the files the graph points to
5. Re-index after significant changes

## Worker integration

When the orchestrator dispatches a coding task to a worker:

1. Query the graph first and include relevant node/edge info in the task prompt
2. The worker can also query the graph directly since the tool is system-wide
3. The worker must report which files it read and why the graph pointed to them
4. The orchestrator verifies the worker touched the right files

## Mosalah: worker profile skills are copies, not symlinks

Each worker profile has its own independent copy of skills under `~/.hermes/profiles/<name>/skills/`. Changes to the default profile's skills do NOT propagate automatically. You must re-copy using the maintenance command in the SKILL.md.

Also: the `mohamed-opencode-go-worker-profiles` skill itself was updated with the codebase memory integration section and re-copied to all five workers (11979 bytes each).

## Tool installation paths

- codebase-memory-mcp: `/root/tools/codebase-memory-test/node_modules/.bin/codebase-memory-mcp`
- Index builder script: `/root/.hermes/scripts/build_codebase_memory_index.py`
- Vault output: `/root/Documents/Obsidian Vault/Projects/Codebase Memory/`

## Indexed repos

| Project | Nodes | Edges |
|---|---:|---:|
| root-Company-Dashboard | 2716 | 9652 |
| root-llm-wiki-agent | 649 | 916 |
| root-company-data-command-center | 101 | 101 |
| root-GenericAgent | 1377 | 3662 |