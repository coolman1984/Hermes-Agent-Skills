# YouTube autosub 429 + long Arabic note pattern

Use this when Mohamed sends a YouTube link and Arabic auto subtitles fail or are rate-limited, but English original/generated captions are available.

## Durable lesson

Do not fail the media-drop workflow just because the Arabic auto-caption download returns an HTTP 429. If `en-orig` or English generated captions are available, proceed from English and produce the required Arabic unified note.

## Practical extraction sequence

1. Dump metadata to a temp JSON file, not terminal stdout:

```bash
yt-dlp --dump-single-json --skip-download --no-warnings "$URL" > /tmp/youtube_$VID/full.json
```

2. Inspect subtitle languages from the JSON.

3. Try subtitles in this order:

```bash
yt-dlp --skip-download --write-auto-subs --sub-langs 'en.*,ar.*' --convert-subs vtt -o '%(id)s.%(ext)s' "$URL"
```

4. If Arabic subtitles hit `HTTP Error 429` but `*.en-orig.vtt` or `*.en.vtt` exists, continue from English. Clearly record source as English auto/original transcript translated into Arabic presentation.

5. Clean VTT by removing timestamps, tags, repeated growing caption fragments, and duplicate adjacent lines. Save both:

- `transcript_clean.txt`
- `transcript_paragraphs.txt`

6. For long transcripts, delegate two separate readings when useful:

- faithful Arabic synthesis in the mandatory media-note sections
- business-intelligence extraction for Mohamed's idea vault

7. Write the final unified note under Downloads, then create/update the idea-vault bridge only if there is a real business/product/workflow signal.

8. Run the media verifier with positional args only:

```bash
python scripts/verify_media_note.py <media-note.md> [idea-note.md] [source-map.md]
```

## Pitfall

Avoid treating translated Arabic captions as mandatory if an English source transcript is available. The mandatory requirement is a transcript-backed note; Arabic output can be produced from English captions when Arabic captions are missing or rate-limited.
