# Romanian localization checkpoint

2026-11-13. My Furry Protogen, Steam build 11915262, Ren’Py 8.0.3.22090809; standard localization, English source, `siteLocale` `ro`. Base and official DLC are in scope. Current stage: **probe — needs-review**. The owner deferred CrossOver to a later joint pass. No game was launched in this assignment.

## Feasibility and next action

The shared [feasibility baseline](../../text-assets/multilingual-probe.L4KEcD/feasibility-baseline.json) SHA-256 `07e6d9bb909f984e86825a7d67e81132f909fa5f67b0d55928e18f2ddf76db4c` pins the renderer and Nunito SemiBold `f1e4f2f2fc3d7c308dd2c7535c10c26020928a3e424a93712392d05429945cef` and Bold `8b9e27ba172e5b535b1d0564b4882f74aecc77a4dc4d20fc400bd2b2bc4418c1`. Its Romanian synthetic sample `Bună ziua, șapte țări, Î și Â.` has no missing cmap characters in either face; sample file SHA-256 `553b3aaf33bbf718da2211f6451fc83c029bbc21025a2e5f2530b8166d84a6c6`, glyph result `943bebf37637f7db25db99290fcd9e346f36e3082e67c6a3cfd2ed60fe884920`. This sample does not cover all Romanian uppercase and lowercase letters and is not renderer proof.

The Polish runtime probe exercised original string mappings, a no-op story mapping, dialogue/nameplate, input, a wait and progression with the same renderer and fonts. It did not exercise Romanian comma-below characters or Romanian line breaks. It supports those shared paths only, not Romanian acceptance. Original `game/gui.rpy` sets SemiBold for dialogue and interface at size 33, Bold for names at size 40; `game/screens.rpy` defines `say_label`, `say_dialogue`, `input_prompt`, `input` and button text. These are required real-path checks, including settings and dynamic name interpolation; save captions and choice/engine text remain final-resource checks.

For the later authorized joint pass, use the existing isolated-save probe mechanism and verify the actual pinned renderer, font identities and installed build before reusing evidence. Prepare synthetic (not game translation) cases exercising `Ăă Ââ Îî Șș Țț`, especially comma-below forms, in dialogue, a nameplate, Preferences/button text and name prompt/input. Exercise a custom name such as `Ștefan`, empty/whitespace fallback, `[pname]`, `NV-0903`, digits, punctuation, `{w}` and subsequent story ID. Use a long Romanian-character sample to inspect wrapping/clipping at actual sizes; separately check decomposed input if the input method can produce it. Record native state and individual visual observations, including any unreadable marks, and test both relevant font faces. Do not infer a pass from static cmap or the Polish frame. Preserve source and player saves under the shared QA procedure. Reconcile font/build/tool changes before applying the existing harness.

The process references pinned in the shared baseline still match the installed prompt (`68acfd48b4408a53af62bc0b021f355f25d089d784d417fe24f30fba3be935dd`), audit (`37ff4269163b17cab4030c2d1c78651f7a79b9c8be3d569a2b9ea7f17748a5dc`), routing (`75fac761503c8cfdeee6281629fa158ce6661f8acaf02e225cee4a66861aa093`), checkpoint (`de6fcd0119aceda9edeed0850eaa659b10aaf8e7cfc7e7c22ce7c627c9849b25`) and early probe (`834ea4fe965447f00c59680d149fc1445fe08b8f042f30c99a0504354c9bc237`). The currently modified `tools/build_localization.py` hashes to `18937f78194ea7503bf14c316b7db3789013ea9accd6e455eadfe2fd3f909d5d`, differing from baseline `5e65b1d77ddcc340985ab5e8ac4865cc5c1c6c9a40cc408fcfcf60959b799164`; applicability of that changed tool to any future build must be checked, not assumed.

## Source and special-scene preparation

The coordinator verified the pinned bundles and glossary fingerprints. This session hashed their core evidence, without rerunning installation-dependent verification:

| Input | Base SHA-256 | DLC SHA-256 |
| --- | --- | --- |
| manifest.json | `1ad9c080caed30f47584a2a4062a1ab9ab665eba5bf7e8c35736c5ccfc05c0a8` | `da9a7f72df14f7b725d7566ae0f1cac40f7390042d74b410c9aaf05a48063b6f` |
| inventory.json | `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff` | `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea` |
| preserve-exactly.json | `f50583a62ea41e826c4668f8595592c60605ca0a3f48e2415a1f695846cd2afd` | `36446dab69a956c65997d173f6d088c617514e4afbafb5158f7d66772a406c22` |
| special-scenes.json | `5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923` | `2412020e4c4024a82dad7535976a6e1ff8239fec1214c4ac7c211492a75c6f8b` |

Both registries identify player-name, juno-nameplate, save-formats, dialogue-timing, main-menu-logo and watch-cutscenes. The base/DLC occurrence counts respectively are 84/92, 4/3, 6/6, 47/42, 1/1 and 20/16. These counts overlap and are not translation denominators. Registries state their own discovery exclusions, including full literary review, remaining image/video review, audio transcription and runtime reachability; project checkpoint separately records the two watch videos reviewed without captions. Do not infer exhaustive literary special-scene discovery from the registries. Locale decisions and full target wording are **not-run**. Once the feasibility gate passes, reconcile source/registry coverage and applicable receipt evidence, then settle every in-scope decision against both editions and the approved glossary before ordinary translation.

`./vnrevival glossary guide` and `./vnrevival glossary work my-furry-protogen ro` report 77/77 structural IDs in order, no empty entries; CLI explicitly does not infer editorial acceptance. Shared glossary receipt (`5935841fb335bb53db74afe2134e70c45068ee8dbea7cf6a87f287aef794cddd`) pins English `611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926`, Romanian layer `07aece1f3b641cbf351ade2e1deeb9584bc4fe5f7b1525362e021ecabdf4584c`, and review receipt `de94fc20a0c29597aa58d45eae56378aca6f046891ec1d1b01ac19ccd81df24a`. Reconfirm actual files and both editorial layers before use, including Pixie. No glossary text was translated here.

## Coverage and handoff

| Stage | Status |
| --- | --- |
| scope | Bound to this checkout and the two pinned bundles; English is sole official locale. |
| probe | Needs-review: Romanian actual rendering and progression not verified. |
| source / glossary | Existing evidence pinned above; full verification for text work pending after probe. |
| translate-edit | 0/1,785 base story, 0/394 base UI, 0/238 explicit DLC story, 0/1 DLC UI authored or edited in this assignment. Preserve shared IDs and aliases; these denominators follow the assignment and do not imply independent IDs for aliases. |
| editorial, fonts, textures, package, runtime, visual, delivery | Not-run. |
| screenshot-upload / screenshot-review | Not-run; outside this assignment. |

Next: perform the later joint Romanian real-game probe when authorized, inspect and record all required roles and outcomes, then verify source/glossary and resolve all special-scene decisions before any ordinary translated batch. The shared checkout has unrelated concurrent changes; this assignment has no authority over the shared Git index or other locales. No commit, installation, publication, deployment or archival was performed. Model receipt for this session: `text-assets/cli-localization-wave-02.4tve4ir7/ro/model-verified.json`, matching thread `01a1d275-ddde-77f3-9d9b-266488e3d5d7`, `gpt-6.1-terra/high`. Actual request usage is not exposed in this checkpoint; do not estimate it from file size.
