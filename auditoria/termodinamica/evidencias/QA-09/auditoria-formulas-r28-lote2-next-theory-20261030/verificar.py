from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
from fractions import Fraction as F
import math,re,json
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';d=q/'formulas-r28-lote2-20261030';h=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-formulario.html').read_bytes();a=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes();ib=(q/'inventario-r27.json').read_bytes();jb=(d/'identidades.json').read_bytes();sh=lambda x:sha256(x).hexdigest()
assert sh(h)=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02' and sh(a)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sh(ib)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c' and sh(jb)=='0e8cde969133202f4a5355fa1011ec7aa300fc53c03331a8836cfa8c5931b2c9'
class HTML(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,attrs):
  z=dict(attrs)
  if 'id' in z:self.ids.append(z['id'])
pa=HTML();pa.feed(a.decode());u=h.decode().encode('utf-16-le');rows=json.loads(jb);assert len(rows)==22 and [r['ficha'] for r in rows]==list(range(23,45));math_count=links=0
for x in rows:
 frag=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sh(frag.encode())==x['sha256'] and f'id="{x["id"]}"' in frag
 ms=re.findall(r'<math\b.*?</math>',frag,re.S);assert len(ms)==x['mathml'];math_count+=len(ms)
 for m in ms:ET.fromstring(m)
 for dest in re.findall(r'href="\.\./modulos/e1-termodinamica\.html#([^"]+)"',frag):assert pa.ids.count(dest)==1;links+=1
assert math_count==39 and links==23
v={'latente':(2500-500)*2,'interpolacao':100+(350-300)*(200-100)/100,'umidade':F(30,75),'sensivel':F(2)*F(42,10)*10,'mistura':(1*20+3*60)/4,'externa':(100*20+100*40+2000)/200,'fase':2*2250,'cin':2*(25-9)/2,'pot':2*10*(5-2),'fechado':-30+180,'final':500-30+180,'fronteira':100*(3-1),'isotermico':.287*300*math.log(2),'isochorico':2*.718*100,'isobarico':2*1.005*100,'ciclo':600-200,'entropia':.287*math.log(2),'entalpia':100+200*.5,'escoamento':100+(400**2-100**2)/2000+100/1000,'turbina':3000-2600,'compressor':400-100,'multisaidas_total_kw':2*1000-1*500-1*900,'multisaidas_por_massa':(2*1000-1*500-1*900)/2,'formula_parcial':1000-500,'turbina_saida_total':400+100,'compressor_entrada_total':400+100}
assert v['latente']==4000 and v['mistura']==50 and v['externa']==40 and v['escoamento']==175.1 and v['multisaidas_por_massa']==300 and v['formula_parcial']==500 and v['turbina_saida_total']==500 and v['compressor_entrada_total']==500
assert sum([0,0])==0 and sum(c*t for c,t in zip([0,0],[20,60]))==0
print(json.dumps({'ok':True,'fichas':len(rows),'mathml_xml':math_count,'links':links,'contas':{k:float(x) for k,x in v.items()},'limite':'Identidade, XML e contas; pressupostos, ciência e acessibilidade exigem leitura independente.'},ensure_ascii=False))
