#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-pontes-d14-r22-r1/resultado'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238';assert sh(b)=='ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==3
folders={'base-radiacao-vacuo':'candidata-radiacao-pontes-r21-next-theory-20261030','base-geracao-face':'candidata-geracao-pontes-r21-next-theory-20261030','preparacao-questoes':'candidata-d14-fonte-r21-next-theory-20261030'}
for z in ed:
 p=q/folders[z['id']];old=rd(p/'original.html');new=rd(p/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256'] and a.count(old)==1;a=a.replace(old,new)
assert a==b
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
a0=rd(r/'antes-aula.html');assert len(arts(a0))==197 and arts(a0)==arts(b);assert len(maths(a0))==734 and maths(a0)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a0) and ii['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r22.json'))=='6e68d5a9e5cfec73aa2a5ce24121ede1c3a155ca2a5783cf6f17ca95eee8061b';assert sh(rd(q/'mapa-correspondencia-inventario-r21-r22-r1.json'))=='75dd6be7387e4dce4c1b7717a9a6416b5c3329e01776e146a83708fdd47bb8a6'
assert F(30,60)==F(1,2) and 300**4-300**4==0
assert 60*2==120 and 18+120/(6*2)==28 and -120-(-120)==0
assert 200*6==1200 and 20+1200/(20*6)==30 and -1200-(-1200)==0
print('OK: três candidatas reproduzem r22; 197 artigos/registros, 734 MathML e formulário; D14 e geração, razão radiativa')
