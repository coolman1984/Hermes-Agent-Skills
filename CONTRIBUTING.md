# Contributing

## Add or update a skill

1. Place the skill under the correct functional domain in `skills/`.
2. Ensure `SKILL.md` has valid frontmatter (`name`, `description`).
3. Update indexes: domain README, CATALOG.md, catalog.json, taxonomy.yaml, A-Z and original-category docs.
4. Do not commit secrets, tokens, or private credentials.
5. Prefer small reviewable diffs.

## Domain placement guide

| If the skill mainly... | Put it in... |
|---|---|
| frames problems, plans, verifies delivery | `core-reasoning-and-execution` |
| runs agents, Hermes, workers, handoffs | `agent-orchestration` |
| writes/reviews/tests software | `software-engineering` |
| extracts or models data | `data-engineering-and-databases` |
| researches markets/web/papers | `research-and-markets` |
| builds knowledge/content systems | `knowledge-notes-and-content` |
| designs, animates, videos | `creative-and-video` |
| trains/serves/evals models | `mlops-and-models` |
| office docs/productivity SaaS | `productivity-and-office` |
| social/media platforms | `media-and-social` |
| devices, Android, cleanup, ops | `device-platform-and-devops` |
| GitHub or MCP bridges | `integrations-github-mcp` |
| security/vetting/red-team | `security-and-skill-safety` |

## Quality bar

- Clear trigger description
- Actionable steps
- Explicit verification
- Pitfalls from real failures when available
