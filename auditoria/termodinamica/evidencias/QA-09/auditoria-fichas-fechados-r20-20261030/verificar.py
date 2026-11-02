#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from decimal import Decimal as D
from math import log
import json,re,xml.etree.ElementTree as ET
Q=Path('auditoria/termodinamica/evidencias/QA-09');F=Q/'fichas-fechados-reconciliacao-r20-20261030'
def read(p,h):
 b=Path(p).read_bytes();assert sha256(b).hexdigest()==h,p;return b
sources=[('r9',Q/'aplicacao-pressao-fichas-r10-r1/antes-formulario.html','cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'),('r10',Q/'aplicacao-pressao-fichas-r10-r1/depois-formulario.html','01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9'),('r20',Path('formulas/termodinamica.html'),'694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58')];docs={id:read(p,h).decode().encode('utf-16-le') for id,p,h in sources};html=read('modulos/e1-termodinamica.html','b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7').decode();read(Q/'inventario-r20.json','e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4');rows=json.loads(read(F/'identidades.json','429cc00638df43bd13e7fb649901bba5b20daf25432623ecf0722a40e2319d1f'));assert [r['ficha'] for r in rows]==list(range(31,42))
class IDs(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,tag,attrs):self.ids.extend(v for k,v in attrs if k=='id')
p=IDs();p.feed(html);nmath=0;links=0;changed=[]
for row in rows:
 fr=[]
 for id,raw in docs.items():
  o=row[id];x=raw[o['inicio_utf16']*2:o['fim_utf16']*2].decode('utf-16-le');assert sha256(x.encode()).hexdigest()==o['sha256'] and x.count('id="'+row['id']+'"')==1;fr.append(x)
 assert fr[1]==fr[2]
 if fr[0]!=fr[2]:changed.append(row['ficha'])
 maths=re.findall(r'<math\b[\s\S]*?</math>',fr[2]);[ET.fromstring(x) for x in maths];nmath+=len(maths)
 for a in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^"]+)"',fr[2]):assert p.ids.count(a)==1;links+=1
assert changed==[40] and links==12
assert 100-30-10+5==65 and 200+100-30==270 and D(100)*(D('.2')-D('.5'))==-30
assert D('.718')*100==D('71.8') and D('1.005')*100==D('100.5') and 500+200*D('.5')==600
assert abs(.287*300*log(2)-59.6799722462)<1e-9 and abs(.287*log(2)-.19893324082)<1e-10
print(json.dumps({'ok':True,'fichas':len(rows),'diferentes_r9':changed,'mathml_xml':nmath,'links':links,'limite':'Parsing estrutural e testes nominais; não prova ciência, apresentação ou outros lotes.'},ensure_ascii=False))
