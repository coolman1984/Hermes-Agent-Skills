# YouTube Tools Skill

Use these tools to fetch YouTube data. No API key needed for any of these.

## Installation (already done)
These are already installed in this environment:
- `yt-dlp` — video/audio download, metadata, comments, chapters
- `youtube-transcript-api` — timestamped transcripts, auto-generated or manual, with translation
- `scrapetube` — search, channel crawling, playlists

## Quick Reference

### Transcript (cleanest approach)
```python
from youtube_transcript_api import YouTubeTranscriptApi

# Get transcript
transcript = YouTubeTranscriptApi().fetch("VIDEO_ID")
for seg in transcript:
    print(f"{seg.start:.1f}s: {seg.text}")

# List available languages
langs = YouTubeTranscriptApi().list("VIDEO_ID")

# Translate to Arabic
trans = YouTubeTranscriptApi().fetch("VIDEO_ID", languages=["en"]).translate("ar")

# Multiple videos
transcripts = YouTubeTranscriptApi().fetch_many(["ID1", "ID2"])
```

### Metadata + Info (yt-dlp)
```python
from yt_dlp import YoutubeDL

with YoutubeDL({}) as ydl:
    info = ydl.extract_info("https://youtube.com/watch?v=VIDEO_ID", download=False)
    print(info["title"], info["view_count"], info["like_count"],
          info["channel"], info["chapters"], info["description"])
```

### Comments
```python
with YoutubeDL({"getcomments": True}) as ydl:
    info = ydl.extract_info(url, download=False)
    for c in info["comments"]:
        print(c["text"], c["author"], c["like_count"])
```

### Search
```python
import scrapetube

results = scrapetube.get_search("topic", limit=20)
for v in results:
    print(v["videoId"], v["title"]["runs"][0]["text"])

# Channel videos
videos = scrapetube.get_channel("https://youtube.com/@CHANNEL")
# Playlist
playlist = scrapetube.get_playlist("PLAYLIST_ID")
```

## Skill Usage in OpenClaw

Before using web search for a YouTube topic, check if a YouTube transcript would be better:
- Podcasts, lectures, tutorials → use transcript
- News, commentary, reviews → use search + scrapetube
- Channel analysis → use scrapetube

## Common Video ID extraction
```python
import re
def get_video_id(url):
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([^&\n?#]+)',
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return url if len(url) == 11 else None
```
