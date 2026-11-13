# Multilingual localization checkpoint

Steam app 2009010, Windows build 11915262, Ren’Py 8.0.3.22090809, CrossOver
`Steam` bottle. Standard localization. English is the sole official language.
The 29 remaining locale rows below share the same English inventory. The
[Russian revision](ru/STATUS.md) is the existing local delivery baseline.

## Process binding

Use the shared stage IDs in the installed `ROUTING.md`, `CHECKPOINT.md`
and `EARLY-PROBE.md`, and the universal localization prompt and editorial
workflow under `~/.codex/instructions/`. Their exact SHA-256 values are in
the feasibility baseline receipt.

| Stage | Project binding and acceptance |
| --- | --- |
| scope | Canonical `main`, build 11915262, local installation and CrossOver QA. The website card is a draft. |
| probe | Synthetic samples in the original opening, preferences and input paths. Record native progress and visual results separately. Preserve the installed base and both player save stores. |
| source | `tools/extract_text.py verify` verifies the original files, inventory, 747 protected occurrences and the special-scene registry. |
| glossary | Reuse the approved 77-ID target layer and both complete review receipts when their exact hashes match. |
| translate-edit | Settle special-scene wording and bindings, then edit the locale's 1,785 story entries and 394 string keys directly from English. |
| editorial | Apply the full semantic audit and independent dependency-aware review under the shared workflow. |
| resources | Verify full font coverage, shaping, wrapping and game text assets. Current logo is original title art and the two reviewed watch videos contain no captions. |
| package | `tools/build_localization.py` is the strict build baseline. It builds complete `ru` and `pl` corpora. Add and validate explicit mappings before packaging further locales. |
| runtime | Test each final build's in-game picker, real renderer and progression in CrossOver. Use `tools/qa_isolate_saves.rpy` for both save locations, and launch with `RENPY_DISABLE_SOUND=1`. |
| screenshot-upload | VN Revival production draft, 180 stored frames across 30 locale galleries. |
| screenshot-review | Native capture and stored draft WebP have separate visual checks. See the six-scene collection checkpoint below. |
| delivery | Commit only verified local deliverables on `main`. |

## Translation queue and deferred CrossOver checks

Owner decision, 2026-11-13. Start or resume Protogen text work while in-game
rendering checks are deferred to one joint CrossOver pass. Reuse the shared
English inventory and approved locale glossary. Mark untested rendering as
unverified, prepare any missing synthetic cases, and continue through special-scene
decisions, ordinary translation and text validation without waiting for the joint
pass. An evidenced renderer failure remains a blocker for the affected mechanism.
New locale workers apply this decision directly and keep CrossOver, installation
and visual checks pending until the owner calls for the joint pass.

Resume completed CLI turns with
`python3 -B tools/continue_locale_text.py <run-dir> <prior-run-dir>` from the
project root. Use a fresh run directory under `text-assets/`. The prior run must
contain the launch manifest and per-locale completed turn receipts. The supervisor
resumes the same verified Terra high sessions from their locale checkpoints and
continues through full text coverage and the author semantic review. Git integration,
independent review and the joint CrossOver pass are separate steps.

## Locale queue and feasibility matrix

The first six CLI locales (`cs`, `de`, `es`, `fr`, `it`, `pt-BR`) completed
text validation and the author semantic pass for both editions. The next six
(`es-419`, `hu`, `id`, `nl`, `ro`, `tr`) completed static preparation and
advance to text under the owner decision above. Consult the per-locale
checkpoints for current coverage. Independent review and final technical
acceptance for these CLI locales are pending.
The production Polish runtime ID is
`polish`. Identifiers prefixed with `vnprobe_` are disposable.

The original Steam depot and the official 18+ DLC are both in scope. Use the
base inventory for the 1,785 SFW statements and the DLC inventory for its
2,007 statements. Reuse the 1,752 shared IDs, then author and review the DLC
delta against its English script. The [edition receipt](edition-qa.json)
records edition tests. Russian and Polish now cover the complete DLC inventory.
Strict builds passed for both languages and editions. Four muted CrossOver
playthroughs reached the credits and returned to the main menu.

