from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
import math,re,json
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';d=q/'formulas-r28-lote4-20261030';h=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-formulario.html').read_bytes();a=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes();ib=(q/'inventario-r27.json').read_bytes();jb=(d/'identidades.json').read_bytes();sh=lambda x:sha256(x).hexdigest()
assert sh(h)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02' and sh(a)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sh(ib)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c' and sh(jb)=='94f5429fc27c9dc36fdf2ab84594f3223882e5c24142948df85467459bf0203b'
class HTML(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,attrs):
  z=dict(attrs)
  if 'id' in z:self.ids.append(z['id'])
pa=HTML();pa.feed(a.decode());u=h.decode().encode('utf-16-le');rows=json.loads(jb);assert len(rows)==17 and [x['ficha'] for x in rows]==list(range(67,84));nc=links=0
for x in rows:
 frag=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sh(frag.encode())==x['sha256'] and f'id="{x["id"]}"' in frag
 ms=re.findall(r'<math\b.*?</math>',frag,re.S);assert len(ms)==x['mathml'];nc+=len(ms)
 for m in ms:ET.fromstring(m)
 for dest in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^"]+)"',frag):assert pa.ids.count(dest)==1;links+=1
assert nc==31 and links==17
r=.287; vals={'qrev':300*.2,'stp':1.0045*math.log(4/3)-r*math.log(2),'stv':.7175*math.log(4/3)+r*math.log(2/3),'isentro':2**(.4/1.4),'etaT':400/500,'etaC':200/250,'sgen':1*(1.2-1)-30/300,'exergia':300*.1,'du':300*.1-200*.1,'dh':300*.1+.001*600,'dhis':.001*600,'dg':(10-7)*.5,'svcp':.8*math.log(4/3)+.001*100-r*math.log(2),'rankine':(600-10)/(3000-110),'brayton':(600-200)/1000,'braytonideal':1-8**(-.4/1.4),'otto':1-8**(-.4),'diesel':1-16**(-.4)*(2**1.4-1)/(1.4*(2-1)),'rankine_eixo':(400-10)/(3000-110),'rankine_total':(600-10)/(3000-110),'turbina_total':400+100}
assert abs(vals['stp']-vals['stv'])<1e-12 and abs(vals['sgen']-.1)<1e-12 and abs(vals['otto']-.5647247183519379)<1e-12 and vals['turbina_total']==500 and vals['rankine_total']>vals['rankine_eixo']
print(json.dumps({'ok':True,'fichas':17,'mathml_xml':nc,'links':links,'contas':vals,'limite':'A sintaxe XML e contas não comprovam domínio físico, modelos reais ou acessibilidade.'},ensure_ascii=False))
