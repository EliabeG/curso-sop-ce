#!/usr/bin/env python3
"""Conferência independente e somente leitura dos seis blocos e contramodelos."""
import hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[5]
sha = lambda b: hashlib.sha256(b).hexdigest()
hb=(root/'auditoria/termodinamica/evidencias/QA-09/aplicacao-wika-r15-r1/resultado/depois-aula.html').read_bytes()
ib=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r15.json').read_bytes()
assert sha(hb)=='f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e'
assert sha(ib)=='c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c'
u=hb.decode().encode('utf-16-le')
blocks=[('base-eficiencia-cop',299262,308797,'d69c923666e5cbc712349c4dfe9e6a18f3ffdd7b5f6fe271dc745b29238c44f9'),('base-limite-carnot',308797,315231,'382a2daf360ad0a04bfb9245f0746d547d8f5fa2d28e6b5b93d53621cb96bcfd'),('base-refrigeracao',365081,377906,'2221e77dbbfa11591bcfac47c254e42941ab8074da717ac90975118425277955'),('base-brayton-real',377906,381233,'ff66d7377eff5357668aae739c6390e23a38ad954acdd1b6af92447575e944a0'),('base-comparar-ciclos',381233,382466,'adfa898e638f94b9eedc18ad7da9881f8bdb8c601bf51a30b8d61422f389f2bd'),('base-ciclos-variantes',382466,387076,'7628014cf26268ba5dd27b7647ac9f89210ea977eba53e556e7c4efd8cd28198')]
for anchor,start,end,digest in blocks:
    f=u[2*start:2*end].decode('utf-16-le')
    assert sha(f.encode())==digest and f'id="{anchor}"' in f
    assert len([x for x in json.loads(ib)['ocorrencias'] if x.get('ancora')==anchor and x.get('tag')=='h3']) == 1
# Carnot: os dois exemplos sintéticos respeitam balanço de energia e Sgen >= 0.
assert F(200,400-200)==1 and F(300,400-300)==3
for tl,ql in [(200,F(9,10)),(300,F(3,5))]:
    w=F(1); qh=ql+w; assert qh/F(400)-ql/F(tl)>0
assert F(3,5)<F(9,10)
# Absorção com três reservatórios: energia e produção total de entropia positivas.
assert 600+1000+40==1640
assert F(1640,300)-F(600,270)-F(1000,500)>0
assert F(600,1000)==F(3,5) and F(600,40)==15
# Turbina com q recebido a 2000 K; contramodelo em gás ideal com c_p=1.
R=.287; pressure_ratio=.7**(1/R)
ds=math.log(.8)-R*math.log(pressure_ratio)
assert abs(ds-math.log(8/7))<1e-12 and ds-.1>0
assert (1000-800)+200==400 and 1000-700==300
# Demais contas exatas e arredondamento.
assert F(90-30,150)==F(2,5) and F(90-45,150)==F(3,10)
assert F(400-300,400)==F(1,4) and F(120,400)==F(3,10) and F(120,300)==F(2,5)
assert (3100-2500)+(3200-2200)-(210-200)==(3100-210)+(3200-2500)-(2200-200)==1590
assert round(F(1590,3590)*100,2)==F(4429,100)
assert abs(F(290,2490)-F(1165,10000))<F(1,20000)
assert F(600,200)==3 and F(600+200,200)==4
print(json.dumps({'ok':True,'blocos':len(blocks),'escopo':'identidade e recálculo; leitura e hipótese no parecer'},ensure_ascii=False))
