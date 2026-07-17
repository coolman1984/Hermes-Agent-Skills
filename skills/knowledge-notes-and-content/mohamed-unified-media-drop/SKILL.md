---
name: mohamed-unified-media-drop
description: Use when Mohamed sends any media link (YouTube, X/Twitter, Substack,
  GitHub) and wants one unified Arabic-first file-drop workflow with strict verification.
version: 1.2.0
author: Hermes + Mohamed
license: MIT
tags: [media, youtube, twitter, substack, github, ingestion, mohamed]
metadata:
  tags:
  - media
  - unified-workflow
  - youtube
  - x
  - substack
  - github
  - arabic-first
  - file-drop
---

# Mohamed Unified Media Drop

## Overview

This is the single canonical media workflow for Mohamed.

If Mohamed sends a link from YouTube, X/Twitter, Substack, or GitHub, process it with this skill only.
No legacy routing, no alternate output modes by default.

## Default Output Policy (Non-Negotiable)

Unless Mohamed explicitly asks for quick summary only:
- produce a full Markdown file in Downloads
- verify file exists and is non-empty
- return exact absolute path
- attach with `MEDIA:` when supported

Mohamed also wants this skill treated as the **default first workflow for any content link he sends** unless he explicitly asks for another path. Do not detour into alternate link-processing workflows by default.

Do not modify this skill's behavior or structure during normal link-processing sessions unless Mohamed explicitly asks for a skill change. A request to use the skill is not a request to edit it.

## The Usual Article Shape (Non-Negotiable)

When Mohamed says he wants the output in the shape of the "usual article we always made", interpret that as this article structure:

1. A clear title stating the core idea.
2. A short introduction explaining what the source is about, why it matters, and the reading angle.
3. A coherent presentation of the main idea in the source's logical order.
4. A full Arabic article-style rewrite/presentation of the source — **not** line-by-line extraction, not fragmented bullets, and not a thin summary.
5. Practical analysis: what is strong, what is missing, what is biased, what is still uncertain.
6. A Mohamed-facing application section that turns the source into a decision, workflow improvement, system attachment, saved idea, or research-needed item.
7. An executive closing judgment: act now, save, attach to an existing project, research more, or park.

In short: do not produce a mere summary. Produce a coherent Arabic article that explains the source, evaluates it, and converts it into practical value for Mohamed.

## Cost-Control Output Policy (Non-Negotiable)

Mohamed explicitly changed the default media workflow to reduce token usage:

- Do **not** run internet research or enrichment by default.
- Do **not** open extra context sources by default.
- Do **not** use the research-enrichment reference unless Mohamed explicitly asks for research, enrichment, cross-checking, verification, or a deep dive.
- The default media note is source-only: extract the original source, summarize it, present it in Arabic, critique it from the source text itself, and apply it to Mohamed's systems.
- If a source makes risky claims about investing, law, health, security, politics, or reputation, do not research automatically. Label the claim as unverified and say that external verification would require an explicit research request.
- Preserve the remaining workflow: deduplication, extraction, structured note, optional source-derived idea-vault bridge, deterministic verification, and file delivery.

## Operational Workflow (Non-Negotiable)

For every substantial media link, follow this order:

1. **Deduplicate** against the media source map and existing Downloads notes.
2. **Extract the source** with the platform-specific path: transcript, article body, repository docs, or web page.
3. **Build a source-only brief**: claims, examples, people, dates, institutions, links, open questions, and obvious limitations from the source itself.
4. **Skip internet enrichment** unless Mohamed explicitly requests it in the same message.
5. **Draft the 14-section note** with clear separation between direct source content, Mohamed-facing interpretation, and unverified claims.
6. **Create or update the intelligence-vault bridge** only when the source itself produces a useful decision lens, business opportunity, workflow, investment angle, or reusable system insight. Do not research around it by default.
7. **Verify deterministically** using the verifier script and a manual skim of source-only quality.
8. **Deliver paths and attachment**; do not just say the work was done.

## Depth Modes

