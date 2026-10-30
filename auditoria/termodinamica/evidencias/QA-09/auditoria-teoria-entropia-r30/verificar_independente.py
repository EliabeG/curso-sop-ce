from pathlib import Path
from hashlib import sha256
from math import log
p=Path('modulos/e1-termodinamica.html');b=p.read_bytes();s=b.decode().encode('utf-16-le')
assert sha256(b).hexdigest()=='c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4'
for name,i,j,h in [('livre',204817,207046,'f3405521cea64595e48e1b03da18afcb10d4017fe78f3d9b7009573dc46408cd'),('entropia',325924,337623,'1f92506c9418009d1ec8bba9cbd51e328946ec89cecae58219936973f02a9df3'),('exergia',346999,349929,'23ce04f24f08f852e88524c64f08f9f3ddc11a41a01ffedefacbead5e9d02a1d')]:
 block=s[2*i:2*j].decode('utf-16-le'); assert sha256(block.encode()).hexdigest()==h; print(name, 'identidade OK')
ds=.287*log(2);assert abs(ds-.1989332408207043)<1e-12
assert abs(300*ds-59.6799722462)<1e-8
R=8.314462618;a=.3658;b=.0000427;cv=20;v1=.010;v2=.020;T1=300
T2=T1+(a/cv)*(1/v2-1/v1)
p=lambda T,v:R*T/(v-b)-a/v**2
dpdv=lambda T,v:-R*T/(v-b)**2+2*a/v**3
entropy=cv*log(T2/T1)+R*log((v2-b)/(v1-b))
assert abs(T2-299.0855)<1e-9 and abs(p(T1,v1)-246845.529)<1 and abs(p(T2,v2)-123688.287)<1
assert v1>b and v2>b and p(T1,v1)>0 and p(T2,v2)>0 and dpdv(T1,v1)<0 and dpdv(T2,v2)<0 and entropy>0
print('ΔS ideal',ds,'kJ/K; exergia destruída',300*ds,'kJ; T₂',T2,'K; p₁,p₂',p(T1,v1),p(T2,v2),'Pa; ΔS modelo',entropy,'J/K')
