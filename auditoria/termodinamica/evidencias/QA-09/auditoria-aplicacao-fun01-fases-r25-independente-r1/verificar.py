#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-fun01-fases-r25-r1/resultado';p=q/'candidata-fun01-fases-r24-next-theory-20261030'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9';assert sh(b)=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==1 and ed[0]['id']=='fun01-fases';old=rd(p/'original.html');new=rd(p/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==ed[0]['original_sha256'] and sh(new)==ed[0]['candidata_sha256'] and a.count(old)==1 and a.replace(old,new)==b
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
assert len(arts(a))==197 and arts(a)==arts(b);assert len(maths(a))==734 and maths(a)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a) and ii['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r25.json'))=='6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116';assert sh(rd(q/'mapa-correspondencia-inventario-r24-r25-r1.json'))=='2b39fde214b9e058e740fb0140f6c40105d5a710fe366ac8f147ce9ba59e4100'
x=F(150-100,400-100);y=x*F(400,150);z=F(1,4);assert x==F(1,6) and y==F(4,9) and (z-x)/(y-x)==F(3,10)
assert (x-x)/(y-x)==0 and (y-x)/(y-x)==1
for beta in (F(0),F(1,5),F(1,2),F(1)):
 assert (1-beta)*F(0)+beta*F(0)==0
w=F(1,2);ml=20;mv=40;assert (w/mv)/(w/mv+(1-w)/ml)==F(1,3)
print('OK: substituição reproduz r25; 197 artigos/registros, 734 MathML/formulário; alavanca, extremos, degenerescência e conversão mássica/molar')
