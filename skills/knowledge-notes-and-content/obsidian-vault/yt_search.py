#!/usr/bin/env python3
"""
yt_search.py — Search YouTube from terminal, pick videos for research pipeline.
Usage: python3 yt_search.py "search query" [--limit 20]
"""
import sys
import argparse
import scrapetube
from pathlib import Path

def search_youtube(query, limit=20):
    """Search YouTube and return list of (video_id, title, channel, views, duration)."""
    videos = []
    results = scrapetube.get_search(query, limit=limit)
    for v in results:
        try:
            vid = v.get("videoId", "N/A")
            title_runs = v.get("title", {}).get("runs", [{}])
            title = title_runs[0].get("text", "N/A") if title_runs else "N/A"
            channel = (v.get("longBylineText", {})
                       .get("runs", [{}])
                       .get("0", {})
                       .get("text", "N/A"))
            # views
            view_text = (v.get("viewCountText", {})
                        .get("simpleText", "N/A"))
            # published
            pub = (v.get("publishedTimeText", {})
                   .get("simpleText", ""))
            # thumbnail
            thumbs = v.get("thumbnail", {}).get("thumbnails", [{}])
            thumb = thumbs[0].get("url", "") if thumbs else ""

            videos.append({
                "id": vid,
                "title": title,
                "channel": channel,
                "views": view_text,
                "published": pub,
                "url": f"https://youtube.com/watch?v={vid}",
                "thumb": thumb,
            })
        except Exception:
            continue
    return videos

def print_results(videos):
    """Display numbered list of videos."""
    print(f"\n{'='*70}")
    print(f"  Found {len(videos)} results")
    print(f"{'='*70}\n")
    for i, v in enumerate(videos, 1):
        print(f"  [{i:02d}] {v['title'][:60]}")
        print(f"       {v['channel']} | {v['views']} | {v['published']}")
        print(f"       {v['url']}")
        print()

def pick_videos(videos):
    """Ask user to pick video numbers, return selected dicts."""
    picks = input("Pick video numbers (e.g. 1,3,5 or 1-5): ").strip()
    selected = []
    try:
        parts = picks.replace("-", ",").split(",")
        for part in parts:
            part = part.strip()
            if not part:
                continue
            idx = int(part) - 1
            if 0 <= idx < len(videos):
                selected.append(videos[idx])
    except ValueError:
        print("Invalid selection.")
    return selected

def save_selected(videos, path="selected_urls.txt"):
    """Save selected video URLs to a file."""
    with open(path, "w") as f:
        for v in videos:
            f.write(f"{v['url']}\n")
    return path

def main():
    parser = argparse.ArgumentParser(description="Search YouTube and pick videos")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("--limit", type=int, default=20, help="Number of results")
    parser.add_argument("--save", default="selected_urls.txt", help="Output file")
    args = parser.parse_args()

    if not args.query:
        print("Usage: python3 yt_search.py 'search query' [--limit 20]")
        sys.exit(1)

    print(f"Searching YouTube for: {args.query} ...")
    videos = search_youtube(args.query, args.limit)

    if not videos:
        print("No results found.")
        sys.exit(1)

    print_results(videos)
    selected = pick_videos(videos)

    if not selected:
        print("No videos selected.")
        sys.exit(0)

    out_path = save_selected(selected, args.save)
    print(f"\n✅ Saved {len(selected)} URLs to: {out_path}")

    # Also print as list for OpenClaw to parse
    print(f"\n📋 Selected URLs:")
    for v in selected:
        print(f"  {v['url']}")

if __name__ == "__main__":
    main()
