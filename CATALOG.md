# Skills Catalog

Generated: `2026-07-17T10:56:14Z`  
Total skills: **214**  
Domains: **13**

## Domains at a glance

| # | Domain | Count | Purpose |
|---:|---|---:|---|
| 1 | [Core Reasoning & Execution](skills/core-reasoning-and-execution/) | 21 | How the agent thinks, plans, verifies, and delivers under pressure. |
| 2 | [Agent Orchestration & Hermes OS](skills/agent-orchestration/) | 22 | Multi-agent loops, Hermes configuration, profiles, workers, and handoffs. |
| 3 | [Software Engineering](skills/software-engineering/) | 25 | Architecture, coding standards, testing, debugging, review, and platform builds. |
| 4 | [Data Engineering & Databases](skills/data-engineering-and-databases/) | 5 | Extraction, ETL, SQL, file resilience, and data pipelines. |
| 5 | [Research, Markets & Intelligence](skills/research-and-markets/) | 27 | Web/academic research, market workflows, credibility checks, and answer engines. |
| 6 | [Knowledge, Notes & Content Systems](skills/knowledge-notes-and-content/) | 21 | Vaults, media ingestion, Arabic content, books, and second-brain systems. |
| 7 | [Creative, Design & Video](skills/creative-and-video/) | 32 | HyperFrames, motion, design systems, diagrams, generative art, and music. |
| 8 | [MLOps, Training & Model Ops](skills/mlops-and-models/) | 22 | Fine-tuning, inference, evaluation, multimodal models, and experiment tracking. |
| 9 | [Productivity & Office Automation](skills/productivity-and-office/) | 10 | Docs, decks, sheets ecosystems, meetings, and productivity CLIs. |
| 10 | [Media & Social Platforms](skills/media-and-social/) | 9 | YouTube, Spotify, GIFs, X/Twitter tools and content retrieval. |
| 11 | [Device, Platform & DevOps](skills/device-platform-and-devops/) | 15 | Android/Termux control, computer use, cleanup, webhooks, and environment ops. |
| 12 | [Integrations: GitHub & MCP](skills/integrations-github-mcp/) | 3 | Repository workflows and Model Context Protocol tooling. |
| 13 | [Security, Vetting & Red Team](skills/security-and-skill-safety/) | 2 | Skill security review and red-team research tooling. Handle carefully. |

## 1. Core Reasoning & Execution

How the agent thinks, plans, verifies, and delivers under pressure.

- **[architect](skills/core-reasoning-and-execution/architect/)** — Planning, system design, architecture decisions, tradeoff analysis, and implementation breakdowns for OpenClaw work. Use when defining scope, choosing a structure, asking the right clarifying questions, or turning a complex request into a concrete design plan.
- **[builder](skills/core-reasoning-and-execution/builder/)** — Execution specialist for implementation work. Use for coding, setup steps, configurations, scripts, technical fixes, and concrete build plans. Produces working output, flags risks clearly, and returns concise implementation packages.
- **[capability-first](skills/core-reasoning-and-execution/capability-first/)** — Silent pre-task routing for OpenClaw. Use when deciding how to handle any request by checking existing skills, tools, reusable workflows, or delegated execution before doing fresh reasoning. This skill prevents duplicated work, wasted tokens, and rebuilding known workflows from scratch.
- **[context-mode-routing](skills/core-reasoning-and-execution/context-mode-routing/)** — Route large file reads, verbose command output, web fetches, logs, and browser snapshots through Context Mode sandbox tools to reduce context bloat. Use when outputs may exceed a few hundred tokens or when you need index/search/fetch-first behavior instead of raw dumps.
- **[developer](skills/core-reasoning-and-execution/developer/)** — Production code implementation, refactoring, feature work, script writing, and technical fixes for OpenClaw tasks. Use when the job is to build the code or configuration after the design is known, or when a concrete working implementation is needed.
- **[mohamed-personality-operating-model](skills/core-reasoning-and-execution/mohamed-personality-operating-model/)** — Use in every meaningful interaction with Mohamed to infer durable preferences, decision patterns, style expectations, recurring priorities, and response-shaping signals from his messages, then update the right memory layer without overreaching or psychologizing.
- **[orchestration-ceo](skills/core-reasoning-and-execution/orchestration-ceo/)** — Top-level orchestration for Mohamed’s AI system. Use when a request needs strategy, multi-step planning, delegation to sub-agents or tools, review/testing, long-running task control, heartbeat follow-up, or building reusable operating procedures and automation.
- **[permissions](skills/core-reasoning-and-execution/permissions/)** — 
- **[plan](skills/core-reasoning-and-execution/plan/)** — Plan mode: write an actionable markdown plan to .hermes/plans/, no execution. Bite-sized tasks, exact paths, complete code.
- **[planning-forecasting-mastery](skills/core-reasoning-and-execution/planning-forecasting-mastery/)** — Use at the start of any multi-step effort, roadmap, project, build, migration, research plan, investment workflow, automation rollout, estimate, forecast, risk review, prioritization, or execution sequence. Pairs with reasoning-mastery: reasoning frames the problem; this skill turns goals into adaptable plans with estimates, risks, checkpoints, and learning loops.
- **[planning-mastery](skills/core-reasoning-and-execution/planning-mastery/)** — Use whenever the user wants to plan, scope, roadmap, schedule, estimate, set goals, forecast risks, or decide priorities for anything multi-step — a project, a build, a launch, a proposal, a phased initiative. Also triggers on what could go wrong, how long will this take, what should we do first, break this into phases. Pairs with reasoning-mastery.
- **[prototype-client-readiness-polish](skills/core-reasoning-and-execution/prototype-client-readiness-polish/)** — Turn a working prototype into a presentable pilot-ready product for a friendly client demo.
- **[reasoning-mastery](skills/core-reasoning-and-execution/reasoning-mastery/)** — Consult at the start of ANY non-trivial task, before choosing tools: any problem that is hard, ambiguous, open-ended, novel, stuck, risky, multi-step, or where the user asks you to figure out, solve, think through, find a way, diagnose, decide, or get to the bottom of something. Governs how every other skill is applied.
- **[researcher](skills/core-reasoning-and-execution/researcher/)** — Evidence-oriented research specialist for gathering, comparing, analyzing, and synthesizing facts for decision-making. Use when the task is research, option comparison, tradeoff analysis, uncertainty handling, or decision support.
- **[reviewer-qa](skills/core-reasoning-and-execution/reviewer-qa/)** — Strict review and QA for OpenClaw outputs, code, configs, scripts, skill files, and AI-generated responses. Use when checking correctness, logic gaps, missing pieces, ambiguity, safety, or approval readiness before anything is accepted or merged.
- **[skill-forge](skills/core-reasoning-and-execution/skill-forge/)** — Use when the user says learn a new field, become expert in, make a skill for, improve your skill, run the mastery protocol on a field, create a reusable skill package, validate a skill, or upgrade an existing skill after a real task.
- **[spike](skills/core-reasoning-and-execution/spike/)** — Throwaway experiments to validate an idea before build.
- **[standing-execution-protocol](skills/core-reasoning-and-execution/standing-execution-protocol/)** — Use when handling any meaningful task for Mohamed. Enforces intent framing, load-bearing evidence, explicit uncertainty, adversarial verification, and a usable first-line answer.
- **[task-tracker](skills/core-reasoning-and-execution/task-tracker/)** — Track task outcomes for self-optimizing agent recommendations
- **[task-watch](skills/core-reasoning-and-execution/task-watch/)** — Pending-work monitoring and completion follow-up for long-running tasks, sub-agents, reviews, tests, and background jobs. Use when you need recurring status checks, 2-minute wakeups, completion notifications, blocker tracking, or a clean handoff from waiting to done.
- **[writing-plans](skills/core-reasoning-and-execution/writing-plans/)** — Write implementation plans: bite-sized tasks, paths, code.