| Mode | Trigger | Research Budget | Output Decision |
|---|---|---|---|
| Source-only | Default for all media links | No internet enrichment | Full media note from the original source only |
| Quick | Mohamed explicitly asks for a quick take | No internet enrichment | Chat answer or short file |
| Research | Mohamed explicitly asks for research, enrichment, cross-checking, verification, or deep dive | Bounded external sources as requested | Full enriched note with clear provenance |
| Parked | Interesting but low leverage | No internet enrichment | Save/park without promoting to project |

Default to **Source-only**. Escalate to **Research** only by explicit request from Mohamed.

## Supported Inputs

- YouTube video URLs
- X/Twitter status/thread/article URLs
- Substack post/note/article URLs
- GitHub repository URLs (README + in-repo docs)
- Official web articles, engineering blogs, product/research posts, and other source links Mohamed drops for durable analysis

## Duplicate / Re-sent URL Detection and Handling

Mohamed may send the same link more than once — intentionally (wanting a fresh angle) or by accident (forgetting it was already processed). Before spending resources on a full extraction and report, check whether this URL has been seen before.

### Detection Procedure

Before routing to the platform-specific extraction path:

1. **Search the source map:** read the first 50 lines of
   `/root/Documents/Obsidian Vault/Ideas/Intelligence Vault/06 - Media Source Map.md`
   for any entry containing the same URL. This is the fastest dedup check.

2. **Search existing Downloads notes:** if the source map is not available or inconclusive, look under
   `/storage/emulated/0/Download/media-notes/<platform>/<author>/`
   for files matching the URL's content signature.

3. **Search the intelligence vault:** when the URL is identical but you cannot find a source-map entry, search note titles in
   `/root/Documents/Obsidian Vault/Ideas/Intelligence Vault/`
   for keywords from the link.

### Decision Tree

**A) Exact same URL found with a complete existing note (media + vault + source map intact):**
   - Do NOT create a duplicate media note file or vault entry.
   - Produce a fresh analysis if you can extract material new insight not present in the existing note — the existing note may have been brief or incomplete.
   - If fresh analysis adds value, create the new media note alongside the old one (clearer format, more sections) and update the source-map entry to reference both paths with a note about what the new version adds.
   - Update the existing intelligence-vault note with new insights using a dated subsection header (`## إضافات من التحليل المحدث (YYYY-MM-DD)`) rather than overwriting or creating a second vault note.
   - Tell Mohamed the link was already processed and summarize what shifted in this session's take.

**B) Same URL found but existing note is incomplete (missing sections, placeholder left, verifier failed):**
   - Write a new comprehensive version that supersedes the old one.
   - Update the source-map entry to point to the new file and mark the old one as superseded.
   - Update the relevant vault note; do not create a second vault note.

**C) Related but different URL (different platform, different author, same topic):**
   - Treat as a new media note.
   - In the "Business Intelligence" section and vault bridge, link to the existing related note explicitly.

### Anti-duplication Principles

- Never create two vault notes (under `Intelligence Vault/`) for the same source URL.
- Never create two source-map entries (`06 - Media Source Map.md`) for the same URL.
- Multiple Downloads media notes for the same URL are acceptable only if each adds a different level of detail or angle — always note the existing one in the new file's metadata section.
- When updating an existing vault note, preserve its original creation date and mark additions with a dated subsection header so the provenance is clear.
- If the same URL appears a third time on a different day, do not repeat the update dance — tell Mohamed the link is already processed and offer a fresh chat-only angle instead of another file write.

## Unified Mandatory Sections

Every final file must include:
1. Source metadata (original URL + canonical URL if available, extraction method, transcript/article source, and whether external research was skipped or explicitly requested)
2. Long professional Arabic summary based on the source itself, with uncertainty labeled clearly
3. Professional opinion on practical value, including whether the source is complete, partial, biased, or needs follow-up research
4. Full professional Egyptian-Arabic translation/presentation of the source content in original logical order
5. 10 practical use cases
6. Main idea, including the deeper philosophy, incentive, or worldview behind the source when relevant
7. Point-by-point argument breakdown, separating source claims, Mohamed-facing interpretation, and unverified claims
8. Practical concept explanations, including what/why/who/how/when/where for important concepts, using the source only unless research was explicitly requested
9. Link-by-link explanation for links present in the source itself
10. Strengths
11. Weaknesses / reservations, including missing context and serious counterarguments visible from the source itself
12. How Mohamed can apply it in his system
13. Business intelligence extraction for the idea vault
14. Executive conclusion with a clear classification: act now, save, attach to an existing project, research more, or park

