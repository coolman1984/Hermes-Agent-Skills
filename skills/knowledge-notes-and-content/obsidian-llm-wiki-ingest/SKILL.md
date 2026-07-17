---
name: obsidian-llm-wiki-ingest
description: Ingest a set of Obsidian project notes into a local llm-wiki-agent repository as raw captures, source pages, entity pages, concept pages, and refreshed overview/index/log files.
---

# Obsidian → LLM Wiki Ingest

Use this skill when turning a cluster of Obsidian notes into a maintained `llm-wiki-agent` wiki.

## Trigger conditions
- The user wants to “bring a note/project into the wiki”.
- There is a stable cluster of project notes in the Obsidian vault.
- You need source pages, entity pages, concept pages, and graph/validation updates.

## Core workflow

1. Read `CURRENT-SNAPSHOT.md` first.
   - Treat it as the current operating context, especially for important or ongoing projects.
2. Read the candidate Obsidian notes fully.
   - Prefer the project notes in `Projects/` and any operational notes in `Investing/`, `egx_system/`, or similar domain folders.
3. Identify the first source pack.
   - Usually the most central project note plus its supporting doctrine, source ladder, and workflow notes.
4. Map the pack into wiki nodes.
   - Source pages: one per source note.
   - Entity pages: recurring organizations, people, systems, or tools.
   - Concept pages: reusable doctrines, frameworks, ladders, workflows, or operating systems.
5. Copy raw source text into `raw/` unchanged.
   - Keep raw captures separate from generated wiki pages.
6. Write or update the wiki pages.
   - Update `wiki/index.md`.
   - Update `wiki/overview.md` with the new synthesis.
   - Append to `wiki/log.md`.
7. Validate the wiki.
   - Run `python tools/ingest.py --validate-only`.
   - Run `python tools/build_graph.py --no-infer`.
8. Inspect the resulting graph and index.
   - Confirm new pages are indexed.
   - Confirm the graph rebuild succeeded.
9. Update the vault snapshot if the wiki state changed materially.
   - Add a short current-state line and a clear next step in `CURRENT-SNAPSHOT.md`.

## Batch Maintenance Workflow

Use this when Mohamed asks to continue the intelligence/wiki project broadly, e.g. "اعمل كله" after a status review.

1. Treat the request as a combined maintenance pass: vault cleanup + wiki ingest + operating-cycle note + snapshot update.
2. Select the next ingest pack from the current snapshot's stated next step, not from novelty. If the snapshot says "sector cases and operational reports", prefer concrete sector-case/project notes already in `Projects/`.
3. For each selected source, copy the original note into `raw/` unchanged, then create concise source pages and only structurally important concept/entity pages.
4. Update `wiki/index.md`, `wiki/overview.md`, and `wiki/log.md` in the same pass.
5. Run validation and graph build before reporting completion.
6. Update `CURRENT-SNAPSHOT.md` with both what changed and the new next step.

Good default for the EGX knowledge base after the first ingest: add a second pack around sector evaluation/case review, then create concept pages for the evaluation matrix and case-review pattern.

## Practical notes
- If a bulk vault search tool returns nothing unexpectedly, fall back to a filesystem walk in terminal or Python (`Path.rglob('*.md')`) before assuming the vault is empty.
- Use the existing project note as the narrative anchor; do not invent a new direction if the note already states the current doctrine.
- When multiple notes describe one operating system, treat them as a cluster and create one shared concept page plus separate source pages.
- Keep the first ingest small but complete: source pages, entity pages, one or more concept pages, overview, index, and log.

## Verification checklist
- [ ] Raw captures exist in `raw/`
- [ ] Source pages exist in `wiki/sources/`
- [ ] Entity pages exist in `wiki/entities/`
- [ ] Concept pages exist in `wiki/concepts/`
- [ ] `wiki/index.md` links every new page
- [ ] `wiki/overview.md` reflects the new cluster
- [ ] `wiki/log.md` records the ingest
- [ ] Validation passes
- [ ] Graph build passes
- [ ] `CURRENT-SNAPSHOT.md` reflects the new state

## Common pitfalls
- Do not let generated markdown retain accidental leading indentation from templating.
- Do not skip validation after writing many pages at once.
- Do not update only the wiki pages and forget the vault snapshot.
- Do not create entity pages for every noun; only recurring or structurally important nodes.
- Do not merge temporary notes into raw source captures.

## Good default output
When successful, report:
- what cluster was ingested,
- how many source/entity/concept pages were added,
- whether validation and graph build passed,
- and what the next ingest target should be.
