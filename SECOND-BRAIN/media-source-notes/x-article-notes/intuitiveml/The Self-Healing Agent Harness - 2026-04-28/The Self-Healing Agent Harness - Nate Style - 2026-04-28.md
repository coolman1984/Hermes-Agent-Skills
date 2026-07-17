# منظومة الوكيل ذاتية التعافي: التحول من تقييمٍ معزول إلى محرك تسليم يومي

**المصدر:**

https://x.com/i/status/2048912026018484317

**الكاتب:**

Peter Pang

**الحساب:**

@intuitiveml

**تاريخ النشر:**

2026-04-28

**تاريخ إعداد الملف:**

2026-04-28

**وضع الأسلوب:**

تحليل عربي مطوّل بروح Nate B Jones (تقليد أسلوب، بدون انتحال شخصية)

---

## ملخص طويل احترافي

الخبر مش مجرد عرض لنظام تقييم جديد، ولا حتى مجرد قصة عن فريق هندسي سرّع الإطلاق. الفكرة الأهم إن المقال بيعلن عن تحول في تعريف وظيفة الجودة داخل شركات الوكلاء الذكية: الجودة ما بقتش مرحلة نهائية بعد البناء، لكنها صارت قلب دورة الإنتاج نفسها. الكاتب يقدّم "منظومة الوكيل ذاتية التعافي" كحلقة مغلقة تبدأ من تقييم الردود الحية، وتتحول مباشرة إلى فرز هندسي، ثم إصلاح، ثم تحقق، ثم إعادة تقييم، ثم حوكمة نشر تدريجية.

التحليل هنا قوي لأنه يفصل بين وهم شائع وحقيقة تشغيلية: مشكلتك مش أن النموذج يجاوب غلط مرة أو مرتين، مشكلتك أن نظامك لا يملك قناة موثوقة لتحويل الخطأ المتكرر إلى قرار هندسي قابل للتنفيذ. لذلك هو يدمج "التقييم" و"ضمان الجودة" في نفس الممر، بدل إبقاء التقييم لوحة مؤشرات منفصلة لا تغيّر سلوك المنتج.

المقال يشرح ثلاثة مكونات مترابطة: مقيّم ثلاثي القضاة على الترافيك الحقيقي، خط هندسي يومي بست مهام من الرصد حتى التقرير، وجسر نشر رمادي محكوم بالنتائج الفعلية وليس الانطباعات. بهذه البنية، أي هبوط جودة يصبح إشارة إنذار هندسية، وأي إصلاح لا يثبت نفسه تلومتريًا يُعاد فتحه تلقائيًا.

الرهان الحقيقي هنا اقتصادي وتشغيلي في نفس الوقت: عندما يقل زمن كتابة الكود من شهور لساعات بفضل الوكلاء، ينتقل الاختناق من "البناء" إلى "الثقة في النشر". الفريق الذي يحل اختناق الثقة أولًا هو الذي يربح سرعة مركبة يصعب اللحاق بها.

---

## رأيي المهني في قيمة المقال

ده واحد من أندر النصوص اللي بتتكلم بوضوح عن الطبقة اللي فعلاً بتفصل بين فريق "بيستخدم ذكاء اصطناعي" وفريق "يشتغل كنظام ذكاء اصطناعي". القوة الأساسية إن الكاتب لا يقدّم أدوات منفصلة، بل يقدّم معمارية تشغيل متماسكة: إشارة تقييم → مسار أعطال → إصلاح مضبوط → إثبات تلومتري → نشر محكوم.

الأقوى من كده إنه يعترف ضمنيًا إن الدقة الأكاديمية المثالية مش دايمًا هدف الشركة الناشئة. الهدف العملي هو إشارة كفاية للتحرك اليوم، لا نموذج قياس أنيق بلا أثر تنفيذي. ده منطق إداري ناضج.

تحفّظي الوحيد: نجاح النموذج ده يفترض نضجًا عاليًا في السجلات والبيانات وحوكمة الصلاحيات. من غير الانضباط ده، الأتمتة قد تتحول إلى تسريع خاطئ بدل تحسين حقيقي.

---

## الترجمة الكاملة للمقال بأسلوب عربي مصري احترافي

Last month, I said 99% of our production code is written by AI.

That wasn’t a small change. We had to rebuild the way we work, with agents at the center. Now we ship to production three to eight times a day.

Since then, the question I hear most from other founders is:

Who tests it?

