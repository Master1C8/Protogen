#!/usr/bin/env python3
"""Reproduce the author-audit correction neighborhood and DLC alias dependencies."""
import csv
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
status = (root / 'localization/vi/STATUS.md').read_text(encoding='utf-8')
audit = status.split('## Turn 017 continuation', 1)[1].split('## Turn 033 continuation', 1)[0]
phrases = re.findall(r'Corrected ([^.]+)\.', audit)
base_fixed = list(dict.fromkeys(x for phrase in phrases for x in re.findall(r'`(start_[A-Za-z0-9_]+)`', phrase)))
dlc_fixed = ['start_342c0dd6', 'start_c67d4386']
paths = {
 'base_source': 'text-assets/renpy-dialogue.tab',
 'dlc_source': 'text-assets/edition-qa.0bfO9x/nsfw-export/renpy-dialogue.tab',
 'base_text': 'localization/vi/dialogue.tsv',
 'dlc_text': 'localization/vi/nsfw/dialogue.tsv',
 'aliases': 'localization/nsfw-story-aliases.json',
 'semantic_coverage': 'localization/vi/semantic-coverage.json',
 'special_decisions': 'localization/vi/special-scenes.md',
}
coverage = json.loads((root / paths['semantic_coverage']).read_text(encoding='utf-8'))
aliases = json.loads((root / paths['aliases']).read_text(encoding='utf-8'))
def neighbors(source, ids, audited):
 with (root / source).open(encoding='utf-8', newline='') as f:
  ordered = [r['Identifier'] for r in csv.DictReader(f, delimiter='\t') if r['Identifier'] in set(audited)]
 assert len(ordered) == len(audited) and len(set(ordered)) == len(ordered)
 pos = {v:i for i,v in enumerate(ordered)}
 result = {}
 for key in ids:
  assert key in pos
  i = pos[key]; result[key] = ordered[max(0, i-1):i+2]
 return result
result = {
 'scope': 'Corrections recorded during author semantic audit turns 017-033; immediate source-order authored story neighbors and DLC aliases. Full authored sets compared with English; runtime and independent review are separate.',
 'reproduce': 'python3 -B localization/vi/dependency-closure.py',
 'sha256': {k: hashlib.sha256((root / p).read_bytes()).hexdigest() for k,p in paths.items()},
 'base_corrections_and_neighbors': neighbors(paths['base_source'], base_fixed, coverage['base_story']),
 'dlc_corrections_and_neighbors': neighbors(paths['dlc_source'], dlc_fixed, coverage['dlc_story']),
 'aliases_referencing_corrected_base': {k:v for k,v in aliases.items() if v in base_fixed},
 'all_alias_bindings': aliases,
 'unresolved_source_evidence': {'start_5c6117e8': 'DLC source speaker is p although the line addresses [pname] amid Juno responses; preserve original binding, do not infer or change the speaker. Owner or source confirmation remains pending.'},
}
out = root / 'localization/vi/dependency-closure.json'
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('recorded', len(base_fixed), 'base corrections,', len(dlc_fixed), 'DLC corrections,', len(aliases), 'alias bindings')
