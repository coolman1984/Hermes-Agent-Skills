# Reasoning Mastery Validation Results

Judgment target: reasoning quality, not only final answers.

| Task | Result | Reasoning move | Evidence | Fix applied |
|---|---|---|---|---|
| 1 vague/solution-shaped request reframed to real problem | PASS | problem-framing + XY detection | Y=bypass blocks → X=collect data reliably and compliantly; action=check API/export/robots/terms first; if forbidden, refuse scraping and seek authorized route |  |
| 2 misleading symptom isolated to root cause | PASS | systems-diagnosis debug checklist | symptom=UI says save failed; divergence=worker log shows queue consumer stopped; root=background queue down |  |
| 3 obvious answer red-teamed before committing | PASS | uncertainty-rigor + second-order thinking | PDF cache becomes stale when source data changes; cache raw validated tables with invalidation by source checksum instead. |  |
| 4 stuck problem unlocked by changing representation | PASS | persistence-search + pipeline representation | Represent pipeline as detect→route→extract; discover detection step marks searchable PDF as image because text threshold too high; relax threshold and add OCR fallback. |  |
| 5 ill-posed task refused without fabrication | PASS | well-posedness check + honest refusal | proof=Future market price is not determined from available current information; stochastic events and hidden order flow make unique exact answer underdetermined.; nearest=Provide scenario ranges, drivers, risk levels, and triggers instead. |  |
| 6 multi-part problem decomposed, solved, recomposed, retro-fed | PASS | decomposition + metacognition | parts=['acquire authorized data', 'extract raw payloads', 'load database', 'validate numbers', 'write decision report']; recompose=Pipeline output is a sourced decision memo; each part has provenance handoff and validation gate.; retro=Reasoning worked: MECE pipeline. Failure risk: skipping legal basis. Prevention: manifest before extraction. | Added validation evidence; ERRORS.md already contains prevention classes. |
