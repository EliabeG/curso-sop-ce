#!/usr/bin/env python3
"""Identidade de fichas r12 e contas de teste fictícias; somente leitura."""
import hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[5]
html=(root/'formulas/termodinamica.html').read_bytes();inv=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r12.json').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(html)=='6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756'
assert sha(inv)=='457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e'
rows=json.loads((Path(__file__).parent/'identidades.json').read_text(encoding='utf-8')); assert [r['ficha'] for r in rows]==[87,88,91,92,93,94,95,97,98,99,100]
db=json.loads(inv)['ocorrencias']; h16=html.decode().encode('utf-16-le')
for r in rows:
 hits=[x for x in db if x['tipo']=='ficha_formula' and x['ancora']==r['ancora']];assert len(hits)==1
 for k in ['arquivo','ancora','inicio_utf16','fim_utf16','sha256_fragmento']:assert hits[0][k]==r[k]
 chunk=h16[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le').encode();assert sha(chunk)==r['sha256_fragmento'] and ('id="'+r['ancora']+'"').encode() in chunk
assert F(8,10)/1==F(4,5) and math.sqrt(1*16)==4  # 87–88
assert -2*(-10)==20 and 20*3==60                   # 91
assert F(2*3*50,F(1,2))==600                      # 92
assert 10*2*(50-20)==600                          # 93
assert F(8,10)*25==20 and 200*10*20==40000       # 94
total=F(1,100)+F(2,100)/2+F(1,200)+F(1,1000)
assert total==F(26,1000) and 1/total==F(500,13)   #95
assert F(8,10)/F(4,10)==2                         #97
assert F(12,1000000)*2*50==F(12,10000)            #98
assert 100000*F(1,100)==1000 and F(1000,10*2)==50 #99
assert 2*3*F(1,2)==3 and 2*3==6                  #100
print(json.dumps({'ok':True,'fichas':[r['ficha'] for r in rows],'U_W_m2_K':float(1/total),'limite':'Testes fictícios; juízo científico e hipótese de regime ainda aguardam Auditor.'},ensure_ascii=False,indent=2))
