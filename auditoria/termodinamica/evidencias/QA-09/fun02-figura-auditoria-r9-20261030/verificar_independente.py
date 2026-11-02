#!/usr/bin/env python3
"""Auditoria QA-09 de FUN-02: leitura e quadratura independentes; não grava."""
from pathlib import Path
from hashlib import sha256
import xml.etree.ElementTree as ET
import math,json
root=Path(__file__).resolve().parents[5]
checks={'modulos/e1-termodinamica.html':'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2','auditoria/termodinamica/evidencias/QA-09/inventario-r9.json':'023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d','assets/termodinamica/fun02-dados-v1.json':'511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319','assets/termodinamica/fun02-calculos-v1.mjs':'2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70','assets/termodinamica/fun02-caminhos-v1.svg':'f324acce9060eb15eeab58958649392f4e5b667fbaf2ad9b63e3c68fbe3eae35'}
for name,expected in checks.items():assert sha256((root/name).read_bytes()).hexdigest()==expected,name
inv=json.loads((root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_text()); data=json.loads((root/'assets/termodinamica/fun02-dados-v1.json').read_text());html=(root/'modulos/e1-termodinamica.html').read_text();h16=html.encode('utf-16-le');refs=[x for x in inv['referencias'] if x.get('ancora')=='fun02-dados' and x.get('valor','').endswith(('fun02-dados-v1.json','fun02-calculos-v1.mjs'))];assert len(refs)==2
for q in refs:
 sub=h16[2*q['inicio_utf16']:2*q['fim_utf16']].decode('utf-16-le');assert q['valor'] in sub
assert html.count('../assets/termodinamica/fun02-caminhos-v1.svg')==1 and 'id="fun02-e1-caminhos"' in html
R=data['gas']['R_JmolK']; n=data['gas']['n_mol']; ta=data['caminhos']['A']['T_K'];tb=data['caminhos']['B']['T_K'];va=data['caminhos']['A']['V_m3'];vb=data['caminhos']['B']['V_m3'];cv=n*R*data['gas']['cv_m_sobre_R'];pa=n*R*ta/va;pb=n*R*tb/vb;tc=ta*vb/va;pd=n*R*ta/vb
# quadratura independente de p(V), em L e kPa (equivalem a J)
N=10000; vl=va*1000;vr=vb*1000; step=(vr-vl)/N; f=lambda v:n*R*ta/v
w2=step/3*(f(vl)+f(vr)+sum((4 if i%2 else 2)*f(vl+i*step) for i in range(1,N)));w1=pa*(vb-va);du=cv*(tb-ta);cy=w1-w2
assert abs(pa/1000-249.42)<1e-9 and abs(pb/1000-187.065)<1e-9 and abs(pd/1000-124.71)<1e-9 and tc==600
assert abs(w1-2494.2)<1e-9 and abs(w2-1728.8476977526154)<1e-8 and abs(du-1870.65)<1e-9
assert round(du+w1,2)==4364.85 and round(du+w2,2)==3599.50 and round(cy,2)==765.35
svg=ET.parse(root/'assets/termodinamica/fun02-caminhos-v1.svg').getroot(); ns={'s':'http://www.w3.org/2000/svg'}
polygon=svg.find('.//s:polygon',ns);pts=[tuple(map(float,p.split(','))) for p in polygon.get('points').split()];pcoords=[(8+(x-90)*14/760,(455-y)*280/370) for x,y in pts];area=abs(sum(pcoords[i][0]*pcoords[(i+1)%len(pcoords)][1]-pcoords[(i+1)%len(pcoords)][0]*pcoords[i][1] for i in range(len(pcoords)))/2);assert abs(area-cy)<0.01
orange=next(e for e in svg.findall('.//s:polyline',ns) if e.get('class')=='orange');op=[tuple(map(float,p.split(','))) for p in orange.get('points').split()];assert len(op)==162
err=max(abs((455-y)*280/370-f(8+(x-90)*14/760)) for x,y in op[:-1]);assert err<0.001
texts=' '.join(''.join(e.itertext()) for e in svg.findall('.//s:text',ns));assert all(x in texts for x in ['2494,20 J','1728,85 J','765,35 J','A · 300 K','B · 450 K','C · 600 K','D · 300 K'])
print(json.dumps({'ok':True,'simpson_WII_J':w2,'WI_J':w1,'dU_J':du,'Wciclo_J':cy,'area_poligono_J_aproximada':area,'desvio_max_isoterma_kPa':err,'refs_externas':len(refs),'limites':'Análise restrita à figura e caso P1; não verifica P2/P3, navegador ou QA-09 integral.'},ensure_ascii=False,indent=2))
