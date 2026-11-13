# Hebrew localization checkpoint

2026-11-13. Standard localization from English; Steam build 11915262, base and official DLC. Scope restricted to `he`. Model receipt: `text-assets/cli-localization-wave-05/he/model-verified.json` matched this thread, `gpt-6.1-terra` / high. Owner defers game launch, installation and CrossOver to the joint pass.

Both pinned export manifests' 13 output hashes match. Base inventory `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`; DLC `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea`. The coordinator verified the 77-entry Hebrew glossary and its review against `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`; the local source glossary and Hebrew review file hashes also match that receipt. The glossary work command reports all IDs present; this structural result is not an independent editorial review.

Static sample coverage: `text-assets/multilingual-probe.L4KEcD/dejavu-glyphs.json` reports no missing sample code points in either DejaVu face, including the sample's Hebrew marks. Stock Nunito lacks Hebrew. The first Arabic style override failed on a navigation button (`text-assets/multilingual-font-probe.FSkUIw/visual-review.json`); the later font replacement map ran and restored prior font map and bidi flag on switching locales (`text-assets/multilingual-map-probe.HopRBo/runtime-evidence.json`), but its visual result remains needs-review. This does not demonstrate a Hebrew-specific failure or a visual pass. Hebrew marks, bidi, mixed text, name input and wrapping remain unverified.

Initial checkpoint before the continuation below: special-scene gate was needs-review, with 9/1,785 base story and 8/394 base strings; DLC authored 0/238 story and 0/1 UI. The draft edition validator checked authored IDs, tags, placeholders, keys and edition/alias bindings. This does not compare every protected occurrence against a delivered build or prove editorial correctness. No ordinary translation batch, full semantic audit, independent review, build, runtime or visual check has been completed.

This initial next action was completed in the continuation below; the source discrepancy and independent audit remain open.

