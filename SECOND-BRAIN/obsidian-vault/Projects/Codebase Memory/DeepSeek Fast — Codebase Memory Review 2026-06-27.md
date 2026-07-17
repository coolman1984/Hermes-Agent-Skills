# DeepSeek Fast — مراجعة فهرسة المستودعات

> تقرير عملي من وكيل `deepseek-fast` بعد قراءة الفهرس التفصيلي وصور الـ MCP Architecture.

**تاريخ المراجعة:** 2026-06-27  
**المصادر:**
- Codebase Memory — Detailed Index 2026-06-27.md (124.4 كيلوبايت)
- Codebase Memory MCP Architecture Snapshots 2026-06-27.md (44.4 كيلوبايت)

---

## 1. Company-Dashboard
`/root/Company-Dashboard` — 153 ملفًا، ~2.5 ميجابايت

### الخريطة العامة
تطبيق ويب متكامل لتحليل P&L مع دعم عربي كامل. خمس طبقات: واجهة (HTML/JS) ← خادم (Node.js) ← محرك تقارير (Python) ← قاعدة بيانات (SQLite) ← مستخرج ملفات (Python).

### الملفات المركزية (اقرأها أولاً قبل أي تعديل)

| الملف | لماذا |
|---|---|
| `AGENTS.md` (1443 سطر) | العقد الملزم لكل وكيل — اقرأ قبل اللمس |
| `ARCHITECTURE.md` (168 سطر) | خريطة الطبقات الخمس — الـ dependency rule |
| `Agent.md` (230 سطر) | أنماط الـ Pre-Computation — أكبر درس في المشروع |
| `FEATURES.md` (326 سطر) | كتالوج كل feature وطريقة إضافة feature جديدة |
| `schema.sql` + `db_schema.py` | تعريف قاعدة البيانات — كل شيء مبني عليها |
| `mcp_server/tools.py` (418 سطر) | بوابة الأدوات التي يشوفها الوكيل — bigger picture |
| `server.js` (1593 سطر) | قلب الخادم — routing, DB connection |
| `brain/search.py` (89 سطر) | محرك البحث في المعرفة — مستعمل من MCP |
| `reports/generate.py` + `render.py` | عمود فقري للتقارير |

### ما يهم الوكيل قبل التعديل
- `scripts/legacy/` يحتوي ملقات قديمة — لا تبنِ عليها
- `AGENTS.md` يفرض الـ mandatory protocol — خالفه على مسؤوليتك
- `knowledge/` و `brain/` هما "العقل الثاني" — أي إضافة Feature تحتاج تحديثهم
- كل التقارير معرفة في `reports/definitions.py`
- خط الـ Data Pipeline واضح: raw ← extract ← map ← ingest ← reports

### تعقيد MCP
- 2,716 عقدة — الأكبر بين المستودعات كلها
- 9,652 حافة — CALLS (3204), DEFINES (2531), USAGE (1289)
- 10 باقة Python خارجية: arabic-reshaper, reportlab, weasyprint, pdfplumber, extract-msg, إلخ

---

## 2. llm-wiki-agent
`/root/llm-wiki-agent` — 66 ملفًا، ~452 كيلوبايت

### الخريطة العامة
نظام Wiki ذكي يغذّيه LLM — ياخذ مستندات خام (خاصة EGX والاستثمار المصري) ويحوّلها إلى صفحات Wiki مترابطة بأدوات Ingest/Query/Lint.

### الملفات المركزية (اقرأها أولاً)

| الملف | لماذا |
|---|---|
| `AGENTS.md` أو `CLAUDE.md` (221 سطر) | بروتوكول الوكيل — Schema, Directory Layout, Ingest Workflow |
| `tools/ingest.py` (370 سطر) | قلب الـ Ingest pipeline — يحول raw → wiki |
| `tools/lint.py` (415 سطر) | مصحّح الوصلات المكسورة والأيتام |
| `tools/build_graph.py` (1244 سطر) | باني الـ Knowledge Graph — أضخم ملف في المشروع |
| `tools/query.py` (214 سطر) | واجهة الاستعلام عبر RAG |
| `tools/refresh.py` (173 سطر) | إنعاش الصفحات من المصادر الخام |
| `wiki/index.md` + `wiki/overview.md` | دليل الـ Wiki نفسه |
| `raw/egx-system.md` | المستند الخام الأهم (يحدد ترتيب القراءة الإلزامي) |

