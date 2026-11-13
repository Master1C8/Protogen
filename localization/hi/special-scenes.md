# Hindi special-scene preparation — 2026-11-13

Status: **wording decisions reviewed for text entry**. The pinned base and DLC registries are `text-assets/special-scenes.json` (SHA-256 `5d3950c98e01d34a49bca5ef8862c5ab5dcec2558c42f709748c68e5134af923`) and `text-assets/edition-qa.0bfO9x/nsfw-export/special-scenes.json` (`2412020e4c4024a82dad7535976a6e1ff8239fec1214c4ac7c211492a75c6f8b`). Their occurrence lists bind both editions. The isolated Ren’Py 8.2.3 HarfBuzz probe in `text-assets/harfbuzz-isolated/result.json` establishes a candidate for dialogue and interpolated names, not final input editing or production feasibility. Those checks remain unverified; current owner decision permits text work. Decisions are author-reviewed, not independently reviewed.

Glossary binding: English `611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926`; Hindi layer `a45014914cf80b2c0ac4e2948c66362055ce7e57fc9adf16425225c7dde879f8`; review receipt `5b0804c29bea6c2b30cfa35b766e7b8d5877131431f5cbd6fad6b6625327f003`, as recorded in `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`. Revalidate if inputs change. Pixie is the proper name पिक्सी for both the AI and the shuttle, distinguished by context; never turn the name into a generic fairy.

## player-name

Source `game/script.rpy` begins with `renpy.input("My name is...", length = 12).strip()`, compares `pname == ""`, and sets `pname = "You"`; both registry lists bind later `[pname]` uses. Proposed display wording: “मेरा नाम है...” and fallback “तुम”. Preserve `pname`, the empty comparison, 12-character limit, `.strip()`, and `[pname]` exactly. Address the male protagonist in agreement with the glossary without inflecting the arbitrary player-supplied name. Do not alter the stored value or assume 12 code points equal 12 visible graphemes. Check entry, deletion, caret and composition of conjuncts and vowel signs, Latin/mixed names, limit behavior and exact persistence in nameplate and dialogue. Positive: a custom name survives unchanged; negative: empty and whitespace-only input select the localized display fallback, not an empty name. Verify source's actual fallback binding and locale display mechanism before implementation; an input prompt image was captured before name insertion, so it does not independently prove the appearance of the entered name.

## juno-nameplate

Source `j` uses `[gname]`, assigned `Juno`. Proposed display “जूनो”; preserve `j`, `gname`, assignment semantics and image attributes, with a locale-scoped display mapping only if compatible with the existing adapter. Positive: opening and later nameplates agree; negative: switching back to English restores Juno and does not alter stored identifiers. Mapping and rendering remain unverified.

## save-formats

Source `screens.rpy:721,763`: `Page {}` → “पृष्ठ {}”; `Automatic saves` → “स्वतः सहेजे गए”; `Quick saves` → “तुरंत सहेजे गए”; `empty slot` → “खाली स्थान”. Keep `{}` exactly once and retain `{#file_time}%A, %B %d %Y, %H:%M` exactly as the proposed timestamp format; runtime platform locale for weekday/month is unverified. Preserve FilePage and FileAction identities. Positive: ordinary, automatic and quick pages and occupied/empty slots display correctly; negative: a missing or changed placeholder/directive must fail validation. Also test editable page name and fit. The isolated shaping route is a candidate; final label layout and fallback adapter remain unverified.

## dialogue-timing

All registry timing IDs have source-context Hindi wording in `dialogue.tsv`; DLC `start_7b64e49d` uses the existing alias to `start_f66bb6fe`. The complete group was compared against English and immediately edited, preserving pauses, the scoped final speed tag, player-name interpolation, speaker intent and Pixie as पिक्सी. The existing edition validator checks shared source bindings, aliases and token counts. Positive: waits advance to the intended next statement and the final slow ellipsis completes; negative: missing, unpaired or changed tags and altered speaker/image bindings must fail validation. A prior synthetic inline wait advanced, but final translated lines and typography remain unverified. Revisit affected uses in the full semantic audit.

## main-menu-logo

Preserve the existing brand artwork “My Furry protogen” unchanged; it is a title, not a puzzle or required Hindi text texture. Keep `game/gui/main_menu.png` and its registry hash unchanged. Positive: the complete logo and translated navigation are visible; negative: clipping or an absent logo fails visual review. Navigation shaping and fit remain unverified.

## watch-cutscenes

No target wording is needed for the two reviewed caption-free videos, `game/images/watches.webm` and `game/images/watchesLong.webm`; retain both exact paths and the registry hashes. The base and DLC have different call-site lists. Positive: each reachable movie returns to its original next statement; negative: a missing/changed path or wrong return fails. Prior visual evidence is documented in `localization/STATUS.md`; this task did not re-review video or run either edition.

For all cases: complete exact protected-field comparison, edition reinsertion, layout, and runtime/visual acceptance remain pending. Source registry exclusions remain exclusions, not evidence of exhaustive literary or audio review. No independent editorial review has been performed.
