# Persian localization checkpoint

2026-11-13. My Furry Protogen build 11915262; Persian `fa`, standard localization from English, base and official DLC. Session receipt `text-assets/cli-localization-wave-05-fa-text/fa/turn-041/model-verified.json` matches this thread and pins `gpt-6.1-terra/high`. Shared process binding and queue rule: `localization/STATUS.md`. Owner defers runtime and visual verification to the joint pass. The recorded replacement-map review resolved the previously observed navigation glyph boxes on the tested Arabic path; Persian joining, ZWNJ, mixed direction, wrapping and editable input remain unverified. The separate Arabic marked-text finding remains open.

## Current text state

- Special-scene decisions and author-reviewed timed wording: `special-scenes.md`. Forty-seven base timed IDs are included in `dialogue.tsv`; DLC `start_7b64e49d` is an alias of base `start_f66bb6fe` and is not authored twice.
- Translated and immediately edited coverage: base story **1785/1785**, base UI **394/394**, explicitly authored DLC story **238/238**, DLC UI **1/1**. All text authored. Full semantic comparison: all 1785 base story IDs, all 394 base UI keys, all 238 explicitly authored DLC story IDs and one DLC UI key reviewed, including 83 story entries this turn, recorded in `semantic-coverage.json`; the author comparison now covers all four authored sets. Corrections to `start_e705b4a2`, `start_6c8eb7dc`, `start_9f120078`, `start_906004a5` and `start_69df61db`, `start_b0bfa435` and `start_2dc51781` and `start_80f8ed21` and `start_55c2c595` and `start_31ab804a`, and `start_6b44fb16` require dependency closure; the latter clarifies they barely touched throughout the day; the two bang lines avoid prematurely identifying the sound as an explosion; Clipboard voicing wording was clarified for `Clipboard voicing enabled. `, `clipboard voicing`, and `Clipboard voicing enabled. Press 'shift+C' to disable.`; DLC `start_30e00b54` was corrected to preserve who approaches whom; DLC `start_adc482e0` was corrected to preserve the conditional; independent review remains pending.
- On these files, `build_localization.edition_text(..., draft=False)` passed source-ID membership, token checks, shared-edition equality and alias binding; it resolves 17 DLC aliases from the 1785 base rows. Both export manifests' 13 output hashes match, and the full protected-record lists match their respective inventories (747 base, 744 DLC). These checks do not prove translated meaning, final reinsertion or runtime behavior.
- Approved glossary receipt `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`: English SHA-256 `611e6dec103d1857ec8ed5ce8dc10470312c5ef6d981e1ef307474b44f85d926`; Persian layer `a4792595c0b4d64605638f3be597adec311c29b0960c9befa4c0b954ba45b3a8`. Preserve Pixie as `پیکسی`.
- Independent review, corpus-wide font coverage, packaging, runtime and visual checks remain pending. No game, installer or CrossOver run in this turn.

## Authored file fingerprints

- `dialogue.tsv`: `2711132c9603960a0c573b2ecbbcafdb67540b60178c9ab0246e877e32ae4529`
- `strings.json`: `4749bc53f7e53c27757d5ec0fbf19e7d82e0b5e8af799e94455a97693eb43813`
- `nsfw/dialogue.tsv`: `858d13f1e0d370bf06b913cb5ce7fc0b699337ef301de168b87561f57aae7acf`
- `nsfw/strings.json`: `8781731abfa42f05256618ab3604b4664aed37d792fc63cf70ba673bfdc2dc57`
- `special-scenes.md`: `3569244d3943c713ef8fa68c4ba6bd6253478418dada8b3b93e595160744b0c1`
- `semantic-coverage.json`: `36ee0939828116af5348b155e69cf1bc6a39e4c6fa8c8b0e7be6cf63b66f35e7`

## Next action

Independent review remains pending. Recheck the closure below whenever an input changes; runtime, font, packaging and Git integration are coordinator work. Runtime, font and packaging work belong to the coordinator. Do not relaunch jobs from this session; the coordinator owns continuation.


## Reproducible text validation closure

Run from the project root with Python 3.9.6 and bytecode disabled; this is a text and edition-binding check, not a runtime or independent review:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import json, pathlib, sys
sys.path.insert(0, "tools")
from build_localization import edition_text
b = pathlib.Path("text-assets")
d = b / "edition-qa.0bfO9x/nsfw-export"
edition_text(json.loads((b / "inventory.json").read_text()), json.loads((d / "inventory.json").read_text()), pathlib.Path("localization/fa"), False)
PY
```

Input fingerprints for this check (authored-file fingerprints above):

- `tools/build_localization.py`: `18937f78194ea7503bf14c316b7db3789013ea9accd6e455eadfe2fd3f909d5d`
- `text-assets/inventory.json`: `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`
- `text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json`: `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea`
- `localization/nsfw-story-aliases.json`: `6b020423fc1c45e678c6c8ef6914161ed2978864f91c805d3c0d286c084b8f7c`

- `tools/extract_text.py`: `db7ae33202a62d85f882e142e11bc60de8332c896e8b1077a1781ab43c5ce691`
- `tools/install_language_picker.py`: `c567eec2abd882dad7e72193cb4619444096469f25a741409873c24846d16428`

Check the recorded semantic ID arrays against the four authored key sets after any edit. The special-scene registry and approved glossary receipts remain source-context dependencies; a change requires renewed editorial review. Independent review and the joint runtime pass are pending.