### ما يهم الوكيل قبل التعديل
- معظم المحتوى عربي — لا تفترض الإنجليزي
- الصفحات الخام في `raw/` هي المصادر الأصلية، الـ Wiki مشتق منها
- أدوات الـ tools الستة (ingest, query, lint, refresh, build_graph, file_to_markdown) مترابطة — تغيير ingest بيأثر على الباقي
- `wiki/concepts/` و `wiki/entities/` و `wiki/sources/` لها Schema ثابت (Summary, Core Claims, Connections, Contradictions)
- `wiki/syntheses/` تركيب أسبوعي — نمط مختلف

### تعقيد MCP
- 649 عقدة فقط — أصغر من GenericAgent لكن أكبر من CDCC
- 916 حافة — DEFINES (576), CALLS (126)
- Hotspot: `read_file` في ingest و lint (Fan-in 6 لكل)

---

## 3. company-data-command-center
`/root/company-data-command-center` — 16 ملفًا، ~19 كيلوبايت

### الخريطة العامة
مشروع صغير جدًا — هيكل عظمي لخط أنابيب بيانات من الملفات إلى التقارير. لا يزال في بدايته.

### الملفات المركزية

| الملف | لماذا |
|---|---|
| `schema.sql` + `docs/data-model.md` | كل ما هو موجود — بائع البيانات |
| `docs/ingestion-contract.md` | عقد الـ Ingestion (Pipeline shape, Stages) |
| `src/files_to_reports/` (4 مجلدات فارغة) | ingest, normalize, reports, store — هيكل فقط |

### ما يهم الوكيل
- لا يوجد كود تنفيذي فعلي — كل `__init__.py` فارغ أو شبه فارغ
- `docs/week-one-plan.md` بالعربية — يوثق خطة الأسبوع الأول
- أي تطوير يحتاج بداية من `schema.sql` و `src/files_to_reports/`

### تعقيد MCP
- 101 عقدة، 101 حافة — الأصغر
- معظم العقد Sections و Variables من الـ markdown

---

## 4. GenericAgent
`/root/GenericAgent` — 128 ملفًا، ~4.2 ميجابايت

### الخريطة العامة
وكيل AI متعدد المنصات (إصدار صيني) — له Frontends متعددة (Telegram, Feishu, WeChat, DingTalk, QQ, Streamlit, Qt Desktop) + محرك LLM خاص به + تحكم في المتصفح عبر TMWebDriver + ذاكرة ونظام SOP.

### الملفات المركزية

| الملف | لماذا |
|---|---|
| `agentmain.py` + `ga.py` | قلب GenericAgent — الـ agent loop و handler |
| `llmcore.py` (948 سطر) | طبقة LLM — كل الجلسات (Claude, OpenAI, MiniMax) |
| `TMWebDriver.py` (285 سطر) | تحكم المتصفح — أكبر أداة خارجية |
| `frontends/qtapp.py` (1747 سطر) | واجهة Qt — أضخم ملف فرونت |
| `frontends/fsapp.py` (548 سطر) | واجهة Feishu (لارك) |
| `frontends/tgapp.py` (159 سطر) | واجهة تليجرام |
| `assets/tmwd_cdp_bridge/background.js` (394 سطر) | إضافة متصفح للتحكم عن بُعد |
| `memory/autonomous_operation_sop/` | سلسلة SOPs للتشغيل الذاتي |
| `memory/skill_search/` | محرك بحث المهارات (105K بطاقة) — مثير للاهتمام |

### ما يهم الوكيل قبل التعديل
- 90% من الوثائق بالصينية — الـ SOPs كلها بالصينية
- GenericAgent مستقل تمامًا ولا يتصل بنظام Hermes
- توجد ملفات إعداد حساسة داخل المشروع، لذلك لا تُعرض محتوياتها ولا تُنسخ خارج الجهاز
- `frontends/` متنوعة جدًا — نفس المنطق بـ 8 واجهات مختلفة
- `temp/` يحتوي ملفات مؤقتة
- `tests/` ضعيفة — 2 ملفات اختبار فقط

### تعقيد MCP
- 1,377 عقدة، 3,662 حافة
- CALLS (901), DEFINES (1275), USAGE (686)
- أكبر package داخلية: `qtapp` (93 عقدة) ← `llmcore` (31 عقدة)
- فرونتends تشترك في `chatapp_common` (26 عقدة)

