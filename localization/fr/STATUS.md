## Turn 036 — completed semantic comparison (2026-11-13)

Reviewed the final 168 DLC-only story entries against English, correcting four entries. Semantic coverage is complete: base story 1785/1785, base UI 394/394, DLC-only story 238/238, DLC UI 1/1. Exact audited IDs and corrections are in `semantic-coverage.json` and the three `semantic-batch-036-*.json` receipts. Independent review remains pending.

Reproduce the text dependency closure with `python3 -B localization/fr/validate-text-closure.py`. It checks the four exact audited ID sets, strict builder text validation, every inventoried story `preserveTokens` value, all 17 DLC alias translations and the latest authored values of 43 editorial corrections. One corrected base ID is used by alias `start_4d5e7851` → `start_35a3ccf5`; the check verifies that dependency. Output and input hashes are recorded in `text-closure-036.txt`. The protected non-translatable source literals and generated/runtime artifacts remain for the coordinator's integration verification; this is not a build, runtime, font or visual pass.

SHA-256: dialogue.tsv `86ff46bb3b55f18290920ffbd4a19f09063e633acf2696a1927d91e6001dda50`; strings.json `2eefdb7414339280a38025e71c18f21e8a512b5664c5c5626bcc55049bc70afb`; nsfw/dialogue.tsv `81903bb636c5691d8ed7717c13200eef9fbc1efdafedd64652c6b1ff6a38e483`; nsfw/strings.json `ece354df31fba7ffbd959a14457692b27d8d6acf7631b421766164e888ad8839`; semantic-coverage.json `056446578eb1be4317cc5c737223ccfd229673d004c0b24b6b318cd6a48cb4e3`; closure script `fd8e0ed98b8cd90ec54712aa2d73eb425caf1e37e7760f22b4ca39d54d190951`; closure receipt `6091b541f7e17d04b8933df29ea12ffec4c5b5a7fff1c7ff518bdb630d8a8dc5`.

## Turn 035 — editorial checkpoint (2026-11-13)

Compared the remaining 294 SFW UI keys, the first 70 DLC-only dialogue IDs in official export order, and the DLC UI key against English. Refined two DLC lines; exact IDs and corrections are recorded in `semantic-batch-035-ui.json` and `semantic-batch-035-dlc.json`. Semantic coverage: base story 1785/1785, base UI 394/394, DLC-only story 70/238, DLC UI 1/1. Continue DLC story at index 70 of the official export filtered to authored DLC IDs, then run the remaining dependency closure and full protected-value comparison. Independent review remains pending.

The `edition_text` text check passed: SFW story 1785/1785 and UI 394/394; DLC delta 255/255 including 17 aliases and UI 1/1. This does not establish build or runtime behavior.

SHA-256: dialogue.tsv `86ff46bb3b55f18290920ffbd4a19f09063e633acf2696a1927d91e6001dda50`; strings.json `2eefdb7414339280a38025e71c18f21e8a512b5664c5c5626bcc55049bc70afb`; nsfw/dialogue.tsv `0355c4044da3c5d0cb5d8554a1124d8cc6f1a21c53ac97ad1985c4ddcd00849b`; nsfw/strings.json `ece354df31fba7ffbd959a14457692b27d8d6acf7631b421766164e888ad8839`; semantic-coverage.json `5506b9a2174d93a00dfb48e5831b7e8ebbc0c252f61d46af38c664acbfdb6c91`.

## Turn 034 — editorial checkpoint (2026-11-13)

Compared the remaining 100 SFW story entries and the first 100 SFW UI keys (in `strings.json` insertion order) against English. Corrected three story entries; exact IDs and before/after text are in `semantic-batch-034.json`. Semantic coverage is now base story 1785/1785, base UI 100/394, DLC-only story 0/238, DLC UI 0/1. Continue UI at insertion-order index 100; then audit DLC and perform the reproducible dependency closure. Independent review remains pending.

The `tools/build_localization.py` `edition_text` text check passed: SFW story 1785/1785, UI 394/394; DLC delta 255/255 including 17 aliases, UI 1/1. This is a text validation, not a build or runtime check. Full protected-value comparison and dependency closure remain pending.