## Intelligence Vault Bridge

After creating and verifying the media note, treat the source as raw business intelligence when it contains ideas, market observations, workflows, customer pain, products, tools, pricing, growth, investing, automation, or business strategy.

Do not leave the output as a passive summary. Extract:

- hidden customer pain
- urgent buying triggers
- possible paying customer
- market wedge
- mispriced or neglected asset
- reusable workflow
- product or service idea
- connection to older idea-vault notes
- one practical experiment toward customers or money

Then create or update a corresponding note under:

`/root/Documents/Obsidian Vault/Ideas/Intelligence Vault/`

If the source teaches a reusable production method for an existing Mohamed system, do not stop at the idea-vault note. Patch the relevant class-level skill or add a concise support reference under it. Example: a storytelling/writing source that changes how book chapters should be written belongs in `mohamed-book-writing-style-factory` as a durable writing lens.

### Relevance Gate for Writer Persona / Book Factory

Do **not** automatically connect every media link to Mohamed's writer persona, book voice, or book-factory skills.

Before patching or referencing writer/book skills, explicitly decide whether the source has a genuine reusable lesson for:

- writing voice or tone
- storytelling craft
- chapter structure
- book positioning
- reader psychology
- publishing or selling books
- audience growth around Mohamed's books or author brand

If the link is about another domain — investing, tools, strategy, technology, general business, or content growth without a direct writing/book angle — create the long Downloads note and, when useful, an idea-vault/business extraction only. Do not force it into the writer-persona system.

When there is only indirect relevance, say so clearly in the final note: e.g. "relevant to distribution or author audience, not to chapter-writing voice." This prevents overfitting random links into the book factory.

Also update the idea vault index, categories, connections, stronger combinations, and review queue when relevant. When a media source creates an idea-vault extraction, use `references/intelligence-vault-bridge-checklist.md` as the operational checklist. The source-map entry is mandatory for every created bridge note; the other index files should be updated when the connection is real rather than forced.

Record the bridge between the Downloads media note and the idea-vault note in:

`/root/Documents/Obsidian Vault/Ideas/Intelligence Vault/06 - Media Source Map.md`

This bridge is automatic unless Mohamed explicitly asks for a quick chat-only summary or says not to store the link.

When Mohamed asks to mine or review older saved summaries, do not assume all historical notes live under this skill's unified output path. Hand off to `mohamed-intelligence-vault` and scan legacy roots such as `youtube-transcripts`, `x-article-notes`, `github-repo-notes`, and `long-topic-splits` under Downloads.

## Language & Style Rules

- Arabic first.
- Keep prose in clear professional Egyptian Arabic: easy, direct, and immediately understandable.
- Avoid heavy classical Arabic, long sentences, academic stiffness, and decorative phrasing.
- Explain the idea fast, then add only the useful detail.
- Treat Mohamed's requested style rules as global for every media/content note generated by this skill.
- Do **not** mix Arabic and English in the same line. This breaks reading direction and layout for Mohamed.
- Translate generic technical terms into clear Arabic whenever possible.
- If an English term is genuinely necessary, put it on its own separate line, not inside an Arabic sentence.
- URLs may stay as raw standalone lines.
- Proper nouns/product names should be transliterated or placed on separate lines when needed; do not scatter English inside Arabic prose.
- When presenting original post/source content, write it as a professional coherent article in the writer's voice and logical order.
- Do **not** present short posts as `Line 1 / Line 2` or numbered transcript fragments unless Mohamed explicitly asks for forensic line-by-line extraction.
- Avoid dumping raw code blocks; explain code conceptually.
- No placeholders.

