# Russian localization checkpoint

Steam app 2009010, base Windows build 11915262, Ren’Py 8.0.3.22090809.
Site locale `ru`, Ren’Py locale `russian`. Standard localization.
Canonical checkout `/Users/antonkrutov/Desktop/Protogen`, branch `main`.

## Pinned inputs

- Shared source inventory SHA-256 `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`.
- Special-scene registry SHA-256 `5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923`.
- VN Revival canonical English glossary fingerprint `83ba6cab8eb3455c48e9e296a489ea2c9d05e8aa6d60dbeab36bdfb00e31c2b7`. Approved Russian layer SHA-256 `68bdb76fb89e37337c5130a1a28ba1474281347ef944eadcec183738f5feafa5` using compact UTF-8 JSON. Both review layers cover all 77 IDs.
- Universal process references are the installed `game-localization-prompt.md`
  (`68acfd48b4408a53af62bc0b021f355f25d089d784d417fe24f30fba3be935dd`)
  and `game-localization-audit-workflow.md`
  (`37ff4269163b17cab4030c2d1c78651f7a79b9c8be3d569a2b9ea7f17748a5dc`),
  and the `vn-game-localize` references `ROUTING.md`
  (`75fac761503c8cfdeee6281629fa158ce6661f8acaf02e225cee4a66861aa093`)
  and `CHECKPOINT.md`
  (`de6fcd0119aceda9edeed0850eaa659b10aaf8e7cfc7e7c22ce7c627c9849b25`).
- Author model verified from current turn context as `gpt-6.1-sol` at medium reasoning.

## Stages and commands

| Stage | State and evidence |
| --- | --- |
| scope | Base Steam depot, one target locale, local installation and CrossOver QA. |
| probe | Existing language picker, Russian menu and opening narration verified under the Windows executable. New probe passed blank name, Russian fallback, input prompt mapping and nameplate binding in an isolated save directory. Evidence `text-assets/ru-preflight/adapter-runtime.txt`, SHA-256 `22fc3efcf5dcde56caaea36acff402726b9afbe00f3468e517e0801edfcbc565`. |
| source | `python3 -B tools/extract_text.py verify "$protogen_game" text-assets` verifies 1,785 story IDs, 747 protected literal occurrences and all source hashes. Both WebM assets are clock animations with no captions in the inspected frames. Main-menu logo remains original title art. |
| glossary | Verified 77 IDs against both canonical layers and the Russian review receipt. |
| translate-edit | 1,785/1,785 story entries and 394/394 string keys authored. The strict validator checks every ID and protected marker. Editable sources are `dialogue.tsv` and `strings.json`. |
| editorial | Targeted review covered player-name insertion, timing, glossary naming and related references. Complete separate semantic audit and independent diff audit pending. |
| resources | Shipped Nunito SemiBold and Bold cover Russian letters, including Ё/ё, plus Russian punctuation. The final desktop text fits an estimated maximum of four wrapped lines at the original dialogue width. |
| package | Strict build passed and two independent build directories were byte-identical. Rebuild with `python3 -B tools/build_localization.py "$protogen_game" ru --output <fresh-directory>`. |
| runtime | Windows executable in the CrossOver Steam bottle verified all 1,785 story rows and 394 string keys from the installed scripts. The walkthrough reached the credits and returned to the main menu after 20 movie entries. The language buttons switched English → Russian → English → Russian. Ordinary, automatic and quick load pages responded, and the Russian player name survived dialogue interpolation. |
| screenshot-upload | Outside requested scope. |
| screenshot-review | Native visual review passed for the title menu, settings, load page, Juno nameplate and closing line. Gallery upload review is outside scope. |
| delivery | Russian text installed locally in the verified Steam build. Complete independent editorial acceptance remains pending. |

The player name keeps the original 12-character limit, trimming, storage and
`[pname]` interpolation. Only the literal fallback branch uses «Ты» under
Russian. `NV-0903` remains unchanged, the Juno nameplate displays «Джуно»,
and both the shuttle and the AI use «Пикси» with distinct agreement.
The source’s `{w}` and scoped `{cps=5}` controls are present in their
translated groups. «Белая ворона» is consistent through the phrase, its
explanation and the narrator’s callback. «Генная инженерия» retains the
narrator’s interrupted repetition. The save format retains the weekday,
day, month, year, hour and minute directives.

## CrossOver evidence

The final localization script SHA-256 is
`bb47bf0bc0c45fe71e048182f599cb23070f0eb7d0cc338b04bd6bc3f87a3f23`.
The exact output, traversal log, five original frames and checksums are indexed
by `text-assets/ru-crossover-final.Zq92Jf/acceptance.json`. The full-run log
SHA-256 is `9f752251cd3c3d2d0390ee67d48fe3362f08ecca6a1ade1f6b47b989fe4d54f5`.

Ren’Py mirrored test data to `game/saves` during the initial verification,
despite the scratch `--savedir`. Restored five original autosave slots and
the prior persistent file using verified byte matches and slot rotation.
The primary AppData saves and persistent file matched their original records.
The recovery manifest is `text-assets/ru-crossover-final.Zq92Jf/save-restore.json`.
The reusable QA helper redirects the game-local mirror before the engine
scans either test save location. A fresh CrossOver launch submitted the blank
name, rendered the first Russian line, and wrote an autosave and persistent
data in both scratch locations. The player save locations matched the recovery
manifest byte-for-byte afterward. All temporary QA scripts were removed.

Measured task-level model usage and its cutoff are in
`text-assets/ru-crossover-final.Zq92Jf/usage.json`.
