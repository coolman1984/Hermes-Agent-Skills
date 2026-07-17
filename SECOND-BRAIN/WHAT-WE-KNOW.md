# WHAT WE KNOW — Distilled Operator Knowledge

Generated: `2026-07-17T11:39:05Z`

This file is a **high-signal export** of durable knowledge. Full detail lives in the folders beside it.

---

## 1) Operating principles

- Context first, then rules, then memory, then verification, then automation.
- Do not jump to autonomy before the foundation is stable.
- Do not mix temporary task noise with durable knowledge.
- Record conflicts instead of hiding them.
- Prefer compounding systems over one-off cleverness.
- For investing: official/primary sources first when money is involved.
- Arabic on Telegram; English on CLI/terminal unless asked otherwise.
- Skills hold procedures. Memory holds durable facts. Vault holds project/knowledge state.

---

## 2) Active systems map

1. **Egyptian equity portfolio OS** (`obsidian-vault/egx_system`, Investing notes, market profiles)
2. **Hermes agent OS** (skills library + operator memory + profiles)
3. **Local knowledge wiki** (`llm-wiki`, `llm-wiki-agent`)
4. **Intelligence vault for ideas** (`obsidian-vault/Ideas/Intelligence Vault`)
5. **Book factory / content products** (vault projects + content skills)
6. **Media/source ingestion** (`media-source-notes`)
7. **Compound / company intelligence direction** (projects notes + compound-ai-vault)

---

## 3) Live snapshot (source of truth at export)

