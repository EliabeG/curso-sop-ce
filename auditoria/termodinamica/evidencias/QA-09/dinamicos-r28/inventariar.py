#!/usr/bin/env python3
"""Inventário estático do HTML r27, não executa JavaScript."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from collections import Counter
import json
r=Path(__file__).resolve().parents[5];f=r/'auditoria/termodinamica/evidencias/QA-09/aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html';b=f.read_bytes();assert sha256(b).hexdigest()=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'
class P(HTMLParser):
 def __init__(self):super().__init__();self.tags=Counter();self.inputs=Counter();self.scripts=[];self.downloads=[]
 def handle_starttag(self,t,a):
  d=dict(a);self.tags[t]+=1
  if t=='input':self.inputs[d.get('type','text')]+=1
  if t=='script':self.scripts.append(d.get('src','inline'))
  if t=='a' and 'download' in d and 'termodinamica/fun0' in d.get('href',''):self.downloads.append(d['href'])
p=P();p.feed(b.decode());assert p.scripts==['../assets/registro.js','../assets/curso.js'];assert not p.tags['canvas'] and not p.inputs['number'] and not p.inputs['range']
print(json.dumps({'ok':True,'scripts':p.scripts,'inputs':dict(p.inputs),'tags':{k:p.tags[k] for k in ('button','select','details','canvas','video','iframe')},'downloads_fun':p.downloads,'limite':'Inspeção estática; não executa ações de navegador.'},ensure_ascii=False,indent=2))
