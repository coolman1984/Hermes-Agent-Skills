# YouTube → Obsidian Research Pipeline Skill

Full research pipeline: search YouTube → fetch transcripts → write Obsidian vault with wikilinks and citations.

## Architecture

```
YouTube search (scrapetube)
    ↓ selected_urls.txt
Fetch transcripts (youtube-transcript-api)
    ↓ Knowledge/Sources/
Create vault (write_obsidian.py)
    ↓ Topic files + Source files + Research files
OpenClaw (you ask questions)
    ↓ cite from transcripts with timestamps
Final research file (with wikilinks)
```

## The 3-Command Research Loop

### Step 1 — Search and Pick
```bash
python3 skills/obsidian-vault/yt_search.py "AI agents workflows" --limit 20
```
Shows numbered results. Pick videos (e.g. `1,3,5` or `1-5`). Saves to `selected_urls.txt`.

### Step 2 — Fetch Transcripts
```bash
python3 skills/obsidian-vault/yt_transcript.py
```
Reads `selected_urls.txt`, fetches all transcripts, saves to:
- `Knowledge/Sources/Source-{VideoTitle}.md`

Each source file has:
- Channel, views, duration, language
- Full timestamped transcript
- Video metadata in YAML frontmatter

### Step 3 — Analyze and Write
```bash
python3 skills/obsidian-vault/write_obsidian.py --question "Main patterns?" --answer "Six creators used Obsidian Bases..."
```
Creates:
- `Knowledge/Topics/Topic-{Name}.md` — hub file linking all relevant sources
- `Knowledge/Research/Research-{date}-{topic}.md` — Q&A with citations and wikilinks

## Full Pipeline (All 3 Steps)
```bash
# Step 1: Search
python3 skills/obsidian-vault/yt_search.py "Claude Code workflows"

# Step 2: Fetch (after picking videos in selected_urls.txt)
python3 skills/obsidian-vault/yt_transcript.py

# Step 3: Analyze
python3 skills/obsidian-vault/research_pipeline.py analyze \
    --question="What are the main patterns?" \
    --answer="Six creators used Obsidian Bases for context..."
```

## Obsidian Vault Structure

```
Knowledge/
├── INDEX.md                  ← Master index
├── Sources/
│   ├── Source-How I Use Claude Code Daily.md
│   ├── Source-Claude Code + Obsidian Setup.md
│   └── _sources_meta.json   ← Pipeline metadata
├── Topics/
│   ├── Topic-ClaudeCode.md
│   └── Topic-Obsidian.md
└── Research/
    └── Research-2026-03-25-Claude-Code-Patterns.md
```

## Citation Format (Wikilinks)

In Research files:
```
**What are the main patterns?**
Six creators used Obsidian Bases for context [[Source-HowIUseClaudeCodeDaily]].

[[Source-ClaudeCodeObsidianSetup]] showed that Bases changed how teams manage context.

Timestamp citations:
[[Source-HowIUseClaudeCodeDaily]] — 4:32 — "I store all context in Bases..."
```

## OpenClaw Usage

**In OpenClaw, the workflow is:**

1. Search YouTube → show results to Mohamed
2. Mohamed picks videos
3. Fetch all transcripts
4. OpenClaw reads transcripts, answers research question
5. OpenClaw writes Research file with proper wikilinks and citations

**Example OpenClaw prompt for analysis:**
```
Read all files in Knowledge/Sources/
Answer: "What are the main patterns across these videos?"
Write a Research file with proper wikilinks and timestamp citations.
Format citations as: [[Source-VideoTitle]] — MM:SS — "exact quote"
```

## Files
- `yt_search.py` — YouTube search with interactive picker
- `yt_transcript.py` — Fetch transcripts from selected URLs
- `write_obsidian.py` — Create Topic and Research files
- `research_pipeline.py` — Orchestrate all 3 steps
- `SKILL.md` — This file

## Requirements
- `scrapetube` — YouTube search (pip install scrapetube)
- `youtube-transcript-api` — Transcripts (pip install youtube-transcript-api)
- `yt-dlp` — Video metadata (pip install yt-dlp)

All three are already installed.