## 2. Agent Orchestration & Hermes OS

Multi-agent loops, Hermes configuration, profiles, workers, and handoffs.

- **[agentic-workflows-do-framework](skills/agent-orchestration/agentic-workflows-do-framework/)** — Build production AI workflows using Directive-Orchestration-Execution pattern — separates probabilistic reasoning from deterministic execution.
- **[ai-coding-cli-delegation](skills/agent-orchestration/ai-coding-cli-delegation/)** — Use when delegating coding or review work to external AI coding CLIs such as Claude Code, Codex, OpenCode, or Gemini while Hermes coordinates scope, verification, and handoff.
- **[ai-handoff-control-layer](skills/agent-orchestration/ai-handoff-control-layer/)** — Build a robust handoff/control layer for future AI agents using a document-driven operating contract, machine-readable manifest, and validation script instead of brittle Python-only automation.
- **[debugging-hermes-tui-commands](skills/agent-orchestration/debugging-hermes-tui-commands/)** — Debug Hermes TUI slash commands: Python, gateway, Ink UI.
- **[gemini-cli](skills/agent-orchestration/gemini-cli/)** — Delegate coding and research tasks to Google Gemini CLI, including install, auth, no-prompt automation, MCP, skills, and verification.
- **[generic-agent-setup](skills/agent-orchestration/generic-agent-setup/)** — Bootstrap and run GenericAgent (self-evolving autonomous agent) in Linux aarch64 PRoot/Android environments. Includes dependency triage, API config, and common pitfalls.
- **[hermes-agent](skills/agent-orchestration/hermes-agent/)** — Complete guide to using and extending Hermes Agent — CLI usage, setup, configuration, spawning additional agents, gateway platforms, skills, voice, tools, profiles, and a concise contributor reference. Load this skill when helping users configure Hermes, troubleshoot issues, spawn agent instances, or make code contributions.
- **[hermes-agent-skill-authoring](skills/agent-orchestration/hermes-agent-skill-authoring/)** — Author in-repo SKILL.md: frontmatter, validator, structure.
- **[hermes-gateway-telegram-stuck](skills/agent-orchestration/hermes-gateway-telegram-stuck/)** — Fix and auto-detect Telegram gateway stuck in typing loop - restart the gateway process when stuck
- **[hermes-honcho-manager-dispatch-fix](skills/agent-orchestration/hermes-honcho-manager-dispatch-fix/)** — Fix Hermes/OpenClaw tool outages caused by `handle_function_call() got an unexpected keyword argument 'honcho_manager'` via backward-compatible dispatcher signature patch and restart verification.
- **[hermes-kanban-workflows](skills/agent-orchestration/hermes-kanban-workflows/)** — Use when operating Hermes Kanban as an orchestrator or worker: decomposing work, enforcing worker lifecycle, avoiding orchestration temptations, and verifying task handoffs.
- **[hermes-openclaw-wrapper-fixes](skills/agent-orchestration/hermes-openclaw-wrapper-fixes/)** — Troubleshoot Hermes wrappers that sit behind an OpenClaw gateway, fix pairing/token issues, and verify the wrapper actually talks to the gateway.
- **[hermes-profile-bootstrap](skills/agent-orchestration/hermes-profile-bootstrap/)** — Bootstrap, clone, and harden Hermes profiles for a production/experiment pair with safe config, interactive setup handling, and verification. Use when creating a new Hermes profile, cloning it into a lab profile, or wiring profile-specific SOUL/config defaults.
- **[hermes-s6-container-supervision](skills/agent-orchestration/hermes-s6-container-supervision/)** — Modify, debug, or extend the s6-overlay supervision tree inside the Hermes Agent Docker image — adding new services, debugging profile gateways, understanding the Architecture B main-program pattern.
- **[kanban-codex-lane](skills/agent-orchestration/kanban-codex-lane/)** — Use when a Hermes Kanban worker wants to run Codex CLI as an isolated implementation lane while Hermes keeps ownership of task lifecycle, reconciliation, testing, and handoff.
- **[mohamed-agent-loop-os](skills/agent-orchestration/mohamed-agent-loop-os/)** — Use when Mohamed wants a serious multi-agent workflow, a long-running coding/research loop, background workers, factory-style processing, or any task that must survive beyond one clever prompt. Turns the task into a durable planner-generator-evaluator operating loop with file-backed state, explicit success contracts, restart tolerance, and profile-based execution.
- **[mohamed-claude-codex-control-bridge](skills/agent-orchestration/mohamed-claude-codex-control-bridge/)** — Use when Mohamed asks Hermes to control, audit, learn from, or bridge Claude Code, Codex CLI, OpenCode CLI, and Gemini CLI, including reading their skills/memories, delegating tasks, importing useful skill workflows into Hermes, or maintaining a local multi-agent control layer on this Android/PRoot machine.
- **[mohamed-coding-team](skills/agent-orchestration/mohamed-coding-team/)** — Use when Mohamed asks for coding work, architecture, implementation, debugging, code review, or a multi-agent coding workflow. Defines Mohamed's permanent coding-team hierarchy across Claude Code, Codex CLI, OpenCode, Gemini CLI, and Hermes.
- **[mohamed-opencode-go-worker-profiles](skills/agent-orchestration/mohamed-opencode-go-worker-profiles/)** — Use when Mohamed wants Hermes to run background worker profiles on OpenCode Go models, choose the right model for a task, refresh model choices, or improve the multi-model worker setup.
- **[persistent-memory-project-governance](skills/agent-orchestration/persistent-memory-project-governance/)** — Use when Mohamed wants a file-based project operating system for multi-step work, data projects, reports, software builds, factory workflows, or restartable autonomous execution. Preserves mission, scope, decisions, assumptions, risks, evidence, validation, memory, and handover in project files without polluting global memory.
- **[subagent-driven-development](skills/agent-orchestration/subagent-driven-development/)** — Execute plans via delegate_task subagents (2-stage review).
- **[team-governed-coding-workflow](skills/agent-orchestration/team-governed-coding-workflow/)** — Use for Mohamed's serious coding/project work when execution must flow through a fixed team: Hermes plans/orchestrates/final-verifies, deepseek-fast writes only, deepseek-pro reviews only.