## Extraction & Access Policy

1. Try normal extraction path first.
2. If source is blocked OR extraction fails, use Camoufox immediately as first fallback.
3. If Camoufox still cannot access content, report clearly what is blocked and what was retrievable.
4. Never fabricate missing content.

## Research Enrichment Layer Before Writing

Default status: **disabled to save tokens**.

Only use this layer when Mohamed explicitly asks for research, enrichment, external verification, cross-checking, or a deep dive.

For normal YouTube and media links, do not run this section. Produce a source-only note from the transcript, article, post, repository, or page itself.

Purpose when explicitly enabled: the source Mohamed sends is often only one window into a bigger topic. The note should not merely summarize the link; it should help Mohamed understand the bigger picture, hidden assumptions, missing answers, and practical implications.

### Mandatory Enrichment Brief

Before drafting, create a short internal brief with exactly these fields:

```markdown
## Enrichment Brief

### Direct source claim

### Missing context found

### Counterpoints and omissions

### Mohamed application

### Confidence level

### Research not done
```

The final media note does not have to include this exact English block, but it must integrate all six fields in Arabic prose or Arabic subsection labels.

### Mandatory Arabic Provenance Labels

Every enriched final note must include clear Arabic provenance labels somewhere in the note, preferably in sections 3, 7, 8, 11, or 14:

- `من المصدر مباشرة`
- `من البحث الإضافي`
- `قراءة عملية لمحمد`
- `ما يزال غير مؤكد`

These labels prevent the note from blending source content, external research, and interpretation into one ungrounded narrative.

### Mandatory Enrichment Questions

For every substantial source, answer these before drafting:

- What exactly is being claimed?
- Why does it matter now?
- Who benefits and who is hurt?
- How did this system, tool, idea, market, or problem emerge?
- When did the key changes happen?
- Where is the action concentrated geographically, institutionally, or technologically?
- What is the deeper philosophy, incentive, or worldview behind it?
- What is missing from the source?
- What would a skeptical expert ask?
- What should Mohamed do with this: act, save, research more, attach to an existing project, or park?

### Research Scope

Use a small but serious research pass:

1. Read the source transcript/article/repository first.
2. Extract names, dates, institutions, claims, studies, books, tools, companies, and links.
3. Open or retrieve the source's own references when available.
4. Search for 2-5 independent context sources when the topic involves history, markets, politics, science, business, investment, tools, or strategy.
5. Prefer primary or high-trust sources over commentary.
6. Capture contradictions and uncertainty instead of smoothing them over.

### Output Integration

The final note must distinguish:

- What came directly from the source.
- What came from enrichment research.
- What is Mohamed-facing interpretation.
- What remains uncertain.

Add enrichment into the existing 14 sections without bloating the note with raw research dumps. If the enrichment materially changes the interpretation, say so explicitly in the professional opinion and executive conclusion.

### Timebox and Anti-Rabbit-Hole Rule

Default enrichment should be deep enough to answer the bigger-picture questions, but not become a new research project. If the source opens a large domain, write the media note and create a separate "research-needed" item or idea-vault note rather than expanding forever.

## Routing Inside the Skill

### YouTube
- Extract transcript and metadata.
- **Transcript is mandatory when available**: do not finalize a YouTube note from metadata/description only if a full transcript can still be retrieved via fallback tools.
- Fallback order for transcript retrieval:
  1) `youtube_transcript_api`: list languages first, then prefer Arabic if available; if Arabic is absent, prefer official/manual English default captions before generated English, then translate/synthesize Arabic from that transcript. Label whether the transcript was official/manual/default or auto-generated.
  2) `yt-dlp` subtitles fallback: `--write-auto-subs --write-subs --sub-langs ar.*,en.* --convert-subs vtt` then parse clean text. If Arabic auto subtitles fail or hit `HTTP Error 429` while English original/default/generated captions exist, do not fail; proceed from English captions and produce the Arabic note from that transcript, labeling the transcript source clearly.
  3) Browser fallback (Camoufox/camoubrain) only for access/block scenarios, not as first choice over direct transcript APIs.
