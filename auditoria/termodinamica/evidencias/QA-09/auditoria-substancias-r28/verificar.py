from pathlib import Path
from hashlib import sha256
from math import log
from decimal import Decimal
q=Path('auditoria/termodinamica/evidencias/QA-09');H=lambda b:sha256(b).hexdigest()
p=Path('modulos/e1-termodinamica.html');b=p.read_bytes();assert H(b)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'
assert H((q/'inventario-r27.json').read_bytes())=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
assert H((q/'graficos-r28-lote2/entrega.md').read_bytes())=='99140e79aa9c72e2ff53deedb0aba88be5035ef85101dd45f888645cc1e717fa'
assert H((q/'graficos-r28-lote2/resultado.json').read_bytes())=='d478d5c281172bbfb788075f0d585984584df2ab5c4c339eb0f23c4a3353dd23'
u=b.decode().encode('utf-16-le')
for name,a,z,h in [('fases tabela',46524,49664,'031b7ef930ce1afac685cbf1452d5a9d36cb312f6e076ee897028b70aa76d6f0'),('fases contexto',45966,49877,'82d085cc1279c534bd3724d94e222676977cc703a1b2b08f1c5d64caf3e2a1af'),('otto/diesel tabela',361096,361647,'1bd0f43dae0d4c6dc9959e2dae469bde9deab205916da21054bf6e815e0402d6'),('otto/diesel contexto',361002,369881,'e9003e6a7fb1909ad6fe78833b6faa166bd3827a29f5d4647b14176eae47f175')]:
 assert H(u[2*a:2*z].decode('utf-16-le').encode())==h,name
 print(name,'identidade confere')
a=.658;c=.0002;R=.287;r=8.;t1=300.;t3=1200.; target=R*log(r)
def integral(t):return a*log(t/t1)+c*(t-t1)
def inv(target,t):
 for _ in range(20):t-=(integral(t)-target)/(a/t+c)
 return t
t2=inv(target,660);t4=inv(integral(t3)-target,580)
def energy(t):return a*t+c*t*t/2
qin=energy(t3)-energy(t2);qout=energy(t4)-energy(t1);eta=1-qout/qin;k=1+R/(a+c*t1);closed=1-r**(1-k)
assert abs(t2-665.0241438448)<1e-8 and abs(t4-584.2080560487)<1e-8
assert abs(eta-.5304465428046)<1e-12 and abs(closed-.5644725201087)<1e-12
print('T2,T4=',t2,t4,'qin,qout=',qin,qout,'eta_integral,eta_k1=',eta,closed)
assert Decimal('101.325')<Decimal('22064') and Decimal('-10')<Decimal('0')<Decimal('100')
print('Comparações do contramodelo de água conferem; fase estável apoiada nas fontes, não inferida pelo programa.')
