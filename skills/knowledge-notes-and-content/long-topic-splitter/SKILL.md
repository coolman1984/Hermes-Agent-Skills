---
name: long-topic-splitter
description: Convert any long source Mohamed cares about into a reusable knowledge
  asset, then split it into practical derivative outputs such as summaries, translations,
  use cases, post ideas, carousel outlines, action lists, links, and skill/memory
  opportunities.
version: 1.0.0
author: Hermes + Mohamed
license: MIT
tags: [content, knowledge-asset, splitting, repurposing, notes]
metadata:
  tags:
  - long-content
  - repurposing
  - note-taking
  - arabic-workflow
  - youtube
  - x
  - substack
  - github
---

# Long Topic Splitter

Use this skill when Mohamed wants to benefit from a long source by turning it into a structured knowledge asset and then splitting it into smaller useful outputs.

This skill was distilled from reviewing and locally inspecting `charlie947/social-media-skills`, especially the idea that one long source should become the master asset and then fan out into platform-specific or task-specific outputs.

## When to Use

Use for:
- a YouTube video or transcript
- a long X/Twitter article or thread
- a Substack post or note
- a GitHub repository note
- a long Markdown file
- a pasted long text
- a research report or market memo
- any topic Mohamed says he wants to split, repurpose, or extract value from

Do not use for:
- short one-off questions
- private/public posting without explicit approval
- automatic publishing to any platform
- raw code extraction

## Core Principle

Treat the source as a single master knowledge asset first.

Then split it into derivative outputs only after the master asset is understood, saved, and verified.

The workflow is:

1. capture the source
2. create or reuse the full note
3. extract the core idea map
4. generate practical derivatives
5. save outputs as Markdown
6. verify files exist and contain the required sections

## User Preferences

### Voice Mode (Mohamed)

When Mohamed asks to use Nate B Jones style:
- load `nate-b-jones-style-card`
- apply its structure and rhetoric to the generated outputs
- keep Arabic-first delivery
- keep analysis-heavy narrative with actionable close
- never claim identity or first-person as Nate

### General Preferences

- Arabic first.
- Use professional Egyptian Arabic.
- If translating, preserve the writer’s tone and sequence.
- Do not mix English inside Arabic lines unless it is a literal URL, username, path, or unavoidable proper noun.
- Keep necessary English on its own line when possible.
- Prefer text-only outputs.
- Do not include images unless Mohamed asks or the image is necessary for understanding.
- Do not copy code verbatim; explain code conceptually.
- Do not publish anything automatically.
- Save outputs under Android Downloads.

## Source-Specific Base Skills

Before using this splitter, use the correct source skill to create the master note:

- YouTube transcript / summary: use Mohamed’s YouTube transcript workflow or `youtube-content` if applicable.
- X/Twitter long article: use `x-article-note-drop`.
- Substack article/note: use `substack-article-note-drop`.
- GitHub repository: use `github-repo-doc-drop`.
- Plain long file/text: read or save the source directly, then continue with this skill.

If a base note already exists, read it and split from that rather than re-fetching the source.

## Output Location

Default split-output folder:

```text
/storage/emulated/0/Download/long-topic-splits/<safe-source-name>/<title-or-id> - <YYYY-MM-DD>/
```

Recommended files:

```text
00-master-summary.md
01-idea-map.md
02-practical-use-cases.md
03-post-ideas.md
04-carousel-outline.md
05-action-list.md
06-links-and-sources.md
07-memory-and-skill-opportunities.md
```

If the source-specific note already lives in another folder, add a small `splits/` folder beside it when that is clearer.

## Required Master Note Sections

Before splitting, verify the source note contains as many of these as relevant:

- metadata and source URL
- long Arabic summary
- professional opinion
- full translation if foreign-language article and Mohamed may want to read it fully
- 10 practical use cases
- arguments / claims / sections breakdown
- links explained one by one
- strengths and weaknesses
- how Mohamed can use it
- executive conclusion

If the master note is missing a critical section, update the master note first.

## Splitting Outputs

### 1) Idea Map

Extract:
- core thesis
- supporting ideas
- examples
- assumptions
- repeated patterns
- interesting contradictions
- what is new or useful for Mohamed

### 2) Practical Use Cases

Produce 10 to 20 use cases, depending on source richness.

Each use case should include:
- what it enables
- when Mohamed would use it
- what the expected output is

### 3) Post Ideas

Generate short-form content ideas from the source.

Use multiple angles:
- actionable how-to
- contrarian take
- comparison
- mistakes list
- before/after
- present/future
- lessons learned
- resource list

Do not write publish-ready posts unless Mohamed asks. Start with ideas and angles.

### 4) Carousel Outline

Create text-only carousel structure:
- slide 1: strong hook
- slides 2 to N-1: one idea per slide
- final slide: practical takeaway or call to action

Rules:
- one idea per slide
- short text per slide
- no image generation by default
- offer image prompts only if Mohamed asks

### 5) Action List

Convert insights into tasks:
- quick wins
- experiments
- automations
- files/skills to create
- follow-up research

Separate:
- do now
- do later
- needs Mohamed decision

### 6) Links and Sources

Explain each meaningful link:
- what it points to
- why it matters
- whether Mohamed should open it
- whether it is a source, tool, example, or promotional link

### 7) Memory and Skill Opportunities

Look for durable patterns:
- user preference to save to memory
- reusable workflow to save as a skill
- existing skill that should be patched
- project convention that should be updated

Only save durable facts. Do not save temporary task progress.

## Security and Scope Rules

When the source is a GitHub repository or external skill collection:
- clone or inspect locally before installing anything
- vet for credentials, external services, scripts, shell commands, and browser/cookie access
- do not install full third-party skill packs by default
- prefer borrowing patterns and building Mohamed-specific skills
- report risky dependencies separately

When the source mentions API keys or tokens:
- never expose values
- reference environment variables only by name
- require explicit approval before setting or using credentials

## Verification Checklist

Before final response, verify:
- master note exists or was updated
- split folder exists if created
- expected derivative files exist
- source URL is preserved
- no raw code blocks were copied unless explicitly requested
- Arabic structure is readable
- any translation section appears after summary and opinion when relevant
- final response includes paths and a concise summary

## Final Response Pattern

Keep the response concise:

- say what was created or updated
- attach or list the main file path
- list the most useful derivative outputs
- mention any security or access caveats
- ask only if a meaningful next decision is needed

Do not paste the full split content into chat unless Mohamed asks.

## Practical Lesson

The useful part of a social-media skill pack is not blindly installing all skills. The useful pattern is the long-source pipeline:

long source → master note → idea map → use cases → post ideas → carousel outline → action list → memory/skill updates

Use this pattern for Mohamed’s YouTube, X, Substack, GitHub, and research workflows.
