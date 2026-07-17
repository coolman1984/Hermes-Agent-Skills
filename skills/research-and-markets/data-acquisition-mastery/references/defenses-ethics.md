# Defenses, Ethics, and Stop Signals

Legality and ethics are part of engineering quality. Check robots.txt, terms, license, copyright, privacy, and rate limits. CAPTCHA, aggressive 403, login walls, and explicit no-automation terms are stop signals.

Use a truthful User-Agent, throttle, cache, and never hammer. Do not bypass access controls or collect personal data unlawfully.

Source: Python robotparser https://docs.python.org/3/library/urllib.robotparser.html

When to use: before every collection. When it fails: source forbids access; stop and ask for authorized export/API.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
