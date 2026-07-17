# Hermes Stack Evaluation Patterns (2026-06-27)

## Context

Mohamed shared a 12-tool "Hermes stack" recommendation from Reddit/GitHub communities and asked for evaluation. He is not a programmer and wants concise verdicts, not tool catalogs.

## Evaluation framework

When Mohamed sends a list of tools/stack recommendations:

1. **Cross-reference with what we already have** — many "must install" tools are already present
2. **Filter to 2-3 that genuinely matter** — don't list all 12 and ask him to choose
3. **Give a clear verdict table**: Already Have / Worth Installing / Wastes Time
4. **Test before recommending** — actually install and try, don't guess
5. **aarch64 PRoot constraints** — heavy ML tools (full Docling, Docker, large models) may not be practical

## Tools evaluated this session

| Tool | Status | Verdict |
|---|---|---|
| GBrain | Already installed, working | Refresh embeddings when needed |
| Hindsight MCP | Installed, needs cloud API token | Cloud-only, not local-first |
| Docling | Installed but heavy | docling-core works, full pipeline too heavy for aarch64 |
| DuckDB | Not installed | Already have SQLite, DuckDB is a future upgrade |
| Playwright | Already installed and working | No action needed |
| MCP Servers | Already supported by Hermes | codebase-memory-mcp is one |
| Vector DB (Chroma/Qdrant) | Not installed | Chroma is the easy option when needed |
| Docker | Not viable on PRoot | Skip |
| Apache Arrow/Parquet | Not needed yet | Premature for current data volume |
| OCR Pipeline | Tesseract already working | No action needed |
| Local Models | 5 worker profiles running | No action needed |
| Obsidian | Working as Second Brain | No action needed |

## Mohamed's communication preference

When evaluating tools:
- Do NOT show code
- Do NOT list 12 tools and ask "which ones?"
- DO filter to the 2-3 that matter
- DO give a clear verdict: worth it / waste of time / already have
- DO explain in simple non-technical Arabic what each tool does and why it matters or doesn't