#!/usr/bin/env python3
"""Reproduce French authored coverage, source token, and edition-alias checks."""
import csv
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys

P = Path(__file__).resolve().parents[2]
F = P / 'localization/fr'
sys.path.insert(0, str(P / 'tools'))
import build_localization as b

base = json.loads((P / 'text-assets/inventory.json').read_text())
dlc = json.loads((P / 'text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json').read_text())
base_d = b.load_dialogue(F / 'dialogue.tsv')
dlc_d = b.load_dialogue(F / 'nsfw/dialogue.tsv')
base_ui = json.loads((F / 'strings.json').read_text(), object_pairs_hook=b.unique_strings)
dlc_ui = json.loads((F / 'nsfw/strings.json').read_text(), object_pairs_hook=b.unique_strings)
c = json.loads((F / 'semantic-coverage.json').read_text())
for name, expected in [('base_story', base_d), ('base_ui', base_ui), ('dlc_story', dlc_d), ('dlc_ui', dlc_ui)]:
    assert len(c[name]) == len(set(c[name])) and set(c[name]) == set(expected), name
edition_d, edition_ui = b.edition_text(base, dlc, F, False)
counts = {}
for label, inv, translated in [('base', base, base_d), ('dlc', dlc, edition_d)]:
    checked = 0
    for row in inv:
        if row['role'] not in b.STORY_ROLES:
            continue
        target = translated[row['id']]
        for token in set(row['preserveTokens']):
            assert target.count(token) == row['text'].count(token), (label, row['id'], token)
            checked += 1
    counts[label] = checked
aliases = json.loads((P / 'localization/nsfw-story-aliases.json').read_text())
assert all(edition_d[target] == base_d[original] for target, original in aliases.items())
fixes = {}
for batch in sorted(F.glob('semantic-batch-*.json')):
    corrections = json.loads(batch.read_text()).get('corrections', {})
    if isinstance(corrections, list):
        for item in corrections:
            fixes[item['id']] = item['new']
    else:
        fixes.update({key: value['after'] for key, value in corrections.items()})
for key, target in fixes.items():
    assert (base_d.get(key) if key in base_d else dlc_d.get(key)) == target, key
affected_aliases = {target: original for target, original in aliases.items() if original in fixes}
paths = ['text-assets/inventory.json', 'text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json', 'localization/nsfw-story-aliases.json', 'tools/build_localization.py', 'localization/fr/dialogue.tsv', 'localization/fr/strings.json', 'localization/fr/nsfw/dialogue.tsv', 'localization/fr/nsfw/strings.json', 'localization/fr/semantic-coverage.json']
print(json.dumps({'semantic_counts': {k: len(v) for k,v in c.items()}, 'story_preserve_token_checks': counts, 'alias_count': len(aliases), 'corrected_ids': sorted(fixes), 'corrected_alias_dependencies': affected_aliases, 'sha256': {name: sha256((P/name).read_bytes()).hexdigest() for name in paths}, 'limits': 'Checks authored text and story preserveTokens; non-translatable original script literals and runtime output require coordinator verification.'}, indent=2))
