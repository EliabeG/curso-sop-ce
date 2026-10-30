from pathlib import Path
from html.parser import HTMLParser
from fractions import Fraction as F
import hashlib,json
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'fontes-r28-figuras-r27-20261030';sha=lambda b:hashlib.sha256(b).hexdigest();h=Path('modulos/e1-termodinamica.html').read_bytes();i=(r/'inventario-r27.json').read_bytes();assert sha(h)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49' and sha(i)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
s=h.decode().encode('utf-16-le');spans=[(172570,173632),(200305,201775),(211566,212886),(408674,410028)]
class P(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.svg=[];self.alt=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='svg':self.svg.append(d)
  if t in ('title','desc'):self.alt.append((t,d.get('id')))
allp=P();allp.feed(h.decode());out=[]
for a,b in spans:
 f=s[2*a:2*b].decode('utf-16-le');x=P();x.feed(f);assert f.startswith('<figure ') and f.endswith('</figure>') and len(x.svg)==1 and x.svg[0].get('role')=='img';refs=x.svg[0]['aria-labelledby'].split();assert all(x.ids.count(k)==1 and allp.ids.count(k)==1 for k in refs) and any(t=='title' for t,_ in x.alt) and '<figcaption>' in f
 out.append({'inicio_utf16':a,'fim_utf16':b,'sha256':sha(f.encode()),'rotulos_aria':refs,'elementos_descritivos':x.alt})
assert (200-100)*(3-1)==200 and 300*(3-1)==600 and 100*(3-1)==200
assert (F(1)*20+F(3)*60)/4==50
manifest=json.dumps({'aula_sha256':sha(h),'inventario_sha256':sha(i),'figuras':out},ensure_ascii=False,indent=2)+'\n';mf=p/'identidades.json'
assert mf.read_text()==manifest
print(manifest);print('ok: identidades, rótulos ARIA, legendas e contas; não testa leitor de tela ou renderização')