```markdown
# الملخص الجاري

## الهدف الحالي
تثبيت خطة تبني مرحلية للوكلاء تبدأ بالسياق وتنتهي بالأتمتة.

## ما تم إنجازه
- إنشاء خزنة منظمة للذاكرة.
- بناء هيكل الملفات والقوالب.
- توثيق قاعدة مراجعة الملخص الجاري قبل أي مهمة مهمة.
- اعتماد خطة مرحلية لتبني الوكلاء.
- إنشاء بروفايل Hermes باسم operator مع alias تشغيلي.
- إنشاء بروفايلَي market وmarketlab وضبط السوق الإنتاجي بشكل أولي.
- إنشاء مساحة egx_system المحلية وملء ملفاتها التشغيلية الأولى.
- تعبئة positions.csv وwatchlist.txt.
- إنشاء مهارة egx-daily-cycle.
- تشديد egx-daily-cycle ليُنتج Markdown وJSON ويَفشل بصراحة عند parsing error.
- إنشاء مهارة egx-decision-gate.
- إصدار تقرير يومي محلي نهائي + JSON.
- إصدار مذكرة قرار محلية نهائية بحكم: مراقبة.
- تشغيل market gateway بنجاح عبر market gateway run.
- إنشاء 3 cron jobs محلية فقط: daily refresh, decision memo, weekly review.
- تفعيل قفل المراجعة البشرية في egx_system/portfolio/rules.md.
- إنشاء note مشروع egx_system في الخزنة.
- اختيار مصدر GitHub عملي للطريقة ووضع مراجعة مختصرة له في الخزنة.
- تهيئة نسخة أولية فعالة من LLM Wiki في /root/llm-wiki-agent مع صفحات البداية والـ graph.
- إدخال أول دفعة من مصادر EGX داخل الويكي المحلي وتحديث الفهرس والـ overview والجراف.
- تنظيف فهرس خزنة الذكاء وتحديث التصنيفات والروابط والتركيبات وقائمة المراجعة.
- إنشاء صفحة دورة الذكاء الأسبوعية وربطها بمشروع الويكي المحلي.
- إدخال الدفعة الثانية من الحالات القطاعية في الويكي المحلي: مصفوفة تقييم القطاعات وتحليل خريطة أبريل مقابل الدستور، مع تحديث الفهرس والنظرة العامة والجراف.
- تشغيل دورة الذكاء الأسبوعية الأولى واختيار تجربة مراجعة النصوص البيعية كحركة الأسبوع، مع تثبيت تقوية نظام الوكلاء وركن صفحات الويب التفاعلية مؤقتًا.
- 🆕 إطلاق مشروع Compound: محرك المعرفة المتراكمة — توصيل Obsidian بسرب وكلاء عبر MCP لاكتشاف الرؤى تلقائيًا. الخطة والبحث في Projects/. في Phase 0.
- إنتاج ثلاث عينات مراجعة نصوص بيعية عامة وصياغة عرض خدمة أولي خلال أربع وعشرين ساعة.
- تأسيس مشروع مركز تقارير وتشغيل ذكي للشركات كمسار ضيق: ملفات مبيعات إلى قاعدة محلية وتقرير بمصدر لكل رقم.
- إنشاء قسم الشرح والبحث والتفكير وتثبيت كتالوج طرق مستقل: بطريقتنا، فلسفة، وتأصيل.
- إضافة طبقة بحث مستعارة من مهارة الميديا إلى تأصيل دون دمج المهارات أو تغيير وظيفة أي مهارة.
- إنشاء مهارة تشغيلية لشخصية محمد وأسلوبه ونمط قراراته، مع مرجع محدث يوجه تخصيص الردود وتحديث الذاكرة والمهارات عند ظهور إشارات مستقرة.
- إنشاء فريق بروفايلات خلفية على باقة أوبن كود جو: deepseek-pro، deepseek-fast، kimi-code، glm-go، minimax-go، مع اختبار تشغيل ناجح ومهارة إدارة دائمة باسم mohamed-opencode-go-worker-profiles.
- إنشاء تجربة Codebase Memory أولى: تثبيت codebase-memory-mcp محليًا، فهرسة Company-Dashboard وllm-wiki-agent وcompany-data-command-center وGenericAgent، وإنشاء فهرس تفصيلي محلي داخل Projects/Codebase Memory.
- 🆕 تثبيت قرار ذاكرة مشروع Compound: البداية بـ Cognee كطبقة ذاكرة أساسية، ثم Graphiti كطبقة زمنية لاحقًا، ثم Onyx كواجهة بحث مؤسسية عند التوسع. تم حفظ الحالة في note مستقلة داخل Projects/.

## ما يجب أن يظل حيًا
- السياق أولًا.
- القواعد ثم الذاكرة ثم التحقق ثم الأتمتة.
- مصدر وثقة وصلاحية لكل سجل مهم.
- كتالوج الشرح: بطريقتنا للتنظيم، فلسفة لليه قبل إزاي، وتأصيل كطريقة ثالثة مستقلة من الأصل إلى التطبيق، مع طبقة بحث اختيارية لا تخلطها بمهارة الميديا.
- تخصيص الردود لمحمد يجب أن يبنى على إشارات مثبتة: تفضيلات صريحة، أنماط متكررة، وحدود واضحة بين الذاكرة والمهارات والخزنة.

## القرارات غير القابلة للتراجع بسهولة
- عدم القفز إلى الاستقلالية قبل تثبيت الأساس.
- عدم خلط المؤقت بالدائم.
- تسجيل التعارضات بدل إخفائها.

## الفرضيات المفتوحة
- أفضل طريقة لربط الذاكرة بالاسترجاع العملي.
- أفضل معايير قياس جودة الذاكرة.

## التعارضات المفتوحة
- 🆕 إطلاق مشروع Compound — Company Intelligence Advisor OS: نظام وكيل ذكي من ٨ طبقات (معرفة ← أنطولوجيا ← أدوات ← تشخيص ← حزام وكيل ← إثبات ← استوديو ← تعلم). الخطة الكاملة في Projects/. Phase 0.

## الخطوة التالية
البدء في Phase 1: إنتاج أول 20 بطاقة معرفة قوية في مجالات المحاسبة والتكاليف والتدفق النقدي.

المسار السابق لتجربة مراجعة النصوص البيعية يظل محفوظًا، لكن لا يزاحم هذا البناء إلا إذا قرر محمد الرجوع إليه.

```

---

## 4) Durable agent memory export

### MEMORY.md

