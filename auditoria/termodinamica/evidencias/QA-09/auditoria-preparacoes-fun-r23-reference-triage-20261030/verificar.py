from pathlib import Path
from decimal import Decimal as D
from fractions import Fraction as F
import hashlib
r=Path('auditoria/termodinamica/evidencias/QA-09');sha=lambda b:hashlib.sha256(b).hexdigest();h=(r/'aplicacao-resumo-glossario-r23-r1/resultado/depois-aula.html').read_bytes();i=(r/'inventario-r23.json').read_bytes()
assert sha(h)=='f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d' and sha(i)=='ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e'
s=h.decode().encode('utf-16-le')
for a,b,v in [(107020,111548,'6a58642fcfbbe49b936c53ea8be9c679fa45607ac3e200fcaf836e12bd1c7a2e'),(250530,253530,'8282aa4e9466aba1ae9402e9587b6e3c065c607897b8f81d450c12f1ad943ebc')]:assert sha(s[2*a:2*b].decode('utf-16-le').encode())==v
assert D(80)*D('.250')==D(160)*D('.125')==20
assert 80-20==60 and 160-20==140
assert F(10,1)/F(50,30)==6 and F(10,1)!=6
assert -1+D('.1')*10*2==1 and D(240)/400==D('.6')
primitive=lambda x: x*x/2-x/2
assert -(primitive(F(1))-primitive(F(0)))==0
assert -(primitive(F(1,2))-primitive(F(0)))==F(1,8)
print('ok: dois blocos, gases, gravidade, mistura sintética, mudança de coordenadas e integrais no retângulo')
