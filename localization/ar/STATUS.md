# Arabic localization checkpoint

## Current state — 2026-11-13

Stage `editorial`: author English comparison complete; independent review and three source-context findings remain pending. The owner permits text work before the joint runtime and visual pass. Locale `ar`, Steam build 11915262, base and official DLC. Coordinator owns runtime, fonts, screenshots, packaging and integration.

Authored coverage: base story **1,785/1,785**, base UI **394/394**, DLC-only story **238/238**, DLC UI **1/1**. The existing alias mechanism supplies 17 additional DLC story IDs. The author compared every authored ID against English; exact ID arrays are in `semantic-coverage.json` and batch evidence is in `semantic-batch-001.json` through `semantic-batch-010-dlc.json`. Thirty-one findings were recorded; 28 proposed corrections were applied after preflight and checked against their exact recorded values in `semantic-corrections-001.json`. These checks do not constitute independent editorial acceptance.

Three findings require source-context decisions: `start_0bf2fe34` and prayer lines `start_63edd260`, `start_6e7f7469`, `start_1cc22a45`, `start_04867749`, `start_90581042` use dual Arabic address although English initially names either divine figure and English “you” does not resolve number; review the full prayer before revising. At `start_3e4333d1`, English calls the backpack Juno's while preceding `start_976b6126` says the protagonist's; Arabic currently leaves ownership neutral. At DLC `start_5c6117e8`, source binds the line to speaker `p` even though it addresses `[pname]` after describing Juno's response; the original binding is preserved. Do not silently claim these issues resolved.

Strict `build_localization.edition_text(..., draft=False)` passed all authored key coverage, markup, placeholders, shared edition fields and alias bindings; base and resolved DLC story `preserveTokens` counts match the source. The audited ID sets exactly match the four authored files, and all 28 post-correction values match the correction record. `semantic-dependency-closure.json` pins source, exports, registries, glossary receipt, aliases, validation tools, authored inputs and review receipts and describes reproduction. This is not an original-versus-reinserted protected-field comparison, a build, runtime verification or independent review.

Current SHA-256: base dialogue `05eabecce4f70ee9882a5f1fc65964907e8ceae467ff545d53562175dd2155a7`; base strings `140529da6184aa9446d4e18d67a61caf003241ea921b011c5cafe86b94b880f2`; DLC dialogue `f0f59d7a8c95d84e872ca158737b9b3030b6963cbf88c1b7bf34e0774a6d9b0d`; DLC strings `e4ef0af0205f116642874b2a6769dbdf951d65379aadce3da63494e715492daa`; decisions `d606fc335cb397b216b55bfce687b6c642470bd03551e1282b1d032e9fb1cc33`. Glossary receipt pins English `611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926` and Arabic `a7d48031eb50242e14d2e11f3ec41296ca6f8f10c1ea7781d179dbc0dae47461`; preserve Pixie as `بيكسي`.

Next: resolve the three precise source-context findings where evidence permits, perform independent editorial review when available, and complete the protected original-versus-reinserted check through the coordinator's authorized workflow. The shipped renderer's disconnected Arabic remains a known failure; an isolated Ren’Py 8.2.3 HarfBuzz test demonstrated an alternative, not a final package. Editable input, bidirectional ordering, font coverage, final rendering, DLC runtime and CrossOver remain unverified.


## Prior rendering decision — 2026-11-13

Proceed with text work. The owner approved an isolated game test. The known
dialogue shaping failure in stock Ren’Py 8.0.3 has a demonstrated alternative
in the actual base game under native macOS Ren’Py 8.2.3 with locale-scoped
`shaper "harfbuzz"` and pinned fonts. Contextual Arabic forms and combining marks visible in speaker and dialogue, with Arabic player name, Arabic-Indic digits and the internally LTR identifier NV-0903.

The input widget accepted the synthetic name, the game stored and interpolated
it, and the story advanced through the inline wait. Editable keyboard and caret
behavior, final font fallback, DLC runtime and CrossOver remain pending. Keep
authored translations in logical Unicode. Finish and review the special-scene
decisions, then proceed with translation and author semantic review. The shared
production engine is not changed. Evidence: `text-assets/harfbuzz-isolated/result.json`
(SHA-256 `cd8e950a0a22bb24e88a3d0e7259543bbff7f5f8a9d8919dc04af6e1045acc1e`).

## Previous checkpoint

2026-11-13 · My Furry Protogen, Steam build 11915262 · siteLocale `ar` · standard localization from English · base and official DLC.

**Current stage: probe — blocked.** The locale-scoped DejaVu replacement removes the observed missing-glyph boxes in the tested Arabic navigation label, and the probe reports story progression and restoration of the prior font map and bidi flag on switching to Polish. It does not resolve Arabic shaping: the settings heading displays the letters of `مَرْحَبًا` disconnected, including connections required between م and ر and between ح and ب. The expected source sample is in `text-assets/multilingual-map-probe.HopRBo/ar-probe.rpy`. Arabic joining is required for the locale, so ordinary translation remains blocked pending a working shaping mechanism and evidence. The observed navigation sample is not proof of coverage in every font role.

Evidence: `text-assets/multilingual-map-probe.HopRBo/runtime-evidence.json` SHA-256 `a61d0b25753c62034712cd795e64921d599d042f8f93c1bc7ea7fb3014838c52`; settings original `screens/ar-02-settings.png` SHA-256 `7595fa82e711c33ab4acd755f5484576532b07c9067776dd1fd9cef262347798`. Prepared review crop `text-assets/cli-localization-wave-05/ar/settings-crop.webp`, source bounds `(35, 20, 180, 100)`, SHA-256 `0e649c38c9ddd6ed731381212301cbb5057cb4bc2d00f36a109ce83cdb2f4ad7`. The crop was produced from the unchanged original using the workstation preview policy. Mixed-direction ordering, input rendering, other text roles and final real-game rendering remain unverified; progression is not visual acceptance.

The coordinator supplied verified shared source and 77-entry glossary receipts; the current assignment pins base `text-assets/`, DLC `text-assets/edition-qa.0bfO9x/nsfw-export`, and `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`. Shared process and command binding: `localization/STATUS.md`. Both special-scene registries were inspected; locale wording and feasible adaptation contracts are not yet complete. Preserve Pixie as a proper name. No authored dialogue or UI exists for this locale in this turn: base story 0/1,785, base UI 0/394, DLC explicit story 0/238, DLC UI 0/1. Aliases must not be authored twice. No semantic audit or protected-field application check has run.

Next: resolve and demonstrate Arabic joining in the required renderer without disturbing the source or other locales; then reassess the gate, complete and review all locale special-scene decisions, and start contextual English-to-Arabic batches. Mixed-direction text, name input, and final runtime/visual checks remain pending the owner-directed joint pass where applicable. No game launch, installation, Git write, or archival was performed in this assignment.