```markdown
Telegram bot: @N8N_mflma1984_bot. Typing-stuck fix uses suppress_typing in base.py + telegram.py.
§
Obsidian: `/root/Documents/Obsidian Vault`; ideas → skill `mohamed-intelligence-vault`.
§
Investing: Egypt official sources → IMF/PMI → Reuters/TradingView.
§
egx_system in /root/.hermes/profiles/market/skills/note-taking/: egx-daily-cycle writes daily-local-review-YYYY-MM-DD.{md,json} and fails loud on parse/input errors; egx-decision-gate reads the latest daily Markdown/JSON and writes decision-local-review-YYYY-MM-DD.md or an ERROR memo.
§
GBrain is runnable via /root/.local/bin/gbrain; camoubrain is /root/.local/bin/camoubrain and captures pages into /root/.gbrain/captures/<timestamp>-<slug>/page.md before import.
§
Content workflows: media=file-drop; books/PDF=factory skills. Methods: Batariqatna, Falsafa, Taaseel (separate; no media-skill merge).
§
EGX watchlist: ADIB ATQA EFID ETEL FWRY ISPH UFO MASP MFPC ORHD SKPC SWDY TMGH.
§
Snapshot: /root/Documents/Obsidian Vault/CURRENT-SNAPSHOT.md.
§
Company-Dashboard: main only; no feature branches; merge/push directly to main by owner instruction.
§
Coding default: load senior-software-engineer. Serious multi-agent workflows: mohamed-agent-loop-os. Governed projects/report factories: persistent-memory-project-governance.
§
Mohamed wants durable fixes for reported problems, not recurring patches. When he flags a bug, find the root cause and add a guard (skill/note/check) so it does not repeat.
§
For content links, default to the `mohamed-unified-media-drop` workflow unless Mohamed explicitly asks for another path. Do not modify that skill unless he asks.
§
Hermes default profile: Grok OAuth works as provider `xai-oauth` model `grok-4.5`; Anthropic Claude works as provider `anthropic` model `claude-sonnet-4-6`; config fallback chain is xai-oauth then anthropic.
§
When Mohamed asks for something technically impossible, do NOT silently substitute an alternative. Say clearly it's impossible, explain why briefly, and ask what he wants instead. Corrected 2026-07-12.
```

### USER.md

```markdown
**Timezone:** GMT+2 (Africa/Cairo)
§
Investing: high-risk but sharia-compliant growth; exclude explicit riba, tobacco, and suspicious activity.
§
Style: warm/direct close-friend tone; emojis okay; المجلس only on request. Requires a verification-first execution protocol: classify intent, identify load-bearing assumptions, verify evidence, self-attack conclusions, and disclose gaps rather than guess.
§
Language: Telegram — Egyptian Arabic; CLI/terminal — English only. Review CURRENT-SNAPSHOT.md before important tasks.
§
Mohamed wants the assistant to own his Egyptian stocks workflow end-to-end as a senior portfolio manager.
§
Media links: Arabic verified source-only notes in Downloads unless Mohamed asks for enrichment.
§
EGX/LLM Wiki: stay anchored in the vault/system; check CURRENT-SNAPSHOT.md and wiki overview first.
§
صور الشاشة: يتوقع OCR تلقائيًا وتمييز الأخضر كمكتمل.
§
Serious coding: Hermes plans/verifies; deepseek-fast writes; deepseek-pro reviews.
§
Company-Dashboard: build continuously on main; no per-task approval.
§
Android control: agent-first Hermes bridges from Telegram, not manual panels.
§
Large agent systems: lightweight router + specialized skills around small core, not monolithic MCP-heavy setup.
§
Mastery tasks: durable class-level skill packages with references, errors, validation logs, zips; not chat-only summaries.
```

---

## 5) Where to find each knowledge type

| Need | Path |
|---|---|
| Ideas & opportunities | `obsidian-vault/Ideas/Intelligence Vault/` |
| Project plans | `obsidian-vault/Projects/` |
| Portfolio operating files | `obsidian-vault/egx_system/` |
| Facts / decisions / conflicts | `obsidian-vault/FACTS`, `DECISIONS`, `CONFLICTS` |
| Wiki synthesis | `llm-wiki/` and `llm-wiki-agent/wiki/` |
| Media learnings | `media-source-notes/` |
| Agent soul/contract | `operator-memory/SOUL.md` |
| Procedures (how-to) | `../skills/` |

---

## 6) Idea intelligence system

The intelligence vault is not a dump. Each idea is refined into:

- clean definition
- market application
- first customer
- smallest sellable version
- category/tags
- connections
- next validation step

Indexes:

- `00 - Index.md`
- `02 - Categories.md`
- `03 - Connections.md`
- `04 - Stronger Combinations.md`
- `05 - Review Queue.md`
- `06 - Media Source Map.md`

---

## 7) Explanation methods catalog (content)

- **بطريقتنا** — organization/method framing
- **فلسفة** — why before how
- **تأصيل** — from origin to application (separate from media skill)

---

## 8) Coding / multi-agent conventions

- Default serious coding skill route: senior software engineer + governed workflows
- Serious multi-agent coding: agent-loop OS / coding team
- Company-Dashboard: main branch only by owner instruction
- Verification before claiming done

---

## 9) Refresh rule

When knowledge changes in the live environment:

1. Update the Obsidian vault / wiki first (source of truth)
2. Re-export into `SECOND-BRAIN/`
3. Refresh `WHAT-WE-KNOW.md` and `MANIFEST.json`
4. Commit: `chore: refresh SECOND-BRAIN YYYY-MM-DD`
