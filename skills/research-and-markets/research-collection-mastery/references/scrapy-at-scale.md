# Scrapy at Scale

Distributed crawling concepts: frontier/queue, request fingerprint dedup, item pipelines, downloader middlewares, autothrottle, robots obedience, depth/host limits, checkpointing, and kill switches.

Source: Scrapy docs https://docs.scrapy.org/

When to use: large structured crawls with many pages. When it fails: small one-off tasks, sites forbidding crawling, data better served by API.

Usage image: choose authorized source, collect raw, manifest it, then hand off.
