#!/usr/bin/env python3
"""Recálculo analítico FUN-01; somente leitura."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
base=Path('.'); sources={'modulos/e1-termodinamica.html':'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2','auditoria/termodinamica/evidencias/QA-09/inventario-r9.json':'023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d','assets/termodinamica/fun01-dados-v1.json':'a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448','assets/termodinamica/fun01-calculos-v1.mjs':'a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88'}
for p,h in sources.items():assert sha256((base/p).read_bytes()).hexdigest()==h,p
h=(base/'modulos/e1-termodinamica.html').read_text().encode('utf-16-le')
for a,b,digest in [(111432,113604,'f2ad9153af7074ac31be0b322be23bf21a8450b3b98411b54961266c89ff94cc'),(119961,125802,'c6a2a5430bdee022dc9db6eb9d0e3c50c33086736b37154dd97d2749f53d4e53'),(125803,131220,'2fad0e042fb945eb44d0f2abe2c4e64322434195395fa4e5c084f17854f432a7')]:assert sha256(h[2*a:2*b].decode('utf-16-le').encode()).hexdigest()==digest
j=json.loads((base/'assets/termodinamica/fun01-dados-v1.json').read_text());m=j['mistura'];assert (m['T_K'],m['pA_sat_kPa'],m['pB_sat_kPa'])==(350,150,50)
A,B=F(150),F(50)
def pb(z):return z*A+(1-z)*B
def pd(z):return 1/(z/A+(1-z)/B)
def coexist(p):x=(p-B)/(A-B);return x,x*A/p
def beta(z,x,y):return (z-x)/(y-x)
z=F(2,5);p80=F(80);p100=F(100);x80,y80=coexist(p80);x100,y100=coexist(p100)
assert (pb(z),pd(z))==(90,F(750,11));assert (pb(F(4,5)),pd(F(4,5)))==(130,F(750,7));assert (x80,y80,beta(z,x80,y80))==(F(3,10),F(9,16),F(8,21)); assert beta(z,x100,y100)==F(-2,5);assert beta(F(4,5),x80,y80)==F(40,21)
b=beta(z,x80,y80); nV=10*b;nL=10*(1-b);assert nL*x80+nV*y80==4 and nL+nV==10
assert beta(F(35,100),x80,y80)==F(4,21) and beta(F(1,2),x80,y80)==F(16,21)
c=j['agua_critico'];assert (c['T_K'],c['p_MPa'])==(647.096,22.064);a=j['supercritico']['lotes'][0];assert (a['T_K']-a['erro_T_K'],a['T_K']+a['erro_T_K'])==(645,655);assert (F(str(a['p_MPa']))-F(str(a['erro_p_MPa'])),F(str(a['p_MPa']))+F(str(a['erro_p_MPa'])))==(F(22),F(111,5));assert F(650)-F('647.096')==F('2.904') and F('22.10')-F('22.064')==F('.036')
print(json.dumps({'ok':True,'p_bolha_z04_kPa':str(pb(z)),'p_orvalho_z04_kPa':float(pd(z)),'p_bolha_z08_kPa':str(pb(F(4,5))),'p_orvalho_z08_kPa':float(pd(F(4,5))),'composicoes_80_kPa':[str(x80),str(y80)],'beta_lote_II':str(b),'nV_mol':str(nV),'nL_mol':str(nL),'limites_erro_A':[2.904,.036],'limite':'Confronto dos modelos e artigos citados; origem da medição não é provada por igualdade recíproca.'},indent=2,ensure_ascii=False))