- For YouTube metadata, prefer dumping `yt-dlp --dump-single-json --skip-download --no-warnings <url>` to a temp file and parsing that file. Do **not** rely on a captured terminal/stdout string for large metadata JSON; wrappers may truncate or inject control characters and break `json.loads`.
- If Arabic transcript is missing but English generated transcript exists, proceed with full extraction from English and produce Arabic output sections from that source.
- Build full unified report sections.
- Keep sequence faithful to video flow.

### X/Twitter
- Resolve status/article content with robust retrieval.
- For `x.com/i/status/<tweet_id>` links that point to internal X articles, first inspect mirror JSON for structured article content: `https://api.fxtwitter.com/i/status/<tweet_id>`.
- Check article blocks in this order because long-form content may live on a quoted post rather than the root tweet:
  1. `tweet.article.content.blocks[]`
  2. `tweet.quote.article.content.blocks[]`
  3. `tweet.quoted_tweet.article.content.blocks[]`
- When present, parse blocks in original order into a coherent Arabic article/presentation and use `r.jina.ai/http://x.com/i/status/<tweet_id>` as a cross-check for readable rendering and media captions.
- If `web_extract` truncates the mirror JSON, fetch it with `curl` to a temporary file and parse with Python before writing the note.
- If blocked, switch immediately to Camoufox fallback.
- Build full unified report sections.
- Clearly label mirror/r.jina/Camoufox extraction sources in metadata; never imply direct live X access when the content came from mirrors.
- `references/x-quoted-article-extraction.md` for the quoted-article pattern and verification targets.
- `references/x-internal-article-extraction.md` for the root `tweet.article` pattern where the visible status is nearly empty but the full internal X article is attached to the same tweet.
- `references/x-article-block-normalization.md` for converting X article JSON blocks into a clean intermediate Markdown source before synthesis, preserving headings, list items, blockquotes, and original order.
- `references/x-quoted-article-with-visual-framework.md` for X posts where the root tweet quotes an internal article and the attached image/diagram contains part of the argument; combine tweet text, quoted article blocks, and vision-extracted image structure before drafting.

### Substack
- Resolve canonical page and content body.
- If blocked, switch immediately to Camoufox fallback.
- Build full unified report sections.

### GitHub
- Read repo README and in-repo docs.
- Explain architecture and usage conceptually without raw code dumps.
- Build full unified report sections.

### Generic Web / Official Articles
- Use for official articles, engineering blogs, product/research posts, and source links outside YouTube/X/Substack/GitHub when Mohamed drops a bare URL and the content is worth durable analysis.
- Extract full page content with `web_extract` first.
- If extraction is truncated, incomplete, blocked, or direct terminal fetch returns access errors, use a readable-page fallback such as `r.jina.ai` and save the full markdown to a temporary file with `curl` before synthesis. Do not rely on a truncated tool snippet for long articles.
- Preserve source metadata: original URL, canonical URL when known, publisher/site, author, publication date, extraction method, and confidence.
- Build the same 14-section unified report, faithful to the article order.
- Use output path:

`/storage/emulated/0/Download/media-notes/web/<site-or-publisher>/<safe-title> - <YYYY-MM-DD>.md`

- If the article contains agent, workflow, business, product, market, automation, investing, or strategy material, create/update the intelligence-vault bridge exactly like other media sources.
- See `references/web-article-extraction-notes.md`.

## Output Destination Rule

By default, media links still use the verified Downloads file-drop workflow below.

If Mohamed has mentioned a separate Google Drive / Second Brain vault, do **not** treat that as permission to write into the assistant's local vault. Keep the assistant vault separate.

If Mohamed explicitly asks to add the note to his Google Drive Second Brain:
- write to that external vault only after its path/sync/auth is configured;
- if not configured yet, create the verified Downloads Markdown file first and clearly state it is ready to import/add to the Second Brain;
- never silently redirect output into `/root/Documents/Obsidian Vault`.

