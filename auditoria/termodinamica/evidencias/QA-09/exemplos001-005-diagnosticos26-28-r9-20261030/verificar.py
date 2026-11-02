#!/usr/bin/env python3
"""QA-09: leitura e contas na fotografia r9. Não grava arquivos."""
from pathlib import Path
import hashlib,json
from decimal import Decimal, getcontext
getcontext().prec=28
root=Path(__file__).resolve().parents[5]
h=(root/'modulos/e1-termodinamica.html').read_bytes()
i=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_bytes()
sha=lambda b: hashlib.sha256(b).hexdigest()
assert sha(h)=='2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2'
assert sha(i)=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
j=json.loads(i); entries=[x for x in j['ocorrencias'] if x['tipo']=='exemplo_ou_diagnostico' and x['arquivo']=='modulos/e1-termodinamica.html']; selected=entries[:5]+[x for x in entries if x.get('diagnostico') in (26,27,28)]
expected=['6a992834b2c455d4432b96b0d885fc7092fa3c034ced4947c7b2738ff78de535','570d1bac8f5a29ec4350c974fbcc797810b3b5a6255f9a543c194c57eb9f96ae','0a78231e1675ba3b239b70b393c4136f645777d039bcfa5ba975b299c6426b39','25c4b655ec5aa4c0d743f6d52e378254643a4e06716b19b0333dbe515ab618f6','cf1e98634d3a42d137ab84e055555bb5bedb3962304fc7fbc8c58134a6b406c7','a82e00538d8a780dddb23b2699f75fb915b546c308c12fd5d44f6d62a74f1e1a','f464a072c29b5744c8fff6663d902628d84e5f8a28f51c68306f3a8a8e242962','d19ea80ff8c3ea479fc09548943bb1bed8c40d129ae265f24aec7f04cba162ed']
h16=h.decode('utf-8').encode('utf-16-le')
assert len(selected)==8
for x,ex in zip(selected,expected):
 frag=h16[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le').encode('utf-8');assert sha(frag)==x['sha256_fragmento']==ex,(x['inicio_utf16'],sha(frag),ex)
D=Decimal
rho=D(9)/D('.010');half=D('4.5')/D('.005');upper=D(-10)+D(120);inter=D(10)+D(30)/D(40)*(D(90)-D(10));quality=(D(900)-D(400))/(D(2400)-D(400));p=D(1)*D('.082')*D(320)/D('26.24');work=D(600)+D(900)-D(20);qin=D(2400)+D(800);reject=qin-work;eta=100*work/qin;y=(D(700)-D(300))/(D(2300)-D(300));flow=D(10)*(1-y);turbine=flow*D(250);dc=(D('.20')+D(500)*(D('.0004')-D('.0006')))/D(200);eq=D('.0004')+D('.20')/D(500)
assert [rho,half,upper,inter,quality,p,work,qin,reject,eta,y,flow,turbine,dc,eq]==list(map(D,['900','900','110','70','.25','1','1480','3200','1720','46.25','.20','8','2000','.0005','.0008']))
print(json.dumps({'ok':True,'itens':[{ 'tipo':'EX-'+str(k+1).zfill(3) if k<5 else 'DIAG-'+str(k+21), 'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256':x['sha256_fragmento']} for k,x in enumerate(selected)], 'limites':'Confronto de identidade e aritmética nominal; exige revisão independente de modelos e hipóteses.'},ensure_ascii=False,indent=2))