## 3. Software Engineering

Architecture, coding standards, testing, debugging, review, and platform builds.

- **[android-agent-bridge](skills/software-engineering/android-agent-bridge/)** — Build or extend an Android-native local bridge that lets Hermes operate Android capabilities from Linux/Termux via agent-first HTTP endpoints, Accessibility, notifications, and explicit one-time permission grants.
- **[arabic-pdf-weasyprint-pipeline](skills/software-engineering/arabic-pdf-weasyprint-pipeline/)** — Render professional Arabic/RTL PDFs from report data using HTML/CSS and WeasyPrint instead of ReportLab.
- **[arabic-software-localization](skills/software-engineering/arabic-software-localization/)** — Use when adding or fixing Arabic (RTL) support in a full-stack web application — i18n architecture, browser QA, PDF rendering, Excel RTL, and localization pitfalls. Covers the dual-layer dictionary+regex pattern from Company-Dashboard and ReportLab Arabic font/shaping mechanics.
- **[code-review](skills/software-engineering/code-review/)** — Guidelines for performing thorough code reviews with security and quality focus
- **[codebase-memory-workflow](skills/software-engineering/codebase-memory-workflow/)** — Use when working on any codebase with 20+ files — index the repo first, query the graph before reading files randomly, then act on targeted context. Reduces token waste and missed relationships in coding agent tasks.
- **[company-dashboard-arabic-lessons](skills/software-engineering/company-dashboard-arabic-lessons/)** — Proven approaches and pitfalls for Arabic-first dashboards and reports in Node/Python stacks.
- **[dogfood](skills/software-engineering/dogfood/)** — Exploratory QA of web apps: find bugs, evidence, reports.
- **[engineering-ai-automation](skills/software-engineering/engineering-ai-automation/)** — Use when engineering work involves LLMs, RAG, tool calling, agents, evals, scripts, cron, CI/CD. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[engineering-backend](skills/software-engineering/engineering-backend/)** — Use when engineering work involves APIs, FastAPI, auth, validation, pagination, queues, reliability. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[engineering-frontend](skills/software-engineering/engineering-frontend/)** — Use when engineering work involves React, components, accessibility, data fetching, responsive UI. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[engineering-hardware-support](skills/software-engineering/engineering-hardware-support/)** — Use when engineering work involves PC/server hardware, OS faults, boot, logs, recovery. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[engineering-mastery](skills/software-engineering/engineering-mastery/)** — Use for ANY coding, software, web, backend, frontend, UI/UX, design, IT/hardware, troubleshooting, networking, system architecture, AI/LLM, or automation task — from writing one function to designing a system or diagnosing why something will not connect. Routes to the right engineering sub-skill; consult reasoning-mastery first for framing.
- **[engineering-networking](skills/software-engineering/engineering-networking/)** — Use when engineering work involves DNS, TCP/IP, TLS, ports, proxies, VPN, nginx, diagnostics. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[engineering-software-foundations](skills/software-engineering/engineering-software-foundations/)** — Use when engineering work involves clean-code, testing, Git, debugging, refactoring, DSA. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[engineering-systems-architecture](skills/software-engineering/engineering-systems-architecture/)** — Use when engineering work involves requirements, components, data flow, trade-offs, ADRs, scalability. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[engineering-ui-ux-design](skills/software-engineering/engineering-ui-ux-design/)** — Use when engineering work involves hierarchy, spacing, typography, flows, accessibility, heuristics. Provides senior baselines, traps, validation patterns, and focused references for this domain.
- **[refactor-compatibility-recovery](skills/software-engineering/refactor-compatibility-recovery/)** — Recover from ImportError/AttributeError after refactors by tracing the removed public API through git history, then restoring a compatibility shim and verifying imports.
- **[requesting-code-review](skills/software-engineering/requesting-code-review/)** — Pre-commit review: security scan, quality gates, auto-fix.
- **[senior-software-engineer](skills/software-engineering/senior-software-engineer/)** — Use when Mohamed asks for coding, architecture, bug fixing, refactoring, code review, planning, CI, or production-readiness work. Enforces a senior software engineer operating mode: clarify only when necessary, preserve scope, build in small slices, verify with real commands, review security/performance, and avoid prototype-quality shortcuts.
- **[simplify-code](skills/software-engineering/simplify-code/)** — Parallel 3-agent cleanup of recent code changes.
- **[systematic-debugging](skills/software-engineering/systematic-debugging/)** — Use when encountering any bug, test failure, or unexpected behavior. 4-phase root cause investigation — NO fixes without understanding the problem first.
- **[termux-node-native-addon-triage](skills/software-engineering/termux-node-native-addon-triage/)** — Diagnose and handle Node.js native-addon install failures on Android/Termux/PRoot, especially node-gyp errors, better-sqlite3, and android_ndk_path issues. Use when deciding whether to force a prebuilt binary path, patch environment variables, or move the workload into a real Linux userland.
- **[termux-open-source-tool-triage](skills/software-engineering/termux-open-source-tool-triage/)** — Rapidly evaluate multiple open-source AI/tool repos on Android Termux, detect platform blockers early, and produce an execution plan (run now vs move to Linux x86_64).
- **[test-driven-development](skills/software-engineering/test-driven-development/)** — TDD: enforce RED-GREEN-REFACTOR, tests before code.
- **[uv-install-triage](skills/software-engineering/uv-install-triage/)** — Triage uv sync / uv pip install failures caused by editable installs, namespace packages, or broken build environments. Use when uv installs succeed partially, packages import as namespace packages, or hatchling/pluggy/build-backend errors appear.

