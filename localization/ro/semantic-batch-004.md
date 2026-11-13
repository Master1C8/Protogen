# Semantic audit batch 004

2026-11-13. Compared 150 English base story IDs in inventory order, `start_1762a30f` through `start_86657c7f`, against the Romanian with scene context. Exact IDs: `semantic-batch-004-ids.json`, SHA-256 `2ce0ca340322aadbc7055a12209b5b179d885fece7bc94becc6dccf5e157717f`. Coverage file now has 526 base story IDs, SHA-256 `e643faa367ca9b54203fbacd520f38d63378da5b98a02ce70616379df3cae1a4`. This is partial author review, not independent review.

Two findings were corrected and reread against English:

- `start_f2f8c58f`: the reference to Pixie as a vehicle now agrees with the feminine `navetă`, following the approved distinction from the AI.
- `start_d9b33a04`: specified feet rather than the ambiguous Romanian word for legs, matching the original threat.

Both are shared same-ID DLC rows; neither is a source of a DLC alias. Reproduce the bounded direct closure by checking these IDs in both inventories and searching alias-map values. These fixes do not change the glossary or its rules. Full semantic review, final dependency closure and independent delta review remain pending. The source-authoring file changed from SHA-256 `49f73be092b8d689bb42bcef7958407b9d8f9bc0c009024d4267fa903de36017` to `ceba3f431a6f36e8aacd7f05ab4388213d989330b752412f13aca7ca432be079`. Strict `edition_text(..., False)` passed complete IDs, shared mappings, aliases and inline tokens after correction; it does not test reinsertion or runtime.
