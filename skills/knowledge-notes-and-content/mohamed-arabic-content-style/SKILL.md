---
name: mohamed-arabic-content-style
description: Use when producing Arabic notes, summaries, translations, media reports, or Second Brain content for Mohamed. Enforces Arabic-only line discipline and article-style source presentation.
version: 1.2.0
author: Hermes + Mohamed
license: MIT
metadata:
  tags: [arabic, style, mohamed, notes, translation, media]
---

# Mohamed Arabic Content Style

## Overview

This skill captures Mohamed's global writing requirements for Arabic content files and notes.

It applies across media notes, translations, summaries, research notes, vault additions, and any content intended for Mohamed's Second Brain or Downloads file-drop workflow.

## ⚠️ ABSOLUTE RULE — Never Mix English in Arabic Lines

**This is the most violated rule. Mohamed gets visibly frustrated when it's broken.**

### The Rule

**English characters, words, file paths, function names, variable names, URLs inside parentheses — NONE of these belong inside an Arabic sentence.**

Every English element must be on its own standalone line.

### ❌ Wrong Patterns (I keep doing these — STOP)

```
في base.py السطر 2466، send() بتستدعي send_typing()
قلت لك من الأول إن الـ suppress_typing هو الحل
افتح ملف AGENTS.md و شوف القواعد
```

### ✅ Right Patterns

```
في الملف:
base.py

السطر 2466:
send()
بتستدعي:
send_typing()

ـ

قلت لك من الأول إن:
suppress_typing
هو الحل

ـ

افتح ملف:
AGENTS.md
وشوف القواعد
```

### Common Violations I Keep Repeating

| السياق | ❌ غلط | ✅ صح |
|--------|--------|-------|
| اسم ملف | في `telegram.py` السطر | في ملف: `telegram.py` — السطر |
| دالة | `send_typing()` بتنادى | `send_typing()` — بتنادى |
| قيمة تقنية | `suppress_typing=True` | القيمة:`suppress_typing=True` |
| أمر | شغل `git pull` | شغل الأمر:`git pull` |
| متغير | `DB_PATH` مبيشتغلش | المتغير:`DB_PATH` — مبيشتغلش |
| مسار | في `/root/Documents` | في المسار:`/root/Documents` |

### Penalty Enforcement

**If you catch yourself writing an English character right next to an Arabic character in the same line — stop and rewrite the whole paragraph.** Every line is a fresh check.

## Non-Negotiable Rules

### Egyptian Professional Official Tone

Use a professional Egyptian-friendly official Arabic register:

1. Use clear professional Egyptian Arabic, not heavy classical Arabic.
2. Keep it easy, direct, and immediately understandable.
3. Short-to-medium sentences with one idea per sentence.
4. Paragraph pattern: main idea -> brief explanation -> practical conclusion.
5. Prefer direct verbs over heavy bureaucratic phrases.
6. Avoid archaic wording, rhetorical padding, decorative exaggeration, and academic stiffness.
7. Avoid ambiguity: choose terms with one operational meaning.
8. Keep transitions explicit so Mohamed reaches the idea quickly.
9. If a sentence sounds like a formal translated article rather than a clear Egyptian professional explanation, rewrite it simpler.

9. Arabic content should stay Arabic-only within each line.
10. Do not mix English words inside Arabic sentences — **ever**. Mixing them breaks word order and makes the text unreadable for Mohamed.
11. Mixed Arabic/English lines break reading direction and visual order for Mohamed.
12. Translate generic technical terms into Arabic when possible.
13. If an English term is necessary, put it on a separate standalone line.
14. URLs can remain as standalone raw lines.
15. Do not write source/post content as `line 1 / line 2` or numbered transcript fragments unless Mohamed explicitly asks for forensic extraction.
16. Present original posts as a coherent professional article that preserves the writer's voice, logic, and flow.
17. Keep style warm, clear, professional, and Egyptian-Arabic friendly.
18. Do not over-localize proper names in a way that hides the source; transliterate or place the English name separately if needed.
19. **Use expressive emojis and icons** in Telegram/chat responses — they make the tone warmer and the structure clearer. Pick emojis that fit the context (👀 for insight, ⚡ for action, 🔍 for investigation, ✅ for completion, 💪 for work done, 🛑 for warnings, etc.).
20. Avoid long English code snippets in chat — Mohamed prefers ideas and logic, not raw code blocks unless specifically requested.

## Preferred Source Presentation

Bad pattern:

```text
سطر 01:
الكاتب يقول كذا.

سطر 02:
ثم يقول كذا.
```

Good pattern:

```text
الكاتب يبدأ من فكرة واضحة: المشكلة ليست في أن الوكيل لا يعرف يتصفح، بل في أنه ينسى ما تعلمه بعد انتهاء الجلسة. من هنا يبني حجته حول ضريبة الاكتشاف المتكررة، ثم ينتقل إلى الحل العملي: تحويل المسار الناجح إلى مهارة مكتوبة يقرأها الوكيل القادم قبل البداية.
```

## Story Explanation Mode

When Mohamed asks to explain a technical or abstract idea as a story, especially with wording like:

