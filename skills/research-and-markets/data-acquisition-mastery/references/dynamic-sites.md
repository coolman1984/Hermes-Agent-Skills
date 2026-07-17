# Dynamic and Browser-Based Sites

Senior habit: inspect Network/XHR first. Most dynamic pages fetch JSON. Use browser automation only when authorized and when no clean endpoint exists. Playwright can render JS, wait for selectors, scroll, and intercept responses.

Source: Playwright Python docs https://playwright.dev/python/docs/intro

Workflow: open page → capture XHR URLs → call API directly if permitted → otherwise Playwright with slow pacing and minimal actions.

When to use: JS-rendered public data. When it fails: login/paywall/CAPTCHA/terms forbid automation. Watch: infinite scroll and duplicate item IDs.

Usage image: acquire only what is authorized, save raw + manifest, then hand off to extraction.