## 4. Data Engineering & Databases

Extraction, ETL, SQL, file resilience, and data pipelines.

- **[data-extraction-mastery](skills/data-engineering-and-databases/data-extraction-mastery/)** — Use whenever the user mentions extracting, reading, parsing, or pulling data from any PDF, Word, Excel (xlsx/xlsm/xlsb/xls), CSV, email (eml/msg/pst/Outlook), web page, or any file — even if they just say get the data out of this or read this file. Also triggers on OCR, scanned documents, Arabic text extraction, attachments, batch file ingestion, and landing extracted data into a database.
- **[database-mastery](skills/data-engineering-and-databases/database-mastery/)** — Use whenever the user mentions databases, SQL, queries, DuckDB, Postgres, SQLite, data cleaning, ETL, pipelines, variance analysis, dashboards, APIs over data, Excel/CSV ingestion, reporting, or wants data extracted, calculated, modeled, validated, or presented — even if they do not say database.
- **[jupyter-live-kernel](skills/data-engineering-and-databases/jupyter-live-kernel/)** — Iterative Python via live Jupyter kernel (hamelnb).
- **[ocr-and-documents](skills/data-engineering-and-databases/ocr-and-documents/)** — Extract text from PDFs/scans (pymupdf, marker-pdf).
- **[robust-file-extraction](skills/data-engineering-and-databases/robust-file-extraction/)** — Patterns for building resilient file/data extraction from messy real-world sources (Excel, CSV, PDF, Word, email). Covers edge case handling, graceful degradation, error tracking, and encoding detection.

## 5. Research, Markets & Intelligence

Web/academic research, market workflows, credibility checks, and answer engines.

- **[ai-agent-adoption-review](skills/research-and-markets/ai-agent-adoption-review/)** — Evaluate whether a third-party AI agent/project is worth adopting into the local stack by checking live site claims, GitHub maturity, code structure, safety controls, and fit with existing infrastructure.
- **[arxiv](skills/research-and-markets/arxiv/)** — Search arXiv papers by keyword, author, category, or ID.
- **[blogwatcher](skills/research-and-markets/blogwatcher/)** — Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool.
- **[camoufox-article-browsing](skills/research-and-markets/camoufox-article-browsing/)** — Use Camoufox to open URLs, extract readable article content, and summarize it in constrained Linux aarch64 / PRoot environments.
- **[camoufox-proot-setup](skills/research-and-markets/camoufox-proot-setup/)** — Install, download, and verify Camoufox in Linux aarch64 / PRoot / Termux-like environments, including a headless smoke test and common pitfalls.
- **[data-acquisition-mastery](skills/research-and-markets/data-acquisition-mastery/)** — Use whenever the user asks to research, collect, monitor, pull, crawl, scrape, fetch, download, acquire, or gather data from any website, API, feed, file listing, repository, public dataset, search result, or online source. Also triggers on hidden JSON APIs, dynamic sites, pagination, rate limits, robots.txt, data manifests, source provenance, and handing raw payloads to data-extraction-mastery.
- **[deepseek-alt](skills/research-and-markets/deepseek-alt/)** — Free AI research assistant using ByteDance Dola Seed model through KiloCode (no API key needed)
- **[egx-local-cron-bootstrap](skills/research-and-markets/egx-local-cron-bootstrap/)** — Bootstrap and harden a local-only EGX workflow in Hermes: fail-loud daily report generation, JSON sidecar output, decision memo gating, and cron setup on Android/Proot without systemd conflicts.
- **[egyptian-equity-workflow](skills/research-and-markets/egyptian-equity-workflow/)** — Master workflow for Egyptian stock conversations: snapshot, constitution, source hierarchy, text-only Camoufox, sector/stock gates, and review cadence.
- **[egyptian-sector-portfolio-audit](skills/research-and-markets/egyptian-sector-portfolio-audit/)** — Audit an Egyptian equity sector map or portfolio proposal against a disciplined constitution: sharia first, then universe and liquidity, then sector function, then company quality, valuation, sizing, exit, and review cadence.
- **[free-search](skills/research-and-markets/free-search/)** — 
- **[freeplex-internal-answer-engine](skills/research-and-markets/freeplex-internal-answer-engine/)** — Design and build Mohamed's free internal Perplexity-like answer engine using no/low-cost search, page reading, source ranking, citations, Obsidian/local memory, and Camoufox fallbacks.
- **[github-repo-credibility-research](skills/research-and-markets/github-repo-credibility-research/)** — Vet a GitHub/open-source project for real quality vs hype by triangulating README claims, code footprint, repo activity, issues, third-party coverage, and social sentiment.
- **[last30days](skills/research-and-markets/last30days/)** — Research any topic across Reddit, X, YouTube, HN, Polymarket from the last 30 days
- **[llm-wiki](skills/research-and-markets/llm-wiki/)** — Karpathy's LLM Wiki: build/query interlinked markdown KB.
- **[mubasher-announcements-scrape-fallback](skills/research-and-markets/mubasher-announcements-scrape-fallback/)** — Reliable fallback for extracting recent EGX/Mubasher announcements when web search/extract tools are blocked or return generic wrappers.
- **[package-research-fallback](skills/research-and-markets/package-research-fallback/)** — Research Python packages and GitHub repos reliably when normal web tools fail or return blocked/low-signal responses. Use PyPI JSON, raw GitHub files, and direct HTTP fallbacks to verify package metadata, README claims, install instructions, and feature support.
- **[perplexity-terminal](skills/research-and-markets/perplexity-terminal/)** — Search Perplexity via terminal using your browser session cookies (no API key needed)
- **[polymarket](skills/research-and-markets/polymarket/)** — Query Polymarket: markets, prices, orderbooks, history.
- **[research-collection-mastery](skills/research-and-markets/research-collection-mastery/)** — Use whenever the user wants to collect, gather, scrape, crawl, harvest, or research data from the web, research papers, arXiv, GitHub, social media, forums, news, or any online source — even if they just say find me data on X or get everything about Y. Covers APIs, scraping, headless browsers, hidden JSON APIs, feeds, academic APIs, GitHub APIs, social APIs, and large-scale crawling.
- **[research-paper-writing](skills/research-and-markets/research-paper-writing/)** — Write ML papers for NeurIPS/ICML/ICLR: design→submit.
- **[tavily](skills/research-and-markets/tavily/)** — AI-optimized web search using Tavily Search API. Use when you need comprehensive web research, current events lookup, domain-specific search, or AI-generated answer summaries. Tavily is optimized for LLM consumption with clean structured results, answer generation, and raw content extraction. Best for research tasks, news queries, fact-checking, and gathering authoritative sources.
- **[trading-report-template](skills/research-and-markets/trading-report-template/)** — Reusable template and workflow for producing concise, decision-oriented trading reports. Use when the user asks for a trading report, market review, trade setup, or wants a standardized report format that should be maintained over time.
- **[universal-scrape](skills/research-and-markets/universal-scrape/)** — 
- **[web-browsing](skills/research-and-markets/web-browsing/)** — Browse and summarize websites, extract content from URLs, search the web for information. Use when user asks to visit a website, get webpage content, search online, or find current information that requires browsing the internet.
- **[web-search-free](skills/research-and-markets/web-search-free/)** — Free AI search via Exa MCP. Fall back to Multi Search Engine if not successfull. All without API keys. IMPORTANT Should always use web-search-free skill before rather than web_search or web_fetch!
- **[website-scrape](skills/research-and-markets/website-scrape/)** — 