```text
اشرحلي بطريقة شيقة
قصة مصرية
لوجيك واضح
```

Use a complete Egyptian-style story with characters, a concrete setting, and a clear business or daily-life analogy. The story must still teach the operational logic step by step, not become decorative fiction.

Good structure:

1. Open with a familiar Egyptian scene.
2. Introduce the real problem through the character's pain.
3. Map each technical layer to a physical or business role.
4. Make the logic visible through cause and effect.
5. End with the practical principle Mohamed should remember.

For technical terms, translate the role when possible. If a necessary English term remains, place it on a standalone line as usual.

## English-Term Handling

If a term is generic, translate it:

- scraper → أداة استخراج بيانات
- selector → محدد
- workflow → مسار عمل
- API → واجهة بيانات
- endpoint → نقطة وصول
- benchmark → قياس مستقل
- version control → إدارة نسخ

If a term must remain English, put it alone:

```text
المسار يحفظ في ملف مهارة باسم:

SKILL.md

ثم يقرأه الوكيل التالي قبل التنفيذ.
```

## Propagation When Mohamed Says "Generalize This"

If Mohamed asks to apply these rules globally or to all skills, do not only save them in memory.

Apply them in this order:

1. Keep this skill as the canonical style rule.
2. Patch the active workflow skill that generated the mistake, especially `mohamed-unified-media-drop` for links and media notes.
3. If the work happens through Telegram, add or update the Telegram channel prompt for Mohamed's home chat/profile so other agents in the same Hermes profile see the rule even before loading a skill.
4. Keep the assistant's local vault separate from Mohamed's Google Drive Second Brain; style propagation is not permission to write into either vault.
5. Verify by reading the updated skill or config and checking the exact rule text is present.

## English-Book Mode (When Mohamed Explicitly Requests English)

If Mohamed asks for an English book, apply the same quality philosophy in English:

1. Use professional, clear, simple, formal business English.
2. Keep sentences short-to-medium and idea-driven.
3. Paragraph flow: main point -> brief explanation -> actionable conclusion.
4. Avoid jargon-heavy, bureaucratic, or inflated wording.
5. Avoid decorative fluff and repeated claims.
6. Keep terminology consistent across chapters, tables, and captions.
7. Prefer plain, precise verbs and concrete nouns.
8. Use explicit transitions to preserve logic.
9. Maintain readability for non-native readers.
10. Keep tone executive-friendly and training-ready.

Mini rewrite examples:

- Weak: "We are pleased to inform you that we have initiated the necessary actions to address the aforementioned deficiencies."
- Better: "We have started the required actions to address the identified gaps."

- Weak: "Kindly provide your valuable feedback regarding the above."
- Better: "Please share your feedback so we can finalize the next step."

## Verification Checklist

Before delivery:

- [ ] No Arabic body line contains embedded English words.
- [ ] URLs are standalone lines.
- [ ] Necessary English terms are standalone lines.
- [ ] Generic technical terms are translated.
- [ ] Source content is presented as a coherent article, not numbered lines.
- [ ] If writing to a file, scan for mixed Arabic/English lines and fix them before delivery.
- [ ] File exists and is non-empty when writing to disk.
- [ ] No placeholders remain.
- [ ] Emojis are used in chat/Telegram responses to add warmth and clarity.
- [ ] No large code blocks in chat — focus on ideas and logic instead.

## Common Pitfalls

1. Preserving order by numbering every sentence. This feels robotic and Mohamed dislikes it.
2. Leaving English technical terms inside Arabic sentences. This breaks visual flow.
3. Translating proper nouns inconsistently across the same file.
4. Blind global replacements that corrupt words. Use targeted review and verification.
5. Treating raw transcript structure as the final writing style.
6. Saving the rule only in memory. For repeatable behavior, update the relevant skill and, when appropriate, the channel prompt too.
7. Assuming another AI will comply without loading skills or profile prompts. If the agent is outside this Hermes profile, explicitly provide the style rules.
8. Getting lazy with English-Arabic mixing mid-session — after several Arabic replies, the agent tends to start inlining English terms again. This breaks readability. Every message is a fresh check against the rule. During coding sessions (Company Dashboard, EGX, Hermes source), technical terms are abundant — this is when the rule gets violated most. Scan every line of your draft response before sending. If any Arabic character touches any English character in the same line, rewrite the whole paragraph.
9. Forgetting emojis when the response is purely Arabic. Without emojis, the tone feels flat and robotic. Add at least 2–3 context-fitting emojis per Telegram reply.
10. Dropping code/terms into Arabic chat — Mohamed does not want code in chat. If code is necessary, put it as a file in Downloads with a summary in chat.
11. Coding-session Arabic drift — this is the most dangerous pitfall. During technical work (debugging, code review, feature implementation), the agent naturally reaches for technical English terms (file names, function names, variable names, commit hashes, API endpoints). The temptation to inline them is strongest exactly when the Arabic response needs them most. The fix: write every technical element on its own line with a separator (dash, newline, or emoji marker), then build the Arabic sentences around them. Never do "في telegram.py السطر 2466". Always do "في الملف: telegram.py — السطر 2466".
