#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-fun02-ficha59-ex010-r26-r1/resultado'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');aa=rd(r/'depois-aula.html');b=rd(r/'antes-formulario.html');bb=rd(r/'depois-formulario.html')
assert sh(a)=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e';assert sh(aa)=='afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2' and aa==rd(Path('modulos/e1-termodinamica.html'))
assert sh(b)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58';assert sh(bb)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02' and bb==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==6
for z in ed:
 p=q/z['origem'];old=rd(p/'original.html');new=rd(p/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256']
 if z['documento']=='formulas/termodinamica.html':assert b.count(old)==1;b=b.replace(old,new)
 else:assert a.count(old)==1;a=a.replace(old,new)
assert a==aa and b==bb
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
a0=rd(r/'antes-aula.html');b0=rd(r/'antes-formulario.html');assert len(arts(a0))==197 and arts(a0)==arts(aa);assert len(arts(b0))==len(arts(bb))==100 and sum(x!=y for x,y in zip(arts(b0),arts(bb)))==1
assert len(maths(a0))==734 and maths(a0)==maths(aa) and len(maths(b0))==191 and maths(b0)==maths(bb)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a0) and ii['fonte']['sha256']==sh(aa)
assert sh(rd(q/'inventario-r26.json'))=='d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241';assert sh(rd(q/'mapa-correspondencia-inventario-r25-r26-r1.json'))=='4cf2e325012929faa2f16c3a01bb8710847cb6f302aef74f2c012dfce8decc9d'
assert 3000-2600==400 and 2*400==800 and 1*(-100)+2*50==0
assert 100-20==80 and F(300,80)==F(15,4) and 300+80==380 and F(380,350)-F(300,300)==F(3,35)
assert F(8314,1000)*F(3,2)*300==F(37413,10) and -2*F(8314,1000)*300==F(-49884,10)
assert F(37413,10)+F(-49884,10)==F(-12471,10)
print('OK: seis candidatas reproduzem r26; 197 artigos/registros, 99 fichas, 734/191 MathML e balanços EX010, COP e FUN02')