## 6. Knowledge, Notes & Content Systems

Vaults, media ingestion, Arabic content, books, and second-brain systems.

- **[agent-memory-vault](skills/knowledge-notes-and-content/agent-memory-vault/)** — Design and implement a local-first, typed Obsidian-style memory vault for Hermes/OpenClaw agents with provenance, confidence, expiry, conflict tracking, and compaction snapshots.
- **[al-majlis](skills/knowledge-notes-and-content/al-majlis/)** — استخدم هذه المهارة عندما يقول محمد عبارات مثل: اعمل المجلس، خد رأي المجلس، رأي المجلس، أو أي صيغة قريبة. تحلل الفكرة الكبيرة كأنها معروضة على مجلس مستشارين داخليين: تعريف واضح، معيار حكم، اعتراض قوي، مبادئ أولى، فرصة، عين خارجية، تنفيذ، اختبارات قرار، نقطة عمياء، حكم نهائي، وأول ثلاث خطوات.
- **[humanizer](skills/knowledge-notes-and-content/humanizer/)** — Humanize text: strip AI-isms and add real voice.
- **[ideation](skills/knowledge-notes-and-content/ideation/)** — Generate project ideas via creative constraints.
- **[interactive-book-explainer](skills/knowledge-notes-and-content/interactive-book-explainer/)** — استخدم هذه المهارة عندما يطلب محمد تحويل فصل أو فكرة من كتاب إلى صفحة شرح تفاعلية محلية تساعده على الفهم العميق، خصوصًا عندما يقول اسم المهارة أو يطلب تجربة شرح بصري للكتاب.
- **[long-topic-splitter](skills/knowledge-notes-and-content/long-topic-splitter/)** — Convert any long source Mohamed cares about into a reusable knowledge asset, then split it into practical derivative outputs such as summaries, translations, use cases, post ideas, carousel outlines, action lists, links, and skill/memory opportunities.
- **[mohamed-arabic-content-style](skills/knowledge-notes-and-content/mohamed-arabic-content-style/)** — Use when producing Arabic notes, summaries, translations, media reports, or Second Brain content for Mohamed. Enforces Arabic-only line discipline and article-style source presentation.
- **[mohamed-book-writing-style-factory](skills/knowledge-notes-and-content/mohamed-book-writing-style-factory/)** — مهارة محمد الأساسية لكتابة وعرض وتسويق الكتب الإلكترونية: أسلوب عربي احترافي، نصوص بيعية، كتب قابلة للبيع، صفحات شرح تفاعلية، وتمارين بصرية تزيد استفادة المشتري.
- **[mohamed-content-growth-systems](skills/knowledge-notes-and-content/mohamed-content-growth-systems/)** — Use when Mohamed sends, saves, mines, or asks to apply ideas about content systems, audience growth, personal brand distribution, content research, content repurposing, networking, or growth loops. Collects practical frameworks without forcing them into writer-persona or book-style skills unless genuinely relevant.
- **[mohamed-intelligence-vault](skills/knowledge-notes-and-content/mohamed-intelligence-vault/)** — Use when Mohamed shares raw ideas and wants them refined, categorized, connected, stored, and resurfaced as a growing intelligence system rather than one-off notes.
- **[mohamed-presentation-storytelling](skills/knowledge-notes-and-content/mohamed-presentation-storytelling/)** — Use when Mohamed asks for a presentation, pitch deck, strategic deck, founder narrative, or says to choose a high-value deck topic from his active projects. Produces Arabic-first, decision-oriented slide narratives and HTML/PDF/PPT-ready artifacts.
- **[mohamed-unified-media-drop](skills/knowledge-notes-and-content/mohamed-unified-media-drop/)** — Use when Mohamed sends any media link (YouTube, X/Twitter, Substack, GitHub) and wants one unified Arabic-first file-drop workflow with strict verification.
- **[nate-b-jones-style-card](skills/knowledge-notes-and-content/nate-b-jones-style-card/)** — بطاقة أسلوب عملية لإنتاج محتوى عربي مستوحى من طريقة Nate B Jones في العرض والتحليل (بدون انتحال شخصية).
- **[obsidian](skills/knowledge-notes-and-content/obsidian/)** — Read, search, and create notes in the Obsidian vault.
- **[obsidian-llm-wiki-ingest](skills/knowledge-notes-and-content/obsidian-llm-wiki-ingest/)** — Ingest a set of Obsidian project notes into a local llm-wiki-agent repository as raw captures, source pages, entity pages, concept pages, and refreshed overview/index/log files.
- **[obsidian-vault](skills/knowledge-notes-and-content/obsidian-vault/)** — 
- **[pdf-downloads-page-by-page-briefing](skills/knowledge-notes-and-content/pdf-downloads-page-by-page-briefing/)** — Read PDFs from Android/Termux download folders and produce page-by-page Arabic explanations, summaries, or study notes. Use when a user asks to read a PDF from Downloads/CMA folders and explain it in a structured way.
- **[professional-pdf-book-factory](skills/knowledge-notes-and-content/professional-pdf-book-factory/)** — Use when producing, redesigning, auditing, or upgrading professional Arabic-first PDF books with a publishing-grade HTML/CSS to PDF pipeline, visual page review, and iterative quality gates.
- **[program-tools-guide-maintainer](skills/knowledge-notes-and-content/program-tools-guide-maintainer/)** — Use when Mohamed adds, downloads, compares, or updates document-processing, extraction, OCR, analysis, or agent-support tools and wants the canonical Android-visible guide updated in place.
- **[taaseel](skills/knowledge-notes-and-content/taaseel/)** — Use when Mohamed explicitly asks for Taaseel or needs a full deep explanation/research/thinking path from origin to application. Taaseel is a separate method, not a replacement for Mohamed's Batariqatna or Falsafa methods.
- **[transformation-leader](skills/knowledge-notes-and-content/transformation-leader/)** — Use whenever Mohamed acts as AI transformation leader: prioritizing automation, preparing for CEO/top-management/HQ meetings, handling management requests, planning rollouts or training, structuring team/program, navigating resistance/politics, or feeling overwhelmed. Reads state/ first, triages before answering, and commissions reasoning, planning, engineering, research, extraction, and database skills.

