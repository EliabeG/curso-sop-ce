from pathlib import Path
from html.parser import HTMLParser
from fractions import Fraction as F
import hashlib,json,re,math
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'fichas-unidades-reconciliacao-r26-20261030';sha=lambda b:hashlib.sha256(b).hexdigest()
fs=[r/'aplicacao-intercooling-r17-r1/resultado/depois-formulario.html',r/'aplicacao-conjunta-r18-r1/resultado/depois-formulario.html',Path('formulas/termodinamica.html')];hs=['dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d','463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895','16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02'];docs=[f.read_bytes() for f in fs];assert [sha(x) for x in docs]==hs
al=[(r/'aplicacao-intercooling-r17-r1/resultado/depois-aula.html').read_bytes(),Path('modulos/e1-termodinamica.html').read_bytes()];assert [sha(x) for x in al]==['6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c','afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2'];assert sha((r/'inventario-r26.json').read_bytes())=='d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241'
class IDs(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
a=IDs();a.feed(al[1].decode());cards=json.loads((p/'identidades.json').read_text());contexts=json.loads((p/'contextos.json').read_text());assert len(cards)==len(contexts)==11
links=0
for row in cards:
 frags=[]
 for n,rev in enumerate(('r17','r18','r26')):
  b=docs[n].decode().encode('utf-16-le');z=row[rev];f=b[2*z['inicio_utf16']:2*z['fim_utf16']].decode('utf-16-le');assert sha(f.encode())==z['sha256'] and f'id="{row["id"]}"' in f;frags.append(f)
 assert frags[1]==frags[2] and (frags[0]==frags[2])==(row['ficha']!=60)
 for target in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^\"]+)"',frags[2]):assert a.ids.count(target)==1;links+=1
assert links==12
for row in contexts:
 vals=[]
 for n,rev in enumerate(('r17','r26')):
  b=al[n].decode().encode('utf-16-le');z=row[rev];f=b[2*z['inicio_utf16']:2*z['fim_utf16']].decode('utf-16-le');assert sha(f.encode())==z['sha256'] and f'id="{row["id"]}"' in f;vals.append(f)
 assert (vals[0]==vals[1])==row['igual']
assert sum(x['igual'] for x in contexts)==9
assert F(100,80)*100-100==25 and F(1000,1000000)==F(1,1000) and F(10)*F(2,100)==F(1,5)
assert F(12,10)/3==F(2,5) and F(6,10)/F(4,10)==F(3,2)
assert F(2,2)*(25-9)==16 and 2*10*3==60
assert F(100)+F(200**2-100**2,2000)+F(981,100)*F(20,1000)==F(575981,5000)
assert abs(math.sqrt(50**2+2000*40)-287.2281323269)<1e-9
assert F(380,80)==F(19,4) and F(300,80)==F(15,4)
print('ok: 11 fichas, 11 contextos, 12 links, identidades r17/r18/r26 e amostra independente de contas')