| Locales | Rendering requirements and evidence | Status and next action |
| --- | --- | --- |
| `pl` | Shipped Nunito passed representative accents in dialogue, nameplate, settings and input. A long sample wrapped to three lines. `Łucja` survived input and interpolation, and the wait advanced to the next story ID. | Probe passed. The [Polish review closure](pl/STATUS.md) is ready for an independent reviewer. The official DLC has its own pinned English export. |
| `cs`, `de`, `es`, `es-419`, `fil`, `fr`, `hu`, `id`, `it`, `nl`, `pt-BR`, `ro`, `sw`, `tr`, `vi` | Shipped Nunito covers the synthetic characters in both faces. Vietnamese exercises stacked diacritics. | Unverified in the game. Exercise accents and marks across actual text roles and line breaks. |
| `bg`, `sr`, `uk` | Shipped Nunito covers the synthetic Cyrillic characters, including Љ, ђ, Ґ and ї. | Unverified in the game. Probe Cyrillic and dynamic mixed-script values. |
| `el` | Shipped Nunito lacks Greek. Engine-shipped DejaVu Sans covers the synthetic Greek sample in both faces. | Baseline blocked. Test locale styles with DejaVu Sans in the game. |
| `ar` | Nunito rendered missing-glyph boxes. The first DejaVu Sans style overrides rendered the heading and dialogue, but the navigation button still had missing glyphs. A second muted run applied a locale-scoped font replacement map and verified that switching to Polish restored the prior fonts and bidi flag. | Baseline blocked; visual review of the second repair is pending. Inspect settings, name input, and the Arabic-first mixed multiline sample. |
| `fa`, `he` | Nunito lacks the target characters. DejaVu Sans covers the samples in both faces. | Baseline blocked. Test Persian joining and zero-width non-joiner, Hebrew marks and mixed direction separately. |
| `hi` | Noto Sans Devanagari 2.007 covers the sample. A muted run loaded it, accepted a Devanagari player name and advanced through the inline wait. | Blocked on the shipped renderer. The dialogue and input show a visible virama in `क्ष` and incorrect vowel placement in `क्षितिज`. The font also lacks the Latin letters in `NV-0903`. A Latin fallback addresses those letters. The shaping path needs an owner decision and runtime proof. Settings-frame review remains pending. |
| `th` | Noto Sans Thai 2.002 covers the sample. | Static coverage only. Verify marks, word breaks and multiline behavior in-game. |
| `ja`, `ko`, `zh`, `zh-TW` | The four regional Noto Sans CJK 2.004 faces cover their respective samples. | Static coverage only. Verify regional glyph forms, wrapping and punctuation with the applicable Ren’Py line-breaking options. |

## Remaining complex-script checks

On 2026-11-13 the preserved Arabic replacement-map settings frame showed visible
glyphs on the navigation button that displayed missing-glyph boxes with the
earlier style override. The original frame has SHA-256
`7595fa82e711c33ab4acd755f5484576532b07c9067776dd1fd9cef262347798`.
The reviewed 1280 × 719 WebP has SHA-256
`432e5ff1dc351b79bcce624d3c48472d9664594fc9caeca3515359395c3604c3`.
The font-map observation supports resuming Persian text. Persian joining,
bidirectional layout and editable input still need an in-game check. Hebrew
continues through its special-scene decisions and text validation.

HarfBuzz 14.5.1 with the pinned fonts produced contextual glyphs for
`مَرْحَبًا` in DejaVu Sans and Bold. It produced different glyph runs for
Persian `می‌روم` and `میروم`, exercising the zero-width non-joiner. Noto
Sans Devanagari formed the `क्ष` conjunct with a pre-base vowel in
`क्षितिज`. DejaVu rendered both Latin letters in `NV-0903`, which the
sampled Devanagari face lacks. Reproduce with `hb-shape --output-format=json
<font> <sample>` using the faces pinned below. Glyph runs and font hashes
are recorded in `text-assets/renderer-followup/harfbuzz-static.json`.

An isolated native macOS base-game run on Ren’Py 8.2.3 showed a viable path
for Arabic and Hindi. The old game compatibility settings selected FreeType
until the test locale explicitly set `shaper "harfbuzz"`. Arabic dialogue
showed contextual forms, marks, Arabic-Indic digits and the intact Latin
identifier `NV-0903`. Hindi dialogue showed the conjunct and pre-base vowel
in `क्षितिज`. A DejaVu font run rendered the Latin identifier. Both runs
submitted a test name through the input widget, verified the stored value and
its interpolation, and advanced through an inline wait. The result and image
hashes are in `text-assets/harfbuzz-isolated/result.json`
(SHA-256 `cd8e950a0a22bb24e88a3d0e7259543bbff7f5f8a9d8919dc04af6e1045acc1e`).

Arabic and Hindi text work can proceed against this demonstrated rendering path.
The joint pass still needs the final packages for both editions, editable input
and caret checks, layout and save/load regressions, language switching, and
Windows through CrossOver. The production engine remains the shipped version.

