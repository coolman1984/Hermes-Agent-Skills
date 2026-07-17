# مراجعة مصدر GitHub للطريقة

مرجع مرتبط: [[LLM Knowledge Base — خطة عملية]]

## النتيجة السريعة
أفضل مصدر عملي وجدته على GitHub لتعلّم الطريقة هو:
SamurAIGPT/llm-wiki-agent

السبب: هذا الريبو يطبّق الفكرة نفسها بشكل مباشر وقابل للتشغيل، وليس مجرد شرح أو prompt pack.

## لماذا هو الأفضل
- فيه طبقة raw/ للمصادر الخام
- فيه wiki/ للمعرفة المركبة
- فيه graph/ للترابط البصري
- فيه tools/ فعلية للبناء والتحديث والتحقق
- فيه workflows واضحة: ingest / query / lint / build graph
- يستخدم Python + litellm لتنفيذ الدورة من الطرف إلى الطرف

## ما الذي يتعلمه منه الواحد
1. كيف تُحوَّل الوثيقة الخام إلى صفحة مصدر داخل الويكي
2. كيف تُحدَّث index.md وoverview.md وlog.md بعد كل ingest
3. كيف تُنشأ entity pages و concept pages تلقائيًا
4. كيف تُفحص الروابط المكسورة والصفحات اليتيمة والتناقضات
5. كيف يُبنى graph.json وgraph.html من wikilinks ثم تُضاف علاقات inferred
6. كيف تُحفَظ الاستفسارات المفيدة كصفحات synthesis داخل الويكي

## مقارنة سريعة مع باقي المرشحين
### 1) SamurAIGPT/llm-wiki-agent
- الأقرب لفكرة Karpathy
- أكواد حقيقية ومباشرة
- أفضل خيار للتعلّم العملي

### 2) swarmclawai/swarmvault
- أقوى كمنصة production
- فيه monorepo، MCP، hybrid search، graph tooling أكثر
- ممتاز لو الهدف توسيع النظام، لكنه أثقل كمصدر تعليمي أول

### 3) mduongvandinh/llm-wiki
- ممتاز كـ template وskill pack
- لكنه أقرب إلى scaffold/تعليمات أكثر من كونه engine كامل

## الخلاصة
لو الهدف هو تعلّم “الطريقة” نفسها بوضوح، ابدأ بـ SamurAIGPT/llm-wiki-agent.
لو الهدف لاحقًا هو بناء نسخة أكثر احترافية وأثقل، انظر إلى SwarmVault بعد ذلك.

## دورة التشغيل المختصرة كما فهمتها
raw source -> ingest.py -> source page/index/overview/entities/concepts/log -> query.py -> synthesis -> lint.py -> build_graph.py -> knowledge graph

## أوامر البداية المهمة
- python tools/ingest.py <source>
- python tools/query.py "..."
- python tools/lint.py
- python tools/build_graph.py --open

## ملاحظات مهمة
- طريقة النجاح هنا ليست في RAG فقط، بل في تراكم المعرفة نفسها.
- نقطة القوة الأساسية هي أن كل مصدر جديد يزيد الويكي ثراءً بدل أن يبدأ البحث من الصفر.
- التحقق بعد الإدخال جزء أساسي، وليس خطوة اختيارية.

## التنفيذ المحلي
- تم تهيئة نسخة أولية فعالة في `/root/llm-wiki-agent`.
- تمت إضافة الصفحات الافتتاحية: overview, index, log, sources, entities, concepts.
- نجح `python tools/ingest.py --validate-only`.
- نجح `python tools/build_graph.py --no-infer` وأنتج `graph/graph.json` و`graph/graph.html`.