SHA-256: dialogue.tsv `86ff46bb3b55f18290920ffbd4a19f09063e633acf2696a1927d91e6001dda50`; strings.json `2eefdb7414339280a38025e71c18f21e8a512b5664c5c5626bcc55049bc70afb`; nsfw/dialogue.tsv `4bb65682ccdf2d77b5537107b311873df81743483addcec77d9f62ee16f8359f`; nsfw/strings.json `ece354df31fba7ffbd959a14457692b27d8d6acf7631b421766164e888ad8839`; semantic-coverage.json `0d60a756823b88a16913dad9bdceab6d3f756dd19b8ccfe5b2d70ddb39cf137d`.

# French localization checkpoint

2026-11-13, completion turn 033. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **1685/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-033.json` records exact IDs and three corrections: `start_e85130c6` preserves both parents’ responsibility, `start_d99074dc` retains the narrator’s description of the anomaly as a creature, and `start_e8ed360a` corrects idiom. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `ae4eef96520030fc30cdcf1e51d2007a61be3c4a3a25be277d4b771ee1da5334`; `semantic-coverage.json` `406fd8da7e652981bf21073036a998823bfe209a7cd7c3f767f7066c43a45df6`; `semantic-batch-033.json` `fb4d33b8509861e919c6cf52cb816f99226fc77a3bea892b51ea7986155a7679`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 1685, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 032. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **1575/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-032.json` records exact IDs and two corrections: `start_5186d4f8` avoids an unsupported gendered Pixie reference; `start_c925e5d0` preserves the source’s actual dates rather than mere invitations. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `af835a70219753cc73db2feeb2b034cd5c8f94e86cf10a85c49cf6b6ce06d5f9`; `semantic-coverage.json` `2c32a5040c6a307387c2d44cd01ec69e174933d5afe7ec3ef95317aaacf4eceb`; `semantic-batch-032.json` `2c2fc8c9b12b8fe034bbe314bc8be69ffa927b7f3d54bcc8a7ff5175d45ab18d`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 1575, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 031. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **1465/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-031.json` records exact IDs and five corrections, including finishing the earlier `start_b37f00c2` speaker agreement fix, clarifying contextual meaning of `start_cd2fe863`, removing unsupported Pixie agreement, and restoring an omitted detail. Alias-linked changes must be included in the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `f68e6e2cc45dd61214b27ebde8e9db34e919cfbfa0d19cf793d8018139c5737a`; `semantic-coverage.json` `80ab1d75f40633922bde88c238c29bf053240bca08047f217a346e223276ef8a`; `semantic-batch-031.json` `24af0ed2cd9a540fc604324111967bc3752312a751d55dc7481675dbb5573b9a`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 1465, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 030. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **1355/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-030.json` records exact IDs and correction `start_1ec245b3`, agreeing « vrai » with the preceding « quelque chose de vrai ». Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `5c732af80d40fb2e28cea65132aad3457c854bf841435fef51945ab416571b8f`; `semantic-coverage.json` `79d3a367c4d5d745a289776c492c000b31c0a416d6f3853eff75cab8c7d8a8f5`; `semantic-batch-030.json` `238556c64b60da8ad77a30f5fadffc9631666d3922ef69fb578b1a3e102c2858`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after correction. Full protected-value comparison remains pending. Continue semantic reading at base story index 1355, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 029. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **1245/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-029.json` records exact IDs and correction `start_1c5ad493`, restoring the action of collecting samples. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `88a7f0fb76bc209b030eff1f86417ef7d15cf296b1e9d2ef5de75f7fa404d052`; `semantic-coverage.json` `1add59f55aebcef37cf5336dd64b467312aa337a191edb95a939ed00e1f74892`; `semantic-batch-029.json` `a541853d84cdddf381acc9dad470d3521c1ef1a8d9767568a7d2e1a2904490e3`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after correction. Full protected-value comparison remains pending. Continue semantic reading at base story index 1245, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 028. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **1135/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-028.json` records exact IDs and two corrections: `start_78736a15` uses feminine agreement for speaker Juno, and `start_ed63ce1e` restores the source’s question about whether his parents thought of him. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `29143ccc2b6d81c55c8c7eb3bf6acec11b84db8c4d0844944735106e211c944b`; `semantic-coverage.json` `d0b296391326a3f1b6d410bf195c5fee2744ae5bdb428aa626731142bd35d8cd`; `semantic-batch-028.json` `98f06fd8cc49865d1a91c963e9a5c995983b02a433a9fd5853b46b91f872c9f9`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 1135, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 027. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **1025/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-027.json` records exact IDs and four corrections: `start_b808c3d7`, `start_f1463985`, and `start_aa18e11b` remove unsupported gender attribution to Pixie; `start_2d9f9777` fixes French grammar. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `b484b0a3826fce955abdce2aaef80c03fa0936eac7167dff28941175cef305e3`; `semantic-coverage.json` `ab792d234c3510c36dc69f52bdd6a262d57adc73f260044f45f2642db92b7c1e`; `semantic-batch-027.json` `14d915a8a92f13bf51a8d4e5c668502c545dc5d62e94c2161ca209cdcd5c370c`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 1025, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 026. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **915/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-026.json` records exact IDs and two corrections: `start_5ac5748e` clarifies the elapsed half-night, and `start_e0adbde7` preserves the number of words the narrator did not understand. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `4374d0f48761c966834111fdf4d67a915eeeb361c3c0f57fd6a3e282730a07c6`; `semantic-coverage.json` `c79b62fbc7ff711578cdc1f570e9d2a338a700f6f56d4f6005e2319ce69e2f14`; `semantic-batch-026.json` `da5093ab128c8f565677a7ade96d90600adbd7955780e2c3af43302fe8e88a02`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 915, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 025. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **805/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-025.json` records exact IDs and correction `start_5fc1d03e`, preserving Tilia’s glow without inconsistent gender agreement. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `7e12250fe35fa1ab73a297b537d3df2f0f0756ae58a429a4d267f087de73c3e7`; `semantic-coverage.json` `5705d9b53ce7b41a4b6d393d078e1d9fc985fe55e57492ea0852dff0f8f5c1cb`; `semantic-batch-025.json` `cdabf22d063ce1153e67642a59da8264882d964ab1ea7b3c4da69c1142a99bb3`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after correction. Full protected-value comparison remains pending. Continue semantic reading at base story index 805, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 024. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **695/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-024.json` records exact IDs and two corrections: `start_cf15cf90` avoids an unsupported gendered pronoun for Pixie, and `start_731484ac` preserves Juno’s order rather than softening it. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `4b99734e3fb262015d22b6013e0a4b64f7fcf344b5ff0575c172787d0d4d31c0`; `semantic-coverage.json` `884b23225dab61bfa7be6ffdaf7bf194df84f0edc636ea014f278eda53c219b7`; `semantic-batch-024.json` `1af6dcde3d6d0fe0845d4de45666c123eb135a1a06f79d5c0ce7822fcbd3aa6c`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 695, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 023. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **585/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-023.json` records exact IDs and two corrections: `start_aaf3cc89` preserves the source’s age boundary, and `start_c7e47d62` preserves the stated order of the lie. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `3fd9d03386683934349c8249a40dbffbb99661bd0d1bbb43afd3b1a9042999cf`; `semantic-coverage.json` `63df8672e9651285621fe6a58d739a1f36d2b77bf1ab802eaa8b5841569c48be`; `semantic-batch-023.json` `7d3e95a7fb123ede1fc2a350066875cd985962ebd9dd7d717330188a1d55bf78`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 585, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 022. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **475/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-022.json` records exact IDs and two corrections: `start_8012a83b` avoids attributing gender to Pixie’s own greeting, and `start_f2f8c58f` uses Pixie naturally as the navette’s name. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `58c9062a826e9b7b6c4474366d340a3eae2dc019e114975e683c7917f8adfefb`; `semantic-coverage.json` `6980c2d0346036cb79ffd012c2fe7205391725d70c31e87b025cc01ad6b50583`; `semantic-batch-022.json` `db77c738bc7f8e209c45169fc49dbf24900c097db461c415d6f086b270f99162`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 475, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 021. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **365/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-021.json` records exact IDs and two corrections: `start_04867749` preserves plural address to the deities across the exchange, and `start_9f120078` restores the sound’s proximity. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `71852ad760bc5554ef8379cc2132545fd8421b767ed1ddee62cef78db1668095`; `semantic-coverage.json` `275e0430915b0c961a981f8f72e862dec5014d635b0c52796ffbd6bbd518d283`; `semantic-batch-021.json` `5f0220d4ccd3d2cee833224db3e6c1416b9d176ee0f81bfaac6da55eec00daaf`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 365, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 020. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Semantic audit in progress: **255/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI in `semantic-coverage.json`; this turn read 110 consecutive source/target pairs. `semantic-batch-020.json` records their exact IDs and three corrections: `start_10b97f61` preserves the parents’ active support of the crowd; `start_4bd93874` retains completed training; `start_ecb0886f` corrects the French time expression. Previous corrections remain in history for the later reproducible dependency closure. Independent review remains pending.

Current SHA-256: `dialogue.tsv` `75cfc25fe77d74f00b5277b70dacc7d037f92a49b516f91e1b4f28beb71e69c8`; `semantic-coverage.json` `e64d70fe13a4a0666a034c287e98035a6dbe5bb250e04ae5e408dbc7f2b2ca4f`; `semantic-batch-020.json` `f6814b4499a541f10ea8977a72ac36eb32be1453af58022c4f8c9706058bcd3c`. Source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections. Full protected-value comparison remains pending. Continue semantic reading at base story index 255, then UI and DLC; consolidate correction dependencies after the full pass.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 019. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Draft remains complete: 1785 base story, 394 base UI, 238 DLC-only story and 1 DLC UI. Full semantic audit is in progress: **145/1785 base story IDs**, 0/394 UI, 0/238 DLC story and 0/1 DLC UI are recorded in `semantic-coverage.json`; this turn read 100 additional consecutive source/target pairs. `semantic-batch-019.json` retains their exact IDs and two corrections: `start_8d2002d0` clarifies the intended comparison with a normal date, and `start_46dca9b7` normalizes glossary capitalization. Previous corrections `start_2a8cfefd` and `start_b37f00c2` remain part of the later dependency closure. No independent review has been performed.

Current SHA-256: `dialogue.tsv` `60694514ec94bcf8f84ba641d78bc3b73c7a7adbb6d8ea37ffef1077dd96b535`; `semantic-coverage.json` `b6ae66730fbb973d45c09e6d656951fc92f3fb6fefb00a8eddd34acdf3e08edb`; `semantic-batch-019.json` `d81dbdae7e4be6151097474549131adaf6951b811c3ae0357fe85a58f6c976d2`. English inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; French glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Strict edition text validation passed after corrections (1785/394 base, 255/1 DLC delta including aliases). Full protected-value comparison and runtime are separate pending checks. Continue semantic reading at base story index 145, then UI and DLC; record full correction dependency closure once findings are consolidated.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 018. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical authored coverage is **1785/1785 base story, 394/394 base UI, 238/238 explicit DLC-only story, 1/1 DLC UI**. The final 64 DLC entries were added in source order. `authored_text(base, fr, False)` and `edition_text(base, dlc, fr, False)` passed: SFW 1785 story and 394 UI; assembled DLC 2007 story and 395 UI, including 17 verified aliases. These are text structure, source/alias mapping, placeholder/markup checks; they do not constitute a build, full protected-value comparison, semantic audit or runtime test.

A complete English-to-French semantic audit has begun, not finished. `semantic-coverage.json` records the first 45 base story IDs actually read side by side; base UI, DLC story and DLC UI coverage are empty. The reviewed text corresponds to current `dialogue.tsv` SHA-256 `7578a97422c9535ee1a21ca29b8a2f52a48fe4726b7a5886732cdbb5e7478b70`, source inventory `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`, glossary layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109`. Corrected `start_2a8cfefd` to express sunrise rather than sun; retain this ID for the later reproducible correction dependency closure. Prior correction `start_b37f00c2` also needs closure. Independent audit remains pending.

