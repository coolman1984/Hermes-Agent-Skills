# Compound — جرد الأصول الموجودة

> **آخر تحديث:** 2026-06-17  
> **حصيلة المسح:** 31 ملف في الخزنة + 7 مستودعات برمجية + 30+ مهارة Hermes  

---

## الطبقة ١: ويكي المعرفة 📚

### الموجود فعلًا ويُعاد استخدامه:

| الأصل | الموقع | ماذا يقدم |
|--------|--------|-----------|
| **LLM Wiki Agent** — أدوات ingest/query/lint/build_graph | `/root/llm-wiki-agent/tools/` | محرك ابتلاع وتحويل المصادر لصفحات ويكي منظمة، مدعوم بـ LLM. فيه 4 أدوات تشغيلية: ingest (ابتلاع)، query (استعلام)، lint (تدقيق)، build_graph (رسم معرفي) |
| **LLM Wiki Agent** — ويكي حي | `/root/llm-wiki-agent/wiki/` | 14 صفحة مصدر + 8 كيانات + 10 مفاهيم + 1 تركيب = نموذج عملي لويكي المعرفة |
| **SwarmVault** — قالب LLM Wiki | `/root/swarmvault/templates/llm-wiki-schema.md` | هيكل كامل للويكي: 3 طبقات، 5 عمليات، أنواع علاقات (يذكر/يدعم/يتعارض/يبني على/يسأل)، قواعد التأريض |
| **Company-Dashboard** — محرك المعرفة (brain/) | `/root/Company-Dashboard/brain/` | 7 ملفات: parse (تحليل Markdown)، search (بحث نصي كامل)، graph (رسم معرفي + backlinks)، data_notes (ملاحظات مولّدة من البيانات)، cli |
| **Company-Dashboard** — FEATURES.md | `/root/Company-Dashboard/FEATURES.md` | نمط بناء Any 1 Feature = Engine (Python) + Endpoint (server.js) + Tab (app.js) + i18n (سلاسل) |
| **قاعدة LLM Knowledge Base** | `Projects/LLM Knowledge Base.md` | منهجية: مصادر خام → ويكي → قواعد ← مراجعة دورية ← أتمتة تدريجية. 4 أنواع صفحات: مصدر، كيان، مفهوم، نظرة عامة |
| **قالب الفكرة** | `Intelligence Vault/Templates/Idea Template.md` | مصفوفة تقييم من 7 معايير — يصلح هيكلًا لبطاقات المعرفة |
| **خدمة جاهزية المستودعات** | `Intelligence Vault/Ideas/2026-06-13-...` | إطار تقييم: تعليمات، مستندات، قواعد، اختبارات، فحوصات — يصلح لفحص جودة الويكي |

### خطة الإنتاج:
- 100 بطاقة معرفة: محاسبة (20)، تكاليف (15)، تدفق نقدي (10)، مخزون (10)، تخطيط مالي (10)، رقابة داخلية (10)، تدقيق (5)، تسعير (5)، أتمتة (10)، وكلاء AI (5)
- استخدام `ingest.py` من llm-wiki-agent كنواة لإنتاج البطاقات آليًا

---

## الطبقة ٢: أنطولوجيا الأعمال 🧬

### الموجود فعلًا ويُعاد استخدامه:

| الأصل | الموقع | ماذا يقدم |
|--------|--------|-----------|
| **Company-Dashboard** — schema.sql | `/root/Company-Dashboard/schema.sql` | هيكل P&L كامل: 59 عمود (إيرادات، تكاليف، هوامش، خصومات، ضرائب)، 3 إصدارات (Actual/T06/T07)، ترميز فترات، جداول المصدر والتتبع (import_run, source_file, row_lineage) |
| **Company Data Command Center** — schema.sql | `/root/company-data-command-center/schema.sql` | 5 جداول: raw_file (ثابت بالمحتوى)، import_run (حالات: running/succeeded/failed/partial)، raw_record (JSON)، entity_sale (مع source_hash لمنع التكرار)، provenance (تتبع كل صف لمصدره)، validation_issue (خطأ/تحذير/معلومة) |
| **LLM Wiki Agent** — build_graph.py | `/root/llm-wiki-agent/tools/build_graph.py` | 1243 سطر: بناء رسم معرفي بتمريرين (محدد + استدلالي بدرجات ثقة)، اكتشاف مجتمعات (Louvain)، تقرير صحة (نسبة orphans، كثافة، عقد إلهية، جسور هشة) |
| **LLM Wiki Agent** — lint.py | `/root/llm-wiki-agent/tools/lint.py` | 414 سطر: فحص الأيتام، الروابط المكسورة، الكيانات الناقصة، التناقضات، العقد الوهمية، الجسور الهشة، المجتمعات المعزولة |
| **Company-Dashboard** — brain/graph.py | `/root/Company-Dashboard/brain/graph.py` | backlinks، التحقق من الروابط، توليد graph JSON، ربط الكيانات بشرائح لوحة القيادة |

