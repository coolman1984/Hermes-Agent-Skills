---
name: mohamed-intelligence-vault
description: Use when Mohamed shares raw ideas and wants them refined, categorized,
  connected, stored, and resurfaced as a growing intelligence system rather than one-off
  notes.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
tags: [ideas, intelligence-vault, synthesis, strategy, mohamed]
metadata:
  tags:
  - ideas
  - intelligence
  - vault
  - categorization
  - synthesis
  - mohamed
---

# Mohamed Intelligence Vault

## Overview

This skill turns Mohamed's stream of ideas into a living idea intelligence system. The goal is not only to store ideas, but to sharpen them, classify them, connect them, and periodically synthesize stronger ideas from combinations.

The assistant should act as an idea strategist, product analyst, market interpreter, business psychologist, and memory librarian. Every idea Mohamed gives should become a structured asset that can be searched, compared, revived, combined, and developed.

Important: Mohamed may not always send a single clean idea. He may send a topic, a problem, a discussion, a video summary, a market observation, a list of ideas, or a rough feeling that something matters. Treat all of these as raw intelligence. Extract possible ideas, hidden demand, customer pain, emotional buying triggers, business models, and system improvements from the material.

## When to Use

Use this skill when Mohamed:

- Shares one or more business ideas.
- Shares a topic, problem, discussion, video summary, market observation, or messy context that may contain ideas.
- Says he wants ideas stored, categorized, remembered, or developed.
- Asks whether an idea is good.
- Sends a video, post, or list of opportunities and wants a practical system from it.
- Wants separate raw thoughts turned into stronger compound ideas.
- Asks to revisit old ideas, compare them, or find connections between them.
- Talks about what makes people pay, buy quickly, feel urgency, avoid pain, gain status, save time, or reduce uncertainty.

Do not use this skill for casual conversation unless Mohamed is clearly ideating.

## Core Mission

See `references/business-idea-intelligence-philosophy.md` for Mohamed's clarified operating philosophy: this system is for extracting business opportunities, customer psychology, and executable revenue paths from ideas, topics, discussions, and messy context — not for passive summarization.

See `references/batch-media-note-mining.md` when Mohamed asks to scan existing saved summaries or media-note libraries and extract opportunities from them.

See `references/weekly-intelligence-cycle.md` when Mohamed says "شغل الدورة" or asks to run the weekly intelligence cycle: inspect the vault/media/wiki, choose one near-money experiment, one internal-system improvement, and one item to park, then update the decision note, review queue, snapshot, and wiki if needed.

See `references/near-money-service-validation-assets.md` when an idea graduates into a small sellable service experiment: create 3 proof samples plus a concise offer note under `Projects/`, then stop building and validate demand with real prospects.

See `references/ai-transformation-role-briefs.md` when Mohamed is proposing himself for an internal AI leadership or transformation role. Treat it as a near-money strategic opportunity: produce a calm, simple, role-winning brief with operational use cases, evidence, a 90-day plan, and a short pitch — not a generic AI explainer.

For every idea, topic, or context block, produce seven things:

1. A clean definition of the idea or hidden opportunity.
2. The practical market application.
3. The customer pain or emotional buying trigger.
4. A sharper commercial version of the idea.
5. A category and tags.
6. Links to related or combinable ideas.
7. One practical path toward money, customers, or a testable business.

Then store it in the Obsidian vault under:

`/root/Documents/Obsidian Vault/Ideas/Intelligence Vault/`

## Required Vault Structure

Create these paths if missing:

```text
Ideas/Intelligence Vault/
Ideas/Intelligence Vault/00 - Index.md
Ideas/Intelligence Vault/01 - Inbox.md
Ideas/Intelligence Vault/02 - Categories.md
Ideas/Intelligence Vault/03 - Connections.md
Ideas/Intelligence Vault/04 - Stronger Combinations.md
Ideas/Intelligence Vault/05 - Review Queue.md
Ideas/Intelligence Vault/Ideas/
Ideas/Intelligence Vault/Templates/
Ideas/Intelligence Vault/Templates/Idea Template.md
```

## When an idea graduates into a project

When Mohamed says phrases like "نبتدي", "أسس المشروع", "نبني ده", or otherwise clearly moves from ideation to execution, do not only save the idea. Treat it as a promoted project and run a reversible bootstrap:

1. Preserve the idea in the intelligence vault as usual.
2. Create or update a dedicated project note under `Projects/`.
3. Update the idea index, categories, connections, and review queue.
4. If the project changes near-term focus, update `CURRENT-SNAPSHOT.md` with the new next step.
5. If it is a software/product build, load and follow `mohamed-coding-team`: Claude for architecture only, Codex for execution planning/review, OpenCode for implementation.
6. Force a narrow first wedge before building. The first version must have one buyer, one data source or workflow, one concrete output, and one acceptance test.

Example narrowing rule:

- Weak: "platform that reads any company file".
- Strong first wedge: "sales files to local reports with provenance for every number".

## Vision Blueprint Bootstrapping (new 2026-06-17)

When Mohamed shares a long-form strategic vision document — not just an idea, but a complete product/system blueprint with multiple architecture layers, market analysis, competitive positioning, use cases, and build phases — do not reduce it to a standard idea note. Treat it as a vision blueprint and produce a structured execution plan.

**Trigger signals:**
- Multi-paragraph text with explicit section headers
- Contains architecture layers, component names, or system design
- References competitors, market gaps, pricing models
- Has explicit build phases or roadmap
- Mohamed says "أعمل فولدر للمشروع ده" or "ضيف ليها الافكار دي"

**What to produce:**

1. **Project execution plan** under `Projects/<Name> — Execution Plan.md`:
   - Project name (simple, expressive, English)
   - One-sentence positioning
   - Architecture as numbered connected layers
   - Killer MVP definition (inputs → outputs)
   - Best first use cases table
   - Technical stack recommendations
   - Competitive positioning and unfair advantage
   - Build roadmap as phased table with durations
   - Overlap analysis with existing Mohamed projects
   - Next immediate step

2. **Research references** under `Projects/<Name> — Research References.md`:
   - Competitor landscape (product, price, gap vs us)
   - Technical alternatives and benchmarks
   - Market sizing data
   - Pricing anchors from comparable products
   - External frameworks and repositories to reference

3. **Snapshot update:** add to `CURRENT-SNAPSHOT.md` and set the next step.

**Pitfalls:**
- Do not treat a vision blueprint as "just another idea" and file it in the idea vault only.
- Do not create the project without mapping overlap with existing projects (avoid duplicate work).
- Do not skip the research pass — external validation strengthens the blueprint and uncovers alternatives.
- The project name must be simple and expressive in English; avoid long descriptive names.
- When the blueprint mentions technologies or competitors, verify them with web search rather than trusting the source uncritically.

**Proven pattern (Compound, 2026-06-17):** Mohamed shared a full 8-layer Company Intelligence Advisor OS blueprint → produced structured plan with architecture, MVP, 7 first use cases, pricing table, 7-phase roadmap, competitive gap table, technical stack, and overlap analysis with existing projects (Company-Dashboard, Hermes, LLM Wiki).

## Idea Processing Workflow

When Mohamed gives an idea, follow this flow:

### Prompt and Screenshot Inputs

If Mohamed shares a prompt, screenshot text, or copied request and says to analyze it or keep useful ideas for future projects, do not store the prompt as-is only. Treat it as raw market intelligence:

- Extract the underlying reusable opportunity behind the prompt.
- Separate the useful system idea from the one-off wording.
- Decide whether it strengthens an existing project, belongs as a parked idea, or deserves a tiny validation test.
- If it is adjacent to the current weekly focus, attach it as an add-on rather than creating a new standalone project.
- Save the sharpened opportunity in the vault and update the index, categories, connections, stronger combinations, and review queue.

Example: a prompt asking for trending affiliate categories on short-form video should become a reusable radar for product-category selection, hooks, saturation, commissions, and beginner content angles — not merely a saved prompt.

### 1. Capture the raw idea

Preserve Mohamed's original meaning. Do not over-clean it before understanding the intention.

### 2. Define the idea clearly

Write a clean definition in Arabic:

- What is the idea?
- Who is it for?
- What problem does it solve?
- What action does it automate, improve, or enable?

### 3. Identify the market application

Explain where the idea could live commercially:

