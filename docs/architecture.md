# Architecture

## Goals

1. Make every skill discoverable by **function**.
2. Preserve full skill packages (procedure + support files).
3. Keep dual compatibility with Hermes historical category layout.
4. Provide machine-readable indexes for tooling.

## Layers

```text
User / operator
      |
      v
README + CATALOG.md
      |
      v
skills/<domain>/README.md
      |
      v
skills/<domain>/<skill>/
      |
      +-- SKILL.md
      +-- references/
      +-- templates/
      +-- scripts/
      +-- assets/
```

## Domain model

Domains are functional buckets. Each skill has one primary domain for browsing. Related skills can still cross-link inside `SKILL.md`.

Assignment priority:

1. Explicit functional map (name-based)
2. Original Hermes top-level category fallback
3. Special-case remaps (OpenClaw imports, etc.)

## Indexes

| Artifact | Purpose |
|---|---|
| `README.md` | landing + domain table |
| `CATALOG.md` | full annotated list |
| `catalog.json` | structured inventory |
| `taxonomy.yaml` | domain to names |
| `docs/alphabetical-index.md` | A-Z lookup |
| `docs/original-hermes-categories.md` | old layout bridge |

## Excluded from export

- root `.archive/`
- curator backups / usage telemetry
- empty scaffold categories without `SKILL.md`

## Refresh contract

Valid only when:

- skill/domain counts regenerated
- every `catalog.json` path exists
- each skill folder has `SKILL.md`
- domain READMEs match membership
