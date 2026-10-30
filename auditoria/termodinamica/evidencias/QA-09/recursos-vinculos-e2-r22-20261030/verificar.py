#!/usr/bin/env python3
"""Identidade de quatro links E1→E2 e seus destinos: somente leitura."""
from html.parser import HTMLParser
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[5]
sha=lambda x:hashlib.sha256(x).hexdigest()
e1=(root/'modulos/e1-termodinamica.html').read_bytes();e2=(root/'modulos/e2-transferencia-de-calor.html').read_bytes()
assert sha(e1)=='ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f'
class P(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.a=[];self.ids={}
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.setdefault(d['id'],[]).append((tag,d))
  if tag=='a' and d.get('href','').startswith('e2-transferencia-de-calor.html#'):self.a.append(d['href'])
a=P();a.feed(e1.decode());b=P();b.feed(e2.decode())
want=['conducao','conveccao','trocadores','radiacao']
assert len(a.a)==4 and {x.split('#')[1] for x in a.a}==set(want)
for name in want:assert len(b.ids[name])==1 and b.ids[name][0][0]=='section'
print(json.dumps({'ok':True,'aula_sha256':sha(e1),'destino_e2_sha256':sha(e2),'vinculos':a.a,'destinos_unicos':want},ensure_ascii=False))
