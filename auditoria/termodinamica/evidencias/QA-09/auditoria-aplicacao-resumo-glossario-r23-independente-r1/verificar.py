#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-resumo-glossario-r23-r1/resultado'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f';assert sh(b)=='f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==2 and {z['id'] for z in ed}=={'resumo','glossario'}
for z in ed:
 p=q/('candidata-'+z['id']+'-r22-next-theory-20261030');old=rd(p/'original.html');new=rd(p/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256'] and a.count(old)==1;a=a.replace(old,new)
assert a==b
r0=rd(r/'antes-aula.html');u=r0.decode().encode('utf-16-le');v=b.decode().encode('utf-16-le');gl=next(x for x in ed if x['id']=='glossario');su=next(x for x in ed if x['id']=='resumo');assert su['inicio']-gl['fim']==1 and su['inicio_novo']-gl['fim_novo']==1 and u[2*gl['fim']:2*su['inicio']]==v[2*gl['fim_novo']:2*su['inicio_novo']]
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
assert len(arts(r0))==197 and arts(r0)==arts(b);assert len(maths(r0))==734 and maths(r0)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(r0) and ii['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r23.json'))=='ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e';assert sh(rd(q/'mapa-correspondencia-inventario-r22-r23-r1.json'))=='9a3c42d4f075f6a686b969a34d82ae439270fd50d49f25458b1d494caa205dd0'
assert F(500,1000+500)==F(1,3) and F(600,2)==300 and 1-F(300,600)==F(1,2)
print('OK: duas candidatas reproduzem r23 com unidade entre seções; 197 artigos/registros, 734 MathML e formulário; modelos/contrastes')
