---
name: camoufox-article-browsing
description: Use Camoufox to open URLs, extract readable article content, and summarize
  it in constrained Linux aarch64 / PRoot environments.
tags: [camoufox, browsing, article, summarization, extraction]
---

# Camoufox Article Browsing

Use this skill when a user gives a URL and wants the page read, summarized, or analyzed, especially when the environment should prefer Camoufox over generic web extraction.

## Goal
Get the readable article text from the page, then summarize the main argument, evidence, and conclusion clearly.

## Workflow

1. Check whether Camoufox is available.
   - If the Python package or browser binary is missing, follow `camoufox-proot-setup` first.
   - If Camoufox is unavailable and the environment also lacks Playwright, fall back immediately to `web_extract` for a quick readable version, then use `terminal` with `requests` + `BeautifulSoup` to fetch the canonical article URL and parse the `<article>` body.
   - In constrained Linux aarch64 / PRoot environments, install into an isolated venv and expect the browser fetch to take a while.
   - If the fetch is long-running, run it in the background and poll until completion instead of retrying randomly in the foreground.

2. Verify the browser actually works before touching the target article.
   - Run a tiny headless smoke test against `https://example.com`.
   - Confirm title and URL load successfully.
   - This catches broken installs early and saves time on article debugging.

3. Open the target page headlessly.
   - Prefer `Camoufox(headless=True)`.
   - Load the page with `wait_until='domcontentloaded'` and give dynamic pages a short settle time.
   - Substack share URLs may redirect to a canonical article URL with `triedRedirect=true`; follow the redirect and treat the canonical page as the source of truth.

4. Extract the article content.
   - Prefer the main article container if it exists.
   - For typical pages, look at `article`, `main`, or the largest readable text block.
   - If those are thin or absent, fall back to `body` and then strip navigation/footer/share clutter.
   - On Substack pages, prefer the post body and paragraph text over share wrappers, comments, or splash pages.
   - Save the extracted text to a file when the page is long so you can inspect and summarize it in chunks.

5. If the user wants durable recall, prefer the local helper `camoubrain` when it is installed.
   - It should browse the URL with Camoufox, capture the page into `captures/<timestamp>-<slug>/page.md`, and import only that directory into GBrain.
   - Never import from a shared inbox of markdown files; that can re-import stale pages on later runs.
   - The page file should include frontmatter with source and canonical URLs.
   - After capture/import, verify with `gbrain stats` and a targeted `gbrain search`.
   - If `camoubrain` is unavailable, do the same pattern manually with a per-page directory and `gbrain import <that-directory> --no-embed` from the brain root.

6. Capture a few metadata fields if available.
   - Title
   - Author
   - Publish date
   - Canonical URL
   - OpenGraph title/description

7. Summarize in the user’s language unless they request otherwise.
   - Start with the thesis.
   - Then explain the supporting points.
   - Then add any nuance, caveats, or surprising claims.
   - If the page is opinion-heavy, make the author’s claim structure explicit instead of flattening it into a neutral news summary.

## Suggested extraction pattern

```python
from camoufox.sync_api import Camoufox

with Camoufox(headless=True) as browser:
    page = browser.new_page()
    page.goto(url, wait_until='domcontentloaded', timeout=30000)
    title = page.title()
    text = page.locator('article').inner_text(timeout=5000) if page.locator('article').count() else page.locator('main').inner_text(timeout=5000)
```

If the page uses a different layout, fall back to `page.content()` and parse the HTML for the largest readable section.

## Common pitfalls

- Some sites return share/redirect pages first; follow through to the real article URL.
- Large pages can take a moment to render; wait briefly after DOMContentLoaded.
- If the content is hidden behind a login wall, note that clearly instead of pretending the article was readable.
- X/Twitter articles commonly redirect Camoufox to `https://x.com/i/flow/login?...` when unauthenticated. This proves a login-wall; it does not mean the article was extracted. Capture title, final URL, and body length, then continue with X mirrors, `r.jina.ai`, indexed search, media OCR/vision, or authenticated cookies if available.
- Avoid repeated fresh X logins from a new Camoufox/VNC profile. In field testing, X showed `Suspicious login prevented` for a new Camoufox VNC session. Stop immediately, do not retry, and prefer an already-authorized browser/session such as the user's normal Android browser, controlled visually via ADB if the user permits. Never ask the user to send the X password.
- `camoubrain --no-import <url>` is useful to preserve evidence of the Camoufox result, but verify the captured Markdown is not just login/signup chrome before importing or summarizing.
- On Substack, the share URL can be less useful than the canonical article URL.
- If `web_extract` fails on a Substack note/share URL (for example with an HTTP 432), try Camoufox immediately; if Camoufox is still noisy, use a direct `requests.get()` on the page HTML and parse the embedded JSON-LD / OpenGraph metadata. Substack notes often expose the full text in `application/ld+json` as `SocialMediaPosting.text`, plus `dateCreated`, author name, and the canonical note URL even when the browser/extractor path is noisy.

## Verification

Before summarizing, confirm:
- the page loaded successfully
- the title matches the expected article
- the body text contains the article, not just navigation
- the extracted text has enough substantive paragraphs to summarize

## When to use

Use this for:
- article summaries
- blog post analysis
- Substack reads
- URL-based research where you want browser-backed extraction rather than generic search snippets
