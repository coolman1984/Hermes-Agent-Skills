# Dynamic Sites

Inspect network/XHR first. If JSON endpoint is public/authorized, collect it directly. Use Playwright for rendering, waiting, scrolling, and response interception only when needed. Infinite scroll needs item-ID dedup and polite pacing.

Source: Playwright Python https://playwright.dev/python/docs/intro

When to use: JS-rendered public data. When it fails: login wall, CAPTCHA, explicit no-automation terms.

Usage image: choose authorized source, collect raw, manifest it, then hand off.
