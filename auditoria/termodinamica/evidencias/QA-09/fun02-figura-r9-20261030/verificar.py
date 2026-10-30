#!/usr/bin/env python3
"""Verificação em leitura: dados autorais e coordenadas da figura FUN-02."""
from pathlib import Path
from hashlib import sha256
import json,math,xml.etree.ElementTree as ET
root=Path.cwd()
phtml=root/'modulos/e1-termodinamica.html'
pinv=root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json'
pdata=root/'assets/termodinamica/fun02-dados-v1.json'
psvg=root/'assets/termodinamica/fun02-caminhos-v1.svg'
pjs=root/'assets/termodinamica/fun02-calculos-v1.mjs'
expected={str(phtml.relative_to(root)):'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2',str(pinv.relative_to(root)):'023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d',str(pdata.relative_to(root)):'511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319',str(psvg.relative_to(root)):'f324acce9060eb15eeab58958649392f4e5b667fbaf2ad9b63e3c68fbe3eae35',str(pjs.relative_to(root)):'2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70'}
for p,h in expected.items():assert sha256((root/p).read_bytes()).hexdigest()==h,p
D=json.loads(pdata.read_text()); H=phtml.read_text(); inv=json.loads(pinv.read_text())
refs=[r for r in inv['referencias'] if r.get('valor','').endswith(('fun02-dados-v1.json','fun02-calculos-v1.mjs'))]
assert len(refs)==2 and all(r['ancora']=='fun02-dados' for r in refs)
assert H.count('../assets/termodinamica/fun02-caminhos-v1.svg')==1
n=D['gas']['n_mol']; R=D['gas']['R_JmolK'];A=D['caminhos']['A'];B=D['caminhos']['B'];PA=n*R*A['T_K']/A['V_m3']/1000; PB=n*R*B['T_K']/B['V_m3']/1000
C=A['T_K']*B['V_m3']/A['V_m3']; PD=n*R*A['T_K']/B['V_m3']/1000
W1=n*R*A['T_K']*(B['V_m3']/A['V_m3']-1); W2=n*R*A['T_K']*math.log(B['V_m3']/A['V_m3']); du=n*R*D['gas']['cv_m_sobre_R']*(B['T_K']-A['T_K']); wc=W1-W2
svg=ET.fromstring(psvg.read_bytes()); ns={'s':'http://www.w3.org/2000/svg'}
lines=svg.findall('.//s:polyline',ns); orange=next(e for e in lines if e.get('class')=='orange'); blue=next(e for e in lines if e.get('class')=='blue')
def points(e):return [tuple(map(float,p.split(','))) for p in e.get('points').split()]
ps=points(orange); assert len(ps)==162
# A-D has 161 quantized vertices; extra final B is isochoric, not an isotherm point.
xy_to_physical=lambda x,y:(8+(x-90)*14/760,(455-y)*280/370)
errs=[]
for px,py in ps[:-1]:
 v,p=xy_to_physical(px,py);errs.append(abs(p-n*R*A['T_K']/v))
assert max(errs)<0.001
assert abs(xy_to_physical(*ps[0])[0]-10)<1e-4
assert abs(xy_to_physical(*ps[-2])[0]-20)<1e-4
b=points(blue); assert len(b)==3
circles=svg.findall('.//s:circle',ns);assert len(circles)==4
expected_states=[(10,PA),(20,PB),(20,PA),(20,PD)]
for circle,(v,p) in zip(circles,expected_states):
 vv,pp=xy_to_physical(float(circle.get('cx')),float(circle.get('cy')));assert abs(vv-v)<1e-8 and abs(pp-p)<1e-8
for x in (W1,W2,wc):assert math.isfinite(x)
assert round(W1,2)==2494.20 and round(W2,2)==1728.85 and round(wc,2)==765.35
texts=' '.join((e.text or '') for e in svg.iter());assert all(t in texts for t in ('2494,20 J','1728,85 J','765,35 J','600 K','450 K'))
print(json.dumps({'ok':True,'pA_kPa':PA,'pB_kPa':PB,'pD_kPa':PD,'TC_K':C,'W_I_J':W1,'W_II_J':W2,'delta_U_J':du,'Q_I_J':du+W1,'Q_II_J':du+W2,'W_ciclo_J':wc,'pontos_isoterma':len(ps)-1,'erro_maximo_kPa':max(errs),'links_fora_artigos':refs,'escopo':'Exame isolado, pendente de revisão independente. Não há teste de navegador.'},ensure_ascii=False,indent=2))
