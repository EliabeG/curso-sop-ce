from pathlib import Path
from decimal import Decimal as D
from html.parser import HTMLParser
import hashlib,json,math
root=Path('auditoria/termodinamica/evidencias/QA-09');p=root/'revisao-r28-reference-2';sha=lambda b:hashlib.sha256(b).hexdigest();h=Path('modulos/e1-termodinamica.html').read_bytes();i=(root/'inventario-r27.json').read_bytes();assert sha(h)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sha(i)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
a=P();a.feed(h.decode());b=h.decode().encode('utf-16-le');rows=json.loads((p/'identidades.json').read_text());assert len(rows)==4
for x in rows:
 f=b[2*x['start']:2*x['end']].decode('utf-16-le');assert sha(f.encode())==x['sha'] and f'id="{x["id"]}"' in f and a.ids.count(x['id'])==1
assert D(200)/D('.010')==20000 and D('.005')*10000+D('.005')*30000==200
assert D(120)==2*60 and abs(.287*math.log(2)-.1989332408207043)<1e-14
print('ok: quatro blocos, IDs, contraste de pressão e aritmética; sem consulta web ou interpretação automática de modelos')
