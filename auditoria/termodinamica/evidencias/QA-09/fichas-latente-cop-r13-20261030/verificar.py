#!/usr/bin/env python3
"""Confere identidades r13 e casos fictícios; somente leitura."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[5]
h=(root/'formulas/termodinamica.html').read_bytes();inv=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r13.json').read_bytes()
sha=lambda x:hashlib.sha256(x).hexdigest()
assert sha(h)=='5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285'
assert sha(inv)=='0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b'
rows=json.loads((Path(__file__).parent/'identidades.json').read_text(encoding='utf-8'));assert [r['ficha'] for r in rows]==[23,58,59]
db=json.loads(inv)['ocorrencias'];h16=h.decode().encode('utf-16-le')
for r in rows:
 hits=[x for x in db if x['tipo']=='ficha_formula' and x['ancora']==r['ancora']];assert len(hits)==1
 for k in ['arquivo','ancora','inicio_utf16','fim_utf16','sha256_fragmento']:assert r[k]==hits[0][k]
 c=h16[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le').encode();assert sha(c)==r['sha256_fragmento'] and ('id="'+r['ancora']+'"').encode() in c
hfg=2500-500; assert hfg==2000 and 2*hfg==4000 and F(6000,hfg)==3 # 23
assert 500-300==200 and F(200,500)==F(2,5)                          #58
assert F(600,200)==3                                                   #59
assert 500+50-300==250 and F(250,550)==F(5,11)                       #58: soma de entrada omitida
assert F(600,1000)==F(3,5)                                           #59: COP térmico hipotético
print(json.dumps({'ok':True,'fichas':[23,58,59],'limite':'Identidade e aritmética hipotética; hipóteses e revisão independente pendentes.'},ensure_ascii=False,indent=2))