Other current SHA-256: `strings.json` `2eefdb7414339280a38025e71c18f21e8a512b5664c5c5626bcc55049bc70afb`; `nsfw/dialogue.tsv` `4bb65682ccdf2d77b5537107b311873df81743483addcec77d9f62ee16f8359f`; `nsfw/strings.json` `ece354df31fba7ffbd959a14457692b27d8d6acf7631b421766164e888ad8839`; `semantic-coverage.json` `03924557d105ebe8da44259ca762aa14033e75d20ad68ee872f5a96512c90380`; turn-018 batch `7d0a02a1f6541e37b8db24a9f629b21079b4cdc3701dfde90a6d4874d2126839`. Continue the complete semantic comparison from base story ID 46 in source order, then all UI and explicit DLC entries; checkpoint actual read IDs and corrections, build dependency closure, run final text gates and leave independent review pending.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 017. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1785/1785**, base UI **394/394**, explicit DLC-only dialogue **174/238**, DLC UI **1/1**. Added 163 English-source DLC story entries in source order; next missing `start_e53ab00f`. `nsfw/dialogue.tsv` SHA-256 `42fc1489f6836ba142a20c2d4ab60509e19cfa42e461e3430f0dd039b96de05b`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-017/batch.tsv` SHA-256 `812a7d1ab91354cc164c47ec56ea570b3cb4b65410c26b84a5a3ab13dd155ec4`. All 174 authored DLC story IDs are unique, in the DLC-only set, exclude aliases and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue the 64 remaining DLC-only story IDs.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 016. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1785/1785**, base UI **394/394**, explicit DLC-only dialogue **11/238**, DLC UI **1/1**. Added remaining 192 English-source UI strings and DLC `Gallery` → `Galerie`. `strings.json` SHA-256 `2eefdb7414339280a38025e71c18f21e8a512b5664c5c5626bcc55049bc70afb`; `nsfw/strings.json` `ece354df31fba7ffbd959a14457692b27d8d6acf7631b421766164e888ad8839`; batch source `text-assets/cli-localization-completion.uuiga3aa/fr/turn-016/ui.py` SHA-256 `80ff61ee4d8703f96bcc4b0e5888b470ac46224c1e5af7dc58dc68c8d85c84dd`. Builder `string_keys` and `check_value` verified exact 394-key base set, nonempty values, markup, placeholders and date directives; DLC key is the exact set difference and passes the same value check. These structural checks do not establish semantic, layout or runtime acceptance. Full protected-value validation, semantic audit and independent review remain pending. Continue the remaining 227 DLC-only story IDs, excluding aliases.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 015. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1785/1785**, base UI **202/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 194 English-source UI strings, including game menus, accessibility, dates, save formats and confirmations. `strings.json` SHA-256 `7a209118cfdd5ae3167754be0015c54327905fa8a3dc0bc8dd52d06b363a7287`; batch source `text-assets/cli-localization-completion.uuiga3aa/fr/turn-015/ui.py` SHA-256 `01a5ec821b05f8fc790742332339c5610336667065242d8c4b934f4e3f2c030b`. Builder `string_keys` and `check_value` verified all 202 authored UI keys exist, are nonempty and preserve its markup, placeholders and date-directive checks. These structural checks do not establish semantic, layout or runtime acceptance. Full protected-value validation, semantic audit and independent review remain pending. Continue remaining 192 UI keys and DLC delta.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 014. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1785/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added the remaining 129 English-source SFW story entries through credits. `dialogue.tsv` SHA-256 `1c6c16c6cf5b6517a61783b4d851fcde39cd00f9febbd68d7add9e06d513a800`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-014/batch.tsv` SHA-256 `618f1b92f08e89a1c8c0c5f30a002769cae9b8e5f331c6aa8bf70593f304ddce`. All 1785 base story IDs are unique and exactly match the English ID set; ordered interpolation/markup tokens match. This is not full protected-value validation or semantic review. Continue with remaining UI and DLC delta; independent review remains pending.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 013. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1656/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 134 English-source story entries in source order through `start_13e22293`; next missing `start_1fc1186b`. `dialogue.tsv` SHA-256 `24ddad9931ff2c37c1bcd4048eede8659c66f6d162642fc48240d82f3220461c`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-013/batch.tsv` SHA-256 `a6328ffad55fbe86a1325b2b79ddfa087d7eea632709e9c7d3cd1f9563426fb4`. All 1656 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 012. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1522/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 131 English-source story entries in source order through `start_138cc431`; next missing `start_feb01a0c`. Corrected player agreement in previously drafted `start_b37f00c2` from « contente » to « content », following its actual speaker; this change is pending the full semantic audit and dependency review. `dialogue.tsv` SHA-256 `085d499598e4e8872b69ac05a4d03ccc14296816017a31f23745bdca194c4f00`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-012/batch.tsv` SHA-256 `cbed7adf8f5e7cecd68e222e5a0f8d805bc97d477d7fcb7e25042c284593eb96`. All 1522 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 011. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1391/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 136 English-source story entries in source order through `start_553ca432`; next missing `start_3f8a1934`. `dialogue.tsv` SHA-256 `2728c639b8e6625f93d1da366273e626c5d60e2f80ed0e302d9cc54a452d2ec7`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-011/batch.tsv` SHA-256 `8e5b1aa7185c874f1720771731401c7a91e50e713181ab249ca6db5df670638c`. All 1391 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 010. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1255/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 137 English-source story entries in source order through `start_89e46f8c`; next missing `start_39a58b13`. `dialogue.tsv` SHA-256 `bc585f7971014c1a1e2d0efe8cbc56c6b2ca35c5ae5ce161fbd44083db8d5ae9`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-010/batch.tsv` SHA-256 `ba3a8cb5f7140bb155d6dd068ff849401c42fcf0e99958a4f8cb67f9459f5e34`. All 1255 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 009. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **1118/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 135 English-source story entries in source order through `start_e42f01a8`; next missing `start_0a4e0551`. `dialogue.tsv` SHA-256 `192533f91fca2bf951177976622af2c912fd282619eb07d42619cbbda7bb449a`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-009/batch.tsv` SHA-256 `dc8744739dc5db6904bc6bd45789b390f3417570e50f1900b3e695ae8ab7172d`. All 1118 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 008. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **983/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 136 English-source story entries in source order through `start_832646fb`; next missing `start_c0e2c4ba`. `dialogue.tsv` SHA-256 `7b171b9444953853d078f6145e36d4a6aed8f0bc01d5bd3f97485e3a74121ad6`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-008/batch.tsv` SHA-256 `b9a7a6be9a5132eb9f690f129a62058066e24995ec79184e858665f40bc7f9a7`. All 983 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 007. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **847/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 138 English-source story entries in source order through `start_10240298`; next missing `start_4716a333`. `dialogue.tsv` SHA-256 `1039022f41ec344986c8ef18aece14bc3621c5498916cf4e937434c0c8939f86`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-007/batch.tsv` SHA-256 `0131167892eaceaeb8b121eea32619c80c9d9272b061dc2d15b60f7d4b6d0d51`. All 847 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 006. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **709/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 140 English-source story entries in source order through `start_731484ac`; next missing `start_d132f23e`. `dialogue.tsv` SHA-256 `39b8d135f94c7808f6b6366c0956388a59033949235799b6393f2330c102a1b2`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-006/batch.tsv` SHA-256 `4a768a9cf32cc139e124135c97f9d1d7760ed7a630f41f0e616cc77bf2c32cfb`. All 709 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 005. Receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical coverage: base dialogue **569/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Added 144 English-source story entries in source order through `start_4c3b67f7`; next missing `start_e17107e7`. The AI Pixie greeting uses neutral wording, avoiding an unsupported gender assertion. `dialogue.tsv` SHA-256 `875881b7e16572985c38deb0731e585e92f3301895b6a56d1bf90f1fa9624480`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-005/batch.tsv` SHA-256 `8ca6bc2a92d670230bb250d23cd43dc6f96a75a2286c64b7a182c4b0142a12aa`. All 569 authored base story IDs are unique, present in English, and match ordered interpolation/markup tokens. Full protected-value validation, full semantic audit and independent review remain pending. Continue from the next missing ID.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 004. Receipt matched the thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns technical checks and integration.

Canonical authored coverage: base dialogue **425/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. This turn added 123 source-ordered story entries through `start_58708b11`; the next missing ID is `start_d4558b38`. `dialogue.tsv` SHA-256 `2c32126b59072f6d8b6189811a9d6606f74d0626f9aa8440f5021522404386f0`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-004/batch.tsv` SHA-256 `a45b3655b625588af250dd2ec61375b1209919420176fd3946d0734bafcffb0f`. All 425 unique authored story IDs were checked against English source membership and ordered interpolation/markup tokens. Full preserve-exactly validation and complete semantic review remain pending; independent review is pending. Continue from the next missing ID, preserving previous special-scene rows.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 003. Receipt matched the thread/session and specified `gpt-6.1-terra` / high. Text-only work; coordinator owns technical checks and integration.

