#!/usr/bin/env python3
"""Simula duas substituições em memória, sem gravar o produto."""
import hashlib,json,re
from fractions import Fraction as F
from html.parser import HTMLParser
from pathlib import Path
r=Path(__file__).resolve().parents[5];d=Path(__file__).parent;sha=lambda b:hashlib.sha256(b).hexdigest()
h=(r/'modulos/e1-termodinamica.html').read_bytes();inv=(r/'auditoria/termodinamica/evidencias/QA-09/inventario-r17.json').read_bytes();mb=(d/'manifesto.json').read_bytes()
assert sha(mb)=='69ebcc8cf1c091c20b040dc43c6bda0467124006b8802d28537b2ce3c1c84115';m=json.loads(mb)
assert sha(h)==m['aula_sha256'] and sha(inv)==m['inventario_r17_sha256'];s=h.decode();u=s.encode('utf-16-le');output=u
assert len(m['itens'])==2
for item in sorted(m['itens'],key=lambda x:x['inicio_utf16'],reverse=True):
 a=(d/(item['id']+'-original.html')).read_bytes().removesuffix(b'\n').decode();b=(d/(item['id']+'-candidata.html')).read_bytes().removesuffix(b'\n').decode()
 assert sha(a.encode())==item['original_sha256'] and sha(b.encode())==item['candidata_sha256']
 start=item['inicio_utf16'];end=item['fim_utf16'];assert u[2*start:2*end].decode('utf-16-le')==a and s.count(a)==1
 changed=a
 for delta in item['mudancas']:
  assert changed.count(delta['antes'])==1;changed=changed.replace(delta['antes'],delta['depois'],1)
 assert changed==b
 assert re.findall(r'<math\b.*?</math>',a,re.S)==re.findall(r'<math\b.*?</math>',b,re.S)
 output=output[:2*start]+b.encode('utf-16-le')+output[2*end:]
result=output.decode('utf-16-le');assert sha(result.encode())==m['aula_hipotetica_sha256']
assert re.findall(r'<math\b.*?</math>',s,re.S)==re.findall(r'<math\b.*?</math>',result,re.S) and len(re.findall(r'<math\b',s))==734
def articles(text):
 out={}
 for match in re.finditer(r'<article\b[^>]*>.*?</article>',text,re.S):
  idmatch=re.search(r'\bid="([^"]+)"',match.group().split('>',1)[0])
  if idmatch:out[idmatch.group(1)]=match.group()
 return out
old,new=articles(s),articles(result);items=json.loads(inv)['artigos_excluidos'];assert len(items)==197
for x in items: assert old[x['id']]==new[x['id']] and sha(old[x['id']].encode())==x['sha256_fragmento']
class Refs(HTMLParser):
 def __init__(self):super().__init__();self.tags=[];self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('a','img','script','link'):self.tags.append((tag,a.get('href'),a.get('src')))
  if 'id' in a:self.ids.append(a['id'])
a,b=Refs(),Refs();a.feed(s);b.feed(result);assert a.tags==b.tags and a.ids==b.ids
# Primeira lei: calor recebido pode coexistir com queda de U.
assert F(50)-F(100)==-50 and 400-F(100,F(718,1000))>0
# Entropia: duas temperaturas não equivalem à média aritmética.
assert F(100,300)+F(100,600)==F(1,2) and F(200,450)==F(4,9)
assert F(3,5)-F(1,2)==F(1,10) and F(3,5)-F(4,9)==F(7,45)
print(json.dumps({'ok':True,'blocos':2,'artigos':197,'mathml':734,'aula_hipotetica_sha256':m['aula_hipotetica_sha256'],'produto_gravado':False},ensure_ascii=False))