The answer is not “more QA.” We don’t have a QA team. We don’t have a staging environment where people click around before a release. No one on the team is sitting there reading transcripts and scoring agent replies by hand.

Instead, we built a system that catches failures and helps fix them. We call it the self-healing Agent Harness

After running this in production, two lessons became obvious:

Grade the outcome, not the trajectory. Agents often take paths that look inefficient or strange to humans, but still produce the right answer. Penalizing the path is not an efficient way to evaluate agent performance.

A score with no ticket means nothing. A bad score that does not feed engineering is just a dashboard. A bug pipeline without grader signals is blind. Build both, or build neither.

Don't get trapped chasing "scientific correctness." I've seen plenty of people with research backgrounds get caught debating whether agent-based evaluation is methodologically rigorous enough. For a startup, that kind of debate is a luxury you can’t afford. It misses the point. The purpose of an agent-based grader isn’t to rank models against each other for a paper. It’s to identify recurring issues in your product, fast. A good enough signal that triggers a fix today beats a perfectly defensible benchmark that ships next quarter.

That loop, grade, triage, fix, verify, and gate releases, is what we call the Agent Harness

The Thesis: Evaluation and QA Are the Same Loop

In a traditional SaaS company,  these usually live in different places:

Model evaluation asks: is the model giving good answers on live traffic? ML or data science owns that. They make dashboards.

QA asks: does the product work in production? Engineering owns that. They file tickets, fix bugs, and ship releases.

For an AI agent platform, those are the same question. A bad agent response is both a metric to chart and a bug to triage and fix. And that bug could come from almost anywhere:

The model reasoned poorly or hallucinated

An integration returned a 500, a stale token, or a malformed payload, and the agent repeated it back

Infra flaked. Maybe Cloudflare timed out, maybe Postgres replica lag hit, maybe an ECS task ran out of memory mid-stream

A tool contract drifted. A schema changed upstream and the agent's arguments silently stopped matching

Prompt or context plumbing broke. A system prompt got truncated, RAG returned the wrong chunk, memory failed to load

A deploy regression quietly degraded one of the dozens of small components behind a single user turn

To the user, all of these look the same: a bad answer. To the grader, they also look the same: a low score on messageId X. This is exactly why we built the Harness. We don’t need to know the root cause at scoring time, we just need to catch the failure fast. Then our triage system can pick it up and work backward from the signal.

A failed tool call should show up as a quality drop, and that quality drop should block the next deployment. The eval pipeline doesn’t sit off to the side. It feeds engineering directly. Every production failure goes through the same funnel.

That funnel is the Agent Harness.

It runs a self-healing loop on three components, and the rest of this post walks through each one.

The Grader. A tri-judge panel that scores every live agent response (Replaces human QA review and offline benchmark eval)

The Engineering Pipeline. Six daily jobs that turn low scores into Linear tickets, draft PRs, and verified fixes (Replaces manual bug triage, sprint planning, and regression testing)

The Bridge. AI-gated grey rollouts where the Grader's scores decide whether new code ships (Replaces staging environments and release approvals)

When AI cuts build time from month to hours, every downstream stage becomes the bottleneck. Evaluation and QA, kept separate, are both that bottleneck. The only way to keep up with AI-speed implementation is to merge them.

The chart below shows the sampled evaluations and average scores collected on the CREAO platform over the past 7 days.



Component 1: The Grader, a Tri-Judge Panel on Live Traffic

The hardest part of grading an AI product isn’t checking whether the code compiles. It’s determining whether the agent gave a good, logical answer to the user.

That used to mean humans reading transcripts. We replaced that with an async grading endpoint that fires after every assistant turn, fully out of band. It never adds a millisecond to user-facing latency.

This is the Harness's eyes. Everything downstream depends on these scores being trustworthy.

A note on intent.

We care a lot about accuracy and fairness, but we’re not building a leaderboard or ranking models against each other. The Grader exists to surface issues in our agent system: bad prompts, broken tool contracts, drifted integrations, infra flakes, regressions from our own deployments. Per-model scores are just a debugging signal, not a benchmark. If two judges score a response "poor" on the same messageId, we don’t learn that one model is better than another. We learn that something in our pipeline produced a bad answer, and we need to fix it.

The Trigger and Sampling

Every agent response triggers a POST to our internal grading endpoint with the messageId, threadId, and the model that served the response after fallback.

Sampling is per model, not flat:

10% for our dominant production model (Sonnet 4.6). It handles about 24x more traffic than anything else on our platform, so a flat rate would drown out the rest