Canonical authored coverage: base dialogue **302/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. This turn added 139 English-source story entries, in source order, through `start_1fb71b2b`; next missing is `start_406e4ab5`. `dialogue.tsv` SHA-256 `1e6b4778749d7e3f005e4d72f99cc5807eb5939e9c8ade5ef9d1abab79063699`; batch evidence `text-assets/cli-localization-completion.uuiga3aa/fr/turn-003/batch.tsv` SHA-256 `8d898be878c3a3f126aedca570d2b4ce849d2eabc77db5176138fb34898ee292`. Verified all 302 unique authored story IDs belong to the source and their ordered interpolation/markup tokens match. This is not a complete preserve-exactly check or semantic audit. Full source-to-target semantic review and independent review remain pending. Continue at the next missing ID; preserve earlier special-scene translations.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 002. Model receipt matched thread/session and specified `gpt-6.1-terra` / high. Text-only scope; coordinator owns runtime, fonts, screenshots, packaging and Git integration.

Canonical authored coverage: base dialogue **163/1785**, base UI **8/394**, explicit DLC-only dialogue **11/238**, DLC UI **0/1**. Previously saved special-scene drafts were integrated in source order, and 40 further opening story entries authored directly from English. `start_ba9a009d` was corrected to feminine Juno agreement after checking context. `start_66e87b19` refers to the approaching navette; `start_3a73faee` refers to the male protagonist’s anatomy. Special-case decisions and proposed runtime scenarios are in `special-scenes.md`. The full semantic review of all authored rows remains pending; preliminary integration is not editorial acceptance.