### خريطة الربط الأولية:

```
حسابات ← مراكز تكلفة ← منتجات ← عملاء ← موردين
    ↓           ↓          ↓        ↓        ↓
عمليات ← KPIs ← تقارير ← ضوابط ← ملفات
    ↓           ↓          ↓
أدوات ← وكلاء ← مشكلات أعمال
```

---

## الطبقة ٣: مكتبة الأدوات 🛠️

### الموجود فعلًا — محركات استخراج جاهزة:

| الأداة | الملف | الحالة |
|--------|-------|--------|
| **قارئ Excel (.xlsx/.xlsm)** | `Company-Dashboard/extractor/excel_openpyxl.py` | ✅ إنتاجي — خلايا مدمجة، read-only، data_only |
| **قارئ Excel (.xlsb)** | `Company-Dashboard/extractor/excel_xlsb.py` | ✅ إنتاجي |
| **قارئ Excel (.xls)** | `Company-Dashboard/extractor/excel_xls.py` | ✅ إنتاجي |
| **قارئ Excel (COM - Windows)** | `Company-Dashboard/extractor/excel_com.py` | ✅ إنتاجي — 790K صف، تنظيف EXCEL.EXE الشارد |
| **قارئ PDF (+ OCR)** | `Company-Dashboard/extractor/pdf_text.py` | ✅ إنتاجي — pdfplumber + tesseract، دعم عربي |
| **قارئ Word (.docx)** | `Company-Dashboard/extractor/word_docx.py` | ✅ إنتاجي |
| **قارئ CSV/TSV** | `Company-Dashboard/extractor/csv_text.py` | ✅ إنتاجي — كشف ترميز تلقائي |
| **قارئ Outlook (.msg)** | `Company-Dashboard/extractor/outlook_msg.py` | ✅ إنتاجي |
| **محوّل ملفات عام** | `llm-wiki-agent/tools/file_to_markdown.py` | ✅ — Microsoft markitdown لأي صيغة |
| **سجل المستخرجات** | `Company-Dashboard/extractor/registry.py` | ✅ — اكتشاف تلقائي بالامتداد |
| **معالجة عربية** | `Company-Dashboard/extractor/arabic.py` | ✅ — match_key، clean_display، parse_number، أرقام عربية |
| **مساعدات COM** | `Company-Dashboard/extractor/com_utils.py` | ✅ — fill_merged_cells، combine_header_rows |
| **غلاف JSON خام** | `Company-Dashboard/extractor/raw.py` | ✅ — SHA-256 + metadata + warnings |

### أدوات التحليل الموجودة:

| الأداة | الملف | ماذا تفعل |
|--------|-------|-----------|
| **محلل الشذوذ (Guardian)** | `Company-Dashboard/reports/anomaly.py` | 5+ قواعد صريحة: هامش سالب، تآكل هامش، اختفاء عميل، spike مصاريف، z-score. حتمي، غير ML. |
| **محلل التسعير** | `Company-Dashboard/reports/pricing.py` | توصيات: خسارة، خصم زائد، رفع سعر — بقواعد قابلة للتدقيق |
| **محلل الحساسية** | `Company-Dashboard/reports/sensitivity.py` | صدمة ±5% لكل محرك — tornado chart |
| **محلل السيناريوهات** | `Company-Dashboard/reports/scenario.py` | Conservative/Base/Aggressive + compare() |
| **محلل التفكيك** | `Company-Dashboard/reports/decomposition.py` | تفكيك الإيراد/التكلفة |
| **محلل التوقعات** | `Company-Dashboard/reports/outlook.py` | Actual + T06 + T07 |
| **استعلام طبيعي** | `Company-Dashboard/reports/nlquery.py` | offline NLQ: metric + group-by + entity + year + quarter |

