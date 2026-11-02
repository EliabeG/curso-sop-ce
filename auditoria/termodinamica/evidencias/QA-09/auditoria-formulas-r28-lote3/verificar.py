from pathlib import Path
from html.parser import HTMLParser
from html import unescape
from fractions import Fraction as F
from xml.etree import ElementTree as E
import hashlib,json,re,math
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'formulas-r28-lote3-20261030';snap=r/'aplicacao-carnot-flashcards-r27-r1/resultado';sha=lambda b:hashlib.sha256(b).hexdigest();f=(snap/'depois-formulario.html').read_bytes();h=(snap/'depois-aula.html').read_bytes();i=(r/'inventario-r27.json').read_bytes()
assert sha(f)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02' and sha(h)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sha(i)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
a=P();a.feed(h.decode());b=f.decode().encode('utf-16-le');rows=json.loads((p/'identidades.json').read_text());assert len(rows)==22 and [x['ficha'] for x in rows]==list(range(45,67));ms=links=0
for x in rows:
 c=b[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(c.encode())==x['sha256'] and f'id="{x["id"]}"' in c
 mathblocks=re.findall(r'<math\b[^>]*>.*?</math>',c,re.S);assert len(mathblocks)==x['mathml'];ms+=len(mathblocks)
 for m in mathblocks:E.fromstring(unescape(m))
 for target in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^\"]+)"',c):assert a.ids.count(target)==1;links+=1
assert ms==36 and links==22
assert F(1,1000)*600==F(3,5) and F(2)*100==200 and 50-10+3*100-150==190 and 100-20+2*300-200==480
assert F(125,100)*320==400 and (F(2,100)+50*(F(4,10000)-F(6,10000)))/100==F(1,10000)
assert F(2,100)/(F(8,10000)-F(4,10000))==50 and F(50,100)==F(1,2)
assert F(1000)*F(981,100)*F(1,100)*10==981 and math.sqrt(100**2+2000*75)==400
assert F(900)-300==600 and F(600,900)==F(2,3) and F(300,100)==3 and F(400,100)==4
assert 1-F(300,600)==F(1,2) and F(900)*F(1,2)==450 and F(300,600-300)==1
assert F(100,300)+F(1,10)==F(13,30) and F(3,10)-F(2,10)==F(1,10)
print('ok: 22 fichas, 36 MathML XML, 22 destinos e contas; sem renderização ou prova automática das hipóteses')