- Service
- Product
- Data product
- Content engine
- Consulting offer
- Marketplace
- Internal tool
- Investment research system
- Automation workflow

### 4. Sharpen the idea

Improve it by answering:

- What is the narrowest first customer?
- What is the smallest sellable version?
- What data or signal gives it an edge?
- What makes it hard to copy?
- What is the fastest proof of demand?

### 5. Categorize

Assign:

- Primary category.
- Secondary category.
- Tags.
- Stage.
- Difficulty.
- Capital requirement.
- Automation potential.
- Revenue type.

Use these default categories:

- أنظمة ذكاء ومراقبة
- أدوات إنتاجية شخصية
- خدمات للشركات الصغيرة
- فرص سوقية واستثمارية
- محتوى وتعليم
- أتمتة المبيعات والتسويق
- منتجات بيانات
- وكلاء ذكاء اصطناعي
- مشروعات محلية واقعية
- أفكار تحتاج تحقق

### 6. Connect

Search existing ideas in the vault and connect the new idea to:

- Similar ideas.
- Complementary ideas.
- Conflicting ideas.
- Ideas that can be merged into a stronger system.
- External idea mines such as X.com discussions and GitHub repositories when relevant.

Do this proactively. Do not wait for Mohamed to explicitly ask for connections.

### 7. Mine external signals when useful

When the material suggests a broader trend, check likely external idea mines if the task scope allows:

- X.com: operator threads, founder comments, customer complaints, pricing debates, trend reactions, and public experiments.
- GitHub: repositories, issues, readme claims, abandoned tools, fast-growing projects, and developer pain signals.
- Product and marketplace sources: launches, reviews, listings, pricing pages, and failed or neglected products.
- Saved media notes and legacy note roots: `/storage/emulated/0/Download/media-notes/`, `/storage/emulated/0/Download/youtube-transcripts/`, `/storage/emulated/0/Download/x-article-notes/`, `/storage/emulated/0/Download/github-repo-notes/`, and `/storage/emulated/0/Download/long-topic-splits/`.

When mining a saved media note, link back to its absolute Downloads path and record the bridge in `06 - Media Source Map.md`.

The goal is not browsing for curiosity. The goal is to identify hidden pain, pricing gaps, urgent buyers, reusable workflows, and business wedges.

### 8. Store

Create one note per idea under:

`Ideas/Intelligence Vault/Ideas/`

Use a date and short Arabic slug in the filename.

Example:

`2026-05-11-ذكاء-تنافسي-للقطاعات-المحلية.md`

### 9. Update indexes

Update:

- `00 - Index.md` with the new idea.
- `02 - Categories.md` with category placement.
- `03 - Connections.md` with links to related ideas.
- `04 - Stronger Combinations.md` if a new combination appears.
- `05 - Review Queue.md` if the idea needs validation.
- `06 - Media Source Map.md` when an idea or batch came from saved media notes.

For batch mining of old summaries, it is acceptable — and often better — to create one consolidated batch-extraction note first, then split only the strongest winners into standalone idea notes later.

## Idea Note Template

Each idea note should include:

```markdown
# عنوان الفكرة

## الفكرة الخام

## التعريف المصقول

## التطبيق في السوق

## العميل الأول المحتمل

## النسخة الأولى القابلة للبيع

## لماذا الآن؟

## مصدر التفوق

## نموذج الإيراد

## درجة الصعوبة

## احتياج رأس المال

## قابلية الأتمتة

## التصنيف

## الوسوم

## أفكار مرتبطة

## أفكار يمكن دمجها معها

## أسئلة تحقق

## الخطوة التالية
```

## Scoring

Give each idea simple scores from 1 to 5:

- وضوح المشكلة
- سهولة الوصول للعميل
- سرعة التجربة
- قابلية الأتمتة
- قابلية البيع
- قوة التمايز
- ملاءمة محمد

Then produce one of these labels:

- احتفظ بها فقط
- تحتاج بحثًا
- اختبرها سريعًا
- ابن نسخة أولى
- فرصة قوية

## Synthesis Rules

When there are at least three related ideas, try to form a stronger combined concept.

A strong combination usually has:

- One data source.
- One repeated pain.
- One paying buyer.
- One clear delivery format.
- One recurring revenue path.

If a combination appears, add it to:

`04 - Stronger Combinations.md`

