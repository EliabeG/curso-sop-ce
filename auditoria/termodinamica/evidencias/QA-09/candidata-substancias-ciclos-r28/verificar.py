#!/usr/bin/env python3
"""Simulação em memória; não aplica candidatas ao produto."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json,re
r=Path(__file__).resolve().parents[5];d=Path(__file__).resolve().parent;sha=lambda x:sha256(x).hexdigest();m=json.loads((d/'manifesto.json').read_bytes());assert m['estado']=='CANDIDATA_NAO_APLICADA'
for key in ('fonte','inventario','parecer'):assert sha((r/m[key]).read_bytes())==m[key+'_sha256']
raw=(r/m['fonte']).read_bytes();u=raw.decode().encode('utf-16-le');ed=m['edicoes'];assert len(ed)==2 and {e['id'] for e in ed}=={'substancias','ciclos'}
for e in ed:
 a,z=e['inicio_utf16'],e['fim_utf16'];original=u[2*a:2*z].decode('utf-16-le');assert original.encode()==(d/(e['id']+'-original.html')).read_bytes().removesuffix(b'\n') and sha(original.encode())==e['original_sha256'];candidate=original
 for sub in e['substituicoes']:assert candidate.count(sub['antes'])==1;candidate=candidate.replace(sub['antes'],sub['depois'],1)
 assert candidate.encode()==(d/(e['id']+'-candidata.html')).read_bytes().removesuffix(b'\n') and sha(candidate.encode())==e['candidata_sha256']
for x,y in zip(sorted(ed,key=lambda e:e['inicio_utf16']),sorted(ed,key=lambda e:e['inicio_utf16'])[1:]):assert x['fim_utf16']<=y['inicio_utf16']
v=u
for e in sorted(ed,key=lambda e:e['inicio_utf16'],reverse=True):v=v[:2*e['inicio_utf16']]+(d/(e['id']+'-candidata.html')).read_bytes().removesuffix(b'\n').decode().encode('utf-16-le')+v[2*e['fim_utf16']:]
new=v.decode('utf-16-le').encode();assert sha(new)==m['aula_combinada_hipotetica_sha256']
math=lambda x:re.findall(rb'<math\b.*?</math>',x,re.S);article=lambda x:re.findall(rb'<article\b.*?</article>',x,re.S)
assert math(raw)==math(new) and len(math(raw))==734;assert article(raw)==article(new) and len(article(raw))==197
class Attr(HTMLParser):
 def __init__(self):super().__init__();self.rows=[]
 def handle_starttag(self,tag,attrs):
  a=tuple((k,v) for k,v in attrs if k in ('id','href','src') or k.startswith('aria-'))
  if a:self.rows.append((tag,a))
a=Attr();a.feed(raw.decode());b=Attr();b.feed(new.decode());assert a.rows==b.rows
form=(r/'formulas/termodinamica.html').read_bytes();assert sha(form)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02'
print(json.dumps({'ok':True,'edicoes':2,'substituicoes':3,'artigos_preservados':197,'mathml_preservados':734,'atributos_preservados':True,'formulario_nao_alterado':True,'aula_combinada_hipotetica_sha256':sha(new),'sem_escrita_em_produto':True}))