100% for every minority or experimental model: Opus, GPT, Gemini, etc.

That’s the only way minority models reach statistical significance fast enough to gate a rollout decision in hours instead of weeks.

Job 0: The Categorical Router



Before the judges see the transcript, a lightweight classifier (Job 0) maps the interaction to one of our 12 core domains: coding, research, data analysis, task automation, agent building, artifact building, traditional app building, planning, writing, creative work, conversation, and error recovery.

We do this before scoring so each judge sees a category-conditioned rubric. A good coding answer and a good research answer get graded against different red flags.

Three Judges, Three Personas

We run three judges from different model families in parallel: Anthropic, OpenAI, and Google. This helps reduce the self-preference bias that can show up when models grade their own work. We call all three concurrently through our AI Gateway, so a single slow or failed judge never drops the verdict. It just lowers the quorum size for that row.

But we don’t trust the panel just because the panel agrees. We still sample a small share of verdicts back to humans for periodic calibration. If a persistent gap shows up between judge consensus and human review, we treat it as a bug in the rubric, not a tolerable error rate.

Each judge has to return structured output through a schema-locked tool call (submit_evaluation). The tool requires five fields: reasoning (2 to 3 sentences of step-by-step rationale), category (the domain being graded), quality (excellent, good, acceptable, poor), issues (drawn from a 9-item taxonomy: incomplete, hallucination, tool_misuse, missed_context, and so on), and confidence (a 0 to 1 float).

The Categorical Rubric



Each judge sees the same transcript but evaluates against category-specific constraints:



Mathematical Consensus

We map quality to a 1-4 scale and average across surviving judges instead of voting. That turns a blunt four-point scale into a continuous metric (3.33 vs 2.66) and makes per-model trends visible at much smaller sample sizes than a majority vote.

If Sonnet grades Sonnet, the score can inflate by ~0.3. However, when the OpenAI and Google judges, each running under different expert personas, flag the same issue, the bias gets washed out by the quorum. We persist each judge's verdict alongside the average (sonnet_quality, gpt_quality, gemini_quality, judge_count) so engineers can audit disagreement after the fact and re-weight if any single judge starts drifting.

The Grader's output is simple: a stream of category-tagged, judge-averaged scores tied to the exact messageId that produced them. That stream feeds everything that comes next.

The chart below illustrates the response quality of selected models available in our service.



Component 2: The Engineering Pipeline, Six Jobs from Score to Fix

Plenty of papers prove autonomous bug fixing is possible. But academic benchmarks don’t run in production. If AI hallucinates a fix on a static benchmark, you get a bad score. If it hallucinates a fix in your live codebase, you get an outage.

The Engineering Pipeline takes the Grader’s scores and turns them into shipped code. A low score from Component 1 is a bug report. From there, six jobs take that bug report to a verified fix. This replaces manual QA: triage, investigation, fix, regression test, sign-off.

The daily workflow runs six sequential jobs:



Job 1: Detect and Triage. An agent pulls poor-quality verdicts from the Grader and clusters them. It scores each cluster on a 9-dimensional severity engine: user impact, velocity, duration, alarm correlation, resource pressure, latency, 4xx rate, blast radius, business criticality. Anything above the urgency cutoff moves forward. The rest go into a log for trend tracking.

Job 2: Investigate. For the top three clusters, an agent walks the stack traces through our monorepo, pulls CloudWatch logs, checks recent deployments, and queries the database replica. It assigns a root cause and routes the ticket to a human with a full evidence bundle.

Job 3: Auto-Fix. For high-confidence, urgent issues, the system branches the code, writes the fix, validates it, and submits a draft PR on GitHub. Guardrails over ambition:

Max three PRs per run. Reviewers have limits. Bot floods exhaust it.

Any diff that touches .env, .github/, or IAM policies gets auto-closed.

Type errors block submission. Failing tests block submission.

We’re not trying to fix deep architectural debt here. We’re aiming to fix the obvious bugs quickly so humans can focus on deep work.

Job 4: Verify. For tickets in In Review, the system queries CloudWatch for the prior six hours. Zero occurrences? It closes the ticket with telemetry evidence pasted into the comment. Still failing? It updates the ticket with the new error count and loops again. Objective proof that fixes work, with zero manual regression testing.

Job 5: Re-grade. The Grader samples closed clusters at 100% for the next 24 hours. A regression reopens the ticket and reverts the fix.