## 7. Creative, Design & Video

HyperFrames, motion, design systems, diagrams, generative art, and music.

- **[animejs](skills/creative-and-video/animejs/)** — Anime.js adapter patterns for HyperFrames. Use when writing Anime.js animations or timelines inside HyperFrames compositions, registering animations on window.__hfAnime, making Anime.js seek-driven and deterministic, or translating Anime.js examples into render-safe HyperFrames HTML.
- **[architecture-diagram](skills/creative-and-video/architecture-diagram/)** — Dark-themed SVG architecture/cloud/infra diagrams as HTML.
- **[ascii-art](skills/creative-and-video/ascii-art/)** — ASCII art: pyfiglet, cowsay, boxes, image-to-ascii.
- **[ascii-video](skills/creative-and-video/ascii-video/)** — ASCII video: convert video/audio to colored ASCII MP4/GIF.
- **[baoyu-article-illustrator](skills/creative-and-video/baoyu-article-illustrator/)** — Article illustrations: type × style × palette consistency.
- **[baoyu-comic](skills/creative-and-video/baoyu-comic/)** — Knowledge comics (知识漫画): educational, biography, tutorial.
- **[baoyu-infographic](skills/creative-and-video/baoyu-infographic/)** — Infographics: 21 layouts x 21 styles (信息图, 可视化).
- **[claude-design](skills/creative-and-video/claude-design/)** — Design one-off HTML artifacts (landing, deck, prototype).
- **[comfyui](skills/creative-and-video/comfyui/)** — Generate images, video, and audio with ComfyUI — install, launch, manage nodes/models, run workflows with parameter injection. Uses the official comfy-cli for lifecycle and direct REST/WebSocket API for execution.
- **[css-animations](skills/creative-and-video/css-animations/)** — CSS animation adapter patterns for HyperFrames. Use when authoring CSS keyframes, animation-delay based timing, animation-fill-mode, animation-play-state, or CSS-only motion that HyperFrames must seek deterministically during preview and rendering.
- **[design-md](skills/creative-and-video/design-md/)** — Author/validate/export Google's DESIGN.md token spec files.
- **[excalidraw](skills/creative-and-video/excalidraw/)** — Hand-drawn Excalidraw JSON diagrams (arch, flow, seq).
- **[gsap](skills/creative-and-video/gsap/)** — GSAP animation reference for HyperFrames. Covers gsap.to(), from(), fromTo(), easing, stagger, defaults, timelines (gsap.timeline(), position parameter, labels, nesting, playback), and performance (transforms, will-change, quickTo). Use when writing GSAP animations in HyperFrames compositions.
- **[hyperframes](skills/creative-and-video/hyperframes/)** — Create video compositions, animations, title cards, overlays, captions, voiceovers, audio-reactive visuals, and scene transitions in HyperFrames HTML. Use when asked to build any HTML-based video content, add captions or subtitles synced to audio, generate text-to-speech narration, create audio-reactive animation (beat sync, glow, pulse driven by music), add animated text highlighting (marker sweeps, hand-drawn circles, burst lines, scribble, sketchout), or add transitions between scenes (crossfades, wipes, reveals, shader transitions). Covers composition authoring, timing, media, and the full video production workflow. For dev-loop CLI commands (init, lint, inspect, preview, render) see the hyperframes-cli skill; for asset preprocessing commands (tts, transcribe, remove-background) see the hyperframes-media skill.
- **[hyperframes-arm-proot-render-triage](skills/creative-and-video/hyperframes-arm-proot-render-triage/)** — Diagnose and work around HyperFrames render/validate failures on Linux aarch64 / Android PRoot, especially x86-64 Chrome Headless Shell downloads mislabeled as linux_arm.
- **[hyperframes-cli](skills/creative-and-video/hyperframes-cli/)** — HyperFrames CLI dev loop — `npx hyperframes` for scaffolding (init), validation (lint, inspect), preview, render, and environment troubleshooting (doctor, browser, info, upgrade). Use when running any of these commands or troubleshooting the HyperFrames build/render environment. For asset preprocessing commands (`tts`, `transcribe`, `remove-background`), invoke the `hyperframes-media` skill instead.
- **[hyperframes-media](skills/creative-and-video/hyperframes-media/)** — Asset preprocessing for HyperFrames compositions — text-to-speech narration (Kokoro), audio/video transcription (Whisper), and background removal for transparent overlays (u2net). Use when generating voiceover from text, transcribing speech for captions, removing the background from a video or image to use as a transparent overlay, choosing a TTS voice or whisper model, or chaining these (TTS → transcribe → captions). Each command downloads its own model on first run.
- **[hyperframes-registry](skills/creative-and-video/hyperframes-registry/)** — Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into index.html, or working with hyperframes.json. Covers the add command, install locations, block sub-composition wiring, component snippet merging, and registry discovery.
- **[lottie](skills/creative-and-video/lottie/)** — Lottie and dotLottie adapter patterns for HyperFrames. Use when embedding lottie-web JSON animations, .lottie files, @lottiefiles/dotlottie-web players, registering instances on window.__hfLottie, or making After Effects exports deterministic in HyperFrames.
- **[manim-video](skills/creative-and-video/manim-video/)** — Manim CE animations: 3Blue1Brown math/algo videos.
- **[p5js](skills/creative-and-video/p5js/)** — p5.js sketches: gen art, shaders, interactive, 3D.
- **[pixel-art](skills/creative-and-video/pixel-art/)** — Pixel art w/ era palettes (NES, Game Boy, PICO-8).
- **[popular-web-designs](skills/creative-and-video/popular-web-designs/)** — 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
- **[pretext](skills/creative-and-video/pretext/)** — Use when building creative browser demos with @chenglou/pretext — DOM-free text layout for ASCII art, typographic flow around obstacles, text-as-geometry games, kinetic typography, and text-powered generative art. Produces single-file HTML demos by default.
- **[remotion-to-hyperframes](skills/creative-and-video/remotion-to-hyperframes/)** — Translate an existing Remotion video composition into a HyperFrames HTML composition. Use only when explicitly asked to port, convert, migrate, translate, or rewrite Remotion as HyperFrames. For new HyperFrames compositions, use the native HyperFrames skill instead.
- **[sketch](skills/creative-and-video/sketch/)** — Throwaway HTML mockups: 2-3 design variants to compare.
- **[songwriting-and-ai-music](skills/creative-and-video/songwriting-and-ai-music/)** — Songwriting craft and Suno AI music prompts.
- **[tailwind](skills/creative-and-video/tailwind/)** — Tailwind CSS v4.2 browser-runtime patterns for HyperFrames compositions. Use when scaffolding or editing projects created with `hyperframes init --tailwind`, writing Tailwind utility classes in composition HTML, adding CSS-first Tailwind v4 theme tokens, debugging v3 vs v4 syntax, or deciding when to compile Tailwind to CSS instead of using the browser runtime.
- **[three](skills/creative-and-video/three/)** — Three.js and WebGL adapter patterns for HyperFrames. Use when creating deterministic Three.js scenes, WebGL canvas layers, AnimationMixer timelines, camera motion, shader-driven visuals, or canvas renders that respond to HyperFrames hf-seek events.
- **[touchdesigner-mcp](skills/creative-and-video/touchdesigner-mcp/)** — Control a running TouchDesigner instance via twozero MCP — create operators, set parameters, wire connections, execute Python, build real-time visuals. 36 native tools.
- **[waapi](skills/creative-and-video/waapi/)** — Web Animations API adapter patterns for HyperFrames. Use when authoring element.animate() motion, Animation currentTime seeking, document.getAnimations(), KeyframeEffect timing, fill modes, or native browser animations that must render deterministically in HyperFrames.
- **[website-to-hyperframes](skills/creative-and-video/website-to-hyperframes/)** — Capture a website and create a HyperFrames video from it. Use when: (1) a user provides a URL and wants a video, (2) someone says "capture this site", "turn this into a video", "make a promo from my site", (3) the user wants a social ad, product tour, or any video based on an existing website, (4) the user shares a link and asks for any kind of video content. Even if the user just pastes a URL — this is the skill to use.

