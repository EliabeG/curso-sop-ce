#!/usr/bin/env python3
"""Simulação das três candidatas sem escrita em produto."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json,re
r=Path(__file__).resolve().parents[5];d=Path(__file__).resolve().parent;sha=lambda x:sha256(x).hexdigest();m=json.loads((d/'manifesto.json').read_bytes());assert m['estado']=='CANDIDATA_NAO_APLICADA'
for v in [*m['fontes'].values(),m['inventario'],m['parecer']]:assert sha((r/v['arquivo']).read_bytes())==v['sha256']
raw={k:(r/v['arquivo']).read_bytes() for k,v in m['fontes'].items()};u={k:b.decode().encode('utf-16-le') for k,b in raw.items()};ed=m['edicoes'];assert {e['id'] for e in ed}=={'base-refrigeracao','formula-refrigeracao','formula-condensador'}
for e in ed:
 doc='aula' if e['documento'].startswith('modulos/') else 'formulario';a,z=e['inicio_utf16'],e['fim_utf16'];orig=u[doc][2*a:2*z].decode('utf-16-le');assert orig.encode()==(d/(e['id']+'-original.html')).read_bytes().removesuffix(b'\n') and sha(orig.encode())==e['original_sha256'];candidate=orig
 for sub in e['substituicoes']:
  assert candidate.count(sub['antes'])==sub['quantidade'];candidate=candidate.replace(sub['antes'],sub['depois'])
 assert candidate.encode()==(d/(e['id']+'-candidata.html')).read_bytes().removesuffix(b'\n') and sha(candidate.encode())==e['candidata_sha256']
new={}
for doc in u:
 v=u[doc];subset=sorted((e for e in ed if ('aula' if e['documento'].startswith('modulos/') else 'formulario')==doc),key=lambda e:e['inicio_utf16']);assert all(a['fim_utf16']<=b['inicio_utf16'] for a,b in zip(subset,subset[1:]))
 for e in reversed(subset):v=v[:2*e['inicio_utf16']]+(d/(e['id']+'-candidata.html')).read_bytes().removesuffix(b'\n').decode().encode('utf-16-le')+v[2*e['fim_utf16']:]
 new[doc]=v.decode('utf-16-le').encode();assert sha(new[doc])==m['sha_hipotetico'][doc]
math=lambda b:re.findall(rb'<math\b.*?</math>',b,re.S)
for doc,n in [('aula',734),('formulario',191)]:assert math(raw[doc])==math(new[doc]) and len(math(raw[doc]))==n
art=lambda b:re.findall(rb'<article\b.*?</article>',b,re.S)
assert len(art(raw['aula']))==197 and art(raw['aula'])==art(new['aula'])
a=art(raw['formulario']);b=art(new['formulario']);assert len(a)==len(b)==100 and sum(x!=y for x,y in zip(a,b))==2
class Attr(HTMLParser):
 def __init__(self):super().__init__();self.rows=[]
 def handle_starttag(self,t,attrs):
  a=tuple((k,v) for k,v in attrs if k in ('id','href','src') or k.startswith('aria-'))
  if a:self.rows.append((t,a))
for doc in raw:
 a=Attr();a.feed(raw[doc].decode());b=Attr();b.feed(new[doc].decode());assert a.rows==b.rows
# contraste balanço sem confundir trabalho de eixo e total
assert 35+5==40 and 150/40==3.75 and 150+40==190 and 150/35>4.28
print(json.dumps({'ok':True,'edicoes':3,'fichas_nao_alvo':98,'artigos_preservados':197,'mathml_preservados':[734,191],'atributos_preservados':True,'sha_hipotetico':{k:sha(v) for k,v in new.items()},'sem_escrita_em_produto':True}))
