from pathlib import Path
from decimal import Decimal as D
import hashlib
r=Path('auditoria/termodinamica/evidencias/QA-09')
h=(r/'aplicacao-notacao-fichas-r19-r1/resultado/depois-aula.html').read_bytes();i=(r/'inventario-r19.json').read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(h)=='9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65'
assert sha(i)=='ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f'
s=h.decode().encode('utf-16-le')
for a,b,v in [(203897,206379,'7c7e654b40f3d57c3d0d128ab5c48f9e9572f50a631c8123e45847df78228853'),(206379,212704,'ee9bafa3d68b1ef06bd39268a717f2474472de6a981bd6b0423f85abcd9eef03'),(212704,215090,'ddaaf9583c9fb8a99341184b41a8886d7e85f543ee2abdd3955c011d92888d88')]:assert sha(s[2*a:2*b].decode('utf-16-le').encode())==v
assert 2*D('4.2')*30==252 and D(252)/(D(2)*D('.8'))==D('157.5')
assert (D(1)*20+D(3)*60)/4==50 and (D(4)*80+D(4)*20+D(2)*20)/10==44
assert D('.5')*D('4.2')*20==42 and D('.1')*334==D('33.4')
assert abs((D(42)-D('33.4'))/(D('.6')*D('4.2'))-D('3.412698412698412698412698413'))<D('1e-25')
assert D('.3')*334==D('100.2') and abs(D(42)/D(334)-D('.1257485029940119760479041916'))<D('1e-25')
assert D(2)*10*2-40==0 and D(200)-D(100)*D('.1')==190 and D(190)+5==195
print('ok: três blocos, aritmética e contramodelos contábeis; sem exame de rede ou visual')
