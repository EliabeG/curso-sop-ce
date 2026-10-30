#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,math
q=Path('auditoria/termodinamica/evidencias/QA-09');p=q/'exemplos-006-020-r25-20261030/resultado.json'
def rd(p):return p.read_bytes()
def sh(x):return sha256(x).hexdigest()
assert sh(rd(p))=='609b9134b94e3acac6e3af33b222d2c692c30ea1ea8b8a40d333a7085e34c1ef';assert sh(rd(q/'inventario-r25.json'))=='6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116'
h=rd(Path('modulos/e1-termodinamica.html'));assert sh(h)=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e';raw=h.decode().encode('utf-16-le');inv=json.loads(rd(q/'inventario-r25.json'));rows=json.loads(rd(p))['identidades'];assert len(rows)==15
for n,e in enumerate(rows,6):
 assert e['id']==f'EX-{n:03d}';z=e['r25'];items=[v for v in inv['ocorrencias'] if v['tipo']=='exemplo_ou_diagnostico' and v['secao']==e['secao'] and v['inicio_utf16']==z['inicio'] and v['fim_utf16']==z['fim']];assert len(items)==1;f=raw[2*z['inicio']:2*z['fim']].decode('utf-16-le').encode();assert sh(f)==items[0]['sha256_fragmento']==z['sha256'];ctx=z['contexto'];c=raw[2*ctx['inicio']:2*ctx['fim']].decode('utf-16-le').encode();assert sh(c)==ctx['sha256']
assert F(3,2)*F(6,5)==F(9,5) and F(60,80)==F(3,4) and (7-5)*F(2,100)*1000==40
assert F(9,10)*200+F(1,10000)*(500**2-300**2)==196 and 3000-2600==400 and 2*400==800
assert -40-(-250)==210 and 50+100*F(42,10)-120==350 and -7-200*F(-20,1000)==-3
assert 300*(3-1)==600 and 100*(3-1)==200 and abs(.287*math.log(2)-.19893324)<1e-7
assert 2*F(42,10)*30==252 and F(252,1)/(F(8,10)*2)==F(315,2)
assert F(20+3*60,4)==50 and F(4*80+4*20+2*20,10)==44
assert F(1,2)*F(42,10)*20==42 and F(1,10)*334==F(167,5) and F(42,334)==F(21,167) and F(86,10)/(F(6,10)*F(42,10))==F(215,63)
assert F(14,10)*300==420
s2=math.log(2600/3000)+.287*math.log(100);s3=math.log(2000/3000)+.287*math.log(100);assert s2+s3>0 and 2*3000-(2600+2000)==1400
print('OK: 15 recortes/contextos r25, contas; contramodelo sintético de duas saídas fecha energia e Sger>0')
