# Batch Mining Saved Media Notes

Use this when Mohamed asks to scan existing summaries, old media notes, or saved link outputs and extract business ideas from them.

## What changed from the session

The saved media library is not only under the new unified path. Older valuable notes may live in several legacy download trees:

- `/storage/emulated/0/Download/media-notes/`
- `/storage/emulated/0/Download/youtube-transcripts/`
- `/storage/emulated/0/Download/x-article-notes/`
- `/storage/emulated/0/Download/github-repo-notes/`
- `/storage/emulated/0/Download/long-topic-splits/`

Do not stop after checking only `media-notes` if it is empty or sparse.

## Recommended workflow

1. Inventory Markdown files across the known roots, excluding `.obsidian` and `.trash`.
2. Prioritize files that look like processed notes, summaries, repo notes, transcripts, or idea maps.
3. For large batches, split by theme and delegate extraction in parallel:
   - agent workflows and operations;
   - content, audience, second brain, and idea mines;
   - accounting, local business, money, and platform strategy.
4. Ask each worker to extract opportunities, not summaries:
   - customer pain;
   - gap or wedge;
   - likely buyer;
   - product or service;
   - nearest sales experiment.
5. Consolidate results into one batch note when the goal is broad review, then create standalone idea notes only for the opportunities chosen for execution.
6. Update:
   - `00 - Index.md`
   - `02 - Categories.md`
   - `03 - Connections.md`
   - `04 - Stronger Combinations.md`
   - `05 - Review Queue.md`
   - `06 - Media Source Map.md`

## Output shape

For a first batch pass, prefer one consolidated note under:

`/root/Documents/Obsidian Vault/Ideas/Intelligence Vault/Ideas/`

Use a title like:

`YYYY-MM-DD-استخراج-فرص-من-ملخصات-الوسائط.md`

The note should include:

- the roots scanned;
- strongest opportunity themes;
- concrete opportunity cards;
- stronger combinations;
- top priorities to start now;
- next validation step.

## Pitfalls

- Do not treat empty `search_files` results as proof no notes exist; run a direct filesystem inventory when needed.
- Do not create dozens of low-quality idea notes in one batch. Consolidate first, then split winners later.
- Do not summarize the source files again. The saved notes already summarize; the value is business extraction and connection.
- Do not forget to record the bridge in `06 - Media Source Map.md`.
