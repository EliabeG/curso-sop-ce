#!/usr/bin/env python3
"""Fotografia r10 e testes aritméticos de fichas 47–56; somente leitura."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[5]
html=(root/'formulas/termodinamica.html').read_bytes()
inv=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r10.json').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(html)=='01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9'
assert sha(inv)=='3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c'
rows=json.loads((Path(__file__).parent/'identidades.json').read_text(encoding='utf8'));assert [r['ficha'] for r in rows]==list(range(47,57))
db=json.loads(inv)['ocorrencias']; h16=html.decode().encode('utf-16-le')
for r in rows:
 hits=[x for x in db if x['tipo']=='ficha_formula' and x['ancora']==r['ancora']];assert len(hits)==1
 for k in ['arquivo','ancora','inicio_utf16','fim_utf16','sha256_fragmento']: assert hits[0][k]==r[k]
 chunk=h16[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le').encode()
 assert sha(chunk)==r['sha256_fragmento'] and ('id="'+r['ancora']+'"').encode() in chunk
assert 2*100==1*200                             # 47 kW
assert 3-1==2                                   # 48 kg/s
assert 20-10+2*100-1*50==160                  # 49 kW
assert 20-10+3*100-1*50==260                  # 50 kJ
assert F(5,4)*320==400                        # 51 K
assert (F(1,100)-30*(F(6,10000)-F(4,10000)))/300==F(1,75000) # 52 fração/h
assert F(1,100)/(F(14,10000)-F(4,10000))==10 # 53 m3/h
assert 600/300==2                             # 54 h−1
assert 1000*F(981,100)*F(1,100)*20==1962 and F(1962,2616)==F(3,4) # 55 W
assert F(2*100+400,3)==200 and F(30+2*100+400,3)==210 # 56 kJ/kg
print(json.dumps({'ok':True,'fichas':list(range(47,57)), 'limite':'Teste fictício, não extrai fórmulas nem aprova QA-09.'},ensure_ascii=False,indent=2))
