# Hungarian text dependency closure

2026-11-13, turn 025. `text-dependency-hashes.json` binds the English base and DLC inventories, their manifests, preserve-exactly and special-scene registries, the accepted glossary receipt, DLC alias mapping, validator, locale decisions, four authored inputs and exact author semantic coverage. Glossary fingerprints and review receipts are recorded in `STATUS.md`; the receipt is evidence of the prior coordinator verification, not a fresh independent glossary audit. The original bundle bytes and renderer are bound by the pinned manifests and existing receipts, not reverified by this text-only check.

From `/Users/antonkrutov/Desktop/Protogen`, reproduce the text-set check and fingerprint/coverage closure:

```sh
python3 - <<'PY'
import csv, hashlib, json, sys
from pathlib import Path
sys.path.insert(0, 'tools')
import build_localization as b
b.edition_text(json.load(open('text-assets/inventory.json')), json.load(open('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json')), Path('localization/hu'), False)
for name, digest in json.load(open('localization/hu/text-dependency-hashes.json')).items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == digest, name
c = json.load(open('localization/hu/semantic-coverage.json'))
def ids(name):
    with open(name, encoding='utf-8', newline='') as f:
        return [r[0] for r in csv.reader(f, delimiter='\t')]
assert c['base_story'] == ids('localization/hu/dialogue.tsv')
assert c['base_ui'] == list(json.load(open('localization/hu/strings.json')))
assert c['dlc_story'] == ids('localization/hu/nsfw/dialogue.tsv')
assert c['dlc_ui'] == list(json.load(open('localization/hu/nsfw/strings.json')))
a = json.load(open('localization/nsfw-story-aliases.json'))
assert len(a) == 17 and not set(a) & set(c['dlc_story'])
print('Fingerprints and authored/audited ID sets match; alias keys excluded.')
PY
```

The validator resolves the 17 DLC aliases from their base inputs and shared story IDs directly from base text; 238 explicitly authored DLC IDs are separate. The alias values and all other correction dependencies remain subject to independent review. This check does not establish source reinsertion, runtime rendering, visual quality, glossary equivalence, or independent editorial acceptance. Changing any bound input invalidates the corresponding prior checks; regenerate the manifest only after reviewing the affected dependency and rerunning validation. Full integration and review belong to the coordinator.
