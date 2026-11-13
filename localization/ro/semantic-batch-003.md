# Semantic audit batch 003

2026-11-13. Compared 150 English base story IDs in inventory order, `start_bf4811ad` through `start_cd1a67c8`, against the Romanian with scene context. Exact IDs: `semantic-batch-003-ids.json`, SHA-256 `18b912cbbf7b86d2e5524d2f78833e0f907d929231a5388f38d0fb485392415c`. Coverage file now has 376 base story IDs, SHA-256 `60238bc1f0f079e48e99eea9372e76ce9015d642e3f7c38683fa5b421a95f623`. This is partial author review, not independent review.

Three findings were corrected and reread against English:

- `start_fb6de52b`: restored a nervous smile rather than an embarrassed one.
- `start_c89cdfa5`: removed the unsupported literal “in flesh and blood”; source calls the intelligent being real.
- `start_cd1a67c8`: restored that his smile made him resemble his father, rather than merely remembering him.

All three are shared same-ID DLC rows; none is the source of a DLC alias. Reproduce the bounded direct closure by checking these IDs in both inventories and searching alias-map values. These fixes do not change a glossary term or global rule. Full semantic review, final dependency closure and independent delta review remain pending. The source-authoring file changed from SHA-256 `333962dbe85c7f68a7b4da58d948e5acf6046222e1c01797e15340712e194048` to `49f73be092b8d689bb42bcef7958407b9d8f9bc0c009024d4267fa903de36017`. Strict `edition_text(..., False)` passed complete IDs, shared mappings, aliases and inline tokens after correction; it does not test reinsertion or runtime.