Current SHA-256: `dialogue.tsv` `705e56c4b17b43e53cb01243fd4886f4e04f5eaafd4ba0acd94e5573cdcc5a7d`; `strings.json` `9428935978ee4d5e896e6fcd232c1618a12384fcc742e322657b8e84a76983d8`; `nsfw/dialogue.tsv` `324a44e52e85f713e267bda6a603be13d87cac1fb00a98c148e26feb01ff8b08`; `nsfw/strings.json` `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`; `special-scenes.md` `53f36eaad8f542f9a6662da63c408da3f8e290a6e0af0490a5dfd91e643aa09f`. Verified unique known story IDs and exact ordered interpolation/markup in both authored TSV files; DLC alias IDs excluded. Full protected-set and semantic checks remain pending. Independent review remains pending.

Next: continue base story in source order from the first missing ID, preserving the existing special-scene rows; author remaining UI and DLC delta, then run complete deterministic and semantic passes. No genuine text input blocker has been identified.

## Historical checkpoint

# French localization checkpoint

2026-11-13, completion turn 001. The fresh model receipt matched thread and session and specified `gpt-6.1-terra` / high. Owner deferred all runtime, font, visual, packaging and integration work to the coordinator.

Special-scene draft now contains 123 SFW story IDs (`special-draft.tsv`, SHA-256 `ee7b32518cae03758bc23d93f2bfb811018976536e7e7c0f551a286975533a32`) and 11 DLC-only IDs (`nsfw/special-draft.tsv`, SHA-256 `324a44e52e85f713e267bda6a603be13d87cac1fb00a98c148e26feb01ff8b08`): 134 total, 112 new this turn. Both edition registries' player-name and dialogue-timing story IDs are covered by these rows, shared IDs or the existing alias map. Automated check verified unique IDs, source membership and ordered interpolation/markup tokens; DLC aliases were excluded. These are preliminary authored rows, not a complete contextual review or canonical corpus. In particular, check ambiguous referents and surrounding scene context for `start_3a73faee`, `start_66e87b19`, `start_ba9a009d` and all other rows before accepting them.

