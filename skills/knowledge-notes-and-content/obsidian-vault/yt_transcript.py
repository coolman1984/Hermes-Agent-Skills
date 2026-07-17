#!/usr/bin/env python3
"""
yt_transcript.py — Fetch YouTube transcripts for selected videos.
Usage: python3 yt_transcript.py [urls_file]
   or: python3 yt_transcript.py --url "https://youtube.com/watch?v=ID"
"""
import sys
import re
import json
import argparse
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    patterns = [
        r'[?&]v=([^&]+)',
        r'youtu\.be/([^?]+)',
        r'youtube\.com/shorts/([^?]+)',
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None

def fetch_transcript(video_id):
    """Fetch transcript, return (segments, language, is_auto)."""
    api = YouTubeTranscriptApi()
    try:
        transcript = api.fetch(video_id)
        segs = list(transcript)
        return segs, "en", False
    except Exception:
        # Try auto-generated
        try:
            transcript = api.fetch(video_id, languages=["en"])
            segs = list(transcript)
            return segs, "en", True
        except Exception:
            return None, None, None

def format_transcript(segments):
    """Format segments as readable text with timestamps."""
    lines = []
    for s in segments:
        mins = int(s.start // 60)
        secs = int(s.start % 60)
        lines.append(f"[{mins:02d}:{secs:02d}] {s.text}")
    return "\n".join(lines)

def format_citation(segment):
    """Format a single segment as citation."""
    mins = int(segment.start // 60)
    secs = int(segment.start % 60)
    return {
        "timestamp": f"{mins}:{secs:02d}",
        "seconds": round(segment.start, 1),
        "text": segment.text,
    }

def fetch_video_metadata(url):
    """Fetch basic video metadata using yt-dlp."""
    try:
        from yt_dlp import YoutubeDL
        with YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title", ""),
                "channel": info.get("channel", ""),
                "views": info.get("view_count", 0),
                "duration": info.get("duration", 0),
                "description": info.get("description", ""),
                "url": url,
            }
    except Exception:
        return {"title": url, "channel": "Unknown", "url": url}

def sanitize_filename(text, max_len=50):
    """Convert text to safe filename."""
    keep = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_ ")
    text = "".join(c if c in keep else "_" for c in text)
    text = "_".join(text.split())[:max_len]
    return text or "untitled"

def fetch_all(urls, output_dir="Knowledge/Sources"):
    """Fetch transcripts for all URLs, save to Obsidian format."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    results = []
    for i, url in enumerate(urls, 1):
        vid = extract_video_id(url)
        if not vid:
            print(f"[{i}/{len(urls)}] ⚠️  Could not extract ID from: {url}")
            continue

        print(f"[{i}/{len(urls)}] Fetching: {vid} ...", end=" ", flush=True)

        meta = fetch_video_metadata(url)
        segments, lang, is_auto = fetch_transcript(vid)

        if not segments:
            print("⚠️  No transcript available")
            continue

        # Build Obsidian source file
        safe_title = sanitize_filename(meta["title"])
        source_file = output_path / f"Source-{safe_title}.md"

        # Format timestamps for citation
        citations = [format_citation(s) for s in segments]

        # Build full text for analysis
        full_text = " ".join(s.text for s in segments)
        duration_mins = int(meta["duration"] // 60) if meta.get("duration") else 0

        content_lines = [
            f"# {meta['title']}",
            "",
            f"> **Channel:** {meta['channel']}",
            f"> **Views:** {meta.get('views', 'N/A')}",
            f"> **Duration:** {duration_mins} minutes",
            f"> **Language:** {lang}{' (auto-generated)' if is_auto else ''}",
            f"> **Source:** [{url}]({url})",
            f"> **Video ID:** `{vid}`",
            "",
            "## Transcript",
            "",
            format_transcript(segments),
            "",
            "## Analysis Notes",
            "",
            "*(Add your notes here)*",
            "",
            f"**Tags:** #source #youtube #research",
            "",
            f"<!-- video_id: {vid} -->",
        ]

        with open(source_file, "w", encoding="utf-8") as f:
            f.write("\n".join(content_lines))

        print(f"✅ Saved to: {source_file.name}")

        results.append({
            "url": url,
            "vid": vid,
            "title": meta["title"],
            "channel": meta["channel"],
            "segments": len(segments),
            "duration_mins": duration_mins,
            "file": str(source_file),
            "auto_generated": is_auto,
        })

    # Save metadata as JSON for downstream processing
    meta_file = output_path / "_sources_meta.json"
    with open(meta_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*50}")
    print(f"✅ Fetched {len(results)}/{len(urls)} transcripts")
    print(f"   Saved to: {output_path}/")
    print(f"   Metadata: {meta_file.name}")

    return results

def main():
    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts")
    parser.add_argument("file", nargs="?", help="File with URLs (one per line)")
    parser.add_argument("--url", dest="single_url", help="Single URL")
    parser.add_argument("--output", default="Knowledge/Sources", help="Output directory")
    args = parser.parse_args()

    urls = []

    if args.single_url:
        urls = [args.single_url]
    elif args.file:
        path = Path(args.file)
        if path.exists():
            urls = [line.strip() for line in path.read_text().splitlines() if line.strip()]
        else:
            print(f"File not found: {args.file}")
            sys.exit(1)
    else:
        # Read from default selected_urls.txt
        default = Path("selected_urls.txt")
        if default.exists():
            urls = [line.strip() for line in default.read_text().splitlines() if line.strip()]
        else:
            print("No URL source provided and selected_urls.txt not found.")
            sys.exit(1)

    if not urls:
        print("No URLs to process.")
        sys.exit(0)

    fetch_all(urls, args.output)

if __name__ == "__main__":
    main()
