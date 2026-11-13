# Hindi localization checkpoint — 2026-11-13

My Furry Protogen, Steam build 11915262, standard localization from English, `siteLocale hi`, canonical checkout `/Users/antonkrutov/Desktop/Protogen`. The current owner decision permits text work now and defers runtime, fonts, visual checks, packaging and Git integration to the coordinator. `text-assets/cli-localization-wave-05-shaping-text/hi/turn-029/model-verified.json` matched this session's thread and recorded `gpt-6.1-terra` / `high`. No delegation or translation service was used.

## Current coverage and next action

| Authored inputs | Coverage |
| --- | ---: |
| Base story | 1,785 / 1,785 |
| Base UI | 394 / 394 |
| Explicit DLC-only story | 238 / 238 |
| DLC UI | 1 / 1 |

All authored text coverage is complete: 1,785 base story, 394 base UI, 238 explicit DLC story, and one DLC UI. All 17 DLC aliases resolve from base and are not separately authored. Turn 018 added the final 108 DLC story IDs in two source-context batches (`text-assets/cli-localization-wave-05-shaping-text/hi/turn-018/batch-01.tsv` and `batch-02.tsv`). Offline strict `edition_text(..., False)` passed coverage, placeholders, shared bindings and alias checks; it does not prove semantic quality or complete protected-value reinsertion.

The author semantic comparison covers all authored IDs: 1,785 base story, 394 base UI, 238 explicit DLC story and one DLC UI, recorded in `semantic-coverage.json`. Turn 029 reviewed DLC story rows 41–238 and the DLC UI key, correcting four phrasing or omission issues. Exact audited IDs, corrections, edition bindings and hashes are in `text-assets/cli-localization-wave-05-shaping-text/hi/turn-029/audit-batch.json`; strict offline validation passed. One precise finding remains: DLC `start_5425eab6` has an ambiguous English pronoun about who arches, while the current Hindi attributes the action to Juno. Resolve through independent editorial review against source context; comparison coverage is not acceptance. Independent review remains pending.

Special-scene target decisions and all registered timed lines are in `special-scenes.md` and `dialogue.tsv`; they were author-reviewed against their English context. Positive and negative acceptance scenarios and implementation limits remain documented. Pixie is the proper name पिक्सी for both AI and shuttle. The owner permits deferring untested rendering. The stock engine's previously demonstrated shaping defect remains recorded; a locale-scoped HarfBuzz alternative produced correct conjunct and vowel placement in an isolated native Ren’Py 8.2.3 base-game test, with explicit Latin font run for `NV-0903` (`text-assets/harfbuzz-isolated/result.json`, SHA-256 `cd8e950a0a22bb24e88a3d0e7259543bbff7f5f8a9d8919dc04af6e1045acc1e`). Editable caret and composition, final fallback, DLC, CrossOver and the final localized game remain unverified. `renderer-plan.md` retains the earlier failure evidence and regression proposal.

## Validation and pinned inputs

Offline draft validation used `build_localization.edition_text` against the two pinned inventories. It passed unique authored IDs, allowed keys, markup/placeholders, shared-edition source fields and alias equality; its strict DLC story delta count was 255/255: 238 explicitly authored rows and 17 populated aliases. It did not launch or install the game, check installed source bytes, perform a complete protected-value reinsertion comparison, prove natural language quality, or verify runtime. No full build or independent review was run.

Current SHA-256: `dialogue.tsv` `b9349b58f3e752f1eabff64691aaf30c157ea4f3bc57c1c049b58d1614d8acf1`; `strings.json` `8635f96f750d0f9b0c57187c034d6cc8cff08dce5651f475259333e400f89b1b`; `nsfw/dialogue.tsv` `f21817a69d76f6f517d96811c51fcb1be0ac0e71c7ac715bc853c2acd74f8bdd`; `nsfw/strings.json` `590e05a35a40397ff829997bd8d697500970ed11eb8b170a6d0906b984f1c5ab`; `special-scenes.md` `932a58b126c3b5d141d80f00108dcadf3cb629b7fc6c9b8c341891c2d9d1f636`.

Base inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`, preserve set `f50583a62ea41e826c4668f8595592c60605ca0a3f48e2415a1f695846cd2afd`; DLC inventory `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea`, preserve set `36446dab69a956c65997d173f6d088c617514e4afbafb5158f7d66772a406c22`. Base manifest `1ad9c080caed30f47584a2a4062a1ab9ab665eba5bf7e8c35736c5ccfc05c0a8`; aliases `6b020423fc1c45e678c6c8ef6914161ed2978864f91c805d3c0d286c084b8f7c`. Approved source glossary `611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926`, Hindi layer `a45014914cf80b2c0ac4e2948c66362055ce7e57fc9adf16425225c7dde879f8` and review receipt `5b0804c29bea6c2b30cfa35b766e7b8d5877131431f5cbd6fad6b6625327f003`, previously verified by coordinator against `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`. Locale mirror and installation were not rechecked this turn.

Process binding is `localization/STATUS.md` and shared ROUTING (`75fac761503c8cfdeee6281629fa158ce6661f8acaf02e225cee4a66861aa093`), CHECKPOINT (`de6fcd0119aceda9edeed0850eaa659b10aaf8e7cfc7e7c22ce7c627c9849b25`), EARLY-PROBE (`834ea4fe965447f00c59680d149fc1445fe08b8f042f30c99a0504354c9bc237`), universal prompt (`68acfd48b4408a53af62bc0b021f355f25d089d784d417fe24f30fba3be935dd`) and audit workflow (`37ff4269163b17cab4030c2d1c78651f7a79b9c8be3d569a2b9ea7f17748a5dc`).

Stage status: scope/source/glossary reused; probe alternative demonstrated with limits above; translate-edit in progress; editorial, resources, package and final runtime pending; screenshot upload/review outside this text assignment; delivery and Git integration assigned to coordinator. Token telemetry by phase was not exposed, so usage is unknown.