Eight additional special-scene UI drafts are in `special-ui-draft.json` (SHA-256 `9428935978ee4d5e896e6fcd232c1618a12384fcc742e322657b8e84a76983d8`); source keys, page placeholder and date directives were checked. They still require contextual review and runtime validation. This turn added 120 draft rows in total.

The special-scene decision gate remains pending: review the full groups against both editions in context, settle save-page and input wording and document cases, adapter invariants and tests. Then integrate accepted rows into canonical `dialogue.tsv` and `nsfw/dialogue.tsv` in source order, and continue the remaining corpus. Canonical coverage remains 0/1785 base story, 0/394 base UI, 0/238 DLC-only story and 0/1 DLC UI. Full semantic audit and independent review remain pending. No technical acceptance is claimed.

---

# French localization checkpoint

2026-11-13, text-only continuation. The owner deferred live probes, fonts, screenshots, packaging and CrossOver to the coordinator; those are not text-work blockers. The fresh `text-assets/cli-localization-text.5s1g3lq4/fr/model-verified.json` matched this thread and session and specifies `gpt-6.1-terra`, high effort.

`special-draft.tsv` contains 22 individually authored French SFW special-scene story rows, keyed by stable ID. A partial check established unique source IDs and exact counts for `[pname]`, `{w}` and `NV-0903`; it is not complete protected-value or semantic validation. The special-scene decision gate is **pending**: finish all cases and both edition dependency groups, review wording in context, and document exact decisions before ordinary batches. No complete corpus, full semantic pass or independent review exists. The draft is not yet integrated into builder inputs. Continue against the pinned English and French glossary; preserve Pixie. Existing fingerprint evidence follows below.

