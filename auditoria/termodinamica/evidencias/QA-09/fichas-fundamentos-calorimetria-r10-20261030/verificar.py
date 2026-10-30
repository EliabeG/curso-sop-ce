#!/usr/bin/env python3
"""QA-09: identidade e aritmética ilustrativa; não escreve arquivos."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[5]
html=(root/'formulas/termodinamica.html').read_bytes()
inv=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r10.json').read_bytes()
sha=lambda x:hashlib.sha256(x).hexdigest()
assert sha(html)=='01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9'
assert sha(inv)=='3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c'
rows=json.loads((Path(__file__).parent/'identidades.json').read_text(encoding='utf8'));assert [r['ficha'] for r in rows]==[1,2,5,6,7,8,9,24,26,27,28,29]
db=json.loads(inv)['ocorrencias'];h16=html.decode().encode('utf-16-le')
for r in rows:
 hits=[x for x in db if x['tipo']=='ficha_formula' and x['ancora']==r['ancora']];assert len(hits)==1
 for k in ['arquivo','ancora','inicio_utf16','fim_utf16','sha256_fragmento']:assert hits[0][k]==r[k]
 chunk=h16[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le').encode()
 assert sha(chunk)==r['sha256_fragmento'] and ('id="'+r['ancora']+'"').encode() in chunk
assert 55-80==-25 and 2*60==120
assert -20+100==80 and F(200,1)/F(1,100)==20000
assert F(2,1)/F(25,10000)==800 and F(1,800)==F(125,100000)
assert F(200,2)==100 and F(300,2)==150 and F(4,2)==2
assert 150-(-50)==200 and F(100,180)*(122-32)==50
assert 100+F(30,100)*(200-100)==130 and 2*4*10==80
assert F(1*20+3*60,4)==50
assert F(4*20+12*60+2*20+60,18)==50 and 2*200==400
print(json.dumps({'ok':True,'fichas':[r['ficha'] for r in rows], 'limite':'Identidade e testes fictícios; não é auditoria independente.'},ensure_ascii=False,indent=2))
