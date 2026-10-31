#!/usr/bin/env python3
"""Simula propostas em memória, sem aplicar."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json,re
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';sha=lambda b:sha256(b).hexdigest();base=(q/'aplicacao-fun01-fases-r25-r1/resultado/depois-aula.html').read_bytes(); assert sha(base)=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e'
u=base.decode().encode('utf-16-le');ed=[]
for name,digest in [('escala','89c37950a565509a6e0d7d54e657f4fd9b6cb174a30429108bfd943e60f8ac89'),('parciais','ef267f6481e3377334309a593ae70b7853fff7254c653b294896c03ba3574e37'),('trabalho','5fee9a61920cfd5a93c0ed47049fbdd3de55676dc0742567ab77a4291d7c2960'),('fator','5bfadef7a0fb1052ffb7c1e09fdf78719464ec6ba61a5f040a4b969e6ed5c21b')]:
 d=q/f'candidata-fun02-{name}-r25-next-theory-20261030';mbytes=(d/'manifesto.json').read_bytes();assert sha(mbytes)==digest;m=json.loads(mbytes);a,z=m['inicio_utf16'],m['fim_utf16'];original=u[2*a:2*z].decode('utf-16-le');candidate=(d/'candidata.html').read_bytes().removesuffix(b'\n').decode();assert original.encode()==(d/'original.html').read_bytes().removesuffix(b'\n') and sha(original.encode())==m['original_sha256'] and sha(candidate.encode())==m['candidata_sha256']
 assert len(m['substituicoes'])==1;sub=m['substituicoes'][0];assert original.count(sub['antes'])==1 and original.replace(sub['antes'],sub['depois'],1)==candidate;ed.append((a,z,candidate,name))
for x,y in zip(sorted(ed),sorted(ed)[1:]):assert x[1]<=y[0]
v=u
for a,z,c,name in sorted(ed,reverse=True):v=v[:2*a]+c.encode('utf-16-le')+v[2*z:]
new=v.decode('utf-16-le').encode();assert len(re.findall(rb'<math\b.*?</math>',base,re.S))==734 and re.findall(rb'<math\b.*?</math>',base,re.S)==re.findall(rb'<math\b.*?</math>',new,re.S)
articles=lambda b:re.findall(rb'<article\b.*?</article>',b,re.S)
assert len(articles(base))==197 and articles(base)==articles(new)
class A(HTMLParser):
 def __init__(self):super().__init__();self.rows=[]
 def handle_starttag(self,tag,attrs):
  rel=tuple((k,v) for k,v in attrs if k in ('id','href','src') or k.startswith('aria-'))
  if rel:self.rows.append((tag,rel))
a=A();a.feed(base.decode());b=A();b.feed(new.decode());assert a.rows==b.rows
print(json.dumps({'ok':True,'candidatas':4,'artigos_preservados':197,'mathml_preservados':734,'atributos_iguais':True,'sha_combinado_hipotetico':sha(new),'nao_aplicado':True}))
