---
name: obsidian
description: Read, search, list, and create notes in a local Obsidian vault via the
  terminal, resolving the vault path from OBSIDIAN_VAULT_PATH. Use when the user wants
  to work with their Obsidian notes — reading, searching, or adding markdown files.
tags: [obsidian, notes, vault, markdown, knowledge-base, terminal]
---

# Obsidian Vault

**Location:** Set via `OBSIDIAN_VAULT_PATH` environment variable (e.g. in `~/.hermes/.env`).

If unset, defaults to `~/Documents/Obsidian Vault`.

Note: Vault paths may contain spaces - always quote them.

## Read a note

```bash
VAULT="${OBSIDIAN_VAULT_PATH:-$HOME/Documents/Obsidian Vault}"
cat "$VAULT/Note Name.md"
```

## List notes

```bash
VAULT="${OBSIDIAN_VAULT_PATH:-$HOME/Documents/Obsidian Vault}"

# All notes
find "$VAULT" -name "*.md" -type f

# In a specific folder
ls "$VAULT/Subfolder/"
```

## Search

```bash
VAULT="${OBSIDIAN_VAULT_PATH:-$HOME/Documents/Obsidian Vault}"

# By filename
find "$VAULT" -name "*.md" -iname "*keyword*"

# By content
grep -rli "keyword" "$VAULT" --include="*.md"
```

## Create a note

```bash
VAULT="${OBSIDIAN_VAULT_PATH:-$HOME/Documents/Obsidian Vault}"
cat > "$VAULT/New Note.md" << 'ENDNOTE'
# Title

Content here.
ENDNOTE
```

## Append to a note

```bash
VAULT="${OBSIDIAN_VAULT_PATH:-$HOME/Documents/Obsidian Vault}"
echo "
New content here." >> "$VAULT/Existing Note.md"
```

## Wikilinks

Obsidian links notes with `[[Note Name]]` syntax. When creating notes, use these to link related content.

## Project setup workflow

When the user starts a new important project in the vault:
1. Read `CURRENT-SNAPSHOT.md` first if it exists.
2. Create or update a dedicated project note under `Projects/`.
3. Add a short decision framework or operating rule note if the project needs one.
4. Link the project note to its executive references using `[[...]]`.
5. If the project establishes a durable rule or repeated workflow, keep it in the vault note rather than internal assistant memory.

## External second brains

If the user mentions a second brain on Google Drive, do not assume it is this local Obsidian vault. Use the Google Workspace skill for Drive access, keep the local vault and Drive knowledge base clearly separated, and only create local mirrors/caches with explicit scope.
