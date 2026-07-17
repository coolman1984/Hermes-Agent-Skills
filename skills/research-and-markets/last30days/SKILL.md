---
name: last30days
description: Research any topic across Reddit, X, YouTube, HN, Polymarket from the
  last 30 days
tags: [research, trends, reddit, twitter, youtube, hackernews, synthesis]
---

# last30days Skill

Research any topic across Reddit, X, YouTube, HN, Polymarket from the last 30 days — then synthesize a grounded summary.

## Usage

### Basic Research

```bash
cd ~/.hermes/skills/research && python3 scripts/last30days.py "<topic>" [options]
```

### Options

| Flag | Description |
|------|-------------|
| `--quick` | Faster research (8-12 sources each) |
| `--deep` | Comprehensive (50-70 Reddit, 40-60 X) |
| `--refresh` | Bypass cache, fetch fresh data |
| `--emit=compact` | Compact output (default) |
| `--emit=json` | JSON output |
| `--emit=md` | Full markdown report |
| `--sources=reddit,x,hn,polymarket,youtube` | Select sources |

### Examples

```bash
# Quick research on AI agents
python3 scripts/last30days.py "AI agents 2026" --quick

# Deep research with all sources
python3 scripts/last30days.py "Claude Code vs Codex" --deep

# Get JSON for programmatic use
python3 scripts/last30days.py "bitcoin" --emit=json
```

## Available Sources

| Source | Free | API Key Needed |
|--------|------|----------------|
| Reddit | ✅ Yes (threads) | Optional for comments |
| Hacker News | ✅ Yes | No |
| Polymarket | ✅ Yes | No |
| YouTube | ✅ Yes | yt-dlp only |
| X/Twitter | ⚠️ Optional | Cookie or xAI key |
| Web Search | ⚠️ Optional | Exa (1000 free/month) |

## Output Files

Saved to `~/.local/share/last30days/out/`:
- `report.md` - Full report
- `report.json` - Normalized data
- `last30days.context.md` - Compact snippet for other skills

## Setup for More Sources

### Add X/Twitter
```bash
# Option 1: xAI API key
echo "XAI_API_KEY=your_key" >> ~/.config/last30days/.env

# Option 2: Browser cookies (run setup wizard)
python3 scripts/last30days.py setup
```

### Add Reddit Comments
```bash
# Get free key at scrapecreators.com
echo "SCRAPECREATORS_API_KEY=your_key" >> ~/.config/last30days/.env
```

### Add Web Search
```bash
# Get free key at exa.ai
echo "EXA_API_KEY=your_key" >> ~/.config/last30days/.env
```

---

## YouTube Download (Bonus)

For downloading YouTube videos with format selection:

```bash
# Show video info and formats
python3 ~/.hermes/scripts/youtube_helper.py formats "<url>"

# Download with format choice (will prompt you)
python3 ~/.hermes/scripts/youtube_helper.py download "<url>"
```

### Available Formats

| Format | Type | Quality |
|--------|------|---------|
| 140 | Audio | m4a (130k) |
| 18 | Video | 360p |
| 134 | Video | 360p |
| 135 | Video | 480p |
| 136 | Video | 720p |
| 137 | Video | 1080p |
| 271 | Video | 1440p |
| 313 | Video | 4K |

### Examples
```bash
# Download 1080p
python3 ~/.hermes/scripts/youtube_helper.py download "<url>" 137

# Download audio only as MP3
python3 ~/.hermes/scripts/youtube_helper.py download "<url>" mp3
