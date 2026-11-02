from pathlib import Path
from fractions import Fraction as F
from html.parser import HTMLParser
import hashlib,json,math
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'exemplos-r28-lote2-fun02-r27-next-examples-20261030';sha=lambda b:hashlib.sha256(b).hexdigest();a=(r/'aplicacao-fun01-fases-r25-r1/resultado/depois-aula.html').read_bytes();b=Path('modulos/e1-termodinamica.html').read_bytes();inv=(r/'inventario-r27.json').read_bytes();assert sha(a)=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e' and sha(b)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sha(inv)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
ps=[P(),P()];ps[0].feed(a.decode());ps[1].feed(b.decode());rows=json.loads((p/'resultado.json').read_text())['blocos'];assert len(rows)==6
for x in rows:
 for n,doc in enumerate((a,b)):
  z=x['versoes'][n];u=doc.decode().encode('utf-16-le');f=u[2*z['inicio']:2*z['fim']].decode('utf-16-le');assert sha(f.encode())==z['sha256'] and f'id="{x["id"]}"' in f and ps[n].ids.count(x['id'])==1
assert sum(x['versoes'][0]['sha256']==x['versoes'][1]['sha256'] for x in rows)==2
assert F(80)*F(6,1000)==F(12,25)
assert 2**2==4 and 3*2**2==12 and 2**3+2*3==14 and 3*2**2+3==15
# unit circle has dx=-sin(t)dt, dy=cos(t)dt => omega=dt and integral=2*pi
for t in [0,.3,1.5,3.7,6]:
 x=math.cos(t);y=math.sin(t);assert abs((-y*(-y)+x*x)/(x*x+y*y)-1)<1e-14
assert F(3,4)*80*F(6,1000)==F(9,25)
assert abs(8.314*300*math.log(2)-1728.8476977526154)<1e-9
assert abs(2*20*math.log(400/300)+2*8.314*math.log(.03/.02)-18.249356715693793)<1e-10
print('ok: seis contêineres r25/r27, unicidade, contas exatas e parametrização do círculo; sem rede ou navegador')
