---
name: youtube-download
description: Download YouTube videos with format selection - shows options, user chooses,
  then downloads
tags: [youtube, download, yt-dlp, video, audio, mp3]
---

# YouTube Download Skill

Download YouTube videos with user-friendly format selection.

## Workflow

1. **Get URL from user**
2. **Infer intent before downloading**:
   - If the user sends a YouTube link plus clear words like download, quality, resolution, audio-only, MP3, or formats, proceed with the matching download flow.
   - If the user sends only a bare YouTube link, do **not** assume download. Ask a quick intent question: summary/transcript, download video, download audio only, or show available qualities.
   - Mohamed exception: for Mohamed Fawzy, a bare YouTube link defaults to the `mohamed-unified-media-drop` file-drop notes workflow, not this download workflow and not an intent question, unless he explicitly asks for download/audio/formats or quick chat-only summary.
   - If the user asks for summary/transcript, route to the YouTube transcript/content workflow instead of this download skill.
3. **Show formats when needed**: Run `python3 ~/.hermes/scripts/youtube_helper.py formats "<url>"`
4. **Ask user to choose** format (number or description) unless they already specified quality/audio-only/best.
5. **Download**: Run `python3 ~/.hermes/scripts/youtube_helper.py download "<url>" <format_id>`

## Commands

### Show Video Info & Formats
```bash
python3 ~/.hermes/scripts/youtube_helper.py formats "<YouTube_URL>"
```

### Download
```bash
python3 ~/.hermes/scripts/youtube_helper.py download "<YouTube_URL>" <format_id>
```

## Format Options

| Format ID | Type | Quality |
|-----------|------|---------|
| 140 | Audio | m4a (130k) - Best |
| 139 | Audio | m4a (49k) - Low |
| 18 | Video | 360p (compatible) |
| 134 | Video | 360p |
| 135 | Video | 480p |
| 136 | Video | 720p |
| 137 | Video | 1080p |
| 271 | Video | 1440p |
| 313 | Video | 4K (2160p) |

## Quick Download Examples

```bash
# Best quality
yt-dlp -f best "<url>"

# Best video + audio combined
yt-dlp -f "bestvideo+bestaudio" "<url>"

# 1080p
yt-dlp -f 137 "<url>"

# Audio only as MP3
yt-dlp -x --audio-format mp3 "<url>"
```

## File Location

Downloads go to current working directory.

## Error Handling

- **"Cannot extract"**: Video might be unavailable or private
- **"HTTP Error 403"**: Video is blocked or needs cookies
- **"Subscribed"**: Age-restricted video - may need cookies

For age-restricted videos, you can try:
```bash
yt-dlp --cookies-from-browser chrome "<url>"
```