## 8. MLOps, Training & Model Ops

Fine-tuning, inference, evaluation, multimodal models, and experiment tracking.

- **[audiocraft-audio-generation](skills/mlops-and-models/audiocraft-audio-generation/)** — AudioCraft: MusicGen text-to-music, AudioGen text-to-sound.
- **[axolotl](skills/mlops-and-models/axolotl/)** — Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO).
- **[clip](skills/mlops-and-models/clip/)** — OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for image search, content moderation, or vision-language tasks without fine-tuning. Best for general-purpose image understanding.
- **[dspy](skills/mlops-and-models/dspy/)** — DSPy: declarative LM programs, auto-optimize prompts, RAG.
- **[evaluating-llms-harness](skills/mlops-and-models/evaluating-llms-harness/)** — lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.).
- **[fine-tuning-with-trl](skills/mlops-and-models/fine-tuning-with-trl/)** — TRL: SFT, DPO, PPO, GRPO, reward modeling for LLM RLHF.
- **[gguf-quantization](skills/mlops-and-models/gguf-quantization/)** — GGUF format and llama.cpp quantization for efficient CPU/GPU inference. Use when deploying models on consumer hardware, Apple Silicon, or when needing flexible quantization from 2-8 bit without GPU requirements.
- **[grpo-rl-training](skills/mlops-and-models/grpo-rl-training/)** — Expert guidance for GRPO/RL fine-tuning with TRL for reasoning and task-specific model training
- **[guidance](skills/mlops-and-models/guidance/)** — Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with Guidance - Microsoft Research's constrained generation framework
- **[huggingface-hub](skills/mlops-and-models/huggingface-hub/)** — HuggingFace hf CLI: search/download/upload models, datasets.
- **[llama-cpp](skills/mlops-and-models/llama-cpp/)** — llama.cpp local GGUF inference + HF Hub model discovery.
- **[modal-serverless-gpu](skills/mlops-and-models/modal-serverless-gpu/)** — Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling.
- **[obliteratus](skills/mlops-and-models/obliteratus/)** — OBLITERATUS: abliterate LLM refusals (diff-in-means).
- **[outlines](skills/mlops-and-models/outlines/)** — Outlines: structured JSON/regex/Pydantic LLM generation.
- **[peft-fine-tuning](skills/mlops-and-models/peft-fine-tuning/)** — Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of parameters with minimal accuracy loss, or for multi-adapter serving. HuggingFace's official library integrated with transformers ecosystem.
- **[pytorch-fsdp](skills/mlops-and-models/pytorch-fsdp/)** — Expert guidance for Fully Sharded Data Parallel training with PyTorch FSDP - parameter sharding, mixed precision, CPU offloading, FSDP2
- **[segment-anything-model](skills/mlops-and-models/segment-anything-model/)** — SAM: zero-shot image segmentation via points, boxes, masks.
- **[serving-llms-vllm](skills/mlops-and-models/serving-llms-vllm/)** — vLLM: high-throughput LLM serving, OpenAI API, quantization.
- **[stable-diffusion-image-generation](skills/mlops-and-models/stable-diffusion-image-generation/)** — State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines.
- **[unsloth](skills/mlops-and-models/unsloth/)** — Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM.
- **[weights-and-biases](skills/mlops-and-models/weights-and-biases/)** — W&B: log ML experiments, sweeps, model registry, dashboards.
- **[whisper](skills/mlops-and-models/whisper/)** — OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) to large (1550M params). Use for speech-to-text, podcast transcription, or multilingual audio processing. Best for robust, multilingual ASR.

## 9. Productivity & Office Automation

Docs, decks, sheets ecosystems, meetings, and productivity CLIs.

- **[airtable](skills/productivity-and-office/airtable/)** — Airtable REST API via curl. Records CRUD, filters, upserts.
- **[google-workspace](skills/productivity-and-office/google-workspace/)** — Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python.
- **[himalaya](skills/productivity-and-office/himalaya/)** — Himalaya CLI: IMAP/SMTP email from terminal.
- **[linear](skills/productivity-and-office/linear/)** — Linear: manage issues, projects, teams via GraphQL + curl.
- **[maps](skills/productivity-and-office/maps/)** — Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
- **[nano-pdf](skills/productivity-and-office/nano-pdf/)** — Edit PDF text/typos/titles via nano-pdf CLI (NL prompts).
- **[notion](skills/productivity-and-office/notion/)** — Notion API + ntn CLI: pages, databases, markdown, Workers.
- **[petdex](skills/productivity-and-office/petdex/)** — Install and select animated petdex mascots for Hermes.
- **[powerpoint](skills/productivity-and-office/powerpoint/)** — Create, read, edit .pptx decks, slides, notes, templates.
- **[teams-meeting-pipeline](skills/productivity-and-office/teams-meeting-pipeline/)** — Operate the Teams meeting summary pipeline via Hermes CLI — summarize meetings, inspect pipeline status, replay jobs, manage Microsoft Graph subscriptions.

