# Hermes Agent Skills Library

> A professionally organized library of **214** Hermes Agent skills, grouped by **what they do**, not only by folder history.

**Generated:** `2026-07-17T10:56:14Z`  
**Layout:** Functional domains → skill packages → `SKILL.md` + support files  
**Machine indexes:** [`catalog.json`](catalog.json) · [`taxonomy.yaml`](taxonomy.yaml) · [`CATALOG.md`](CATALOG.md)

---

## Why this repo exists

Hermes skills are the operating procedures of the agent: how it reasons, codes, researches, extracts data, runs multi-agent work, and ships durable output.

This repository turns a live local skill tree into a **clear, navigable product**:

- **Functional domains** (purpose-first browsing)
- **Full skill packages** (not just names)
- **Dual indexes** (functional + original Hermes categories + A–Z)
- **Stable machine catalog** for tools and automation

---

## Domains (by function)

| # | Domain | Skills | What it covers |
|---:|---|---:|---|
| 1 | [Core Reasoning & Execution](skills/core-reasoning-and-execution/) | 21 | How the agent thinks, plans, verifies, and delivers under pressure. |
| 2 | [Agent Orchestration & Hermes OS](skills/agent-orchestration/) | 22 | Multi-agent loops, Hermes configuration, profiles, workers, and handoffs. |
| 3 | [Software Engineering](skills/software-engineering/) | 25 | Architecture, coding standards, testing, debugging, review, and platform builds. |
| 4 | [Data Engineering & Databases](skills/data-engineering-and-databases/) | 5 | Extraction, ETL, SQL, file resilience, and data pipelines. |
| 5 | [Research, Markets & Intelligence](skills/research-and-markets/) | 27 | Web/academic research, market workflows, credibility checks, and answer engines. |
| 6 | [Knowledge, Notes & Content Systems](skills/knowledge-notes-and-content/) | 21 | Vaults, media ingestion, Arabic content, books, and second-brain systems. |
| 7 | [Creative, Design & Video](skills/creative-and-video/) | 32 | HyperFrames, motion, design systems, diagrams, generative art, and music. |
| 8 | [MLOps, Training & Model Ops](skills/mlops-and-models/) | 22 | Fine-tuning, inference, evaluation, multimodal models, and experiment tracking. |
| 9 | [Productivity & Office Automation](skills/productivity-and-office/) | 10 | Docs, decks, sheets ecosystems, meetings, and productivity CLIs. |
| 10 | [Media & Social Platforms](skills/media-and-social/) | 9 | YouTube, Spotify, GIFs, X/Twitter tools and content retrieval. |
| 11 | [Device, Platform & DevOps](skills/device-platform-and-devops/) | 15 | Android/Termux control, computer use, cleanup, webhooks, and environment ops. |
| 12 | [Integrations: GitHub & MCP](skills/integrations-github-mcp/) | 3 | Repository workflows and Model Context Protocol tooling. |
| 13 | [Security, Vetting & Red Team](skills/security-and-skill-safety/) | 2 | Skill security review and red-team research tooling. Handle carefully. |

---

## Quick navigation

| Want… | Go here |
|---|---|
| Full human catalog | [`CATALOG.md`](CATALOG.md) |
| A–Z list | [`docs/alphabetical-index.md`](docs/alphabetical-index.md) |
| Original Hermes categories | [`docs/original-hermes-categories.md`](docs/original-hermes-categories.md) |
| Machine-readable catalog | [`catalog.json`](catalog.json) |
| Domain map | [`taxonomy.yaml`](taxonomy.yaml) |
| How skills work | [`docs/how-skills-work.md`](docs/how-skills-work.md) |
| Repo architecture | [`docs/architecture.md`](docs/architecture.md) |

---

## Repository structure

```text
.
├── README.md
├── CATALOG.md
├── catalog.json
├── taxonomy.yaml
├── LICENSE
├── CONTRIBUTING.md
├── docs/
│   ├── architecture.md
│   ├── how-skills-work.md
│   ├── alphabetical-index.md
│   └── original-hermes-categories.md
└── skills/
    ├── core-reasoning-and-execution/
    ├── agent-orchestration/
    ├── software-engineering/
    ├── data-engineering-and-databases/
    ├── research-and-markets/
    ├── knowledge-notes-and-content/
    ├── creative-and-video/
    ├── mlops-and-models/
    ├── productivity-and-office/
    ├── media-and-social/
    ├── device-platform-and-devops/
    ├── integrations-github-mcp/
    └── security-and-skill-safety/
```

Each domain folder has:

- `README.md` — domain purpose + skill table
- one folder per skill, with at least `SKILL.md`

Optional inside a skill: `references/`, `templates/`, `scripts/`, `assets/`.

---

## Skill package format

Every skill is a directory with a `SKILL.md` file. Typical frontmatter:

```yaml
---
name: example-skill
description: "When to use this skill and what it does."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [example, domain]
    related_skills: [other-skill]
---
```

---

## Using these skills with Hermes

1. Copy or symlink a skill folder into your Hermes skills directory (commonly `~/.hermes/skills/<category>/<skill-name>/`).
2. Ensure `SKILL.md` is valid.
3. Start a **new session** so discovery reloads.
4. Invoke by task intent or explicitly via skill tools.

Core packages:

- Hermes OS guide: [`skills/agent-orchestration/hermes-agent/`](skills/agent-orchestration/hermes-agent/)
- Skill authoring: [`skills/agent-orchestration/hermes-agent-skill-authoring/`](skills/agent-orchestration/hermes-agent-skill-authoring/)

---

## Design principles

1. **Purpose over history** — browse by job-to-be-done.
2. **Complete packages** — procedures stay with their references.
3. **No orphan skills** — every skill appears in domain + A–Z + JSON.
4. **Operator clarity** — short domain READMEs.
5. **Automation-ready** — `catalog.json` / `taxonomy.yaml`.

---

## Scope and privacy

This export is a **private operator library**. It may include environment-specific and personal operating procedures.

Do **not** publish blindly without a privacy review. Never commit secrets, tokens, cookies, or live credentials.

---

## Counts snapshot

- **Total skills:** 214
- **Domains:** 13
- **Largest domains:** Creative, Design & Video (32), Research, Markets & Intelligence (27), Software Engineering (25), Agent Orchestration & Hermes OS (22), MLOps, Training & Model Ops (22)

---

## License

Unless a skill file declares otherwise, content is under MIT. See [`LICENSE`](LICENSE).

---

## Maintenance

1. Export skill packages from `~/.hermes/skills` (resolve symlinks).
2. Rebuild domain assignment + indexes.
3. Update `catalog.json`, `taxonomy.yaml`, `CATALOG.md`, domain READMEs.
4. Commit: `chore: refresh skills export YYYY-MM-DD`.

---

## Credits

- Hermes Agent (Nous Research) skill system
- Operator custom skills and mastery packages
- Bundled / community sources retained in package metadata where present
