#!/usr/bin/env python3
"""Reconstituição independente das candidatas sem alterar produto."""
import hashlib,json,re
from fractions import Fraction as F
from pathlib import Path
r=Path(__file__).resolve().parents[5];p=r/'auditoria/termodinamica/evidencias/QA-09/candidatas-ficha60-ex027-r17-20261030';sha=lambda b:hashlib.sha256(b).hexdigest()
mb=(p/'manifesto.json').read_bytes();assert sha(mb)=='4a61b863e2acfe76c043d58322e695ad2139653199240737b56ed0c5c70c1c92';m=json.loads(mb)
inv=(r/'auditoria/termodinamica/evidencias/QA-09/inventario-r17.json').read_bytes();assert sha(inv)==m['fotografia']['inventario_sha256']
for x in m['itens']:
 source=(r/x['arquivo']).read_bytes();key='aula_sha256' if x['id']=='ex027' else 'formulario_sha256';assert sha(source)==m['fotografia'][key]
 orig=(p/(x['id']+'-original.html')).read_bytes().removesuffix(b'\n').decode();cand=(p/(x['id']+'-candidata.html')).read_bytes().removesuffix(b'\n').decode()
 assert sha(orig.encode())==x['original_sha256'] and sha(cand.encode())==x['candidata_sha256']
 u=source.decode().encode('utf-16-le');assert u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le')==orig
 result=orig
 for edit in x['mudancas']:
  assert result.count(edit['antes'])==edit['ocorrencias'];result=result.replace(edit['antes'],edit['depois'])
 assert result==cand and re.findall(r'<math\b.*?</math>',orig,re.S)==re.findall(r'<math\b.*?</math>',cand,re.S)
 out=u[:2*x['inicio_utf16']]+cand.encode('utf-16-le')+u[2*x['fim_utf16']:];h=out.decode('utf-16-le').encode()
 expected={'ficha60':'463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895','ex027':'36d46e4d240a5a79732faac3d7d2a7a0eab813ca01ac8cb3dd9d16552bb51f53'}
 assert sha(h)==expected[x['id']]
 # Reversão do bloco candidato recupera todo o documento anterior.
 assert h.decode().count(cand)==1 and h.decode().replace(cand,orig,1).encode()==source
assert F(100-20)==80 and F(300,80)==F(15,4) and F(380,80)==F(19,4)==1+F(15,4)
assert F(380,350)-F(300,300)==F(3,35)>0
assert F(380,100)==F(19,5) and 1000-600==400 and F(400,1000)==F(2,5)
assert 1000+200-600==600 and F(600,300)-F(1000,800)-F(200,600)==F(5,12)>0
print(json.dumps({'ok':True,'candidatas':2,'contrastes':'energia e entropia','produto_gravado':False},ensure_ascii=False))