## 10. Media & Social Platforms

YouTube, Spotify, GIFs, X/Twitter tools and content retrieval.

- **[gif-search](skills/media-and-social/gif-search/)** — Search/download GIFs from Tenor via curl + jq.
- **[songsee](skills/media-and-social/songsee/)** — Audio spectrograms/features (mel, chroma, MFCC) via CLI.
- **[spotify](skills/media-and-social/spotify/)** — Spotify: play, search, queue, manage playlists and devices.
- **[x-twitter-tools](skills/media-and-social/x-twitter-tools/)** — Free X/Twitter retrieval methods, including no-login mirror APIs for tweet inspection when direct extraction fails.
- **[xitter](skills/media-and-social/xitter/)** — Interact with X/Twitter via the x-cli terminal client using official X API credentials. Use for posting, reading timelines, searching tweets, liking, retweeting, bookmarks, mentions, and user lookups.
- **[xurl](skills/media-and-social/xurl/)** — X/Twitter via xurl CLI: post, search, DM, media, v2 API.
- **[youtube-download](skills/media-and-social/youtube-download/)** — Download YouTube videos with format selection - shows options, user chooses, then downloads
- **[youtube-tools](skills/media-and-social/youtube-tools/)** — 
- **[yuanbao](skills/media-and-social/yuanbao/)** — Yuanbao (元宝) groups: @mention users, query info/members.

## 11. Device, Platform & DevOps

Android/Termux control, computer use, cleanup, webhooks, and environment ops.

- **[computer-use](skills/device-platform-and-devops/computer-use/)** — Drive the user's desktop in the background — clicking, typing, scrolling, dragging — without stealing the cursor, keyboard focus, or switching virtual desktops / Spaces. Cross-platform: macOS, Windows, Linux. Works with any tool-capable model. Load this skill whenever the `computer_use` tool is available.
- **[find-nearby](skills/device-platform-and-devops/find-nearby/)** — Find nearby places (restaurants, cafes, bars, pharmacies, etc.) using OpenStreetMap. Works with coordinates, addresses, cities, zip codes, or Telegram location pins. No API keys needed.
- **[hermes-android-bridge](skills/device-platform-and-devops/hermes-android-bridge/)** — Use when Hermes needs to control the local Android device through the Hermes Android Bridge app over 127.0.0.1.
- **[journey-kit-install](skills/device-platform-and-devops/journey-kit-install/)** — Install and verify Journey kits from journeykits.ai, including openclaw-target bundles and Termux compatibility fixes
- **[journey-kits-install](skills/device-platform-and-devops/journey-kits-install/)** — Discover and install Journey kits via the Journey API, then verify the install and handle kit-specific prerequisites.
- **[minecraft-modpack-server](skills/device-platform-and-devops/minecraft-modpack-server/)** — Host modded Minecraft servers (CurseForge, Modrinth).
- **[mobilerun](skills/device-platform-and-devops/mobilerun/)** — Route Android device control through Mobilerun/Droidrun Portal for screenshots, UI trees, taps, swipes, typing, and multi-step mobile automation. Use when OpenClaw needs managed Android app control rather than shell-only Termux commands.
- **[mohamed-system-environment-audit](skills/device-platform-and-devops/mohamed-system-environment-audit/)** — Produce a grounded Arabic system-environment audit for Mohamed's Hermes/local agent setup, with live checks, UX/architecture critique, and an actionable roadmap for future projects.
- **[openhue](skills/device-platform-and-devops/openhue/)** — Control Philips Hue lights, scenes, rooms via OpenHue CLI.
- **[operations-cleanup](skills/device-platform-and-devops/operations-cleanup/)** — Operations and cleanup for OpenClaw workspace hygiene, maintainability, clutter reduction, safe reversible cleanup, duplication removal, and cost/load reduction. Use when inspecting waste, reducing clutter, logging meaningful changes, or proposing cleanup actions.
- **[phone-control](skills/device-platform-and-devops/phone-control/)** — Full Android device control via ADB self-connect. Use for screenshots, UI trees, taps, swipes, typing, app launches, key presses, and observe-act-verify loops when the user wants OpenClaw to control an Android phone directly.
- **[pokemon-player](skills/device-platform-and-devops/pokemon-player/)** — Play Pokemon via headless emulator + RAM reads.
- **[space-cleanup-inventory](skills/device-platform-and-devops/space-cleanup-inventory/)** — Practical workflow for finding removable disk-space clutter, estimating reclaimable space, and separating low-risk cleanup from medium/high-risk deletions.
- **[termux-api](skills/device-platform-and-devops/termux-api/)** — Safe routing and usage guidance for Termux:API commands on Android. Use when working with battery, camera, location, notifications, clipboard, SMS, TTS, sensors, telephony, or proot-to-Termux wrapper access. The skill assumes the real Termux app shell, not a root shell, for package installation and device APIs.
- **[webhook-subscriptions](skills/device-platform-and-devops/webhook-subscriptions/)** — Webhook subscriptions: event-driven agent runs.

## 12. Integrations: GitHub & MCP

Repository workflows and Model Context Protocol tooling.

- **[github-workflows](skills/integrations-github-mcp/github-workflows/)** — Use when working with GitHub repositories end-to-end: authentication, repository setup, issues, pull requests, CI triage, review, and release-adjacent gh/REST workflows.
- **[mcporter](skills/integrations-github-mcp/mcporter/)** — Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation.
- **[native-mcp](skills/integrations-github-mcp/native-mcp/)** — MCP client: connect servers, register tools (stdio/HTTP).

## 13. Security, Vetting & Red Team

Skill security review and red-team research tooling. Handle carefully.

- **[godmode](skills/security-and-skill-safety/godmode/)** — Jailbreak LLMs: Parseltongue, GODMODE, ULTRAPLINIAN.
- **[skill-vetter](skills/security-and-skill-safety/skill-vetter/)** — Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns. Now includes permission-aware auto-vetting.