### أنماط قابلة لإعادة الاستخدام:
- `extractor/registry.py` — نمط Base Extractor: `is_available()` + `extract_content()` + extension mapping
- `robust-file-extraction/` (مهارة Hermes) — 5 حراس: سلامة الملف، أخطاء المحتوى، تدهور متدرج، كشف ترميز، صمود الدفعات

---

## الطبقة ٤: محرك التشخيص 🏢

### الموجود فعلًا:

| الأصل | الموقع | ماذا يقدم |
|--------|--------|-----------|
| **Guardian (كاشف الشذوذ)** | `Company-Dashboard/reports/anomaly.py` | نموذج عملي لكشف المشكلات المالية آليًا — يصلح أساسًا لمحرك التشخيص |
| **مدقق الويكي** | `llm-wiki-agent/tools/lint.py` | يفحص: أيتام، تناقضات، فجوات، عقد هشة، مجتمعات معزولة — نمط قابل للتطبيق على تشخيص الشركات |
| **محلل الأسئلة الطبيعية** | `Company-Dashboard/reports/nlquery.py` | نموذج للاستعلام دون SQL — يصلح لتحويل أسئلة الإدارة إلى تحليلات |
| **أداة التدقيق** | `Company-Dashboard/reports/validation.py` | إحصاءات + اكتشاف تكرار + فحص القيم الخالية — أساس لطبقة التحقق |
| **قالب مركز التقارير** | `Intelligence Vault/Ideas/2026-06-14-...` | 8 أسئلة تشخيص + 8 مخرجات — أول نسخة لمحرك التشخيص |

### خطة التطوير:
- بناء `diagnostic/engine.py` — يجمع المحللات الموجودة في محرك واحد
- 8 أسئلة أساسية → 8 مخرجات معيارية
- كل تشخيص ← تقرير تلقائي بالقالب الموحد

---

## الطبقة ٥: حزام الوكيل ⚙️

### الموجود فعلًا — نظام تحكم متكامل:

| الأصل | الموقع | ماذا يقدم |
|--------|--------|-----------|
| **AGENTS.md** (Company-Dashboard) | `/root/Company-Dashboard/AGENTS.md` | بروتوكول متعدد الوكلاء: اقرأ أولاً، طالب بمهمتك، سجّل عند الانتهاء، لا تكسر البناء. Task Board + Work Journal |
| **قوالب سير عمل الوكلاء** | `Intelligence Vault/Agent Dynamic Workflow Templates - Codez 2026-06-06.md` | 3 قوالب: مراجعة تضادية، منجم مصادر إلى فرص، فرز محتوى آمن. كل قالب: قارئ محدود الصلاحية ← منفذ ← مراجع مستقل |
| **طبقة حكم الوكلاء** | `Intelligence Vault/Agent Judge Layer for Production Control - 2026-05-13.md` | تصنيف الإجراءات (قراءة/كتابة/خارجي/خطر) + بوابة قرار + سجل (سماح/رفض/تعديل/تصعيد) |
| **عقد روح الوكيل** | `Intelligence Vault/Agent Soul Operating Contract - Tony Simons 2026-05-15.md` | هوية، نبرة، حدود autonom، حق الاعتراض، خريطة مهمة، حلقة مساءلة |
| **حلقة وكيل قابلة للتحقق** | `Intelligence Vault/Ideas/2026-06-11-...` | هدف ← معايير ← منفذ ← مراجع ← ذاكرة. لا تؤتمت قبل إرساء الحكم والذاكرة |
| **خدمة مسار عمل آمن** | `Intelligence Vault/Ideas/2026-06-07-...` | دور + أدوات + محفز + قالب مخرجات + قواعد مراجعة بشرية |
| **GenericAgent — subagent.md** | `/root/GenericAgent/memory/subagent.md` | بروتوكول وكلاء بالملفات: input.txt ← output.txt ← reply.txt. map-reduce للمعالجة المتوازية. ملفات تدخل (_stop, _keyinfo, _intervene) |
| **GenericAgent — hub.pyw** | `/root/GenericAgent/hub.pyw` | مكتشف تلقائي للخدمات، start/stop، قفل فردي، بث المخرجات |
| **GenericAgent — ga.py** | `/root/GenericAgent/ga.py` | تنفيذ كود في صندوق رمل: ملفات مؤقتة، timeout/kill، بث المخرجات |
| **Hermes — MCP Server** | `/root/Company-Dashboard/mcp_server/` | أدوات للقراءة فقط: استعلام DB، توليد تقارير، بحث ويكي — نموذج لأدوات الوكيل |
| **فريق Mohamed للبرمجة** | مهارة `mohamed-coding-team` | هرمية: Claude Code (معماري) ← Codex (مهندس مشرف) ← OpenCode (عمال) ← Hermes (منسق، مدقق، تقارير عربية) |
| **منسق Kanban** | مهارة `kanban-orchestrator` | تفكيك + قواعد مكافحة الإغراء + اكتشاف البروفايلات + توزيع المهام |

