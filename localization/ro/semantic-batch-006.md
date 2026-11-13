# Semantic audit batch 006

2026-11-13. Compared 150 English base story IDs in inventory order, `start_fd318b0a` through `start_679a328a`, against Romanian with scene context. Exact IDs: `semantic-batch-006-ids.json`, SHA-256 `e472df11fcb1f3264902aa6de181ada8b3f00b18411d03bd64349abcd7ddd59c`. Coverage file now has 826 base story IDs, SHA-256 `3e4ceeabb73c6f84c7cc89bd12c08b4be022d944212fae22b18df2874a5bcc0b`. This is partial author review, not independent review.

Three findings were corrected and reread against English:

- `start_fd318b0a`: restored that the narrator knows nothing about mushrooms, including the emphatic tone, rather than almost nothing.
- `start_c0524654`: restored “once again” instead of “always” for avoiding the creatures.
- `start_8244e6ed`: corrected the reversed question about whether having no friends is acceptable. This row falls immediately after this batch's coverage; it and the following response `start_ffb8e16b` were checked together for coherent polarity, but neither is counted as audited until the next sequential batch. It is also a registered player-name case: `[pname]` is unchanged, and `special-scenes.md` references the canonical authored row rather than duplicating its wording.

All three changed IDs are shared same-ID DLC rows; none is a source of a DLC alias. Reproduce this bounded direct closure by checking the IDs in both inventories and searching alias-map values. Full semantic review, final dependency closure and independent delta review remain pending. The source-authoring file changed from SHA-256 `eae34c341bc029266d385932d1199247fc55e1d16f9b182ab8b05c04b3a014a0` to `2783ccaca1e42bd7df3d5a386f2c231f096c995d9af7d2b47dde3e7b03707cbb`. Strict `edition_text(..., False)` passed complete IDs, shared mappings, aliases and inline tokens after correction; it does not test reinsertion or runtime.