## Evidence

- `text-assets/multilingual-probe.L4KEcD/feasibility-baseline.json`
  (`07e6d9bb909f984e86825a7d67e81132f909fa5f67b0d55928e18f2ddf76db4c`).
  Includes pinned fonts and process inputs, the 29 synthetic samples, cmap results
  and runtime evidence. Two original story mappings were tested with a generated
  Ren’Py no-op round trip preserving the statement and runtime attributes.
- `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`
  (`5935841fb335bb53db74afe2134e70c45068ee8dbea7cf6a87f287aef794cddd`).
- `text-assets/multilingual-font-probe.FSkUIw/runtime-evidence.json`
  (`03a71260cd521a171fa1d6a72ef832b586754a83d7cda602ff2df0f09026afa5`).
  Contains the first muted DejaVu Sans probe. Its
  `visual-review.json` records the navigation button failure. The audio backend reported PCM disabled before the opening.
  The temporary add-ons were removed and both player save stores matched after
  each run.

- `text-assets/multilingual-map-probe.HopRBo/runtime-evidence.json`
  (`a61d0b25753c62034712cd795e64921d599d042f8f93c1bc7ea7fb3014838c52`).
  Locale-scoped font replacement probe and its untouched Arabic and Polish
  captures of settings, name input and opening dialogue. Both used isolated saves.
- `text-assets/font-candidates.vUrRKa/provenance.json`
  (`c89a1ffd96b67fd91314d85072ec1b4d4ec178454f69cc3831418d7597b72db4`).
  Versioned upstream font sources, OFL license hashes and cmap sample coverage.
- `text-assets/multilingual-devanagari-probe.Z7siFr/runtime-evidence.json`
  (`0e14903aa5c7d36401c78f9a589b666176b8f8addbf92db830a57980cf06d830`).
  Muted Hindi runtime probe, exact font file and prepared previews. Both player
  save stores matched and the temporary scripts and font were removed.

