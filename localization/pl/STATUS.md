# Polish localization checkpoint

Steam build 11915262, source `en`, site locale `pl`, Ren’Py locale `polish`.
Standard localization. The approved target glossary digest is
`9c711f181bed107fa66075abcd522cf11903844b69f89a62d8496ecdae5549ad`.
The shared [process and source binding](../STATUS.md) applies.

## Probe and special scenes

The muted CrossOver probe reached the fourth original story ID with the submitted
name `Łucja`. The opening sample occupied three wrapped lines and 94 of the
210 virtual pixels available under the dialogue baseline. The settings heading,
navigation button and input prompt showed the Polish accents without clipping.
Both player save stores matched before and after. See
`text-assets/polish-wrap-retry.G6Y0wS/acceptance.json`
(`9a6e8a67b701d01eb0913bd506aad42f7f4a96db2d0e70f28555bef27215d76d`).

The special-scene wording is pinned to registry SHA-256
`5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923`
and English inventory SHA-256
`8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`.
The 123 story IDs in the registry were authored first. Their decision snapshot
has dialogue SHA-256
`211547d2eccefcb11e8a48107ffb20f991aeb6c41faca661fc558fb304ce3ac4`
and string SHA-256
`145cf51ae8c3f67378cd4a0741f61037748a42c87d7a936991f357a595d2ab6f`.
The stable IDs remain in [dialogue.tsv](dialogue.tsv) and exact UI keys in
[strings.json](strings.json).

| Case | Wording and preserved behavior | Final runtime check |
| --- | --- | --- |
| player-name | `Nazywam się…`, fallback `Ty`. Keep the original 12-character limit, trim, and comparison to the source empty value. Use the exact entered name in the nameplate and keep `[pname]` uninflected. Where an object case is required, use a pronoun and keep the name in a separate nominative or vocative construction. | Custom and empty/whitespace input, limit, nameplate and later name references. |
| juno-nameplate | `Juno` and `NV-0903`. Juno uses feminine agreement. The display mapping preserves the `j` speaker and its original binding to `gname`. | First introduction and later nameplates, including English after switching back. |
| save-formats | `Strona {}`, `Zapisy automatyczne`, `Szybkie zapisy`, `Puste miejsce`. Format full dates as weekday, day, genitive month, year and time. Leave navigation arrows and actions intact. | Compare empty and occupied slots and numbered, auto and quick pages. Check that the engine uses the authored month forms without changing the saved timestamp. |
| dialogue-timing | Keep every `{w}` in its intended beat and the final `{cps=5}...{/cps}` unchanged. The interrupted `Inży… {w}Co?` repeats the beginning of `inżynieria genetyczna`. | Wait and advance normally through a double wait and the scoped closing ellipsis. |
| main-menu-logo | Keep the branded title artwork. Its text remains `My Furry Protogen`. | Inspect the logo and surrounding Polish navigation at the original size. |
| watch-cutscenes | The reviewed watch assets contain no caption. Preserve both video files and all 20 original call sites. | Verify that a movie advances to its original next story ID. |

## Current corpus

- 1,785/1,785 story entries.
- 394/394 string keys authored, including the engine accessibility,
  developer, updater and renderer strings.
- Authored dialogue SHA-256
  `bf1755f461695b07ccee90342196be439612e7963504918c9184ac91ba7e6912`.
  Authored strings SHA-256
  `071cc66f96343b7ce8c4853751ccfb1cca3733fdeca35da26b414a70cd32fa85`.
- The generated gallery uses the existing `Return` key in translated locales,
  while the quick menu uses `Back`. The native CrossOver probe inspected the
  captions and action classes in English → Polish → Russian → English.
  Polish resolved `Wróć` with Return and `Cofnij` with Rollback. The probe
  composed the original quick menu in its test screen and used placeholders
  for the unavailable gallery thumbnails. The gallery entry in the base
  menu is commented out. This was a binding check, not a gallery playthrough.
- Binding evidence is `text-assets/gallery-binding-verified.79Onas/acceptance.json`
  (`2b678bbd4b45b492be300ae3a7b598be000ac7ed16337c40185e5564610eabef`).
  The muted test restored the previous installed display source and compiled
  file. Both player save stores matched. An isolated installer regression
  verified exact upgrade, idempotence, conflicting-file rollback and rejection
  of unknown display source or bytecode.
- Two strict builds of the complete draft produced identical bytes and verified
  all 747 protected occurrences. The new `Polski` option uses the native
  Ren’Py language action and is conditional on the installed Polish pack.
  [Build and installer evidence](draft-build.json) covers fresh installation,
  exact upgrades, idempotence, rollback and foreign-file rejection in an
  isolated directory. The Russian rebuild also matched the installed Russian
  locale script byte-for-byte.

## Editorial checkpoint

The semantic pass covered all 1,785 story rows, 394 UI keys and both
registered image/video plans. It compared the complete draft with English and
the approved Polish glossary. Applied 83 story and 12 UI corrections. The
[review receipt](semantic-review.json) pins both corpus versions, exact changed
IDs and keys, and the reproducible export builds. The source registry still
records broader artwork and media coverage exclusions.

The exact original depot is available as a detached Steam download. Its strict
build and muted CrossOver opening test passed. The official DLC is identified
separately. All 2,007 DLC story IDs and 395 UI keys pass strict packaging.
Both editions reached the credits and returned to the main menu in muted
CrossOver tests. See the [edition receipt](../edition-qa.json). Independent
editorial acceptance of the DLC text remains pending.
The [first review cycle](review-cycle-01/manifest.json) binds 83 story and 12
UI corrections to 1,017 story IDs and 233 UI keys. The tracked dependency
specification records exchanges, callbacks, glossary forms, UI bindings and
regressions. Reproduce the exact before/after rows and the protected scene
context with `python3 -B tools/prepare_polish_review.py <fresh-directory>`
from this checkout with the pinned English export. Two generations matched
byte-for-byte. An independent reviewer still needs to read the closure.
Current scope does not authorize an additional reviewer.
