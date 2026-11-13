# My Furry Protogen localization

English source extraction and language picker for Steam app 2009010, Windows
build 11915262, installed depot 2009011, and Ren’Py 8.0.3.22090809. The VN Revival
project selected Standard localization. The generated game text and original
scripts live in the ignored local `text-assets/` directory.

## Windows localization installer

See [the installer build and player guide](installer/README.md) for the offline
Steam installer and its bundled Ren’Py runtime. It installs all 30 languages
for the detected base game or DLC.

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

The `protogen_source` template folder is an extraction label.

## Steam editions

The build identifies the original Steam depot and the official 18+ DLC by their
exact source and bytecode hashes. The two English inventories have 1,785 and
2,007 story statements respectively. The 1,752 statements with shared IDs use
one translation. The DLC has 255 additional or replacement IDs and one extra
UI key, `Gallery`. The [DLC receipt](text-asset-nsfw-receipt.json) pins its export.
The builder uses the matching Ren’Py templates and retains the original
speaker and image attributes for each edition.

Export the DLC from the installed Steam game to a fresh directory with
`python3 -B tools/extract_text.py extract "$protogen_game" <dlc-export>`.
For that installation, pass `--nsfw-bundle <dlc-export>` to the build command.
The strict build requires every DLC translation before emitting an installer
payload. Use `--draft` to check partial source files. The detached original
Steam depot accepts `--steam-manifest <appmanifest_2009010.acf>`.
See the [edition test receipt](localization/edition-qa.json) for the current
coverage and CrossOver results.

## Language picker

All 30 localizations use Ren’Py’s built-in language selector. Close the game
before installing. Use a fresh output directory for each locale and append
`--nsfw-bundle <dlc-export>` when the DLC is installed.

```zsh
python3 -B tools/build_localization.py "$protogen_game" ru --output text-assets/ru-build --install
python3 -B tools/build_localization.py "$protogen_game" pl --output text-assets/pl-build --install
```

The build validates the Steam scripts, extracted inventory, complete stable-ID
coverage and placeholders. It produces additive scripts and locale-specific font resources. The installer
retires the earlier Russian sample if its contents match the checked-in version.
Rebuild and reinstall each locale when switching editions. The installer can
replace the verified Russian and Polish packages from either edition and
retires their matching bytecode so Ren’Py recompiles them on launch.

- `game/vnrevival_protogen_preferences.rpy`
- `game/vnrevival_protogen_display.rpy`
- `game/tl/russian/vnrevival_protogen_text.rpy`
- `game/tl/polish/vnrevival_protogen_text.rpy`

Open **Preferences → Language** to choose English or any installed
localization by its native name. The builder’s installer upgrades recognized
older versions of the shared Preferences script.
To remove a localization, select English, close the game and remove that
locale’s generated scripts and their matching `.rpyc` files.

The editable Russian sources contain 1,785 story entries and 394 distinct
string keys, including interface, character labels, credits and Ren’Py
system strings. See [the checkpoint](localization/ru/STATUS.md) for the pinned
glossary, validation and CrossOver evidence.

For CrossOver automation, place `tools/qa_isolate_saves.rpy` in `game/` only
for the duration of QA. Set `RENPY_DISABLE_SOUND=1`. Launch with an absolute scratch `--savedir` containing
a `.vnrevival-qa` marker. Ren’Py 8.0.3 normally writes to both `--savedir` and
`game/saves`. The QA script redirects the second location into the scratch
directory before the engine scans any saves. When testing the first name prompt,
verify that the autosave and persistent data appear only in those scratch
locations. Compare the checksums and slot names of both player locations before
and after the run, then remove the temporary script and its matching `.rpyc`.

## Scope and evidence

- The installed base depot contains the original English Ren’Py scripts and the
  default engine string table. English is the only language listed on the
  [Steam store page](https://store.steampowered.com/app/2009010/My_Furry_Protogen/).
  A [community Russian patch](https://github.com/e24x5-Fox/claude-rus-hub) is
  available as a separate reference. This export uses the installed source.
- The original inventory covers depot 2009011. The official
  [adult DLC](https://store.steampowered.com/app/2022550/) uses depot 2022550
  and has its own pinned export.
- The main-menu background contains the brand logo. The reviewed in-game menu
  and gallery backgrounds showed no visible wording in the prepared preview.
  The rest of the artwork, the two WebM cutscenes, fonts, and audio were
  excluded from text conversion. The source registry records the linked video
  assets and visual review gap.
- The built-in export is documented by
  [Ren’Py](https://www.renpy.org/doc/html/cli.html).

## Localized fonts

The builder accepts all 30 authored locale codes. For the pinned Noto faces,
point `--font-source` at a directory containing the exact font and license
files in [font-sources.json](localization/font-sources.json). The local default
is `text-assets/font-candidates.vUrRKa`. The build checks both SHA-256
fingerprints before writing the package. For fonts distributed in a release
ZIP, extract the named face and license from the pinned upstream release and
use the filenames from the receipt. The installer copies font resources and
licenses alongside the generated Ren’Py scripts.

The packages for Arabic, Persian, Hindi and Thai use HarfBuzz on Ren’Py
8.2.3. Build these as additive packages and test them on a separate copy
running that SDK. The original Steam Ren’Py 8.0.3 installation is unsupported
for these shaping paths. Use the pinned Steam depot for extraction and
packaging validation. The previously tested Windows SDK is version
`8.2.3.24061702`, archive SHA-256
`0043c0110654d9c526ddf6419c800fc99ddf35dea8993ebf2126c4b2f16c90c2`.
