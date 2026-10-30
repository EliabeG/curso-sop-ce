from pathlib import Path
from html.parser import HTMLParser
from fractions import Fraction as F
from decimal import Decimal as D
import hashlib,json,re
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'formulas-r28-fundamentos-gases-r27-20261030';sha=lambda b:hashlib.sha256(b).hexdigest()
f=Path('formulas/termodinamica.html').read_bytes();h=Path('modulos/e1-termodinamica.html').read_bytes();i=(r/'inventario-r27.json').read_bytes();assert sha(f)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02' and sha(h)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sha(i)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.math=0;self.tagcounts={}
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='math':self.math+=1
  self.tagcounts[t]=self.tagcounts.get(t,0)+1
a=P();a.feed(h.decode());rows=json.loads((p/'identidades.json').read_text());assert len(rows)==22 and [x['ficha'] for x in rows]==list(range(1,23))
b=f.decode().encode('utf-16-le');ms=0;links=0
for row in rows:
 x=b[2*row['inicio_utf16']:2*row['fim_utf16']].decode('utf-16-le');assert sha(x.encode())==row['sha256'] and f'id="{row["id"]}"' in x
 parsed=P();parsed.feed(x);assert parsed.math==row['mathml'];ms+=parsed.math
 for target in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^\"]+)"',x):assert a.ids.count(target)==1;links+=1
assert ms==58 and links==24
assert D(120)/60==2 and D(2)/D('.0025')==800 and D('.0025')/2==D('.00125')
assert D(2)*D('.287')*300==D('172.2') and D(1)*D('.287')*300/D('.861')==100
assert D('1.005')-D('.718')==D('.287') and D(2)*D('.718')*100==D('143.6')
assert D('.8')*100+D('.001')*(D(400)**2-D(300)**2)/2==D(115)
assert F(1,4)*2500+F(3,4)*500==1000
print('ok: 22 hashes/IDs, 58 MathML, 24 destinos e amostra independente de contas; inspeção física e estrutura MathML exigem leitura manual')
