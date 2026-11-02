#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from decimal import Decimal as D
import json,re,xml.etree.ElementTree as ET
Q=Path('auditoria/termodinamica/evidencias/QA-09');F=Q/'fichas-gases-fases-reconciliacao-r19-20261030'
def read(p,h):
 b=Path(p).read_bytes();assert sha256(b).hexdigest()==h,p;return b
old=read(Q/'aplicacao-flashcards-ficha80-r1/depois-formulario.html','cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb').decode().encode('utf-16-le');new=read('formulas/termodinamica.html','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58').decode().encode('utf-16-le');html=read('modulos/e1-termodinamica.html','9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65').decode();read(Q/'inventario-r19.json','ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f');rows=json.loads(read(F/'identidades.json','93eee99a4326cbd56695226d7a79c6f2b84b15a0c73ea627fa5c1455174488fc'));assert [o['ficha'] for o in rows]==[13,14,15,16,17,18,20,21,22]
class IDs(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,tag,attrs):
  self.ids.extend(v for k,v in attrs if k=='id')
p=IDs();p.feed(html);counts={};destinations=[]
for r in rows:
 b=[]
 for key,raw in [('r9',old),('r19',new)]:
  o=r[key];frag=raw[2*o['inicio_utf16']:2*o['fim_utf16']].decode('utf-16-le');assert sha256(frag.encode()).hexdigest()==o['sha256'];b.append(frag)
 assert b[0]==b[1] and b[1].count('id="'+r['id']+'"')==1
 maths=re.findall(r'<math\b[\s\S]*?</math>',b[1]);[ET.fromstring(m) for m in maths];counts[str(r['ficha'])]=len(maths)
 links=re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^"]+)"',b[1]);assert len(links)==1 and p.ids.count(links[0])==1;destinations.append(links[0])
assert sum(counts.values())==20
assert D(1)*D('.287')*D(300)/D('.861')==100 and D('.287')*400/200==D('.574') and D(90)*D('.861')/(D('.287')*300)==D('.9')
assert D('.718')*100==D('71.8') and D('1.005')*100==D('100.5') and 2*D('.718')*100==D('143.6')
assert D('.8')*100+D('.001')*(D(400)**2-D(300)**2)/2==115
assert D(1)/(1+3)==D('.25') and D('.75')*500+D('.25')*2500==1000 and D('.75')*D('.001')+D('.25')==D('.25075')
print(json.dumps({'ok':True,'artigos':len(rows),'mathml_xml':counts,'destinos':destinations,'limites':'Leitura estrutural e exemplos nominais; não comprova estado real, apresentação visual nem mérito científico automático.'},ensure_ascii=False,indent=2))