---

## 5. Hermes-skills (لمحة سريعة فقط)
`/root/.hermes/skills` — 925 ملفًا، ~12.2 ميجابايت

### الخريطة العامة
هذه هي مكتبة المهارات الكاملة لنظام Hermes الخاص بمحمد. ليست "مستودعًا" بالمعنى التقليدي — إنها ذاكرة إجرائية.

### التقسيم
- **creative/:** baoyu (articles, comics, infographics), ASCII video, p5js, manim, excalidraw
- **autonomous-ai-agents/:** hermes-agent (السكل الرئيسي), mohamed-coding-team, control bridge
- **openclaw-imports/:** orchestration-ceo, researcher, architect, builder, tavily search
- **software-development/:** senior-software-engineer, TDD, plan, systematic-debugging
- **note-taking/:** كل مهارات محمد العربية (المجلس، factory الكتب، intelligence vault)
- **research/:** egyptian-equity-workflow, llm-wiki, last30days
- **mlops/:** fine-tuning, inference, huggingface, vllm, dspy

### ما يهم الوكيل
- لا تعدل شيئًا هنا من وكيل `deepseek-fast` إلا بأمر مباشر (cross-profile guard)
- 668 ملف .md + 105 ملف .py + ملفات XSD و JSON
- `.archive/` يحتوي مهارات قديمة (claude-code, codex, kanban)
- `/research/README.md` (1256 سطر) — وثيقة last30days الضخمة

---

## أين تصلح فكرة Codebase Memory في نظام محمد

### الفكرة
فهرسة المستودعات وإنشاء خريطة قابلة للاستعلام عنها قبل أن يقرأها الوكيل واحدًا واحدًا.

### أين تخدم محمد أكثر

**1. قبل أي مهمة في Company-Dashboard**
الـ Detailed Index يعطي الوكيل خريطة فورية: "أنا عايز أعدل في التقارير، أروح على `reports/generate.py` و `reports/definitions.py`". بدون الفهرس، الوكيل هيقرأ ملفات عشوائية أو يفوت ملفات مهمة.

**2. وكيل جديد بيشتغل أول مرة**
بدل ما يقرأ AGENTS.md كاملاً (1443 سطر)، يشوف الـ Index ويقرر بسرعة أين يبدأ.

**3. فهرسة مستودعات EGX / الاستثمار**
llm-wiki-agent هو المستودع الأكثر استفادة — فيه 52 ملف .md بالعربية، كثير منها EGX. الفهرس يساعد في تحديد الروابط بين concepts و entities و sources بسرعة.

**4. التدقيق الدوري (Cron)**
يمكن عمل cron job يفحص هل الملفات التي تغيرت تستدعي إعادة فهرسة — مثل `mohamed-system-environment-audit` ولكن للمستودعات.

### حدود الفكرة
- الفهرس يمنح خريطة ثابتة — لا يخبرك ما الذي تغير في الأسبوع الأخير
- Hermes-skills فهرسته (925 ملف) مفرط — يحتاج فلترة للملفات الأهم فقط
- GenericAgent بالصينية — الفهرس لا يترجم، يعطي أسماء فقط

---

## خلاصة سريعة للمستودعات

| المستودع | الملفات | الحجم | عقد MCP | اللغة المسيطرة | الحالة |
|---|---|---|---|---|---|
| Company-Dashboard | 153 | 2.5 ميغا | 2716 | Python + JS | ناضج، في إنتاج |
| llm-wiki-agent | 66 | 452 كيلو | 649 | Markdown + Python | ناضج، نشط |
| company-data-command-center | 16 | 19 كيلو | 101 | Python (هيكل) | في البداية |
| GenericAgent | 128 | 4.2 ميغا | 1377 | Python + صيني | ناضج لكن منفصل |
| Hermes-skills | 925 | 12.2 ميغا | — | Markdown | المكتبة الرئيسية |

---

**ملاحظة:** الـ MCP Architecture Snapshots يحتوي بيانات JSON كاملة لكل مشروع (أسماء الحزم، نقاط الدخول، hotspots، قائمة الملفات كاملة) — يمكن لأي وكيل استخدامها مباشرة بدل الفهرسة من الصفر.
