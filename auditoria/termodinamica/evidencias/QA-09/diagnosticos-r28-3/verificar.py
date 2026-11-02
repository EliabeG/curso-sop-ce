#!/usr/bin/env python3
"""Reextrai e recalcula diagnósticos 1–5 na foto r27."""
from hashlib import sha256
from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
import re,json,math
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';sha=lambda b:sha256(b).hexdigest();raw=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes();assert sha(raw)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49';doc=raw.decode();u=doc.encode('utf-16-le');inv=(q/'inventario-r27.json').read_bytes();assert sha(inv)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c';o=json.loads(inv)
ids=[1,2,3,4,5];items=[]
for n in ids:
 matches=[x for x in o['ocorrencias'] if x.get('diagnostico')==n and x['tipo']=='exemplo_ou_diagnostico'];assert len(matches)==1;x=matches[0];frag=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(frag.encode())==x['sha256_fragmento'] and f'<h3>{n}.' in frag
 refs=re.findall(r'href="#([^"]+)"',frag)
 for name in refs:assert len(re.findall(r'\bid="'+re.escape(name)+r'"',doc))==1
 items.append({'numero':n,'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256':x['sha256_fragmento'],'links':refs})
assert -20+150==130 and abs(353.15/293.15-1.2046733754)<1e-9
assert F(30,100)/F(75,100)==F(2,5)
print(json.dumps({'ok':True,'fotografia':'r27','diagnosticos':items,'sem_escrita_em_produto':True},ensure_ascii=False,indent=2))