## Periodic Review Behavior

When Mohamed asks to review ideas, summarize by:

- Best three ideas now.
- Ideas that can merge.
- Ideas that should be archived.
- Ideas needing one validation step.
- Ideas closest to revenue.

## Full-Vault Cleanup / "Do All" Behavior

When Mohamed asks to "do all" after a status review of the intelligence project, treat it as permission to execute the full reversible internal maintenance pass rather than asking again. Default sequence:

1. Rebuild `00 - Index.md` from the actual Markdown files under `Ideas/Intelligence Vault/`, not from stale index assumptions.
2. Update `02 - Categories.md`, `03 - Connections.md`, `04 - Stronger Combinations.md`, and `05 - Review Queue.md` together so the vault stays coherent.
3. Include both standalone idea notes under `Ideas/` and root-level opportunity/source notes, excluding templates and system index files.
4. Add a short operating-cycle note under `Projects/` when the work reveals a repeated review loop, and link it from the vault index.
5. Keep the output focused on execution lanes: what is closest to money, what strengthens Mohamed's internal system, and what should remain parked.

This cleanup is not a content-writing exercise. The goal is fewer orphan notes, clearer execution lanes, and a next practical decision.

## Weekly Intelligence Cycle Behavior

When Mohamed says "شغل الدورة" or asks to run the weekly intelligence cycle, do not ask for more instructions if the vault and snapshot are available. Use the reference workflow in `references/weekly-intelligence-cycle.md`.

Default output of the cycle:

1. One best near-money opportunity.
2. One best internal-system improvement.
3. One thing to park or stop for now.
4. One execution experiment for the week.

Required updates when running the cycle:

- Create a dated decision note under `Projects/`.
- Update `05 - Review Queue.md`.
- Update the vault index if a new decision note should be linked.
- Add a wiki synthesis only when the decision is durable knowledge.
- Update `CURRENT-SNAPSHOT.md` if the next step changes.
- Verify wiki integrity if the wiki was modified.

Avoid turning the cycle into a broad report. Mohamed needs a decision and a next action, not a bigger idea pile.

## Arabic Style Rules

Use Arabic body text. Avoid mixing English words inside Arabic lines. Translate generic terms when possible. If an English term is unavoidable, put it on a standalone line.

## Common Pitfalls

1. Storing the idea without improving it.
2. Creating too many categories too early.
3. Treating every idea as equally good.
4. Forgetting to link related ideas.
5. Writing long analysis but no next step.
6. Saving only in assistant memory instead of the vault.
7. Overbuilding before validation.
8. Summarizing a video, discussion, or market topic without extracting hidden demand, buyer psychology, and a path to money.
9. Rejecting weak-looking ideas too early; sometimes the value is in the emotional trigger, timing, distribution path, or connection to another idea.
10. Waiting for Mohamed to present a clean idea instead of actively mining messy context for business opportunities.
12. Assuming saved summaries only live in the newest `media-notes` tree; older valuable outputs may be under `youtube-transcripts`, `x-article-notes`, `github-repo-notes`, and `long-topic-splits`.
13. Saving prompt text without extracting the reusable commercial system behind it. A prompt is often just packaging around a deeper opportunity, buyer psychology pattern, or repeatable service workflow.
14. Letting a newly extracted opportunity compete with the active weekly experiment. If it is related, attach it as an add-on or validation angle; if not, park it with a clear test and anti-distraction note.
15. Continuing to polish service samples after enough proof assets exist; once 3 samples and a concise offer note exist, switch to prospect outreach and demand validation.
16. Treating a multi-paragraph vision blueprint as a standard idea — it needs a project execution plan, research references, and snapshot update, not just an idea-note filing.
17. Creating a new project from a vision blueprint without checking overlap with existing projects (Company-Dashboard, Hermes, LLM Wiki, etc.) — Mohamed often builds on what exists.

## Verification Checklist

Before finishing:

- [ ] The idea note exists in the vault.
- [ ] The index is updated.
- [ ] The category is updated.
- [ ] Connections were checked.
- [ ] Source-map bridge was updated if saved media notes or legacy summary roots were mined.
- [ ] The idea has a clear next step.
- [ ] No Arabic line contains embedded English terms unless unavoidable.
