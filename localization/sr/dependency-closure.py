#!/usr/bin/env python3
"""Reproduce the recorded cross-edition dependencies of semantic corrections."""
import csv, hashlib, json
from pathlib import Path
P=Path('.'); ids='start_7e6bbff6 start_5c3962b6 start_d4346f8c start_13d35f98 start_57e49fb0 start_731484ac start_e4801bf6 start_85324022 start_bad91272 start_df9b08f4 start_4b50c481 start_05713692 start_91c3ad14'.split()
def rows(path):
    with path.open() as f: return [x for x in csv.DictReader(f,delimiter='\t') if x['Identifier']]
def tsv(path):
    with path.open() as f: return dict(line.rstrip('\n').split('\t',1) for line in f if line.strip())
b=rows(P/'text-assets/renpy-dialogue.tab'); d=rows(P/'text-assets/edition-qa.0bfO9x/nsfw-export/renpy-dialogue.tab'); dm={x['Identifier']:x for x in d}; bt=tsv(P/'localization/sr/dialogue.tsv'); dt=tsv(P/'localization/sr/nsfw/dialogue.tsv'); aliases=json.loads((P/'localization/nsfw-story-aliases.json').read_text()); out=[]
for key in ids:
    i=next(i for i,x in enumerate(b) if x['Identifier']==key); x=b[i]; y=dm[key]
    assert x['Dialogue']==y['Dialogue'] and x['Character']==y['Character'] and key not in dt
    out.append({'id':key,'previous':b[i-1]['Identifier'],'next':b[i+1]['Identifier'],'shared_english_and_speaker':True,'aliases':[k for k,v in aliases.items() if v==key],'target':bt[key]})
assert all(not x['aliases'] for x in out)
key='start_0e2799a2'; i=next(i for i,x in enumerate(d) if x['Identifier']==key); assert 'Повукла ме' in dt[key]
files=['text-assets/inventory.json','text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json','text-assets/renpy-dialogue.tab','text-assets/edition-qa.0bfO9x/nsfw-export/renpy-dialogue.tab','localization/nsfw-story-aliases.json','localization/sr/dialogue.tsv','localization/sr/strings.json','localization/sr/nsfw/dialogue.tsv','localization/sr/nsfw/strings.json','localization/sr/semantic-coverage.json']
print(json.dumps({'sha256':{f:hashlib.sha256((P/f).read_bytes()).hexdigest() for f in files},'base_corrections':out,'dlc_correction':{'id':key,'previous':d[i-1]['Identifier'],'next':d[i+1]['Identifier'],'target':dt[key]},'source_anomaly':{'id':'start_5c6117e8','speaker':dm['start_5c6117e8']['Character'],'target':dt['start_5c6117e8']},'source_name':{'id':'start_75bdc594','target':dt['start_75bdc594']}},ensure_ascii=False,indent=2))
