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
| package | `tools/build_localization.py` is the strict build baseline. It currently supports `ru`; add and validate explicit mappings before packaging additional locales. |
| runtime | Test each final build's in-game picker, real renderer and progression in CrossOver. Use `tools/qa_isolate_saves.rpy` for both save locations, and launch with `RENPY_DISABLE_SOUND=1`. |
| screenshot-upload | Not run. Local delivery scope. |
| screenshot-review | Native visual checks are part of the probe and runtime evidence. Post-upload review is not applicable to this local delivery. |
| delivery | Commit only verified local deliverables on `main`. |

## Locale queue and feasibility matrix

All listed locales are at `probe` with **0/1,785 story entries** and **0/394 string keys**
in the authored corpus. The exact 77-ID glossary layers and their two coverage
receipts verified for all 29 locales. Editorial, final resources, build, runtime,
visual and release acceptance are pending for every locale. The probe identifiers
`vnprobe_pl` and `vnprobe_ar` are disposable. Production runtime IDs for these
29 languages have yet to be bound.

| Locales | Rendering requirements and evidence | Status and next action |
| --- | --- | --- |
| `pl` | Shipped Nunito passed representative accents in the dialogue and nameplate. In-game preferences opened, player name interpolated, wait advanced to the next ID. | Partial. Check localized preferences and input rendering, plus multiline layout. |
| `cs`, `de`, `es`, `es-419`, `fil`, `fr`, `hu`, `id`, `it`, `nl`, `pt-BR`, `ro`, `sw`, `tr`, `vi` | Shipped Nunito covers the synthetic characters in both faces. Vietnamese exercises stacked diacritics. | Unverified in the game. Exercise accents and marks across actual text roles and line breaks. |
| `bg`, `sr`, `uk` | Shipped Nunito covers the synthetic Cyrillic characters, including Љ, ђ, Ґ and ї. | Unverified in the game. Probe Cyrillic and dynamic mixed-script values. |
| `el` | Shipped Nunito lacks Greek. Engine-shipped DejaVu Sans covers the synthetic Greek sample in both faces. | Baseline blocked. Test locale styles with DejaVu Sans in the game. |
| `ar` | Nunito rendered missing-glyph boxes. A muted rerun with the engine's DejaVu Sans loaded the intended style fonts and advanced to the fourth story ID. | Baseline blocked; repair visual review pending. Inspect joining, marks, mixed direction, line wrap and settings. |
| `fa`, `he` | Nunito lacks the target characters. DejaVu Sans covers the samples in both faces. | Baseline blocked. Test Persian joining and zero-width non-joiner, Hebrew marks and mixed direction separately. |
| `hi`, `th` | Both tested font families lack the required samples. | Baseline blocked. Verify suitable fonts, conjuncts and mark positioning in the game. |
| `ja`, `ko`, `zh`, `zh-TW` | Both tested font families lack the required samples. | Baseline blocked. Verify regional glyph forms and the applicable Ren’Py line-breaking options. |

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
  Contains the muted DejaVu Sans probe and two prepared previews for pending
  visual review. The audio backend reported PCM disabled before the opening.
  The temporary add-ons were removed and both player save stores matched after
  each run.
