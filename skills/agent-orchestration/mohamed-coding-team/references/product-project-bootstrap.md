# Product project bootstrap pattern

Use this when Mohamed graduates a business/product idea into “نبتدي” or “أسس المشروع”.

## Pattern validated in session

For a serious software-product idea, do not stop at strategy. Execute a reversible internal bootstrap:

1. Load `mohamed-coding-team`, `mohamed-intelligence-vault`, and `obsidian` if relevant.
2. Read `CURRENT-SNAPSHOT.md` before changing project focus.
3. Search the intelligence vault for related ideas to avoid duplicate project sprawl.
4. Use Claude Code as architect only:
   - architecture decision
   - phase boundaries
   - risks
   - tests
   - instructions for Codex/OpenCode
   - no implementation code
5. Use Codex as supervisor to turn the architecture into worker-ready execution order.
6. Use OpenCode for the first repo scaffold or small implementation slice.
7. Save durable project state in the vault:
   - project note under `Projects/`
   - idea note under `Ideas/Intelligence Vault/Ideas/`
   - update index/categories/review queue/snapshot when focus changes
8. Verify real artifacts:
   - repo exists
   - schema/config parses if created
   - expected files exist
   - git status is known

## Scope discipline

If the idea is broad, force a narrow first product and first vertical before building. Example pattern:

- Not: “read any company file”.
- First product: “files to reports”.
- First vertical: sales files only.
- First proof: raw file → local database → report → provenance for every number.

## Pitfall

Do not create autonomous monitoring/guard infrastructure as a side quest during bootstrap unless Mohamed explicitly asks for it. Keep the build focused on the first proof slice.
