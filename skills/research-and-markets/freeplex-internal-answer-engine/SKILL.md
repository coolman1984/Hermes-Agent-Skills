---
name: freeplex-internal-answer-engine
description: Design and build Mohamed's free internal Perplexity-like answer engine using no/low-cost search, page reading, source ranking, citations, Obsidian/local memory, and Camoufox fallbacks.
---

# Freeplex Internal Answer Engine

Use this skill when Mohamed asks to build, improve, or use a free Perplexity-like research system for the assistant, or when designing an internal answer engine that combines web search, page extraction, source ranking, citations, and local memory.

## Objective

Build an internal `Search + Read + Rank + Synthesize + Cite` pipeline that is free where possible and better suited to Mohamed than Perplexity because it can use:

- The live web.
- Obsidian vault context.
- Local LLM Wiki / saved notes.
- Mohamed-specific source preferences.
- Camoufox immediately when links are blocked or difficult.

## Default architecture

1. **Query understanding**
   - Classify the question: quick fact, current news, deep research, code, academic, finance, X/Twitter, YouTube, or local-vault lookup.
   - Generate 3-8 search queries for non-trivial topics.

2. **Free search layer**
   Prefer no-key/free sources first:
   - SearXNG if available or self-hostable.
   - Jina Search: `https://s.jina.ai/<encoded query>`.
   - DuckDuckGo HTML fallback parsed locally.
   - Built-in `web_search` only when appropriate.
   - GitHub search / raw GitHub files for projects and code.
   - arXiv for papers.
   - X/Twitter mirrors and existing X workflow for X links.

3. **Reading/extraction layer**
   Try in this order unless the source type requires otherwise:
   - Jina Reader: prefix URL with `https://r.jina.ai/`.
   - Built-in `web_extract`.
   - Direct requests + BeautifulSoup/readability/trafilatura if installed.
   - Crawl4AI for dynamic or multi-page extraction when installed.
   - Camoufox immediately for blocked, JS-heavy, Cloudflare, X/Substack, or otherwise difficult pages; verify the captured content is not just a login wall.

4. **Source scoring**
   Score higher for:
   - Official/primary sources.
   - Recent publication date when freshness matters.
   - Original data, filings, docs, or direct quotes.
   - Clear author/date and source reputation.
   - Consistency with multiple independent sources.

   Score lower for:
   - SEO summaries, clickbait, scraped duplicates.
   - No date/author for time-sensitive claims.
   - Thin pages, paywalls, missing content, or marketing copy.
   - Sources that cite others without adding primary evidence.

5. **Synthesis**
   - Answer only from retrieved evidence.
   - Cite sources for important claims.
   - Separate confirmed facts, uncertainty, and judgment.
   - Mention conflicts between sources instead of hiding them.
   - For Mohamed, prefer Arabic output unless CLI mode requires English.

6. **Persistence**
   - Save reusable outputs as Markdown under `Downloads/research-notes/` or the Obsidian vault when appropriate.
   - For important domains, ingest durable notes into the local LLM Wiki / vault rather than leaving them as temporary chat context.

## Recommended implementation phases

### v0.1: lightweight script
Create a script such as `~/.hermes/scripts/freeplex.py` that:

1. Accepts a question and optional mode.
2. Searches Jina Search + DuckDuckGo HTML + available Hermes search.
3. Reads top URLs via Jina Reader/web_extract.
4. Deduplicates and ranks sources with simple heuristics.
5. Emits:
   - JSON evidence bundle.
   - Markdown report with citations.

### v0.2: specialized modes
Add modes:

- `web`
- `news`
- `github`
- `academic`
- `egypt-stocks`
- `x`
- `youtube`
- `obsidian`
- `deep`

### v0.3: local memory/RAG
Add local retrieval over:

- `/root/Documents/Obsidian Vault`
- Existing media notes in Downloads.
- EGX system notes.
- Local LLM Wiki pages.

Use SQLite FTS as the first lightweight option before heavier vector databases. Consider ChromaDB or embeddings later only if the lexical approach is insufficient.

### v0.4: UI/API
Expose as:

- CLI command: `freeplex "query" --mode deep`.
- Hermes script callable from future cron jobs or skills.
- Optional local web UI only after CLI is stable.

## Tool/project evaluation notes

- **Perplexica** is the closest open-source Perplexity alternative and uses SearXNG/Ollama, but it is heavier and Docker-oriented. Use it as architecture inspiration before adopting it wholesale in PRoot/Android.
- **SearXNG** is the best open/free search backbone when JSON is enabled, but local non-Docker setup may take effort.
- **Jina Reader/Search** is the fastest v0.1 path: no install, LLM-friendly Markdown/search, but can rate-limit and is external.
- **Crawl4AI** is a strong local page reader/crawler for later phases, especially dynamic pages, but requires dependency setup.
- **GPT Researcher** is useful as a deep-research reference but is heavier and commonly expects API keys/providers.

## Mohamed-specific rules

- For important tasks, read `/root/Documents/Obsidian Vault/CURRENT-SNAPSHOT.md` first.
- For blocked/difficult content, use Camoufox immediately as the first fallback and verify the page is real content, not login/signup chrome.
- Prefer official sources first for finance/EGX work.
- Prefer Markdown files with sources over long chat-only responses when the research is substantial.
- Avoid paid APIs unless Mohamed explicitly approves them.
- Do not ask Mohamed for credentials; use existing sessions or safe visual-control workflows when authentication is needed.

## Verification checklist

Before reporting completion:

- Search results came from at least two routes for non-trivial topics, or explain why one authoritative route was enough.
- Important sources were opened/read, not only snippets.
- Claims are tied to source URLs.
- Blocked pages were either recovered via Camoufox/fallback or clearly labeled as inaccessible.
- Output file exists and is non-empty if a file was promised.
- No API keys, cookies, passwords, pairing codes, or private connection strings are exposed.
