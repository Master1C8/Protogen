#!/usr/bin/env python3
"""Recheck Romanian authored/audited ID sets and DLC reuse from project root."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path('tools').resolve()))
from build_localization import edition_text

def read(path):
    return json.loads(Path(path).read_text())

def tsv(path):
    return dict(line.split('\t', 1) for line in Path(path).read_text().splitlines())

root = Path('localization/ro')
base = read('text-assets/inventory.json')
dlc = read('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json')
alias = read('localization/nsfw-story-aliases.json')
coverage = read(root / 'semantic-coverage.json')
bt, dt = tsv(root / 'dialogue.tsv'), tsv(root / 'nsfw/dialogue.tsv')
bu, du = read(root / 'strings.json'), read(root / 'nsfw/strings.json')
edition_text(base, dlc, root, False)
for key, expected in {'base_story': bt, 'base_ui': bu, 'dlc_story': dt, 'dlc_ui': du}.items():
    actual = coverage[key]
    assert len(actual) == len(set(actual)) and set(actual) == set(expected), key
    print(key, len(actual), 'exact audited set')
def story(inv):
    return {r['id']: r['text'] for r in inv if r['role'] in ('dialogue', 'narration')}
bs, ds = story(base), story(dlc)
shared = set(bs) & set(ds)
assert all(bs[k] == ds[k] for k in shared)
assert set(alias).isdisjoint(dt) and set(alias) <= set(ds) and set(alias.values()) <= set(bt)
assert all(ds[k] == bs[v] for k, v in alias.items())
assert set(ds) == shared | set(dt) | set(alias)
print('DLC story', len(ds), 'shared', len(shared), 'explicit', len(dt), 'aliases', len(alias))
