# egx_system

## الهدف
بناء نظام قرار وانضباط للمحفظة المصرية يكون واضحًا لأي AI أو مشغل بشري، ويُدار بعقلية مدير محفظة هجومي منضبط: رفع رأس المال بسرعة، لكن عبر مخاطرة عالية محسوبة.

## الحالة الحالية بعد إعادة التنظيم
- المسار الرئيسي: `/root/Documents/Obsidian Vault/egx_system`
- القواعد والدستور وخريطة القطاعات ودليل التشغيل تمّت إعادة كتابتها على النظام الجديد
- تم تثبيت فلتر "نشاط مقبول شرعياً" بدل الفلتر الشكلي المتشدد
- تم تثبيت قاعدة Camoufox-first للمصادر الصعبة مثل X وSubstack
- تم الإبقاء على بنية التقارير المحلية اليومية + JSON + decision memo
- ما زال التنفيذ النهائي بشريًا وليس آليًا

## الملفات الأساسية المعتمدة الآن
- `AI-START-HERE.md`
- `AI-HANDOFF-PROMPT.md`
- `EGX-SESSION-RUNBOOK.md`
- `ai_manifest.json`
- `tools/validate_system.py`
- `portfolio/positions.csv`
- `portfolio/watchlist.txt`
- `portfolio/rules.md`
- `playbook/investment_constitution.md`
- `playbook/sector_map.md`
- `playbook/workflow.md`
- `../Investing/EGX Portfolio Monitoring System.md`

## ترتيب القراءة الإلزامي لأي AI
1. `CURRENT-SNAPSHOT.md`
2. `egx_system/portfolio/rules.md`
3. `egx_system/playbook/investment_constitution.md`
4. `egx_system/playbook/sector_map.md`
5. `Investing/EGX Portfolio Monitoring System.md`
6. `positions.csv`
7. `watchlist.txt`

## منطق النظام الحالي
- التركيز أهم من كثرة الأسماء
- النواة تقود النتيجة
- المراكز الصغيرة تُراجع بصرامة
- لا نبدأ من السعر بل من الحقيقة الرسمية ثم الدور ثم التوقيت
- ندوّر رأس المال نحو الأفضل بدل توزيع الضعف على أسماء كثيرة

## دورة التشغيل
- يوميًا: حقائق جديدة → أثر قطاعي → أثر على المحفظة → قرار مختصر
- أسبوعيًا: ترتيب القطاعات والأوزان والأدوار
- شهريًا: إعادة بناء خريطة الشهر كاملة

## ملاحظات مهمة
- إذا تغيرت القواعد أو أسلوب الإدارة، يجب تحديث الملفات الستة الأساسية معًا
- إذا تغيّرت تصنيفات الأسهم أو أوزانها المستهدفة، يجب تحديث `positions.csv`
- إذا تغيّرت قائمة المتابعة الحقيقية، يجب تحديث `watchlist.txt`
- إذا كانت الصفحة صعبة نصيًا، نستخدم Camoufox مباشرة

## الخطوة التالية المنطقية
- تحديث `positions.csv` و`watchlist.txt` ليعكسا النسخة المركزة الحالية من المحفظة
- ثم تشغيل الدورة اليومية/الأسبوعية على النظام المحدث

[[CURRENT-SNAPSHOT]]