### هيكل مهمة الوكيل المعتمد:

```
موجز المهمة: ماذا ولماذا
ملفات المدخلات: مسارات دقيقة
الأدوات المسموحة: قائمة حصرية
الإجراءات الممنوعة: حدود صريحة
المخرجات المتوقعة: شكل ومعايير
قواعد التحقق: كيف نعرف الصحة
مجلد الأدلة: أين يُحفظ الإثبات
بوابة الموافقة البشرية: متى وأين
تقرير الإثبات النهائي: ملخص موثّق
```

---

## الطبقة ٦: نظام الإثبات ✅

### الموجود فعلًا:

| الأصل | الموقع | ماذا يقدم |
|--------|--------|-----------|
| **غلاف JSON الخام** | `Company-Dashboard/extractor/raw.py` | `schema_version`، `source` (SHA-256، bytes، mtime)، `extractor`، `content`، `warnings` — التقاط أمين قبل أي تفسير |
| **جداول التتبع** | `Company-Dashboard/schema.sql` | `import_run` (حالة، عدد صفوف، ملاحظات)، `source_file` (اسم، مسار، SHA-256، مستخرج)، `row_lineage` (كل صف ← ملف مصدر ← صف مصدر) |
| **جداول الإثبات** | `company-data-command-center/schema.sql` | `raw_file` (ثابت المحتوى)، `raw_record` (JSON لكل صف)، `provenance` (كل كيان ← سجل خام مع field_map)، `validation_issue` (خطأ/تحذير/معلومة، رموز آلية، إلحاقي فقط) |
| **مدقق الاستيراد** | `Company-Dashboard/reports/validation.py` | إحصاءات + تكرار + قيم خالية — نموذج للتحقق |
| **نمط المراجعة التضادية** | `Intelligence Vault/Agent Dynamic Workflow Templates` | قارئ ← منفذ ← مراجع مستقل — 3 وكلاء منفصلين لنفس المهمة |
| **حالة Guardian المرئية** | `Company-Dashboard` — guardian_state.json | تتبع التنبيهات التي رآها المستخدم + شارة "جديد" |

### سجل الإثبات المعتمد لكل نتيجة:

```
الملف المصدر
الصفوف المستخدمة
المعادلة المستخدمة
نتيجة الحساب
نتيجة التحقق
ملخص استدلال الوكيل
الموافقة البشرية
النسخة النهائية
```

---

## الطبقة ٧: استوديو المخرجات 📊

### الموجود فعلًا — جاهز للإنتاج:

| المخرج | الأصل | الحالة |
|--------|-------|--------|
| **لوحة قيادة HTML** | `Company-Dashboard/index.html` + `app.js` (2571 سطر) + `i18n.js` (824 سطر) | ✅ إنتاجي — RTL عربي، Chart.js، 10+ تبويبات، 4 نقاط تكسر responsive |
| **خادم API** | `Company-Dashboard/server.js` (1592 سطر) | ✅ إنتاجي — 20+ endpoint، better-sqlite3، متعدد العملاء، تصدير CSV/XLSX/PDF |
| **تقارير JSON/CSV** | `Company-Dashboard/reports/generate.py` | ✅ — 9 تقارير مسماة، غلاف ذاتي الوصف |
| **تقارير Excel** | `Company-Dashboard/reports/render.py` (742 سطر) | ✅ — openpyxl، RTL، تنسيق أرقام |
| **تقارير PDF عربي** | `Company-Dashboard/reports/render.py` + مهارة `arabic-pdf-weasyprint-pipeline` | ✅ — WeasyPrint + خط Noto Naskh Arabic مدمج، RTL كامل |
| **تقارير PowerPoint** | `Company-Dashboard/reports/render.py` | ⚠️ يحتاج تطوير — الأساس موجود |
| **حزمة مجلس إدارة** | `Company-Dashboard/reports/render.py` | ✅ — غلاف + كل التقارير + صفحة ثقة المصدر |
| **قوالب عملاء** | `Company-Dashboard/reports/client_templates.py` | ✅ — تقارير مخصصة لكل عميل |
| **وكلاء خارجيون** | مهارات `claude-code`، `codex`، `opencode`، `gemini-cli` | ✅ — 4 منصات وكلاء جاهزة |
| **صفحات HTML للمراجعة** | `Intelligence Vault/HTML Artifacts for Agent Review` | نمط: واجهات محلية لمراجعة المخرجات المعقدة |

