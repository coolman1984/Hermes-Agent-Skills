# 2026-06-27 — Codebase Memory First Run

## Why this reference exists

Mohamed asked to read the latest source note about codebase-memory / repo graph context, use the `deepseek-v4-flash` worker profile, and build detailed indexing for the local files so future agents can reach and understand them faster.

## Source notes read

- `/storage/emulated/0/Download/media-notes/x/Voxyz_ai/codebase-memory-repo-graph-agent-context - 2026-06-27.md`
- `/root/Documents/Obsidian Vault/Ideas/Intelligence Vault/Codebase Memory as Agent Context Layer - 2026-06-27.md`

Operational interpretation: the pattern is valuable as a context layer before large coding work; it should not become a separate infrastructure project unless it proves value in repeated tasks.

## Package found and installed

Candidate package used:

`codebase-memory-mcp@0.8.1`

Install path:

`/root/tools/codebase-memory-test`

Known-good commands:

```bash
mkdir -p /root/tools/codebase-memory-test
cd /root/tools/codebase-memory-test
npm init -y >/dev/null
npm install codebase-memory-mcp@0.8.1
./node_modules/.bin/codebase-memory-mcp --help
```

Important package detail: `index_repository` expects `repo_path` and `project_name`. An attempted shape using `path` / `project` failed with `repo_path is required`.

## Repositories indexed

Commands were run through the package CLI. Verified results:

| Repo | Project name returned | Nodes | Edges | Notes |
|---|---|---:|---:|---|
| `/root/Company-Dashboard` | `root-Company-Dashboard` | 2716 | 9652 | Biggest useful target; mature dashboard/reports/extractors repo |
| `/root/llm-wiki-agent` | `root-llm-wiki-agent` | 649 | 916 | Wiki/graph/RAG tools and EGX knowledge |
| `/root/company-data-command-center` | `root-company-data-command-center` | 101 | 101 | Early skeleton; schema/docs matter more than code |
| `/root/GenericAgent` | `root-GenericAgent` | 1377 | 3662 | Separate agent system; many Chinese docs; treat sensitive config carefully |

Example verified query:

```bash
cd /root/tools/codebase-memory-test
./node_modules/.bin/codebase-memory-mcp cli search_graph '{"project":"root-Company-Dashboard","query":"reports render pdf arabic","limit":10}'
```

This correctly returned `reports/render.py` and PDF/Arabic render functions such as `render_pdf`, `render_pdf_pack`, `_render_pdf_single_html`, and `render_pdf_pack_html`.

## Artifacts written

Folder:

`/root/Documents/Obsidian Vault/Projects/Codebase Memory/`

Files produced and verified:

| File | Size / lines at verification |
|---|---:|
| `Codebase Memory — Detailed Index 2026-06-27.md` | 124446 bytes / 732 lines |
| `codebase-memory-index-2026-06-27.json` | 2494947 bytes / 100791 lines |
| `Codebase Memory MCP Architecture Snapshots 2026-06-27.md` | 44382 bytes / 31 lines |
| `DeepSeek Fast — Codebase Memory Review 2026-06-27.md` | 11761 bytes / 201 lines |

`CURRENT-SNAPSHOT.md` was updated with a one-line note that the first Codebase Memory experiment exists.

## Worker profile use

Worker used:

`deepseek-fast` → `deepseek-v4-flash`

Invocation pattern:

```bash
hermes -p deepseek-fast chat -Q --max-turns 4 -q 'SELF-CONTAINED TASK WITH EXACT FILE PATHS AND OUTPUT FILE'
```

Use foreground mode for worker calls unless the task is truly long-running and Mohamed benefits from a raw background completion notice.

## Lessons

1. Codebase memory is a preflight context layer. It helps choose which files to read; it does not replace reading source files before editing.
2. For Mohamed's repos, the most useful immediate target is `Company-Dashboard`; then `llm-wiki-agent`.
3. Generated reports should avoid exposing secrets or private config details. If a worker mentions a sensitive setup file too explicitly, sanitize the report before final delivery.
4. Package/API discovery can hit rate limits. The durable lesson is to verify the candidate by installing and running real commands, not to rely on search snippets.
5. The output should be both human-readable Markdown and machine-readable JSON so future agents can consume it directly.
