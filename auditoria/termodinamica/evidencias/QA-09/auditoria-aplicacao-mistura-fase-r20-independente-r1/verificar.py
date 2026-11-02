#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-mistura-fase-r20-r1/resultado'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65'
assert sh(b)=='b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==2
for z in ed:
 name=z['id'];folder='candidata-mistura-termica-r19-20261030' if name=='base-mistura-termica' else 'candidata-fase-calorimetria-r19-20261030';p=q/folder;old=rd(p/'original.html');new=rd(p/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256'] and a.count(old)==1;a=a.replace(old,new)
assert a==b
articles=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S)
maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
a0=rd(r/'antes-aula.html');assert len(articles(a0))==197 and articles(a0)==articles(b);assert len(maths(a0))==734 and maths(a0)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a0) and ii['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r20.json'))=='e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4';assert sh(rd(q/'mapa-correspondencia-inventario-r19-r20-r1.json'))=='324337242a6e59422c64a72565ecc0c555a3122511f1d24cd55f8343df12ec53'
assert F(2*90+6*30,8)==45 and F(4*80+4*20+2*20-20,10)==42
assert F(1,2)*F(42,10)*20==42 and F(1,5)*334==F(334,5) and F(42,334)==F(21,167)
print('OK: duas candidatas reproduzem r20; 197 artigos e registros, 734 MathML e formulário; cálculos de mistura/fusão')
