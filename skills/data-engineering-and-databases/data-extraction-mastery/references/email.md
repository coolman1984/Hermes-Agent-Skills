# Email Extraction

Use Python `email` package for `.eml`: headers, plain/html body, MIME charsets, base64/quoted-printable, attachments. Use `extract-msg` for Outlook `.msg`. Use `readpst`/libpst for PST/OST archives, exporting messages to eml then recursing.

Source: https://docs.python.org/3/library/email.parser.html ; extract-msg project docs.

Always recurse attachments through `detect_and_route.py`. Save body, headers, attachment manifest, and extracted attachment outputs.

When to use: email evidence and attachments. When it fails: proprietary MSG/PST without tools, encrypted attachments. Watch: charset and nested attachments.

Usage image: detect, preserve structure, validate, and only then normalize/load.
