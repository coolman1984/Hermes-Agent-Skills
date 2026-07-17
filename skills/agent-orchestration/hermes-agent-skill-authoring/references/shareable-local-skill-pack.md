# Shareable Local Skill Pack

Use this reference when a user asks for "all your skills in one folder", a portable copy of the skill library, or a downloadable archive they can send to another person.

## Goal

Create a shareable snapshot of local Hermes skills without leaking private Hermes state.

## Safe source and destination pattern

- Source: `~/.hermes/skills`
- Friendly destination on Mohamed's Android/PRoot setup: `/sdcard/Download/<pack-name>`
- Archive: create both `.zip` for easy phone sharing and optionally `.tar.gz` for Unix users.

## What to include

- Non-hidden skill/category folders.
- Each skill's original folder structure and `SKILL.md`.
- Supporting files inside skill folders: `references/`, `templates/`, `scripts/`, and `assets/`.
- A generated `README.md` explaining what is inside and how to reuse it.
- A generated `SKILLS_MANIFEST.json` listing copied skills and relative paths.
- A `SECURITY-AUDIT.txt` summarizing exclusions and scan results.

## What to exclude

Never copy these into a share pack:

- `.env`
- `auth.json`
- `config.yaml`
- memories
- sessions/transcripts
- cron jobs
- gateway state and PID files
- hidden curator state, backups, caches, and usage files such as `.curator_*`, `.hub`, `.usage.json`, `.bundled_manifest`

## Practical workflow

1. Confirm `~/.hermes/skills` exists and locate a user-friendly downloads directory. Prefer `/sdcard/Download` on Android/PRoot when available.
2. Copy only non-hidden skill folders into a new dated folder.
3. Generate a manifest by counting `SKILL.md` files and recording relative paths.
4. Add a README that clearly says this is a skill-only export, not a full Hermes profile.
5. Run a conservative secret scan over copied text files:
   - raw API-key assignments
   - token/secret/password assignments
   - common token prefixes such as `sk-` and `ghp_`
6. Manually review any hits. Skill docs often contain placeholders or public URL query parameters; do not treat those as real secrets without inspection.
7. Write `SECURITY-AUDIT.txt` with the review result.
8. Create a `.zip` archive and test archive integrity before saying it is done.
9. Return the folder path and a `MEDIA:` link to the archive when on Telegram.

## Verification checklist

- [ ] Folder exists in Downloads.
- [ ] Archive exists in Downloads.
- [ ] Archive integrity check passes.
- [ ] `SKILL.md` count is reported.
- [ ] File count and size are reported.
- [ ] Forbidden sensitive filenames are absent.
- [ ] Secret-like scan hits are either absent or manually reviewed.
- [ ] User is warned that Mohamed-specific wording/paths may remain if sharing publicly.

## Sharing caveat

This workflow creates a private-to-friends export, not a public sanitized release. If the user wants a public release, make a second cleaned copy that removes Mohamed-specific operating context, local paths, and personal workflows before archiving.