## Output Path Convention

Use unified tree:

`/storage/emulated/0/Download/media-notes/<platform>/<author-or-owner>/<safe-title-or-id> - <YYYY-MM-DD>.md`

## Verification Checklist (Must Pass Before Delivery)

- File exists
- File size > 0
- All mandatory sections present (accept numbered headings like `## 6) ...` as valid)
- Translation/presentation section exists and is complete
- Source/post presentation is written as a coherent professional article, not numbered line fragments
- 10 use cases present
- No unresolved placeholders
- No Arabic body line contains embedded English words; ignore URL-only lines and standalone English-only required terms
- Necessary English terms, if any, are on separate standalone lines
- Output path is under `/storage/emulated/0/Download/media-notes/`
- The note includes provenance labels: `من المصدر مباشرة`, `قراءة عملية لمحمد`, and `ما يزال غير مؤكد`.
- The verifier currently requires `من البحث الإضافي` even for source-only notes. For source-only notes, include it with an explicit negative statement such as: no external research was run because Mohamed did not request enrichment. Do not imply enrichment happened when it did not.
- The note answers the relevant what/why/who/how/when/where questions for the source's core idea
- The note contains at least one serious limitation, counterargument, missing context item, or uncertainty statement
- The executive conclusion classifies the source as: act now, save, attach to an existing project, research more, or park
- After writing, re-open the file and verify final content matches requested section names and order
- If the source contains business, product, market, customer, automation, investing, or strategy material, verify an idea-vault extraction note or source-map entry was created or updated

## Support References

- `references/research-enrichment-before-media-note.md`: optional enrichment pattern. Use only when Mohamed explicitly asks for research, enrichment, external verification, cross-checking, or a deep dive. Do not load or follow it for normal media links because the default workflow is now source-only to save tokens.
- `references/agent-workflow-media-bridge.md`: use when Mohamed sends AI-agent, loop, cron, subagent, skill, memory, or agent-operating-system media; attach the lesson to existing Hermes/vault/market systems and avoid premature autonomy or new-project drift.
- `references/ai-infrastructure-media-bridge.md`: use when Mohamed sends media about model serving, local LLM hardware, inference engines, quantization, GPU memory, self-hosting, or AI infrastructure choices; turn the source into a decision lens and attach it to existing systems rather than promoting a new infra project without a concrete workload.
- `references/telegram-image-ocr-fallback.md`: when Mohamed sends a Telegram screenshot/image instead of a link and `vision_analyze` fails, use tesseract OCR + green-pixel color detection to recover text and color-coded markings.
- `references/youtube-extraction-notes.md`: session-tested YouTube metadata/transcript extraction notes, including why to dump large `yt-dlp` JSON to a file and Mohamed's bare-link default.
- `references/youtube-autosub-429-and-long-note-pattern.md`: use when Arabic auto subtitles fail or rate-limit but English captions are available; proceed from English captions, clean VTT, delegate long synthesis if needed, and verify the final media note plus idea-vault bridge.
- `references/youtube-political-economy-bridge.md`: use when a YouTube explainer is about political economy, power structures, governance, regulation, or investing risk; create a compact decision-lens bridge rather than promoting it into a new project.
- `references/youtube-geopolitical-economy-verification.md`: use when a YouTube source makes broad geopolitical-economy claims around war, energy chokepoints, diplomacy, AI infrastructure, or investing; verify hard claims with official/wire/academic sources, label blocked wire snippets as low-confidence context, and save the output as a decision lens rather than a new project.
- `references/intelligence-vault-bridge-checklist.md`: concrete checklist for media notes that produce an idea-vault extraction, including which vault indexes to update and how to verify the bridge.
- `references/source-only-provenance-verifier-note.md`: explains the current verifier compatibility rule for source-only notes: include `من البحث الإضافي` only as an explicit statement that no external research was run, not as a claim of enrichment.
- `references/web-article-extraction-notes.md`: fallback and verification pattern for official web articles, including `r.jina.ai` full-page markdown capture and avoiding truncated snippets.

