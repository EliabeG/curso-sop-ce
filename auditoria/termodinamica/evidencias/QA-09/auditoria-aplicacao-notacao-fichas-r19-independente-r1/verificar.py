#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-notacao-fichas-r19-r1/resultado';t=q/'candidata-notacao-propriedades-r18-20261030';f=q/'candidatas-fichas-61-80-r18-20261030'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');aa=rd(r/'depois-aula.html');b=rd(r/'antes-formulario.html');bb=rd(r/'depois-formulario.html')
assert sh(a)=='7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca';assert sh(aa)=='9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65' and aa==rd(Path('modulos/e1-termodinamica.html'))
assert sh(b)=='463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895';assert sh(bb)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58' and bb==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==3
for z in ed:
 id=z['id']; p=t if id=='base-propriedades' else f; prefix='' if id=='base-propriedades' else ('61-' if id=='formula-carnot' else '80-');old=rd(p/(prefix+'original.html'));new=rd(p/(prefix+'candidata.html'));assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256']
 if id=='base-propriedades':assert a.count(old)==1;a=a.replace(old,new)
 else:assert b.count(old)==1;b=b.replace(old,new)
assert a==aa and b==bb
articles=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S)
maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
a0=rd(r/'antes-aula.html');b0=rd(r/'antes-formulario.html');assert len(articles(a0))==197 and articles(a0)==articles(aa);assert len(articles(b0))==len(articles(bb))==100 and sum(x!=y for x,y in zip(articles(b0),articles(bb)))==2
assert len(maths(a0))==734 and maths(a0)==maths(aa) and len(maths(b0))==191 and maths(b0)==maths(bb)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a0) and ii['fonte']['sha256']==sh(aa)
assert sh(rd(q/'inventario-r19.json'))=='ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f';assert sh(rd(q/'mapa-correspondencia-inventario-r18-r19-r1.json'))=='42c39e8093294c19a12526262140056fc0e2da71120c48e142cab3cd06ed9be5'
assert 1-F(300,600)==F(1,2) and F(300,600-300)==1 and F(600,600-300)==2
assert 1000+100-600==500 and F(600,300)-F(1000,800)-F(100,600)==F(7,12) and F(500,1100)==F(5,11)
print('OK: três candidatos reproduzem r19; 197 artigos e registros, 98 fichas, 734/191 MathML e contramodelo de energia conferem')
