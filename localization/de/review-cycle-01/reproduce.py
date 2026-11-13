import hashlib,json,re,sys
from pathlib import Path
sys.path.insert(0,'tools')
from build_localization import edition_text,authored_text
root=Path('localization/de'); evidence=Path(sys.argv[1]); evidence.mkdir(parents=True,exist_ok=True); run=Path('text-assets/cli-localization-text.5s1g3lq4/de/cycle-01'); before=root/'review-cycle-01/before'
base=json.load(open('text-assets/inventory.json')); dlc=json.load(open('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json'))
# Read the old draft via a locale-named parent, without generating wording.
old=run/'candidate-old/de'; (old/'nsfw').mkdir(parents=True,exist_ok=True)
for n in ['dialogue.tsv','strings.json','nsfw/dialogue.tsv','nsfw/strings.json']:
 p=old/n; data=(before/n).read_bytes()
 if p.exists(): assert p.read_bytes()==data
 else: p.write_bytes(data)
oldbase,oldui=authored_text(base,old,False); newbase,newui=authored_text(base,root,False)
olddlc,olddui=edition_text(base,dlc,old,False); newdlc,newdui=edition_text(base,dlc,root,False)
assert oldui==newui and olddui==newdui
allout={}
for name,inv,oldmap,newmap,reg in [('sfw',base,oldbase,newbase,Path('text-assets/special-scenes.json')),('nsfw',dlc,olddlc,newdlc,Path('text-assets/edition-qa.0bfO9x/nsfw-export/special-scenes.json'))]:
 rows=[x for x in inv if x['role'] in ('dialogue','narration')]; ids=[x['id'] for x in rows]; byid={x['id']:x for x in rows}; assert set(ids)==set(newmap)==set(oldmap)
 changed=[k for k in ids if oldmap[k]!=newmap[k]]; assert changed
 context=set()
 for k in changed:
  i=ids.index(k); context.update(ids[max(i-1,0):min(i+2,len(ids))])
 sources={byid[k]['text'].strip() for k in changed}; targets={v for k in changed for v in (oldmap[k],newmap[k])}
 repetitions={k for k in ids if byid[k]['text'].strip() in sources or oldmap[k] in targets or newmap[k] in targets}
 # The changed shuttle wording can affect all related occurrences, including inflections.
 concept={k for k in ids if re.search(r'\b(?:ship|ships|jet|jets|pixie|shuttle|shuttles|schiff\w*|shuttle\w*)\b',byid[k]['text']+' '+oldmap[k]+' '+newmap[k],re.I)}
 cases=json.loads(reg.read_text())['cases']; runtime={k for c in cases for k in c.get('occurrences',[]) if k in byid}
 closure=set(changed)|context|repetitions|concept|runtime
 components={'changed':changed,'neighbor_context':[k for k in ids if k in context], 'exact_repetitions':[k for k in ids if k in repetitions], 'ship_shuttle_pixie':[k for k in ids if k in concept], 'registered_runtime':[k for k in ids if k in runtime]}
 ordered=[k for k in ids if k in closure]
 review=[{'id':k,'source':byid[k]['text'],'before':oldmap[k],'after':newmap[k]} for k in ordered]
 files={name+'-changed.json':changed,name+'-closure.json':ordered,name+'-components.json':components,name+'-review.json':review,name+'-nonstory-context.json':[c for c in cases for k in c.get('occurrences',[]) if k not in byid]}
 for fn,value in files.items():
  p=evidence/fn; assert not p.exists(),p; p.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
 allout[name]={'changed':len(changed),'closure':len(ordered),'total':len(ids)}
manifest={'schemaVersion':1,'encoding':'UTF-8','newline':'LF','description':'First correction cycle; broad ship/shuttle/Pixie selector and registered special-scene IDs. Independent review and completeness reconciliation pending.', 'counts':allout,'inputs':{},'files':{}}
for p in [Path('text-assets/inventory.json'),Path('text-assets/edition-qa.0bfO9x/nsfw-export/inventory.json'),Path('text-assets/special-scenes.json'),Path('text-assets/edition-qa.0bfO9x/nsfw-export/special-scenes.json'),Path('/Users/antonkrutov/Desktop/SiteForMods/data/games/my-furry-protogen/glossary.json')]+[root/n for n in ['dialogue.tsv','strings.json','nsfw/dialogue.tsv','nsfw/strings.json']]+[before/n for n in ['dialogue.tsv','strings.json','nsfw/dialogue.tsv','nsfw/strings.json']]: manifest['inputs'][str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
for p in sorted(evidence.glob('*.json')):manifest['files'][p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
p=evidence/'manifest.json'; assert not p.exists(); p.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(allout))