## Continuation, 2026-11-13

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-001/model-verified.json` matches the same thread and records `gpt-6.1-terra` / high. The special-scene decision preparation is complete for the two registered cases' story bindings and the four other registered cases; see `special-scenes.md` for actual wording, mapping, acceptance scenarios and limits. The DLC line `start_5c6117e8` retains the original player speaker and self-address despite surrounding text suggesting Juno; it is an unresolved source discrepancy, not a silent correction. Full semantic audit must revisit it.

Current authored coverage: **152/1,785 base story; 8/394 base UI; 11/238 explicitly authored DLC story; 0/1 DLC UI**. This turn added 143 base story and 11 DLC story rows. The first ordinary narrative batch runs from `start_6f3a1b7b` through `start_b43cb176`; the other additions are registry-bound case lines in source order. All source English was the translation source and immediate edits were made in context. The draft edition validator passed after the batch: 152 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 resolved aliases). It checks authored keys, placeholders, markup, date directives, source shared-ID equality and edition aliases. The previously verified source manifests pin the untouched original scripts and protected inventory; this is not a full post-build protected-value comparison or a semantic audit. No delivery has been built.

Next: continue ordinary base text in source order immediately after `start_b43cb176`, skipping already authored case IDs; then complete all 394 UI keys and 238 explicitly authored DLC delta rows and its `Gallery` key. Validate after contextual batches. Complete the full English comparison with durable stable-ID audit coverage only after text is complete; independent review remains pending. The supervisor resumes the same verified session; this session does not launch jobs. Rendering, font replacement, bidi and input are unverified and belong to the later joint pass.

## Continuation, turn 002

The turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-002/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **135 base story rows**, from `start_1f3e372c` through `start_ee209a95`, skipping the existing case-bound lines. The batch follows the protagonist's memories of the prophecy, Damien, an attempted date and the approach to his birthday celebration. Translated directly from English and immediately edited in context; this is not the separate full semantic audit.

Current authored coverage: **287/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. The draft edition validator passed after each contextual batch and after source-order sorting: 287 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). It checks authored IDs, markup, placeholders, format directives and edition bindings; it does not establish editorial correctness or final protected-field parity in a package. No runtime or visual test was performed. The source discrepancy in `start_5c6117e8` and independent review remain pending.

Next: continue base story immediately after `start_ee209a95`, retaining prior special-scene rows; complete remaining UI and explicit DLC content in source order. Validate each batch, then perform the full semantic review with exact coverage IDs after translation is complete. The coordinator owns resumption and the later runtime, font, visual, packaging and Git stages.

## Continuation, turn 003

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-003/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **124 base story rows**, from `start_dad3e62c` through `start_58b443e9`, skipping previously authored special-scene lines. The translated sequence covers the birthday speech, escape, riverbank and first encounter with Juno. Wording was authored from English and immediately edited in context; the separate full semantic audit is pending.

Current authored coverage: **411/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each contextual batch and source-order sorting: 411 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). These checks cover authored IDs, placeholders, markup and edition bindings, not complete semantic review or final protected-field parity in a package. The recorded `start_5c6117e8` discrepancy, independent review, and actual rendering remain pending.

Next: continue base story immediately after `start_58b443e9`, retaining and skipping existing case-bound rows; then complete remaining UI and explicit DLC content. The coordinator resumes the verified session and owns the later runtime, visual, font, packaging and Git stages.

## Continuation, turn 004

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-004/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **123 base story rows**, from `start_c0b04ea7` through `start_7eb4de78`, skipping existing special-scene entries. The batch covers Juno's introduction, the guide agreement, and the first encounter with Pixie. Written from English and immediately edited in context, including distinct AI and shuttle references. The full semantic audit remains pending.

Current authored coverage: **534/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed for each batch and after source-order sorting: 534 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). It checks authored keys, markup, placeholders and edition bindings; it is not semantic or final package protected-value acceptance. The source discrepancy `start_5c6117e8`, independent review and rendering remain pending.

Next: continue base story after `start_7eb4de78`, preserving already authored case-bound rows; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 005

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-005/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **129 base story rows**, from `start_0d81f008` through `start_3d7fdd0c`, skipping previously authored case-bound lines. This covers their preparation, the conversation about birthdays, the river crossing, forest sampling and the protagonist's symptoms. Written from English and immediately edited in context; the full semantic audit remains pending.

Current authored coverage: **663/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 663 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). This checks authored keys, placeholders, markup and edition bindings, not semantic correctness or final package protected-field parity. The previously recorded `start_5c6117e8` source discrepancy and independent review remain pending. Rendering remains unverified.

Next: continue base story after `start_3d7fdd0c`, skipping existing case-bound rows; complete remaining UI and DLC content. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 006

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-006/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **128 base story rows**, from `start_212ce61a` through `start_e8c0a9bf`, skipping previously authored special-scene rows. This covers the poisoned fruit, overnight stay, the protagonist's thoughts about home, and the meal of roots. Wording is directly from English and immediately edited in context; full semantic audit is pending.

Current authored coverage: **791/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 791 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The source discrepancy `start_5c6117e8`, independent review and rendering remain pending.

Next: continue base story after `start_e8c0a9bf`, skipping existing case-bound rows; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 007

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-007/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **125 base story rows**, from `start_f03430dc` through `start_04111b8a`, skipping previously authored case-bound lines. The batch covers the swamp, Juno's origins and their conversation about fate and freedom. Written from English and immediately edited in context; the full semantic audit remains pending.

Current authored coverage: **916/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 916 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The previously recorded source discrepancy `start_5c6117e8`, independent review and rendering remain pending.

Next: continue base story after `start_04111b8a`, skipping already authored special-scene lines; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 008

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-008/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **126 base story rows**, from `start_83690d06` through `start_bfdffee3`, skipping previously authored special-scene rows. The batch covers the desert, giant-worm attack and the confrontation over the protagonist's lie. Written from English and immediately edited in context; the full semantic audit remains pending.

Current authored coverage: **1,042/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 1,042 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy, independent review and rendering remain pending.

Next: continue base story after `start_bfdffee3`, skipping already authored special-scene lines; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 009

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-009/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **124 base story rows**, from `start_14a7fb29` through `start_071fb6a2`, skipping existing case-bound lines. The batch covers the confession, Juno's account of Toshi, reconciliation and discovery of diseased vegetation. Authored from English and immediately edited in context; the full semantic audit remains pending.

Current authored coverage: **1,166/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 1,166 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy, independent review and rendering remain pending.

Next: continue base story after `start_071fb6a2`, skipping previously authored special-scene rows; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 010

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-010/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **128 base story rows**, from `start_f1b69ec8` through `start_1c5ad493`, skipping existing case-bound lines. This covers the infected forest, Juno's investigation and the decision to work together. Written from English and immediately edited in context; full semantic audit remains pending.

Current authored coverage: **1,294/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 1,294 base story, 8 UI and 14/255 DLC delta bindings (11 authored plus 3 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy, independent review and rendering remain pending.

Next: continue base story after `start_1c5ad493`, skipping previously authored special-scene rows; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 011

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-011/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **122 base story rows**, from `start_a55ec2b9` through `start_0504e2d9`, skipping previously authored special-scene lines. The batch covers cure research and the developing relationship. Written from English and immediately edited in context; the complete semantic audit remains pending.

Current authored coverage: **1,416/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 1,416 base story, 8 UI and 23/255 DLC delta bindings (11 authored plus 12 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy, independent review and rendering remain pending.

Next: continue base story after `start_0504e2d9`, skipping existing special-scene rows; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 012

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-012/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **124 base story rows**, from `start_4d49d9a8` through `start_dfc37bc0`, skipping existing case-bound lines. This batch covers the cure test and preparations to visit the village. Written from English and immediately edited in context; full semantic audit remains pending.

Current authored coverage: **1,540/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 1,540 base story, 8 UI and 28/255 DLC delta bindings (11 authored plus 17 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy, independent review and rendering remain pending.

Next: continue base story after `start_dfc37bc0`, skipping previously authored special-scene lines; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 013

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-013/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **123 base story rows**, from `start_83ba1284` through `start_298cb907`, skipping existing case-bound lines. This covers the devastated village, the protagonist's mother and his decision to confront the anomaly. Written from English and immediately edited in context; the full semantic audit remains pending.

Current authored coverage: **1,663/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 1,663 base story, 8 UI and 28/255 DLC delta bindings (11 authored plus 17 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy, independent review and rendering remain pending.

Next: continue base story after `start_298cb907`, skipping previously authored special-scene lines; complete remaining UI and DLC text. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 014

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-014/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **122 base story rows**, from `start_016d04d6` through `start_af456bab`, skipping previously authored case-bound lines. The base story is now fully authored, including credits. Written from English and immediately edited in context; full semantic audit remains pending.

Current authored coverage: **1,785/1,785 base story; 8/394 base UI; 11/238 explicit DLC story; 0/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 1,785 base story, 8 UI and 28/255 DLC delta bindings (11 authored plus 17 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy, independent review and rendering remain pending.

Next: author remaining base UI and explicit DLC text in source context, preserving aliases. After all four authored sets are complete, run strict text validation and a full English semantic comparison with durable stable-ID coverage. The coordinator resumes the verified session and owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 015

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-015/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **138 base UI keys and the DLC Gallery key**. The batch covers character labels, navigation, preferences, controls, accessibility and calendar names. Unchanged key names such as Enter, Ctrl and font names are intentional; `MyFurryProtogen` remains the original title identifier. English was the source and wording was immediately edited. Full semantic audit remains pending; interface rendering, including RTL controls and dates, is unverified.

Current authored coverage: **1,785/1,785 base story; 146/394 base UI; 11/238 explicit DLC story; 1/1 DLC UI**. Draft edition validation passed after each batch: 1,785 base story, 146 UI and 28/255 DLC delta bindings (11 authored plus 17 aliases), 1/1 DLC UI. It checks keys, markup, placeholders, directives and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy and independent review remain pending.

Next: continue missing base UI in inventory order after `{#month_short}Aug`, including extra display keys, then translate the remaining explicit DLC story in source context without authoring aliases. After all four authored sets are complete, run strict text validation and a full English semantic comparison with durable stable-ID coverage. The coordinator owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 016

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-016/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **140 base UI keys** covering date abbreviations, save slots, confirmation prompts, accessibility settings and developer tools. Original key names and symbols such as `a`, `q`, arrows and checkmarks remain unchanged where they are controls or symbols. Authored from English and immediately edited; full semantic review and rendered RTL/date/layout checks remain pending.

Current authored coverage: **1,785/1,785 base story; 286/394 base UI; 11/238 explicit DLC story; 1/1 DLC UI**. Draft edition validation passed: 1,785 base story, 286 UI and 28/255 DLC delta bindings (11 authored plus 17 aliases), 1/1 DLC UI. It checks keys, markup, placeholders, directives and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy and independent review remain pending.

Next: continue missing base UI in inventory order after `q`, including extra display keys, then translate remaining explicit DLC story in source context without authoring aliases. Once all four authored sets are complete, run strict text validation and the full English semantic comparison with durable stable-ID coverage. The coordinator owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 017

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-017/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **108 base UI keys and 18 explicit DLC story rows**. Base UI is fully authored. The UI batch covers updater, renderer, errors and console help, preserving literal commands, file names and control names. The DLC batch starts at `start_f8b7e1b5` and continues through `start_fe188a59` in source order, skipping existing case lines and aliases. Authored from English and immediately edited in context; full semantic audit and rendered interface checks remain pending.

Current authored coverage: **1,785/1,785 base story; 394/394 base UI; 29/238 explicit DLC story; 1/1 DLC UI**. Draft edition validation passed: 1,785 base story, 394 UI and 46/255 DLC delta bindings (29 authored plus 17 aliases), 1/1 DLC UI. It checks keys, markup, placeholders, directives and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy and independent review remain pending. Rendering remains unverified.

Next: continue missing explicit DLC story after `start_fe188a59` in context, skipping authored case lines and aliases. Once all four sets are complete, run strict text validation and full English semantic comparison with durable stable-ID coverage. The coordinator owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 018

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-018/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added **127 explicit DLC story rows**, from `start_e3a7d7ac_2` through `start_07839bcc`, skipping previously authored special-scene rows and aliases. They were authored from English and immediately edited in context; the full semantic audit remains pending. `start_75bdc594` retains the DLC-only name Katie as קייטי.

Current authored coverage: **1,785/1,785 base story; 394/394 base UI; 156/238 explicit DLC story; 1/1 DLC UI**. Draft edition validation passed after each batch and source-order sorting: 173/255 DLC delta bindings (156 authored plus 17 aliases). It checks keys, markup, placeholders and edition bindings, not semantic correctness or final package protected-value parity. The recorded `start_5c6117e8` source discrepancy and independent review remain pending; rendering is unverified.

Next: continue missing explicit DLC story after `start_07839bcc`, skipping existing case lines and aliases. Once all sets are complete, run strict text validation and the full English semantic comparison with durable stable-ID coverage. The coordinator owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 019

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-019/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Added the final **82 explicit DLC story rows**, `start_66eeffcc` through `start_4cfbe8d2`, skipping already authored case lines and aliases. All four text sets are now authored: **1,785/1,785 base story; 394/394 base UI; 238/238 explicit DLC story; 1/1 DLC UI**. The strict `edition_text(..., draft=False)` text validation passed for 1,785 base story, 394 UI, all 255 DLC delta bindings (238 authored plus 17 aliases), and one DLC UI key. This exercises authored keys, token checks, shared source bindings and aliases; it is not a full build, runtime, final protected-value comparison or editorial acceptance.

The author semantic comparison has begun: the first **25 base story IDs** were read against English and recorded individually in `semantic-coverage.json`; no corrections were made in this initial batch. This is a partial author review, not the full audit or independent review. At the checkpoint the SHA-256 values are: base dialogue `488398ea2fdec7b245fa0856e34cd738c8faacc86fdb66a6984da096dde2be31`, base UI `4d41953cb21941c8d60e75236d5b74c51dfa1cfc4bda372538cd4b8d2325c0a6`, DLC dialogue `7bb4c770e85d8e0facb7685528e439f6db16780cf2adea69c739884c5ce4be3a`, DLC UI `27a576d885b92ae6ab0adfffa61f40a26f6fc005a77c1627475514217c08a76a`, coverage `1b589f4b30d50a49358b3be932525f0e727ec99acab8342dd9bc8825145a3b79`. The coverage is tied to these inputs and pinned inventories/glossary above; later edits require invalidating affected IDs and their semantic dependencies. Preserve the exact `start_5c6117e8` source speaker/self-address discrepancy for adjudication during review. Independent review remains pending, and rendering is unverified.

Next: resume the English-to-Hebrew semantic comparison at the first base story ID after `start_9c30f04d`, update `semantic-coverage.json` only for actual reviewed IDs, cover all UI and explicit DLC IDs, collect and correct findings with dependency closure, then rerun strict text validation. The coordinator owns runtime, visual, font, packaging and Git stages.

## Continuation, turn 020

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-020/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. The author compared **200 additional base story IDs** with English in context, through `start_780db5d2`. `semantic-coverage.json` now records **225/1,785 base story; 0/394 base UI; 0/238 explicit DLC story; 0/1 DLC UI** actually read in this audit. This is an ongoing author comparison, not independent or final editorial acceptance.

Corrected `start_941cb47d` from the feminine role noun to the gender-neutral loanword בייביסיטר for male Damien. Dependency closure searched both source inventories for `babysit`: the same shared ID and `start_966900e9`/`start_c05ca554`; the latter two refer to Juno and already use בייביסיטר. The corrected shared ID is reviewed in this batch and resolves to the same text in both editions. No other affected source occurrence was found by that search; broader semantic audit is still pending. Strict `edition_text(..., draft=False)` validation passed after correction: complete keys, token and edition alias checks. It does not establish runtime or packaged protected-value parity.

Checkpoint SHA-256: base dialogue `4b72803c0311f4d6f9fafba5b83307bbe7a604c88c7be14824852b00ec8cb008`; coverage `bce03858025bbb8ddb46e0733fa572884f492d955a8763fe661acc5cf06463a9`. Base UI and DLC authored files remain unchanged from turn 019. Next: resume base story after `start_780db5d2`, then review all base UI and explicit DLC IDs, collect findings and recheck affected dependency closures. Independent review, rendering and the `start_5c6117e8` source discrepancy remain pending.

## Continuation, turn 021

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-021/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Compared **250 additional base story IDs** against English in context, from `start_541b9195` through `start_5d8d1160`. The durable author audit now records **475/1,785 base story; 0/394 base UI; 0/238 explicit DLC story; 0/1 DLC UI** in `semantic-coverage.json`. No corrections were made in this batch. This is ongoing author review, not independent or final editorial acceptance.

Strict `edition_text(..., draft=False)` validation passed for complete key, token and edition alias checks. Authored file hashes remain unchanged from turn 020; coverage SHA-256 is `6980c2d0346036cb79ffd012c2fe7205391725d70c31e87b025cc01ad6b50583`. An initial hash assertion used a mistyped expected UI digest and stopped before any write; the actual digest matched the prior checkpoint on inspection, and the corrected verification passed. No content was changed by that attempt. Next: resume base story after `start_5d8d1160`, then review all UI and explicit DLC IDs, collect findings and close affected dependencies. Independent review, rendering and the `start_5c6117e8` source discrepancy remain pending.

## Continuation, turn 022

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-022/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Compared **250 additional base story IDs** against English in context, from `start_54eb656a` through `start_a50c17dc`. The durable author audit now records **725/1,785 base story; 0/394 base UI; 0/238 explicit DLC story; 0/1 DLC UI** in `semantic-coverage.json`. No corrections were made in this batch. This remains ongoing author review, not independent or final editorial acceptance.

Strict `edition_text(..., draft=False)` validation passed for complete key, token and edition alias checks. Authored file hashes match turn 020; coverage SHA-256 is `9a4a621e94da7cf66b09c7c815c9e5fd3ab5fc3b41415f9ed368fcfd40dd5614`. Next: resume base story after `start_a50c17dc`, then review all UI and explicit DLC IDs, collect findings and close affected dependencies. Independent review, rendering and the `start_5c6117e8` source discrepancy remain pending.

## Continuation, turn 023

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-023/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Compared **200 additional base story IDs** against English in context, from `start_659f8df2` through `start_5a5ed74d`. The durable author audit now records **925/1,785 base story; 0/394 base UI; 0/238 explicit DLC story; 0/1 DLC UI** in `semantic-coverage.json`. No corrections were made in this batch. This is ongoing author review, not independent or final editorial acceptance.

Strict `edition_text(..., draft=False)` validation passed for complete key, token and edition alias checks. Authored file hashes match turn 020; coverage SHA-256 is `68aead1590dcfa4d1e257f0c2d562c50848cf0676a420774dfb1864b4c207a00`. Next: resume base story after `start_5a5ed74d`, then review all UI and explicit DLC IDs, collect findings and close affected dependencies. Independent review, rendering and the `start_5c6117e8` source discrepancy remain pending.

## Continuation, turn 024

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-024/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Compared **200 additional base story IDs** against English in context, from `start_71e15efb` through `start_c4e3de73`. The durable author audit now records **1,125/1,785 base story; 0/394 base UI; 0/238 explicit DLC story; 0/1 DLC UI** in `semantic-coverage.json`. No corrections were made in this batch. This is ongoing author review, not independent or final editorial acceptance.

Strict `edition_text(..., draft=False)` validation passed for complete key, token and edition alias checks. Authored file hashes match turn 020; coverage SHA-256 is `400ca559f5468ce75806f1e851af88305d7e5177a851013f891e53f95bb2a346`. Next: resume base story after `start_c4e3de73`, then review all UI and explicit DLC IDs, collect findings and close affected dependencies. Independent review, rendering and the `start_5c6117e8` source discrepancy remain pending.

## Continuation, turn 025

Turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-025/model-verified.json` matches the thread and records `gpt-6.1-terra` / high. Compared **200 additional base story IDs** against English in context, from `start_63fd69d1` through `start_fba90d35`. The durable author audit now records **1,325/1,785 base story; 0/394 base UI; 0/238 explicit DLC story; 0/1 DLC UI** in `semantic-coverage.json`. No corrections were made in this batch. This is ongoing author review, not independent or final editorial acceptance.

During this turn a coverage update initially advanced 200 IDs after only 50 new IDs had been read; the remaining three batches accidentally repeated earlier ranges. That overstatement was detected immediately and rolled back to 1,175 before continuing. The next 150 IDs were then actually compared against English, making the final 1,325-ID checkpoint accurate. Strict `edition_text(..., draft=False)` validation passed for complete key, token and edition alias checks. Authored file hashes match turn 020; coverage SHA-256 is `ad990e6a687f8533e0fd326e539ba6ce450c0ded3a48b8ce566ab9554d755dac`. Next: resume base story after `start_fba90d35`, then review all UI and explicit DLC IDs, collect findings and close affected dependencies. Independent review, rendering and the `start_5c6117e8` source discrepancy remain pending.

## Continuation, turn 026

The turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-026/model-verified.json` matches this thread and records `gpt-6.1-terra` / high. Compared 200 additional base story IDs against English in context, from `start_51bbf806` through `start_cb9b40c8`. Author semantic coverage is now 1,525/1,785 base story, 0/394 base UI, 0/238 explicitly authored DLC story and 0/1 DLC UI. Corrected `start_1ec245b3` from plural to singular in the question about the preceding singular “something real.” This is ongoing author review, not independent editorial acceptance.

Strict `edition_text(..., draft=False)` passed: 1,785/1,785 base story, 394/394 base UI, 255/255 DLC delta story including 17 aliases, and 1/1 DLC UI. Reproducible text dependencies remain the pinned base `text-assets/inventory.json` and `text-assets/renpy-dialogue.tab`, DLC `text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json`, tracked alias/binding data and `tools/build_localization.py`, plus the four canonical Hebrew authored inputs. Dialogue SHA-256 is `1c03af475a8c76d36935ba6ea03d712f0a53baa04b435fa0b2213e9683df851a`; semantic coverage SHA-256 is `45d9333d566131b71fb49d3c2fac8213c4849b9bd60890e513f7262b876be254`. An initial pre-write hash assertion mistakenly copied the coverage digest and stopped without changes; the actual saved prefix was checked against source before the successful update. Next: compare base story after `start_cb9b40c8`, then all UI and explicit DLC IDs. Independent review and rendering remain pending and unverified; the source speaker discrepancy `start_5c6117e8` remains unresolved.

## Continuation, turn 027

The turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-027/model-verified.json` matches this thread and records `gpt-6.1-terra` / high. Compared the final 260 base story IDs, `start_20a0ff3c` through `start_af456bab`, and the first 200 base UI keys, `My name is...` through the Ren'Py license paragraph, with English. Author semantic coverage is now 1,785/1,785 base story, 200/394 base UI, 0/238 explicitly authored DLC story and 0/1 DLC UI. This is author review, not independent editorial acceptance.

Corrected `start_cf580d17` (missing verb), `start_39f2ee38` (natural address to a son), `start_e7b5eac4` (idiomatic sense of rushing in recklessly), and `start_06176eb1` (natural breathing expression). Strict `edition_text(..., draft=False)` passed after the edits: 1,785/1,785 base story, 394/394 base UI, 255/255 DLC delta story including 17 aliases and 1/1 DLC UI. Canonical dialogue SHA-256 is `ff402fece67d00e85fae3d044bc86149c4d3d16f7a0f2886ba34fdc80516d8fb`; semantic coverage SHA-256 is `4543fd790f44f76bf1b60d1dc3e32074fc2f06b9f277fe7d01be7789a4f89026`. The dependency closure is as recorded in turn 026; semantic review of all remaining inputs and independent review are pending. Next: base UI key after the Ren'Py license paragraph, followed by explicit DLC IDs and DLC UI. Runtime rendering remains unverified and the `start_5c6117e8` source speaker discrepancy remains unresolved.

## Continuation, turn 028 — author comparison complete

The turn receipt `text-assets/cli-localization-wave-05-he-text/he/turn-028/model-verified.json` matches this thread and records `gpt-6.1-terra` / high. Compared the remaining 194 base UI keys, all 238 explicitly authored DLC story IDs in source order and the DLC `Gallery` key with English. Durable exact-ID author coverage is now **1,785/1,785 base story, 394/394 base UI, 238/238 explicit DLC story, 1/1 DLC UI** in `semantic-coverage.json`. The 17 DLC aliases are resolved by the shared alias mechanism and are not authored twice. Corrected `start_6f4ee077` and `start_0e3c55b5` to refer to the shaft rather than the whole body, and improved `start_973d7ac2` and `start_0af64753` to avoid misleading literal phrasing.

Strict validation after these changes passed: base 1,785/1,785 story and 394/394 strings; DLC 255/255 story bindings including 17 aliases and 1/1 UI. Reproduce from the project root with `python3 -B -c "import json,sys; from pathlib import Path; sys.path.insert(0,'tools'); import build_localization as b; b.edition_text(json.load(open('text-assets/inventory.json')),json.load(open('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json')),Path('localization/he'),False)"`. This exercises text keys, placeholders, tags and edition binding, not a packaged build or rendering.

The reproducible closure for this author pass (SHA-256) is:

- Base `text-assets/inventory.json` `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`, `text-assets/renpy-dialogue.tab` `4ba57708ea623be3177c60680b318461469741b1109e7874d8e4c3131e007ad5`, and manifest / tracked receipt `1ad9c080caed30f47584a2a4062a1ab9ab665eba5bf7e8c35736c5ccfc05c0a8`.
- DLC `text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json` `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea`, its `renpy-dialogue.tab` `74ff2174cd5eb7515bbb5bc2ae8ce82dc672f80bf16909f57af23432fe29ab93`, and manifest / tracked receipt `da9a7f72df14f7b725d7566ae0f1cac40f7390042d74b410c9aaf05a48063b6f`. `localization/nsfw-story-aliases.json` is `6b020423fc1c45e678c6c8ef6914161ed2978864f91c805d3c0d286c084b8f7c`.
- `tools/build_localization.py` `18937f78194ea7503bf14c316b7db3789013ea9accd6e455eadfe2fd3f909d5d`, `tools/extract_text.py` `db7ae33202a62d85f882e142e11bc60de8332c896e8b1077a1781ab43c5ce691`, and `tools/install_language_picker.py` `c567eec2abd882dad7e72193cb4619444096469f25a741409873c24846d16428`. Approved glossary verification is bound to `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json` `5935841fb335bb53db74afe2134e70c45068ee8dbea7cf6a87f287aef794cddd`; prior checkpoint records the verified glossary and reviews.
- Authored `dialogue.tsv` `ff402fece67d00e85fae3d044bc86149c4d3d16f7a0f2886ba34fdc80516d8fb`, `strings.json` `4d41953cb21941c8d60e75236d5b74c51dfa1cfc4bda372538cd4b8d2325c0a6`, `nsfw/dialogue.tsv` `29db8be45b893ae4e7a6a7bece1d769fa66dac64d5bc998485c65bed251d7b7e`, `nsfw/strings.json` `27a576d885b92ae6ab0adfffa61f40a26f6fc005a77c1627475514217c08a76a`, `special-scenes.md` `294965a52cbfa58b0de0eff28cca7cb3ea2129c37dd06dcc8af89b46f9618f60`, and `semantic-coverage.json` `f3b7f63c6323067ce0630f84d9e40f8834eb8c843575aed82d43edbbfa4233df`.

The DLC `start_5c6117e8` discrepancy was revisited in scene context: the source assigns the player as speaker while the line addresses `[pname]` and the surrounding action suggests Juno; the original binding remains intact and a source/editorial decision is still needed. Full author comparison and mechanical validation do not establish independent editorial acceptance. Independent review is pending; Hebrew rendering, marks, mixed direction, input, font behavior, packaging and runtime verification remain unverified and belong to the coordinator's later joint pass. Next: independent review and disposition of the source discrepancy; rerun affected checks if inputs or text change.
