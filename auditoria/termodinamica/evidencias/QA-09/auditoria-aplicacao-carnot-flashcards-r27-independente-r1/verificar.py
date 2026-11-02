#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-carnot-flashcards-r27-r1/resultado'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2';assert sh(b)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
ed=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(ed)==4
for z in ed:
 assert z['id'].startswith('QA-09-');p=q/z['id'].removeprefix('QA-09-');old=rd(p/'original.html');new=rd(p/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==z['original_sha256'] and sh(new)==z['candidata_sha256'] and a.count(old)==1;a=a.replace(old,new)
assert a==b
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
a0=rd(r/'antes-aula.html');assert len(arts(a0))==197 and arts(a0)==arts(b);assert len(maths(a0))==734 and maths(a0)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));ii=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==ii['itens'] and io['fonte']['sha256']==sh(a0) and ii['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r27.json'))=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c';assert sh(rd(q/'mapa-correspondencia-inventario-r26-r27-r1.json'))=='2eff0a63420831284ca726ed4efaadb436ffc6c976de151d2f70eb9e2e9790b4'
assert 1-F(300,600)==F(1,2) and F(300,100-20)==F(15,4)
assert F(30,40)==F(3,4) and F(30*1,40*2)==F(3,8)
print('OK: quatro candidatas, incluindo compressor r2, reproduzem r27; 197 artigos/registros, 734 MathML, formulário e exemplos')