- `text-assets/multilingual-devanagari-probe.Z7siFr/visual-review-01.json`
  (`266a987a6534e64fc7f472f89a0991ba5ba5a578e1f2111cc7a0eb31e9c24ae4`).
  The dialogue and input fail Devanagari shaping. The cmap check separately
  identifies the two missing Latin characters. Upstream added complex shaping
  through HarfBuzz in [Ren’Py 8.2](https://www.renpy.org/doc/html/changelog.html#harfbuzz-integration).

## Editorial queue closed by owner

The owner closed this editorial task on 2026-11-13 and asked to keep the current
translations. Strict authored-text validation passed for all 30 locales against
the pinned base and DLC inventories. The independent reviews for Russian,
Polish, Arabic and Bulgarian returned proposed corrections. Six reviews were
stopped in progress, and 20 had not started. The existing reports and
checkpoints are indexed in the local
`text-assets/cli-editorial-review-20261113/closure.json`.
Proposed corrections remain in the reports. Final editorial acceptance is
incomplete. CrossOver remains deferred to a joint pass.

## CrossOver font and text rendering

The build 11915262 smoke tests exercised 30 languages in both editions using
CrossOver 26.3 in the BLOODMONEY bottle. The original 300 frames, the per-frame
visual review ledgers and the runtime receipts are under
`text-assets/crossover-all-locales-20261113/`. Review is tracked independently
of launch success.

The font adapter supplies DejaVu for Arabic, Persian, Hebrew and Greek, regional
Noto for Japanese, Korean and both Chinese variants, and Noto with DejaVu
fallback for Hindi and Thai. The builder preserves Japanese U+3000 during
Ren’Py script parsing. All 60 packages built successfully. Repeat opening
tests for the ten affected locales passed in both editions. Arabic, Persian,
Hindi and Thai used the isolated Windows Ren’Py 8.2.3 SDK with HarfBuzz.
The other six used the original 8.0.3 runtime. See
`font-regression-summary.json` in the QA directory for package and frame hashes.

All 300 original frames and 122 repair or regression frames were inspected.
The original set showed missing glyphs for all ten affected locales in both
editions and low-contrast load-slot captions in several base-game locales.
The shared caption style was enlarged and brightened. The six replacement
dialogue frames passed the RTL ordering check after the shared sentence-wait
repair. Some frame-level checks remain open for small marks, source context
and mixed-direction scenarios. The complete per-frame status and review
usage are indexed in `final-visual-accounting.json` in the QA directory.

## Preferences picker follow-up

The generated Preferences screen uses the builder’s locale catalog and shows
English plus every installed localization by its native name. Each button
uses its script’s font independently of the active locale. The installer
upgrades the three recognized earlier picker scripts and retires matching
bytecode. It rejects edited scripts and mismatched bytecode.

CrossOver selected all 30 localizations and English in both editions across
the stock and isolated HarfBuzz runs. The test also confirmed that the selected
language survived a restart in both editions. The full picker in the base
game was visually inspected on both runtimes. The opening scene in Arabic,
Persian and Hebrew verified the mixed-script player name, the localized Dad
speaker label, and progression after the dialogue wait in both editions.
The original mixed-script dialogue frames matched across editions pixel
for pixel. Both real save stores matched before and after the tests.

Runtime receipts, frame hashes and the two reviewed previews are indexed in
`text-assets/crossover-picker-fix/verification.json`.

## RTL dialogue alignment follow-up

Short Arabic, Persian and Hebrew dialogue previously started near the
left edge of the field because Ren’Py aligned against the natural width
of the text. The locale font adapter now gives RTL say text the full
dialogue field width before alignment. It retains the existing wrapping
limit and the separate speaker nameplate position. The installer upgrades
the previous verified font adapter and retires its matching bytecode.

In both editions, the mixed-script greeting and the birthday dialogue
after its wait reached the next authored statement. All twelve new
CrossOver frames passed visual review. The Persian greeting’s two
commas were confirmed using source-pixel WebP crops. The regression
compares the right edge of the short greeting and every visible line
after the wait against the dialogue field’s right edge. Both player
save stores matched the original baseline.

The ledgers, runtime provenance and usage receipts are indexed in
`text-assets/crossover-picker-fix/rtl-alignment-verification.json`
(SHA-256 `5c74eb930fa18c280d8ba96833be6dbbd4319fff172b45f423243d4c3db99aa7`).

## Six-scene screenshot collection

The base-game CrossOver collection contains six distinct scenes for each
of the 30 localizations. All 180 frames received individual full-frame
WebP80 visual reviews. The final check passed 180 frames with no open
findings. For 30 frames flagged solely for uncertain backdrop identity,
pixel comparison against the pinned game assets confirmed the intended
shipped backdrop and its original blur. The review required zero
replacement frames.

The per-frame results and original screenshot bindings are indexed in
`text-assets/all-languages-background-selection/visual-review/review-summary-20261113T193815Z.json`
(SHA-256 `e606d5167ef043f89a4b6b8f114f570cb93abda4a37673dd23e37c7e9b6d991b`).

The VN Revival CLI added all 180 verified frames to the existing
`my-furry-protogen` production draft. The upload used two batches because
three pairs of European and Latin American Spanish PNGs share identical
bytes. Authenticated read-back confirmed six stored WebP originals for
every translated locale, with the source hash and delivery hash matched
for every slot. Repeated dry-runs reported 180 skips. The card remains a
private draft.

The slot and Media bindings are in
`text-assets/all-languages-background-selection/vnrevival-upload/verified-upload.json`
(SHA-256 `a0b22229370385e46171c31f5ffe92fc8c4d59ac4ccaf3dff865b09c48350470`).

All 180 stored draft WebP originals received individual post-upload visual
reviews. Every frame passed, including the 18 Arabic, Persian and Hebrew
frames. The report links the authenticated export, exact Media hashes and
per-image observations in
`text-assets/all-languages-background-selection/vnrevival-upload/hosted-review-result.json`
(SHA-256 `9a8deec6d5f82e46d5bfc5f63e7754116614bd94bb01a20e3b1dbe016002c12f`).

## Windows installer

The local Windows x64 installer is built from the Sonic installer and uses the
Protogen Preferences language picker. It installs one of two package layouts
based on the exact Steam script hashes. Both layouts include 30 translations.
The separate Windows Ren’Py 8.2.3 runtime is used by the installer's launch
action. See [the installer guide](../installer/README.md) for build inputs.

Local ZIP SHA-256: `ff8afdab0f1f775fec8dbea4227e8f22ddc251f56c34d6e0565bde814fdacb47`.
All 1,447 runtime files and 104 edition payload files matched their packaged
hashes. The installer window was inspected in Windows 11. The installation
transaction passed both edition fixtures, repeat and interrupted installs,
foreign-file refusal and payload corruption. An isolated test of the patched
Ren’Py 8.2.3 engine on macOS registered all 30 languages in both editions,
selected Arabic, Persian, Hindi and Thai with HarfBuzz active, and preserved
the original scripts and bytecode. Windows launch and CrossOver runtime
checks are tracked separately from these results.
