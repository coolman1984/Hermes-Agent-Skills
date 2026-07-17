# Google Drive Second Brain Workflow

Use when the user has a personal second brain stored in Google Drive and wants the agent to work with it.

## Key distinction

A Google Drive second brain is user-owned external knowledge. Do not confuse it with the assistant's local Obsidian vault or Hermes internal memory. The local assistant vault can reference or cache it, but should not silently become the canonical source.

## Recommended sequence

1. Clarify the target access scope only if not obvious:
   - read/search only
   - create notes
   - reorganize folders
   - sync/mirror locally
2. Authenticate with the minimum Google scopes needed, usually Drive/Docs only.
3. Discover before changing:
   - root folder name/link
   - file types: Google Docs, Markdown, PDFs, Sheets, images
   - naming conventions and folder hierarchy
   - whether there is an index/start-here note
4. Establish a safe local working layer:
   - cache exported Docs/PDF text for search and summarization
   - keep a mapping of local cache path -> Drive file ID/link -> modified time
   - never overwrite canonical Drive content from stale cache
5. For agent memory integration:
   - promote only verified stable facts to Hermes memory
   - keep project notes and user knowledge in the Drive second brain unless asked otherwise
   - write back changes only after showing the proposed change or receiving standing permission

## Default answer shape for setup questions

- Explain the three options: read-only access, local mirror/index, or full write workflow.
- Recommend starting read-only plus local cache.
- Give OAuth/setup steps via the Google Workspace skill.
- Ask for the folder link or folder name only after explaining what access is needed.

## Unauthenticated fallback: import bundle

If the user asks to add new local files to a Google Drive second brain but `setup.py --check` returns `NOT_AUTHENTICATED`, do not stop at setup instructions when the files are already available locally.

Create a verified import bundle under Downloads so the user can upload it manually or so a later authenticated run can upload the same folder:

```text
/storage/emulated/0/Download/second-brain-import/<date>-<short-topic>/
```

Recommended bundle contents:

- copied Markdown, HTML, PDF, or asset files arranged in a second-brain-friendly folder hierarchy
- `README.md` explaining purpose, source status, and suggested destination folders
- `manifest.json` with source path, destination path, and file size for each copied file
- optional `.zip` created with Python `zipfile` when the system `zip` command is unavailable

Verification before delivery:

- bundle folder exists
- `README.md` exists and is non-empty
- `manifest.json` exists and lists every copied file
- every destination file exists and is non-empty
- missing files are reported explicitly
- if direct Drive upload was skipped, state the exact auth reason, such as `NOT_AUTHENTICATED`

## Safety rules

- Confirm before moving, deleting, renaming, or bulk-editing files.
- Preserve Drive links and file IDs in notes produced from Drive sources.
- If the user also has an assistant Obsidian vault, state clearly which vault is being used for which purpose.
- When direct Drive access is unavailable, clearly label local bundles as ready-to-import, not already uploaded.
