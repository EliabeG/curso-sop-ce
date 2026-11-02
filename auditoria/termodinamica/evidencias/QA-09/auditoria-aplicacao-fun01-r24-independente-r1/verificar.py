#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re,math
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-fun01-combinada-r24-r1/resultado'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d';assert sh(b)=='2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
changes=[];original=None
for cat,expected in [('gases','797fe338ed7108cf2e3644868ffea7d7ce900bd88511dff26df8c79c6a996e1c'),('liquido','129a789ff993feb9419ea2a327bee46a83fd9acdb595f03d0ddde73a7246b027'),('gravidade','a6be90eb5c2cc40229f7807bacd90afc5e7d8db9d8807e4c4bdf4e5f5f6e2a61')]:
 p=q/f'candidata-fun01-{cat}-r23-next-theory-20261030'; mb=rd(p/'manifesto.json');assert sh(mb)==expected;m=json.loads(mb);old=rd(p/'original.html');new=rd(p/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==m['original_sha256'] and sh(new)==m['candidata_sha256'];assert original is None or original==old;original=old
 isolated=old
 for z in m['substituicoes']:
  x=z['antes'].encode();y=z['depois'].encode();assert old.count(x)==1;assert isolated.count(x)==1;isolated=isolated.replace(x,y);pos=old.index(x);changes.append((pos,pos+len(x),x,y))
 assert isolated==new
assert len(changes)==6; changes.sort();assert all(changes[i][1]<=changes[i+1][0] for i in range(5)); combined=original
for _,_,x,y in reversed(changes):assert combined.count(x)==1;combined=combined.replace(x,y)
assert sh(combined)=='9e6c7edc5562eba7c10143cd0af90d4b61a8f6398abe96ffb39031e9a5a4e736';assert a.count(original)==1 and a.replace(original,combined)==b
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
assert len(arts(a))==197 and arts(a)==arts(b);assert len(maths(a))==734 and maths(a)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a) and ii['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r24.json'))=='469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf';assert sh(rd(q/'mapa-correspondencia-inventario-r23-r24-r1.json'))=='63b3b5fc54566c617eb025458fec7dce979369dc180d01ec3bdc4a0ff31c9044'
assert 80*F(1,4)==160*F(1,8)==20 and 80*F(3,4)==60 and 160*F(7,8)==140
assert F(-1)+F(1,10)*10*2==1 and math.log(1)==0
print('OK: 3 manifestos, 6 edições disjuntas em um bloco, r24 reproduzida; 197 artigos/registros, 734 MathML, formulário e cálculos')
