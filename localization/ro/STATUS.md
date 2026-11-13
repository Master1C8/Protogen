# Romanian localization checkpoint

2026-11-13. My Furry Protogen, Steam build 11915262, English → Romanian (`ro`), standard, base and official DLC. Current stage: **author semantic pass complete; independent review pending**. The owner explicitly permits text work before the later joint CrossOver pass; Romanian rendering remains unverified. Process binding, evidence and pinned source hashes remain in [preparation](preparation-2026-11-13.md). No runtime, visual, font, packaging or Git work is assigned to this session.

| Authored coverage | Done / total |
| --- | --- |
| Base story | 1,785 / 1,785 |
| Base UI | 394 / 394 |
| Explicit DLC-only story | 238 / 238 |
| DLC UI | 1 / 1 |

These are authored unique IDs/keys, not semantic-audit coverage. The existing alias map additionally resolves all 17 DLC alias IDs from the current base rows; the draft validator reports 255/255 DLC delta including those aliases. Do not author alias keys. Preserve both editions and shared IDs.

[Special-scene decisions](special-scenes.md) cover the currently registered name, Juno nameplate, save format, dialogue timing, logo and watch cases, with exact wording in authored inputs, source bindings, positive and negative checks, and outstanding runtime checks. All registered story IDs resolve to a direct row or authorized alias. Registry discovery exclusions remain explicit; reconcile newly discovered cases when encountered. `start_5c6117e8` has an apparent source speaker/context discrepancy: retain original binding and review in the full semantic pass. DLC source `start_75bdc594` names Katie for a past attempt; retain the source name and check its relation to the unnamed girl during semantic review, without assuming identity. Save date directives are retained but rearranged; actual locale-dependent month/day rendering remains unverified.

The prior turn translated the registered name/timing groups and the opening. Turn 002 added 137 base story rows through the start of the birthday celebration. Turn 003 added 130 base story rows through Juno’s introduction. Turn 004 added 136 base story rows through the first Pixie and provision scene. Turn 005 added 133 base story rows through the forest illness scene. Turn 006 added 134 base story rows through the swamp conversation. Turn 007 added 133 base story rows through the start of the desert expedition. Turn 008 added 130 base story rows through Juno’s account of Toshi. Turn 009 added 133 base story rows through the first virus investigation. Turn 010 added 133 base story rows through the confession scene. Turn 011 added 128 base story rows through preparation to visit the village. Turn 012 added 131 base story rows through the return to his family. Turn 013 added 128 base story rows through the recovery aboard ship. Turn 014 added the final 47 base story rows and 103 base UI keys. Turn 015 added 130 base UI keys covering accessibility, dates, save actions, confirmations and engine settings. Turn 016 added the remaining 154 base UI keys. Turn 017 added 120 explicitly authored DLC-only story rows. Turn 018 added the remaining 107, completed strict text coverage validation and began the author semantic audit. Author review accompanied the batch; no claim of full semantic or independent review. Current input SHA-256:

- `dialogue.tsv`: `e21df145d97601f3861a587558d065b3b8e805f009d350ae7b9764d5dc392d62`
- `strings.json`: `c6864409550b3351a1cc6386419d882fcde4d40ae7cd50782b59c799a488072d`
- `nsfw/dialogue.tsv`: `c2799c1e728f40733e296a0e4ee5b4718a5d94ae9baad3ec91b6d763436b20a6`
- `nsfw/strings.json`: `4dbf34478ec71bc71dea3ebe825902ba43c1457052ffb7ef4d53b24fc4ba466e`
- `special-scenes.md`: `2abdfd88ca926fd13a91c07443fe711313725c96c4f8534cff7eb1e23bdac56e`

Validation: `build_localization.edition_text(base, dlc, Path('localization/ro'), False)` passed source IDs, shared mappings, aliases and inline protected-token checks for the complete authored corpus. A direct comparison of each inventory's `preserve-exactly` rows to its manifest passed: 747 base and 744 DLC. This is source-manifest equality, not a reinserted-artifact comparison or runtime test. Full protected-value validation after application/build remains assigned to the coordinator. No install was read or changed.

Semantic review: 1,785/1,785 base story IDs, 394/394 base UI keys, 238/238 explicit DLC story IDs and 1/1 DLC UI key compared with English in batches 001–016; latest: [batch 016](semantic-batch-016.md). Exact audited IDs are in `semantic-coverage.json`. Twenty-two corrected rows and their bounded edition reuse are documented in the batch records. Reproduce the structural dependency closure and strict text checks with `python3 -B localization/ro/verify-semantic-closure.py`; this passed for the current pinned inputs. This is author review, not independent review. The source-bound speaker discrepancy and Katie identity question remain as recorded above. Next: coordinator arranges independent review and the joint runtime/visual pass, followed by applied-artifact validation, packaging and integration; recheck affected dependencies if inputs change.

This turn's receipt matched thread `01a1d275-ddde-77f3-9d9b-266488e3d5d7`, turn `01a1d2bd-62bd-7b20-914b-e17aeaea1bb7`, `gpt-6.1-terra/high`. Exposed per-request token usage was unavailable; no estimate has been substituted.