---

# French localization checkpoint

2026-11-13. Status: blocked at `probe`; project remains active. No French game corpus has been authored. Independent game-text review is pending; this assignment does not authorize a separate reviewer.

- My Furry Protogen, Steam build 11915262, Ren'Py 8.0.3.22090809, standard localization, English source, French `fr`; original SFW and official NSFW DLC are in scope. The project binding and fixed stage commands are in `localization/STATUS.md`.
- The launcher receipt `text-assets/cli-localization.1_omcg92/fr/model-verified.json` matched this worker's `CODEX_THREAD_ID` and `CODEX_SESSION_ID`, and specified `gpt-6.1-terra`, high effort.
- SFW manifest and receipt both SHA-256 `1ad9c080caed30f47584a2a4062a1ab9ab665eba5bf7e8c35736c5ccfc05c0a8`; NSFW manifest and receipt both `da9a7f72df14f7b725d7566ae0f1cac40f7390042d74b410c9aaf05a48063b6f`. All 13 outputs listed in each receipt match. Inventories: SFW 1,785 story entries and 394 string keys; NSFW 2,007 and 395. Project evidence identifies 1,752 shared story IDs.
- English glossary file SHA-256 `611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926`; French layer `fb9cf9001e409789f4b5909e9c0c80d10403d94a2a2c95c945b2998325bbf109` (UTF-8 compact JSON, unescaped Unicode, original key order); French review receipt `700e2627b6fdc6fde4565379529e284391ac64efc2e17d84e8dd71703f462f1a`. All match `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`. The CLI reports 77 IDs in matching order and no empty entries; the receipt records two 77-entry author self-review layers. Both Pixie entries use `Pixie`. This is glossary evidence, not an independent game-text review.
- Shared feasibility baseline SHA-256 `07e6d9bb909f984e86825a7d67e81132f909fa5f67b0d55928e18f2ddf76db4c`. It records static Nunito coverage for French but no French in-game proof. Czech retry runtime log `text-assets/czech-probe.YNlsON/retry/runtime.txt` SHA-256 `633b3e8894570cab28de42767f4d256591789a3426223d8bae16b30fd5acd313` records muted audio, native mappings, three-line layout, `Štěpán` input and story progression. This is useful harness evidence, not French glyph, wrapping, interpolation, or visual acceptance. Czech checkpoint records incomplete review/restoration evidence; preserve its originals.
- A live game process was present during this session: Wine wrapper PID 88007 and game PID 88011, started 06:41:51 local from the installed Steam directory. Ownership and current state are unknown. The visual-QA skill requires stopping before automation when the game is already running unless that session is explicitly in scope. It was not touched; no new game launch, installation, screenshot or save mutation was attempted. Recheck process state before resuming. Once the existing session is safely closed by its owner, use the existing isolated-save harness and a French-specific muted probe; verify capture provenance, restoration, actual glyphs, wrapping, input/interpolation and progression. The screenshot workflow requires bounded authorized review contexts; this assignment forbids nested agents and CLI sessions, so do not claim unavailable separate review coverage.
- Before ordinary translation, resolve every applicable case in both edition `special-scenes.json` registries with actual French wording, full dependencies, branch identities and feasible technical contracts. The decision gate remains pending. Then translate directly against English and the pinned glossary, preserving protected values and the 1,752 shared IDs. Full semantic review, dependency closure, strict builds for both editions, prior-language regression, runtime and visual checks are not run. SFW coverage: 0/1,785 story, 0/394 strings. NSFW coverage: 0/2,007 story, 0/395 strings.
- Universal process references: `ROUTING.md` SHA-256 `75fac761503c8cfdeee6281629fa158ce6661f8acaf02e225cee4a66861aa093`; `CHECKPOINT.md` `de6fcd0119aceda9edeed0850eaa659b10aaf8e7cfc7e7c22ce7c627c9849b25`; `EARLY-PROBE.md` `834ea4fe965447f00c59680d149fc1445fe08b8f042f30c99a0504354c9bc237`; universal prompt `68acfd48b4408a53af62bc0b021f355f25d089d784d417fe24f30fba3be935dd`; editorial workflow `37ff4269163b17cab4030c2d1c78651f7a79b9c8be3d569a2b9ea7f17748a5dc`. Compare on resume.
- No publication, deployment, push, archival, or site data changes are authorized. No completed French delivery has been committed. Actual model token usage was not exposed in this session; do not infer it from file sizes.
