from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,math
root=Path('.');f=root/'formulas/termodinamica.html'; inv=root/'auditoria/termodinamica/evidencias/QA-09/inventario-r10.json';ids=root/'auditoria/termodinamica/evidencias/QA-09/fichas-fundamentos-calorimetria-r10-20261030/identidades.json';
assert sha256(f.read_bytes()).hexdigest()=='01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9';assert sha256(inv.read_bytes()).hexdigest()=='3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c';assert sha256(ids.read_bytes()).hexdigest()=='c12c72cfeb39b0d91a18095d0178eaff9e67bf32e15e5d0d386cb561805eaa22'
utf=f.read_text().encode('utf-16-le'); arr=json.loads(ids.read_text());items=json.loads(inv.read_text())['ocorrencias'];assert len(arr)==12
for a in arr:
 start,end=a['inicio_utf16'],a['fim_utf16']; chunk=utf[start*2:end*2].decode('utf-16-le').encode();assert sha256(chunk).hexdigest()==a['sha256_fragmento']
 occ=[x for x in items if x['arquivo']=='formulas/termodinamica.html' and x['tipo']=='ficha_formula' and x['ancora']==a['ancora'] and x['inicio_utf16']==start and x['fim_utf16']==end and x['sha256_fragmento']==a['sha256_fragmento']];assert len(occ)==1
assert 55-80==-25 and F(120,60)==2 and (-20+100)==80 and F(200,F('0.01'))==20000
assert F(2,F('0.0025'))==800 and F('0.0025')/2==F(1,800) and F(200,2)==100 and F(300,2)==150 and F(4,2)==2
assert 150-(-50)==200 and (F(122-32,212-32)*100)==50 and 100+F(30,100)*100==130 and 2*4*10==80
assert F(20+3*60,4)==50 and F(4*20+12*60+2*20+60,4+12+2)==50
# Modelo exemplo: u=cv*T-a/v; Cv=1 kJ/(kg K), a=1 kJ*m^3/kg^2, v1=1, v2=2.
# Massa 1 kg, sistema isolado, sem trabalho, expansão livre; ΔU=0 define Tf=299,5 K.
cv=F(1);att=F(1);v1=F(1);v2=F(2);T1=F(300);T2=T1+att/cv*(1/v2-1/v1);assert T2==F(599,2)
u=lambda t,v:cv*t-att/v
assert u(T1,v1)==u(T2,v2) and cv*(T2-T1)==F(-1,2)
# P fase fixa =100 kPa, ΔV=.1m3, ΔH=200 kJ; Wb distinto 5 kJ se p_b=50kPa.
# Balanço algébrico mostra condição adicional para Q=ΔH; sem alegar processo real construído.
p=F(100);dv=F('0.1');dH=F(200);dU=dH-p*dv;W=F(50)*dv;Q=dU+W;assert (dU,W,Q,dH)==(190,5,195,200)
print(json.dumps({'ok':True,'fichas':len(arr),'Tf_expansao_livre_K':float(T2),'deltaU_kJ':str(u(T2,v2)-u(T1,v1)),'termo_C_deltaT_kJ':str(cv*(T2-T1)),'fase_algebra_Q_kJ':str(Q),'fase_algebra_deltaH_kJ':str(dH),'limites':'A hipótese de pressão de fronteira no cenário algébrico não estabelece por si só realização física; análise formal do balanço.'},ensure_ascii=False,indent=2))
