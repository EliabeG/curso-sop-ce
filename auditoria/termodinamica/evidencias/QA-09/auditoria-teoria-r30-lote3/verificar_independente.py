from hashlib import sha256
from pathlib import Path
from fractions import Fraction as F
h=lambda b:sha256(b).hexdigest()
root=Path('auditoria/termodinamica/evidencias/QA-09')
files=[('atual',Path('modulos/e1-termodinamica.html'),'c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4'),('r17',root/'aplicacao-intercooling-r17-r1/resultado/depois-aula.html','6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c'),('r18',root/'aplicacao-conjunta-r18-r1/resultado/depois-aula.html','7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca')]
s={}
for name,path,sha in files:
 b=path.read_bytes();assert h(b)==sha;s[name]=b.decode().encode('utf-16-le')
def frag(name,a,b):return s[name][a*2:b*2].decode('utf-16-le').encode()
checks=[('gas','atual',64994,78360,'a44f30b844520b9feacb8a73858b06a0f05b4428533886a7b982a0c926972ef9'),('lei','atual',159486,165066,'415c39abbefe84139c5b8bcd82f5523c26353ba2181fd844912354fbe9858704'),('fechado','atual',197427,203368,'e3b1df3efdff5d189b33dd706d1b94f83207280f346bf657970918aeed2d7dbb'),('quimica','atual',203368,204817,'4eb200663af71a191ec684d940e66eec601219488b60238a245e684cb68af648'),('entropia','atual',432031,447209,'7c86184a37044b68219f4b84c444ce89ee400c46547b569e6b47ced86cec64d9'),('gas-r18','r18',64037,77403,'a44f30b844520b9feacb8a73858b06a0f05b4428533886a7b982a0c926972ef9'),('lei-r17','r17',157256,162652,'332677c5d3ea50033ff1c6145ba8d6d039c5b98299d830e4b7d3435f67d2fdca'),('fechado-r17','r17',193976,199917,'e3b1df3efdff5d189b33dd706d1b94f83207280f346bf657970918aeed2d7dbb'),('quimica-r17','r17',199917,201366,'4eb200663af71a191ec684d940e66eec601219488b60238a245e684cb68af648'),('entropia-r17','r17',426459,441261,'ecd08e62bcdc7799132b011fe111dfae8948487b8203559cd085918c95fd35ef')]
for name,version,a,b,sha in checks: assert h(frag(version,a,b))==sha,name
R=F(287,1000);k=F(14,10);cv=R/(k-1);cp=cv+R
assert (cv,cp)==(F(7175,10000),F(10045,10000))
assert 250-40==210 and 50+100*F(42,10)-120==350 and -7-200*F(-20,1000)==-3
assert F(35,1)/F(70,100)==50 and 300*(3-1)==600 and 100*(3-1)==200
assert F(100,300)+F(100,600)==F(1,2) and F(200,450)!=F(1,2)
assert -F(20,100)+F(30,100)==F(1,10)
print('Identidades r17/r18/r30, alterações e aritmética independente: OK')