Job 6: Report. A nightly digest lands in Linear and the team channel: clusters detected, PRs shipped, PRs reverted, score changes per category, and per-model leaderboard. The dashboard isn’t the goal, it’s just a record of what already happened.

Component 3: The Bridge, AI-Gated Grey Rollouts



The first two components close the loop on bugs that already shipped. The third closes the loop on bugs about to ship.

A self-healing pipeline handles papercuts well. What happens when you swap a foundational model, rewrite a core system prompt, or hand an agent vast new tool access? Behavioral risk goes vertical. You cannot push a major update to 100% of production and hope.

The Bridge is where the Grader and the Engineering Pipeline meet. We use the Grader's scores as one of the release gates (there are many others, but here we focus on grader’s scores). No staging environment. No human approval. No "looks good to me" in a PR comment.

When a major agent change merges, we route a small slice of real traffic, typically 10%, to the new variant. The Grader scores it head-to-head against the current production baseline in real time.

The promotion ladder runs automatically:

Fail. If the panel's average score drops by 0.15 or more against baseline (p < 0.05 over a minimum 200-interaction window), or our deterministic bug hunter detects a spike in novel error clusters in that 10% cohort, the pipeline aborts the rollout, flips traffic back to stable, and opens a Linear ticket with the regression cohort attached. That ticket enters Component 2 as Job 1 input. The loop closes.

Hold or improve. The cohort scales: 5% to 20% to 50% to 100%. Each step is gated by the same statistical test on a fresh window.

The models prove their own safety on real user traffic, with the blast radius capped by cohort size.

The Hard Truths About Running a Harness

If you’re transitioning to an AI-first engineering workflow, write these down.

Grade the outcome, not the trajectory. Early on, we penalized agents for making "unnecessary" tool calls. That didn’t last long. We quickly learned what recent agentic research has proven: AI often discovers highly effective, non-linear solutions that look strange to humans but work extremely well. Grading what the agent produced is far more robust than micromanaging how it got there.

Sample by model, not by traffic. Flat sampling makes the dominant model look like the only model. You’ll under-invest in the rest.

A score with no ticket is a dashboard nobody looks at. The Grader is worthless without the Engineering Pipeline behind it. The Engineering Pipeline is worthless without the Grader feeding it. Build both, or build neither.

The New Standard

A self-healing system isn't a single feature. It’s a cycle: grade, triage, fix, verify. Every component runs on the model's own output.

In my last post, I wrote that the primary job of an engineering team is to enable agents to do useful work.

The Agent Harness is what that looks like in practice. The Grader replaces subjective human review. The Engineering Pipeline replaces manual bug triage and regression testing. The Bridge replaces the anxiety of the big-bang release.

Most founders are still bolting tools like Copilot onto the same old workflow. They run standard CI/CD with standard manual QA. They write code in hours and test it in days. They’re AI-assisted. They are not AI-first.

The competitive advantage goes to the teams that stop treating evaluation and QA as separate functions and build the harness that fuses them.

We build an agent platform. We test it with an AI jury, ship it on the jury's verdict, and let the jury reopen the case when something regresses.

The harness tightens day by day.

---

## ١٠ استخدامات عملية للأفكار الموجودة في المقال

1. بناء بوابة نشر تلقائية تربط الجودة الفعلية بقرار التوسيع أو التراجع.
2. تحويل أحكام الجودة مباشرة إلى تذاكر هندسية بدل تقارير للعرض فقط.
3. تطبيق تقييم متعدد القضاة لتقليل انحياز نموذج واحد.
4. تشغيل أخذ عينات غير متساوٍ حسب حجم كل نموذج في الإنتاج.
5. تأسيس مسار "تحقق تلومتري" قبل إغلاق أي إصلاح.
6. فرض إعادة تقييم إلزامي بعد الإغلاق لمنع الارتداد.
7. تقليل الاعتماد على الاختبار اليدوي في المنتجات الحوارية واسعة النطاق.
8. عزل الأعطال المتكررة في عناقيد أولوية بدل التعامل معها فرديًا.
9. تحويل فشل النشر إلى دورة تعلم تلقائية بدل مطاردة يدوية.
10. بناء ثقافة هندسية تعتبر الجودة جزءًا من التدفق اليومي لا خطوة نهائية.

---

## الفكرة الرئيسية للمقال

الميزة التنافسية في عصر الوكلاء ليست سرعة كتابة الكود وحدها، بل سرعة تحويل خطأ الإنتاج إلى إصلاح موثوق قابل للنشر تحت حوكمة مستمرة.

---

