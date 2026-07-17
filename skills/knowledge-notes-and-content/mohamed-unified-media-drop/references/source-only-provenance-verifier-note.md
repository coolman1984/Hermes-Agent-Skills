# Source-only provenance and verifier compatibility

## Context

During a YouTube media-drop run, the workflow correctly stayed source-only because Mohamed sent a bare link and did not request enrichment.

The media-note verifier still required the provenance marker:

`من البحث الإضافي`

This can look contradictory if the source-only note omits the marker entirely.

## Durable rule

For source-only notes, include the marker but phrase it as a negative provenance statement:

```text
من البحث الإضافي

لم يتم تشغيل بحث خارجي لأن محمد لم يطلب توسيعًا أو تحققًا خارجيًا. هذه الملاحظة مبنية على المصدر نفسه فقط.
```

This satisfies deterministic verification while preserving factual provenance.

## Do not do

- Do not imply external research was performed when it was skipped.
- Do not remove the marker until the verifier script is changed.
- Do not use this as permission to run enrichment by default.

## Future cleanup option

If the verifier is updated later, split required markers into:

- source-only required markers
- enriched-note required markers

Until then, keep the explicit negative statement.
