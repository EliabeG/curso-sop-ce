from pathlib import Path
from html.parser import HTMLParser
from fractions import Fraction as F
import hashlib,json,re,math
r=Path('auditoria/termodinamica/evidencias/QA-09');sha=lambda b:hashlib.sha256(b).hexdigest();ps=[r/'aplicacao-conjunta-r14-seis-r1/resultado/depois-formulario.html',r/'aplicacao-conjunta-r16-r1/resultado/depois-formulario.html',Path('formulas/termodinamica.html')];hs=['3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce','dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58'];ds=[p.read_bytes() for p in ps];assert [sha(x) for x in ds]==hs
lesson=Path('modulos/e1-termodinamica.html').read_bytes();assert sha(lesson)=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e';assert sha((r/'inventario-r25.json').read_bytes())=='6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116'
class IDs(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
a=IDs();a.feed(lesson.decode());rows=json.loads((r/'fichas-ciclos-latente-reconciliacao-r25-20261030/identidades.json').read_text());assert len(rows)==10
count=0
for row in rows:
 frags=[]
 for idx,rev in enumerate(('r14','r16','r25')):
  b=ds[idx].decode().encode('utf-16-le');z=row[rev];f=b[2*z['inicio_utf16']:2*z['fim_utf16']].decode('utf-16-le');assert sha(f.encode())==z['sha256'] and f'id="{row["id"]}"' in f;frags.append(f)
 assert frags[1]==frags[2] and (frags[0]==frags[2])==(row['ficha'] not in (89,90))
 for link in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^\"]+)"',frags[2]):assert a.ids.count(link)==1;count+=1
assert count==10
assert (F(300),F(80),F(380,350)-F(300,300))==(300,80,F(3,35)) and F(300,80)==F(15,4)
k=1.4;assert abs(300*4**((k-1)/k)-445.7982867411)<1e-8
assert abs((1-8**(-(k-1)/k))-.4479552432)<1e-8 and abs((1-8**(1-k))-.5647247184)<1e-8
assert abs((1-18**(1-k)*(2**k-1)/(k*(2-1)))-.6315775314)<1e-8
assert abs(1.3/.3*.287*300*(4**(.3/1.3)-1)-140.6622262406)<1e-8
assert abs(.287*300*math.log(4)-119.3599444924)<1e-8 and abs(.8*5.67e-8*2*(500**4-300**4)-4935.168)<1e-8
print('ok: dez fichas em três versões, dez destinos locais e aritmética')
