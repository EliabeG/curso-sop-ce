#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json, math
q=Path('auditoria/termodinamica/evidencias/QA-09');i=q/'exemplos-021-030-r17-20261030/resultado.json'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
assert sh(rd(i))=='e906843d39c1f6689a6dc79f1df3f7b40922c056afa12b75b3fece430720ba71'
x=json.loads(rd(i));h=rd(Path('modulos/e1-termodinamica.html'));assert sh(h)=='6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c';raw=h.decode().encode('utf-16-le'); inv=json.loads(rd(q/'inventario-r17.json'));assert sh(rd(q/'inventario-r17.json'))=='b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b';assert len(x['identidades'])==10
for n,item in enumerate(x['identidades'],21):
 assert item['id']==f'EX-{n:03d}';r=item['r17'];obj=inv['ocorrencias'][r['indice']];assert obj['tipo']=='exemplo_ou_diagnostico' and obj['secao']==item['secao'] and obj['inicio_utf16']==r['inicio'] and obj['fim_utf16']==r['fim'];z=raw[2*r['inicio']:2*r['fim']].decode('utf-16-le').encode();assert sh(z)==r['fragmento']==obj['sha256_fragmento'];ctx=r['contexto'];part=raw[2*ctx['inicio']:2*ctx['fim']].decode('utf-16-le').encode();assert sh(part)==ctx['sha256']
assert F(100+3*300,4)==250 and math.isclose(math.sqrt(50**2+2*40000),287.2281323269,abs_tol=1e-9)
assert F(950-400,2600-400)==F(1,4) and F(1)-F(400,800)==F(1,2)
assert F(120,400)-F(600,800)==F(-9,20) and F(290)*F(1,10)==29 and F(1,1000)*800==F(4,5)
assert 1000-600==400 and F(400,1000)==F(2,5) and F(600,200)==3 and F(800,200)==4
assert F(90-30,150)==F(2,5) and F(90-45,150)==F(3,10) and F(400-300,400)==F(1,4) and F(120,400)==F(3,10) and F(120,300)==F(2,5)
assert 1000+200-600==600 and F(600,300)-F(1000,800)-F(200,600)==F(5,12)
print('OK: dez identidades e contextos r17, recálculos e contramodelo EX027 (Sger=5/12 kJ/K)')
