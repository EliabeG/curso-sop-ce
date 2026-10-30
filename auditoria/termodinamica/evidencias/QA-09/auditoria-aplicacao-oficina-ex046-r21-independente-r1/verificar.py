#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-oficina-ex046-r21-r1/resultado'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7'
assert sh(b)=='239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==2
for z in ed:
 id=z['id']; p=q/('candidata-ex046-r20-20261030-r3' if id=='ex046' else 'candidata-entropia-oficina-r20-20261030');old=rd(p/'original.html');new=rd(p/'candidata.html')
 if id!='ex046': assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1]
 assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256'] and a.count(old)==1;a=a.replace(old,new)
assert a==b
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
a0=rd(r/'antes-aula.html');assert len(arts(a0))==197 and arts(a0)==arts(b);assert len(maths(a0))==734 and maths(a0)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a0) and ii['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r21.json'))=='d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1';assert sh(rd(q/'mapa-correspondencia-inventario-r20-r21-r1.json'))=='6930666290d17dc5fc1d7c1375d4bf1a454d5a509d4578be691b58f463cdb99c'
assert 200*3*2*1==1200 and 20+1200/(20*6)==30 and -1200-(-1200)==0
assert 900-300==600 and F(300,900)==F(1,3) and 1-F(300,500)==F(2,5) and F(600,300)-F(900,500)==F(1,5)
print('OK: duas candidatas reproduzem r21; 197 artigos/registros, 734 MathML, formulário; balanços de EX046 e oficina')
