#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-conjunta-r18-r1/resultado';t=q/'candidatas-primeira-lei-entropia-r17-20261030-r2'; f=q/'candidatas-ficha60-ex027-r17-20261030'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');aa=rd(r/'depois-aula.html');b=rd(r/'antes-formulario.html');bb=rd(r/'depois-formulario.html')
assert sh(a)=='6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c';assert sh(aa)=='7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca' and aa==rd(Path('modulos/e1-termodinamica.html'))
assert sh(b)=='dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d';assert sh(bb)=='463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895' and bb==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==4
for z in ed:
 id=z['id']; p=t if id.startswith('base-') else f; old=rd(p/(id+'-original.html'));new=rd(p/(id+'-candidata.html'));assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256']
 if id=='ficha60':assert b.count(old)==1;b=b.replace(old,new)
 else:assert a.count(old)==1;a=a.replace(old,new)
assert a==aa and b==bb
art=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S)
m=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
a0=rd(r/'antes-aula.html');b0=rd(r/'antes-formulario.html');assert len(art(a0))==197 and art(a0)==art(aa);assert len(art(b0))==len(art(bb))==100 and sum(x!=y for x,y in zip(art(b0),art(bb)))==1
assert len(m(a0))==734 and m(a0)==m(aa) and len(m(b0))==191 and m(b0)==m(bb)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'];assert io['fonte']['sha256']==sh(a0) and ii['fonte']['sha256']==sh(aa)
assert sh(rd(q/'inventario-r18.json'))=='717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc';assert sh(rd(q/'mapa-correspondencia-inventario-r17-r18-r1.json'))=='54ef57e0479f4a8143fd5c7fde4021e45330d0125da939b02bc08fe3855ac1a7'
assert 50-100==-50 and F(100,300)+F(100,600)==F(1,2) and F(200,450)==F(4,9) and F(6,10)-F(1,2)==F(1,10)
assert 1000-600==400 and F(400,1000)==F(2,5);assert 100-20==80 and 300+80==380 and F(300,80)==F(15,4) and F(380,80)==F(19,4)
print('OK: quatro candidatos reproduzem r18; 197 artigos/itens, 99 fichas, 734/191 MathML; balanços e entropia conferem')
