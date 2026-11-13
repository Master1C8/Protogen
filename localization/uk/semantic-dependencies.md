# Ukrainian author comparison dependency binding

2026-11-13. SHA-256 of the inputs and authored outputs at the conclusion of this comparison. Approved glossary source, Ukrainian layer and review were verified against the pinned glossary receipt as recorded in STATUS.md; this binding does not replace that evidence. Recheck affected comparison and validation if these inputs change.

- `text-assets/inventory.json`: `8b9c6008ad1b13c40f0abfcfb7f0cf94f8fda0777a3eb3e59aa6bbf6f8cf56ff`
- `text-assets/renpy-dialogue.tab`: `4ba57708ea623be3177c60680b318461469741b1109e7874d8e4c3131e007ad5`
- `text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json`: `b0feab1e5d5dfa697bbeee0a98a8dc310edd30ce6acc908aee8e776b5f0aa2ea`
- `text-assets/edition-qa.0bfO9x/nsfw-export/renpy-dialogue.tab`: `74ff2174cd5eb7515bbb5bc2ae8ce82dc672f80bf16909f57af23432fe29ab93`
- `localization/nsfw-story-aliases.json`: `6b020423fc1c45e678c6c8ef6914161ed2978864f91c805d3c0d286c084b8f7c`
- `tools/build_localization.py`: `18937f78194ea7503bf14c316b7db3789013ea9accd6e455eadfe2fd3f909d5d`
- `tools/extract_text.py`: `db7ae33202a62d85f882e142e11bc60de8332c896e8b1077a1781ab43c5ce691`
- `tools/install_language_picker.py`: `c567eec2abd882dad7e72193cb4619444096469f25a741409873c24846d16428`
- `localization/uk/dialogue.tsv`: `bcde755774ebc24ab9995db197a4fb46087d0688b67b3b631eae3b4221546078`
- `localization/uk/strings.json`: `76ae72fbd456d1be75d69ef59914ce10a364f418e6f3be6c970f2f1c5258b7c7`
- `localization/uk/nsfw/dialogue.tsv`: `f403fa189e70fbcae51dbb98c4bc68e0aeb1213961e15d7799bef09ec79d6ff3`
- `localization/uk/nsfw/strings.json`: `39fc2ffa542e3ee4b3c003e7520ac9e30dc69e6b11f3d05de66cd6a948a94a58`
- `localization/uk/special-scenes.md`: `c08a981a7d5a0fa50ea01b5274274cdc7780f84210481171cbe413c10e3ad7ce`
- `localization/uk/semantic-coverage.json`: `2cf78c39b4f0554b1a6d91e9c6aa5ac5153c74e32b7c2057cefb461291a3d5b4`
- `text-asset-receipt.json`: `1ad9c080caed30f47584a2a4062a1ab9ab665eba5bf7e8c35736c5ccfc05c0a8`
- `text-asset-nsfw-receipt.json`: `da9a7f72df14f7b725d7566ae0f1cac40f7390042d74b410c9aaf05a48063b6f`
- `text-assets/multilingual-probe.L4KEcD/glossary-receipts.json`: `5935841fb335bb53db74afe2134e70c45068ee8dbea7cf6a87f287aef794cddd`

Reproduce the strict text-set check from the project root (Python 3, standard library):

```sh
PYTHONPATH=tools python3 -B - <<'PY2'
import json
from pathlib import Path
from build_localization import edition_text
base = json.loads(Path('text-assets/inventory.json').read_text())
dlc = json.loads(Path('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json').read_text())
edition_text(base, dlc, Path('localization/uk'), False)
PY2
```

This exercises authored key sets, duplicates, tags/placeholders, shared-edition fields and alias mappings. It does not establish editorial acceptance, protected-field equality after reinsertion, runtime or visual correctness. Independent review remains pending; the two source inconsistencies and the full timed-scene contextual audit remain open in STATUS.md.
