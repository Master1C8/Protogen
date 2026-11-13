# Bulgarian author review dependency closure

2026-11-13. `semantic-dependency-closure.json` records the 11 corrected IDs from batches 001, 003–005, 007–008 and 011, each immediately neighboring authored IDs, shared-edition membership, alias dependents, input hashes and outstanding source findings. The author rechecked those corrected lines and immediate neighbors against English in this turn. All ten corrected base IDs are shared with the DLC; none has an alias dependent. The corrected DLC ID is not shared. The wider context and Pixie referent were reviewed in the corresponding batches; immediate neighbors are a reproducible minimum, not proof that literary dependencies are exhaustive.

The four authored ID sets were reconciled against the inventories, authored files and alias map. The strict edition validator also passed after the last correction. Reproduce the mechanical binding and coverage checks from the project root:

```sh
python3 -B - <<'PY'
from pathlib import Path
import hashlib, json, sys
sys.path.insert(0, 'tools')
import build_localization as b
p = Path('localization/bg')
c = json.loads((p / 'semantic-dependency-closure.json').read_text())
for path, expected in c['inputs_sha256'].items():
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == expected, path
base = json.loads(Path('text-assets/inventory.json').read_text())
dlc = json.loads(Path('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json').read_text())
a = json.loads(Path('localization/nsfw-story-aliases.json').read_text())
bs, ds = b.story_rows(base), b.story_rows(dlc)
bd, dd = b.load_dialogue(p / 'dialogue.tsv'), b.load_dialogue(p / 'nsfw/dialogue.tsv')
st, du = json.loads((p / 'strings.json').read_text()), json.loads((p / 'nsfw/strings.json').read_text())
v = json.loads((p / 'semantic-coverage.json').read_text())
expected = {'base_story': set(bs), 'base_ui': b.string_keys(base), 'dlc_story': set(ds)-set(bs)-set(a), 'dlc_ui': b.string_keys(dlc)-b.string_keys(base)}
for key, values in v.items():
    assert len(values) == len(set(values)) and set(values) == expected[key]
for item in c['corrections']:
    ordered = list(bd if item['edition'] == 'base' else dd)
    other = ds if item['edition'] == 'base' else bs
    i = ordered.index(item['id'])
    assert item['authored_neighbors'] == ordered[max(0, i-1):i+2]
    assert item['shared_with_other_edition'] == (item['id'] in other)
    assert item['dlc_aliases'] == [k for k, val in a.items() if item['edition'] == 'base' and val == item['id']]
b.edition_text(base, dlc, p, False)
print('Coverage and correction bindings verified')
PY
```

The approved glossary hash is the previously verified coordinator receipt, not a new independent glossary review. This closure does not prove runtime behavior, visual fit, protected source fields after reinsertion, editorial acceptance or independent review. Those remain pending. The source speaker mismatch at DLC `start_5c6117e8` remains unresolved; preserve `p` and `[pname]` until source-authoritative evidence supports a change. The source names Katie in `start_75bdc594` without establishing identity with the earlier unnamed girl.