## Support Scripts

- `scripts/verify_media_note.py`: deterministic verifier for unified media notes. Use after writing X/YouTube/Substack/GitHub media notes to check required headings, exactly 10 use cases, placeholder leaks, Arabic/Latin line mixing, optional idea-note existence, and source-map bridge paths. Invoke it with positional arguments only: `python scripts/verify_media_note.py <media-note.md> [idea-note.md] [source-map.md]`; do not pass `--idea-note` or `--source-map` flags.

## Post-processing Guard (Critical)

- Do not run blind global find/replace for English tokens across the whole file.
- Use targeted replacements only; global replacements can corrupt proper nouns and mixed tokens.
- If localization is needed, patch specific lines/sections and re-validate mixed-language lines afterward.
- If delegated writing returns section labels that differ from required labels, normalize headings before delivery.
- Do not embed absolute vault paths that contain both Latin directory names and Arabic filenames inside the Arabic body of the media note. The verifier treats these as mixed Arabic/Latin lines. Put detailed media-note and idea-note paths in the source-map bridge and final chat response instead; inside the report body, say that a linked intelligence note was created and registered.
- Avoid placing Obsidian/vault file paths inside the Arabic body of the media note. Paths that include both Latin directory names and Arabic filenames can fail the mixed Arabic/Latin verifier. Put durable path bridges in the source-map file instead, and describe the existence of the linked idea note in Arabic prose inside the media note.
- For translated technical prose, run the verifier after writing and treat any single embedded English technical token as a fixable localization defect. Patch the exact line only; do not globally replace technical terms across the file.
- When the verifier flags lines containing essential proper nouns (product names like Obsidian/Kimi, protocol names like MCP, URLs, company names), classify them using the triage in `references/mixed-line-verifier-pragmatics.md`. Do not destroy readability by extracting every proper noun to its own line — note Bucket-1 warnings and deliver.

### Section 5 Is Use Cases (verifier-critical)

The verifier checks that section `## 5)` contains exactly 10 numbered use cases. Getting the section order wrong — e.g., putting use cases in section 9 and the main idea in section 5 — causes a hard failure ("expected 10 use cases, found 0"). The 14 sections follow this fixed sequence:

1. Source metadata — `## 1)`
2. Arabic summary — `## 2)`
3. Professional opinion — `## 3)`
4. Full presentation — `## 4)`
5. **10 practical use cases** — `## 5)` ← verifier target
6. Main idea — `## 6)`
7. Argument breakdown — `## 7)`
8. Concept explanations — `## 8)`
9. Link-by-link explanation — `## 9)`
10. Strengths — `## 10)`
11. Weaknesses — `## 11)`
12. Mohamed application — `## 12)`
13. Business intelligence — `## 13)`
14. Executive conclusion — `## 14)`

Before running the verifier, confirm section 5 is the use-cases section.

### Proper Nouns in Mixed Arabic/Latin Lines

The verifier flags any line containing both Arabic and Latin characters. For technical articles whose subject is an English-named product (Obsidian, Kimi K2.6, MCP, ChatGPT), strict separation is impractical:

- **Fix aggressively:** general English technical terms embedded in Arabic prose (e.g., "هذا الـ workflow" → "مسار العمل هذا")
- **Leave alone:** proper nouns and product names with no accepted Arabic equivalent (Obsidian, Kimi, GitHub, Claude)
- **Isolate when possible:** if a proper noun dominates a paragraph, put it on its own line or in a standalone parenthetical rather than mid-sentence
- **Disclose in chat:** if remaining mixed lines are due to necessary proper nouns, note this when delivering the file

## Final Response Format to Mohamed

- One concise completion message
- Absolute file path
- `MEDIA:<absolute path>` attachment
- Very brief verification notes
- If any access issue happened, explicitly note Camoufox fallback usage and remaining block scope

## Failure Discipline

Do not deliver partial output as final.
If quality checks fail, fix and re-verify before sending.

## Scope Rule

For this user, this skill supersedes old split workflows for YouTube/X/Substack/GitHub content-note generation.