## تفكيك الحجج نقطة نقطة

- الحجة 1: التقييم وضمان الجودة حلقتان منفصلتان في الأنظمة القديمة.
  - الرد: في منتجات الوكلاء، الرد السيئ هو مقياس جودة وعيب منتج في نفس اللحظة.

- الحجة 2: لجنة قضاة متعددة تقلل الانحياز.
  - الرد: تنوع العائلات + حفظ حكم كل قاضٍ يرفع قابلية التدقيق.

- الحجة 3: الدرجة وحدها بلا مسار إصلاح لا قيمة لها.
  - الرد: أي إشارة لا تتحول إلى تذكرة وإصلاح تظل ديكورًا رقميًا.

- الحجة 4: النشر الكبير دفعة واحدة مخاطرة في تغييرات الوكلاء.
  - الرد: التدرج المحكوم إحصائيًا يقلل نصف قطر الانفجار.

- الحجة 5: النظام ذاتي التعافي أهم من أداة منفردة.
  - الرد: الاستمرارية تأتي من الدورة، لا من مكون واحد.

---

## الشرح العملي للمفاهيم

- المقيّم الحي:
طبقة تقييم خارج زمن استجابة المستخدم، تعطي إشارة جودة دون إبطاء الخدمة.

- راوتر الفئات:
يوجه كل حالة إلى معيار تقييم مناسب لنوع المهمة.

- محرك الشدة:
يعطي أولوية متعددة الأبعاد بدل قرارات حدسية.

- خط الإصلاح:
ينقل الإشارة من تقييم إلى تحقيق إلى إصلاح إلى إثبات.

- الجسر:
آلية نشر تدريجي لا تسمح بترقية غير مثبتة على بيانات حية.

---

## الروابط والمصادر المذكورة ومعناها

### الرابط الأساسي

https://x.com/i/status/2048912026018484317

المنشور الأصلي الذي يشرح معمارية منظومة الوكيل ذاتية التعافي.

### أدوات ومنصات ذُكرت وظيفيًا

Linear

إدارة التذاكر وتتبع حالة الإصلاحات عبر الدورة.

CloudWatch

إثبات اختفاء الأعطال تلومتريًا بعد الإصلاح.

GitHub

ممر إخراج الإصلاحات بصيغة طلبات دمج قابلة للمراجعة.

---

## نقاط القوة

- نموذج تشغيلي واضح وقابل للتنفيذ.
- دمج مباشر بين القياس والفعل الهندسي.
- حوكمة نشر واقعية للتغييرات عالية المخاطر.
- دورة تعلم سريعة من بيانات إنتاج فعلية.

---

## نقاط الضعف أو التحفظات

- يتطلب نضجًا مرتفعًا في المراقبة والسجلات.
- يحتاج انضباط صلاحيات قوي لتجنب آثار الأتمتة الخاطئة.
- يتأثر بجودة تعريف المقاييس والروبرك بمرور الوقت.

---

## كيف نستفيد منه في نظامك أنت

1. نبدأ بمقيّم مبسط على نسبة عينة من الترافيك.
2. نربط كل هبوط جودة بتذكرة وتحقيق قصير إجباري.
3. نضيف تحقق تلومتري قبل الإغلاق كقاعدة ثابتة.
4. نفعّل إعادة تقييم بعد الإصلاح لمدة 24 ساعة.
5. نطبق نشرًا تدريجيًا لأي تغيير حساس في الوكلاء.

---

## خلاصة تنفيذية

المقال ده بيقول بوضوح: إذا كانت الوكلاء خفضت تكلفة البناء، فربح المرحلة القادمة سيكون لمن يخفض تكلفة الثقة. والثقة هنا لا تُشترى بالانطباع، بل تُبنى بنظام يغلق الحلقة بين التقييم والإصلاح والنشر يومًا بعد يوم.

## الرهان الأساسي

التحول من "مراقبة الجودة" إلى "إدارة الجودة التشغيلية" هو ما يصنع فارق السرعة الحقيقي.

## أين الاختناق الحقيقي

الاختناق ليس في كتابة الكود، بل في تحويل إشارة الخطأ إلى قرار هندسي مثبت.

## القرار العملي الآن

ابنِ حلقة صغيرة اليوم: تقييم حي + تذكرة تلقائية + تحقق تلومتري قبل الإغلاق.

## سؤال ختامي للنقاش

في فريقك اليوم، هل الجودة عندكم مسار تشغيل يومي… ولا لوحة مؤشرات مؤجلة؟
