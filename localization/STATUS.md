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
| screenshot-upload | Not run. Local delivery scope. |
| screenshot-review | Native visual checks are part of the probe and runtime evidence. Post-upload review is not applicable to this local delivery. |
| delivery | Commit only verified local deliverables on `main`. |

## Locale queue and feasibility matrix

Polish is at `editorial` with **1,785/1,785 story entries** and **394/394 string
keys** in the authored draft. The other 28 locales are at `probe` with zero
authored entries. The exact 77-ID glossary layers and their two coverage receipts
verified for all 29 locales. The Polish semantic pass is complete and its corrected export build is reproducible.
Independent review, final resources, strict installed validation, runtime, visual and release acceptance remain pending.
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
