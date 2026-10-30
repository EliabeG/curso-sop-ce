#!/usr/bin/env python3
"""Reextrai e recalcula diagnósticos 6–10 e 21–25 na foto r27."""
from hashlib import sha256
from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
import re,json,math
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';sha=lambda b:sha256(b).hexdigest();raw=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes();assert sha(raw)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49';doc=raw.decode();u=doc.encode('utf-16-le');inv=(q/'inventario-r27.json').read_bytes();assert sha(inv)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c';o=json.loads(inv)
ids=[6,7,8,9,10,21,22,23,24,25];items=[]
for n in ids:
 matches=[x for x in o['ocorrencias'] if x.get('diagnostico')==n and x['tipo']=='exemplo_ou_diagnostico'];assert len(matches)==1;x=matches[0];frag=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(frag.encode())==x['sha256_fragmento'] and f'<h3>{n}.' in frag
 refs=re.findall(r'href="#([^"]+)"',frag)
 for name in refs:assert len(re.findall(r'\bid="'+re.escape(name)+r'"',doc))==1
 items.append({'numero':n,'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256':x['sha256_fragmento'],'links':refs})
assert -30-(-180)==150 and 500+150==650 and F(300,900)==F(1,3) and 900*F(300,900)==300
assert 280*F(15,100)==42 and F(1,1000)*600==F(6,10)
assert F(125,100)*320==400 and F(80,100)*100+F(1,2000)*(400**2-300**2)==115
assert F(2*100+400,3)==200 and F(2*100+400+30,3)==210
assert 100**2+2000*75==400**2 and round(math.sqrt(150000),2)==387.30
assert F(1000-500,2500-500)==F(1,4) and F(2700-500,2500-500)==F(11,10)
print(json.dumps({'ok':True,'fotografia':'r27','diagnosticos':items,'sem_escrita_em_produto':True},ensure_ascii=False,indent=2))
