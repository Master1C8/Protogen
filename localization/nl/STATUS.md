# Dutch localization checkpoint — 2026-11-13

## Current state

My Furry Protogen, Steam build 11915262, Ren’Py 8.0.3.22090809; standard localization, English source, siteLocale `nl`, base and official DLC. The owner decision in [the shared checkpoint](../STATUS.md#translation-queue-and-deferred-crossover-checks) permits text work before the joint CrossOver pass. This turn's receipt verifies this thread as `gpt-6.1-terra` / `high`. Scope is text and editorial; runtime, fonts, screenshots, packaging and Git integration belong to the coordinator.

| Field | Actual state |
| --- | --- |
| Authored text | Base story **1,785/1,785**, base UI **394/394**; explicitly authored DLC story **238/238**, DLC UI **1/1**. The DLC validator also resolves 17 aliases from base (255/255 total edition delta). All authored rows are present. |
| Special-scene decisions | Registered case decisions passed after review of all drafted name/timing lines against their English and immediate neighbors; see [special-scenes.md](special-scenes.md). Full-scene semantic review and runtime remain separate and pending. |
| Glossary | 77/77 IDs and pinned standard review receipt reused; Pixie kept as approved. |
| Editorial | Author semantic comparison complete: 1,785/1,785 base story IDs; base UI 394/394, explicit DLC story 238/238, DLC UI 1/1. Exact IDs are in `semantic-coverage.json`; independent review not run. |
| Fonts / feasibility | Dutch synthetic cmap sample covered in both pinned Nunito faces; actual Dutch rendering unverified, deferred by owner. |
| Text validation | Strict `edition_text(..., draft=False)` passed full identity, alias coverage and placeholder/tag count checks on both inventories on 2026-11-13. It does not validate contextual meaning, runtime or full source-versus-applied protected values. |
| Build / runtime / visual / screenshots / delivery | Not run; assigned to coordinator or outside this session. |

Authored artifact SHA-256: `dialogue.tsv` `1717a55495e408dbc379bceef739f52752f2a8f5a5972a57a62e0e2757da0539`; `strings.json` `82722a59e747d87cc527d5ff48c7cd9d44d62515390635d2b616f6438f509fb3`; `nsfw/dialogue.tsv` `aada5ac07b41833f7a2525ad9df9ce37ed012f4948fa3adb6b3280a083a92058`; `nsfw/strings.json` `c88448b3716b8b7869477d91de799f1bc7a4293e2664481068956e619d32dd1c`.

**Next:** Complete source-versus-applied protected-value comparison and arrange independent editorial review; preserve the edition alias rule. Runtime, fonts, screenshots, packaging and Git integration remain with the coordinator.

## Pinned evidence and applicability

The shared [feasibility baseline](../../text-assets/multilingual-probe.L4KEcD/feasibility-baseline.json) SHA-256 `07e6d9bb909f984e86825a7d67e81132f909fa5f67b0d55928e18f2ddf76db4c` pins game version, renderer, fonts, source and process references. The process references currently match its hashes: prompt `68acfd48b4408a53af62bc0b021f355f25d089d784d417fe24f30fba3be935dd`, audit `37ff4269163b17cab4030c2d1c78651f7a79b9c8be3d569a2b9ea7f17748a5dc`, routing `75fac761503c8cfdeee6281629fa158ce6661f8acaf02e225cee4a66861aa093`, checkpoint `de6fcd0119aceda9edeed0850eaa659b10aaf8e7cfc7e7c22ce7c627c9849b25`, early probe `834ea4fe965447f00c59680d149fc1445fe08b8f042f30c99a0504354c9bc237`.

The Polish in-game probe tested native story/string mappings, name input, dialogue, wait and advancement; its sample contains Polish accents and mixed Latin/digits, not Dutch `ë` and `é`. It supports the existence of shared paths, not Dutch acceptance. The current `tools/build_localization.py` hash `18937f78194ea7503bf14c316b7db3789013ea9accd6e455eadfe2fd3f909d5d` differs from baseline `5e65b1d77ddcc340985ab5e8ac4865cc5c1c6c9a40cc408fcfcf60959b799164`; assess the relevant adapter delta before reusing that evidence. This difference alone does not establish a defect.

Pinned font faces: `game/fonts/Nunito-SemiBold.ttf` `f1e4f2f2fc3d7c308dd2c7535c10c26020928a3e424a93712392d05429945cef`; `game/fonts/Nunito-Bold.ttf` `8b9e27ba172e5b535b1d0564b4882f74aecc77a4dc4d20fc400bd2b2bc4418c1`. Original `game/gui.rpy:58,62,65` assigns SemiBold to dialogue/interface and Bold to names; choices use the text font. `game/screens.rpy` defines `say_dialogue`, `say_label`, input/prompt, navigation and preferences styles; `game/script.rpy:82` calls name input with length 12. These are source bindings, not proof of actual rendered output.

Existing synthetic sample: `Geëerd, één nieuwe coöperatie en ideeën.` (`samples.json` SHA-256 `553b3aaf33bbf718da2211f6451fc83c029bbc21025a2e5f2530b8166d84a6c6`). `glyphs.json` SHA-256 `943bebf37637f7db25db99290fcd9e346f36e3082e67c6a3cfd2ed60fe884920` records no missing characters in either face for this sample. It does not prove marks, metrics, wrapping, input, or full Dutch corpus coverage. For the eventual real probe, use this sample in dialogue, nameplate, preferences/navigation and name prompt; enter a 12-character-or-shorter name such as `Zoë`, verify interpolation with `NV-0903` and `42`, exercise an inline `{w}` and next story ID, plus a deliberately long Dutch synthetic line to inspect wrapping/clipping. Include blank and whitespace input fallback. Verify actual glyphs, sizes, line breaks and the applicable renderer/adapter on each path; do not infer acceptance from cmap or Polish frames.

Source pins, independently hashed this session (coordinator reported full bundle verification): base manifest `1ad9c080caed30f47584a2a4062a1ab9ab665eba5bf7e8c35736c5ccfc05c0a8`, inventory `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`, preserve-exactly `f50583a62ea41e826c4668f8595592c60605ca0a3f48e2415a1f695846cd2afd`, special scenes `5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923`. DLC manifest `da9a7f72df14f7b725d7566ae0f1cac40f7390042d74b410c9aaf05a48063b6f`, inventory `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea`, preserve-exactly `36446dab69a956c65997d173f6d088c617514e4afbafb5158f7d66772a406c22`, special scenes `2412020e4c4024a82dad7535976a6e1ff8239fec1214c4ac7c211492a75c6f8b`. These individual hashes do not substitute for the full source verification stage.

The glossary receipt `5935841fb335bb53db74afe2134e70c45068ee8dbea7cf6a87f287aef794cddd` pins English raw source `611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926`, Dutch locale fingerprint `79db69215ba5b6c5f31cc18d73ae984aeb243ce293255ac337319de70868de79`, Dutch review receipt `5fbfcd924174a821258236fc3389a81caacc24622dce1a1ba2a675c77a8e0ae2`. English source and review receipt file hashes match; coordinator verified the locale fingerprint. `glossary guide` and `glossary work my-furry-protogen nl` were run read-only.

## Special-scene scope

Both pinned registries enumerate player name/interpolation, Juno nameplate, save page/date formats, dialogue waits and speed tag, main-menu logo, and watch cutscenes. The edition-specific occurrence lists differ; both must be used. See [the Dutch decisions](special-scenes.md) for wording, pending contextual review and exact next checks.

Semantic comparison checkpoint: 2026-11-13, all 1,785 base story IDs, 394 base UI keys, 238 explicitly authored DLC story IDs and one DLC UI key compared with English. Exact IDs are in `semantic-coverage.json`, SHA-256 `c0f071319531793571cebb21211006a592b25698f8c28263ac913b9ebab37241`, bound to the authored hashes above and pinned inventories. Ten findings in `semantic-findings.md` were rechecked in neighboring context and corrected; strict text validation passed after correction. This is an author comparison, not independent review. Full protected-value comparison and runtime remain pending.

## Reproducible text validation closure

Inputs: base inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; DLC inventory `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea`; `tools/build_localization.py` `18937f78194ea7503bf14c316b7db3789013ea9accd6e455eadfe2fd3f909d5d`; `tools/extract_text.py` `db7ae33202a62d85f882e142e11bc60de8332c896e8b1077a1781ab43c5ce691`; `localization/nsfw-story-aliases.json` `6b020423fc1c45e678c6c8ef6914161ed2978864f91c805d3c0d286c084b8f7c`; and the four authored hashes above. Glossary and special-scene pins are recorded above and in `special-scenes.md`.

From the project root, run `python3 -B -c "import sys,json; from pathlib import Path; sys.path.insert(0, 'tools'); from build_localization import edition_text; edition_text(json.loads(Path('text-assets/inventory.json').read_text()), json.loads(Path('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json').read_text()), Path('localization/nl'), False)"`. Result: base 1,785/1,785 story, 394/394 UI; DLC delta 255/255 including 17 aliases, 1/1 UI. This validates mappings and marker counts; it does not apply files to the game or establish rendering.