---

## الطبقة ٨: حلقة التعلم 🔁

### الموجود فعلًا:

| الأصل | الموقع | ماذا يقدم |
|--------|--------|-----------|
| **مجلة العمل** | `Company-Dashboard/AGENTS.md` — Work Journal | نموذج: كل مهمة ← إدخال (ماذا، لماذا، الحالة، الخطوة التالية) |
| **جدول المهام** | `Company-Dashboard/AGENTS.md` — Task Board | تتبع: Ready ← In Progress ← Done مع commit hash |
| **مكتشف التغيير** | `llm-wiki-agent/tools/refresh.py` | يقارن hashes المصادر ← يكشف التغييرات ← يعيد الابتلاع آليًا |
| **المعالج الذاتي** | `llm-wiki-agent/tools/heal.py` | يمسح الفجوات ← يولّد صفحات تعريف بالكيانات الناقصة |
| **المجدول الآلي** | `GenericAgent/reflect/scheduler.py` | مهام مجدولة بالملفات: يومي/أسبوعي/شهري/كل N ساعة. تتبع done-file |
| **الوضع الذاتي** | `GenericAgent/reflect/autonomous.py` | ينشط عند خمول المستخدم >30 دقيقة |
| **سجل التعلم** | Compound Execution Plan (Layer 8 spec) | 10 عناصر لكل حالة: نوع الشركة، المشكلة، البيانات، التشخيص، الحل، النتيجة، القالب، الأخطاء، القاعدة، فكرة الأداة |
| **قائمة المراجعة** | `Intelligence Vault/05 - Review Queue.md` | إطار أولويات: الأقرب للمال، تقوية النظام الداخلي، الإيقاف المؤقت |
| **التركيبات الأقوى** | `Intelligence Vault/04 - Stronger Combinations.md` | 6 تركيبات قوية + معايير قبول |

---

## أولويات البناء — من أين نبدأ؟

لدينا 3 مكونات جاهزة تمامًا (✅ إنتاجي) يمكن البناء عليها فورًا:

### المسار ١: المعرفة
- llm-wiki-agent (الابتلاع ← الويكي ← الرسم البياني)
- Company-Dashboard brain/
- SwarmVault LLM Wiki template

### المسار ٢: التحليل والتقارير
- Company-Dashboard كاملاً: مستخرجات ← قاعدة بيانات ← تحليل ← تقارير ← لوحة قيادة
- أنماط Agent Harness من GenericAgent + AGENTS.md

### المسار ٣: التحكم
- بروتوكول AGENTS.md + قوالب سير العمل + طبقة الحكم + عقد الروح
- أدوات MCP + فريق Mohamed للبرمجة

---

## ما ينقص ويحتاج بناء:

| # | المكون | الأولوية |
|---|--------|----------|
| 1 | **100 بطاقة معرفة** في مجالات المحاسبة والمالية | ⭐ فوري — Phase 1 |
| 2 | **20 دليل تشخيص** (تكاليف، مخزون، تدفق نقدي، AP، إقفال...) | ⭐ Phase 2 |
| 3 | **محرك تشخيص موحد** يجمع أدوات anomaly + pricing + lint | Phase 4 |
| 4 | **أدوات مالية متخصصة:** trial balance analyzer، budget vs actual، inventory aging، AP checker | Phase 3 |
| 5 | **استوديو مخرجات كامل:** PowerPoint، risk register، KPI tree، process map | Phase 7 |
| 6 | **قاعدة معرفية متراكمة:** حفظ كل حالة ← قالب ← قاعدة ← أداة | Phase 8 |

---

_آخر تحديث: 2026-06-17_
_عدد الأصول المجرودة: 31 ملف خزنة + 7 مستودعات + 30+ مهارة_
