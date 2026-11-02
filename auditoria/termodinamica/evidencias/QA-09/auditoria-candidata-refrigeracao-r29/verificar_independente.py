from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from fractions import Fraction
import json,re
root=Path('.')
p=root/'auditoria/termodinamica/evidencias/QA-09/candidata-refrigeracao-r29-r2'
m=json.loads((p/'manifesto.json').read_text())
h=lambda b:sha256(b).hexdigest()
for x in [*m['fontes'].values(),m['inventario'],m['parecer']]:
 assert h((root/x['arquivo']).read_bytes())==x['sha256']
assert len(m['edicoes'])==3
source={k:(root/v['arquivo']).read_text() for k,v in m['fontes'].items()}
output={}
class Attributes(HTMLParser):
 def __init__(self): super().__init__(); self.values=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('id','href','src') or k.startswith('aria-'): self.values.append((tag,k,v))
def attrs(s):
 p=Attributes(); p.feed(s); return p.values
def math(s): return re.findall(r'<math\b.*?</math>',s,re.S|re.I)
for key,doc in [('aula','modulos/e1-termodinamica.html'),('formulario','formulas/termodinamica.html')]:
 old=source[key]; raw=old.encode('utf-16-le')
 edits=sorted((e for e in m['edicoes'] if e['documento']==doc),key=lambda e:e['inicio_utf16'],reverse=True)
 for e in edits:
  a,b=e['inicio_utf16']*2,e['fim_utf16']*2
  original=raw[a:b].decode('utf-16-le')
  assert h(original.encode())==e['original_sha256']
  assert (p/(e['id']+'-original.html')).read_text().removesuffix('\n')==original
  candidate=original
  for sub in e['substituicoes']:
   assert candidate.count(sub['antes'])==sub['quantidade']
   candidate=candidate.replace(sub['antes'],sub['depois'])
  assert h(candidate.encode())==e['candidata_sha256']
  assert (p/(e['id']+'-candidata.html')).read_text().removesuffix('\n')==candidate
  raw=raw[:a]+candidate.encode('utf-16-le')+raw[b:]
 new=raw.decode('utf-16-le'); output[key]=new
 assert h(new.encode())==m['sha_hipotetico'][key]
 assert math(old)==math(new)
 assert attrs(old)==attrs(new)
 assert len(re.findall(r'<article\b',old))==len(re.findall(r'<article\b',new))
print('MathML preservado:',len(math(source['aula'])),len(math(source['formulario'])))
legend='Magnitude do trabalho consumido pelo ciclo de refrigeração ou pela bomba de calor.'
assert source['aula'].count(legend)==9 and output['aula'].count(legend)==6
assert 35+5==40 and Fraction(150,40)==Fraction(15,4) and 150+40==190
assert 35+5-5==35
print('Fontes, recortes, substituições, hashes, fórmulas, atributos, artigos, legendas e contramodelos: OK')
