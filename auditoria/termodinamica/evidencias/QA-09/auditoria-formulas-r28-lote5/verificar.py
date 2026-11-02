from pathlib import Path
from fractions import Fraction as F
from html import unescape
from html.parser import HTMLParser
from xml.etree import ElementTree as E
import hashlib,json,re,math
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'formulas-r28-lote5-20261030';snap=r/'aplicacao-carnot-flashcards-r27-r1/resultado';sha=lambda b:hashlib.sha256(b).hexdigest();f=(snap/'depois-formulario.html').read_bytes();h=(snap/'depois-aula.html').read_bytes();i=(r/'inventario-r27.json').read_bytes();n=Path('formulas/termodinamica.html').read_bytes();nh=Path('modulos/e1-termodinamica.html').read_bytes();ni=(r/'inventario-r28.json').read_bytes()
assert sha(f)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02' and sha(h)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sha(i)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
assert sha(n)=='3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46' and sha(nh)=='d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8' and sha(ni)=='0a7a12fbf0cd2a0898bcebfdfa7ae98c850bdb0bf7d2b34eea06cc6a8d9afb44'
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
a=P();a.feed(h.decode());b=f.decode().encode('utf-16-le');rows=json.loads((p/'identidades.json').read_text());assert len(rows)==17 and [x['ficha'] for x in rows]==list(range(84,101));ms=links=0
for x in rows:
 c=b[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(c.encode())==x['sha256'] and f'id="{x["id"]}"' in c
 matches=re.findall(r'<article\b[^>]*\bid="'+re.escape(x['id'])+r'"[^>]*>.*?</article>',n.decode(),re.S);assert matches==[c]
 maths=re.findall(r'<math\b[^>]*>.*?</math>',c,re.S);assert len(maths)==x['mathml'];ms+=len(maths)
 for m in maths:E.fromstring(unescape(m))
 for target in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^\"]+)"',c):assert a.ids.count(target)==1;links+=1
assert ms==27 and links==17
for d,start,end in [(h,369881,382864),(nh,370901,383884)]:assert sha(d.decode().encode('utf-16-le')[2*start:2*end].decode('utf-16-le').encode())=='cffc3aa7e5c04aca69bb2b0e2716858f11e33f9a6806c9b8bf8e6661b1881305'
assert F(400)-250==150 and F(440)-400==40 and F(440)-250==190 and F(150,40)==F(15,4) and F(150,35)==F(30,7)
assert F(500-100,2500-100)==F(1,6) and F(8,1000)/F(10,1000)==F(4,5) and math.sqrt(100*900)==300
assert F(1,10)+F(2,100)+F(1,20)+F(1,100)==F(18,100) and abs(1/F(18,100)-F(50,9))<1e-10
assert abs(.8*5.67e-8*2*(400**4-300**4)-1587.6)<1e-9 and F(1000)*F(2,100)==20
print('ok: 17 fichas idênticas r27/r28, base vinculada igual, 27 MathML XML, 17 destinos e contas; sem renderização')
