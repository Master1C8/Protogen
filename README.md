# My Furry Protogen text assets

English source extraction for Steam app 2009010, Windows build 11915262, installed
depot 2009011, and Ren’Py 8.0.3.22090809. The VN Revival project selected Standard
localization. This checkout contains the extraction recipe and its receipt. The
generated game text and original scripts live in the ignored local `text-assets/`
directory.

## Outputs

| File | Contents |
| --- | --- |
| `text-assets/manifest.json` | Source and compiled SHA-256 checksums, output hashes, and counts |
| `text-assets/inventory.json` | 2,952 literal occurrences with roles, file positions, exact source literals, and Ren’Py dialogue IDs where applicable |
| `text-assets/preserve-exactly.json` | 747 protected source occurrences, including resource names, action arguments, conditions, IDs, and lookup keys |
| `text-assets/renpy-dialogue.tab` | Native export with 1,785 story entries and 68 interface strings |
| `text-assets/renpy-templates/` | Native unchanged-source translation templates with 76 game string keys and 286 common-engine string keys |
| `text-assets/original/game/` | Byte-identical copies of the five installed text scripts |
| `text-assets/special-scenes.json` | Source bindings for names, save formats, dialogue timing, the main-menu logo, and cutscenes |

The story export contains 845 spoken entries and 940 narration entries. The
inventory includes 102 game interface occurrences, four display labels, one
name-entry prompt, and 313 common-engine display values. Repeated occurrences
retain distinct IDs. The native TSV omits eight interface keys present in the
full template. Some directly rendered strings, including the name prompt and
credit headings, also require source inspection to find.

## Reproduce and verify

Use Python 3.9 or later, CrossOver's existing `Steam` bottle, and the installed
Steam build. Run from this checkout. Choose a fresh output directory if
`text-assets` already exists.

```zsh
protogen_game='/Volumes/KINGSTONMAC/CrossOver/Bottles/Steam/drive_c/Program Files (x86)/Steam/steamapps/common/My Furry Protogen'
python3 -B tools/extract_text.py extract "$protogen_game" text-assets
python3 -B tools/extract_text.py verify "$protogen_game" text-assets
```

The tool runs the shipped Ren’Py `dialogue None --strings` and
`translate protogen_source --no-todo` commands headlessly on disposable copies
of the engine and script inputs, with a separate save directory. The installer
and its save data are not copied into this checkout. The verifier checks each
installed compiled script's embedded source MD5, exact original bytes, all
output SHA-256 checksums, the dialogue/template crosswalk, protected fields, and
the special-scene bindings. Ren’Py collapses repeated whitespace in six
dialogue literals. The inventory preserves both the original literal and the
engine text.

The `protogen_source` template folder is an extraction label. A future release
will need an actual target locale, and unmarked interface strings will need a
display mapping or source patch. The project contains no compiled mod.

## Scope and evidence

- The installed base depot contains the original English Ren’Py scripts and the
  default engine string table. English is the only language listed on the
  [Steam store page](https://store.steampowered.com/app/2009010/My_Furry_Protogen/).
  A [community Russian patch](https://github.com/e24x5-Fox/claude-rus-hub) is
  available as a separate reference. This export uses the installed source.
- The separately listed [adult DLC](https://store.steampowered.com/app/2022550/)
  is outside the installed depot used here. No external patch was installed.
- The main-menu background contains the brand logo. The reviewed in-game menu
  and gallery backgrounds showed no visible wording in the prepared preview.
  The rest of the artwork, the two WebM cutscenes, fonts, and audio were
  excluded from text conversion. The source registry records the linked video
  assets and visual review gap.
- Runtime reachability, reinsertion, renderer feasibility, and full literary
  review are pending. The next planning stage is a localization estimate
  against the verified text inventory. The built-in export is documented by
  [Ren’Py](https://www.renpy.org/doc/html/cli.html).
