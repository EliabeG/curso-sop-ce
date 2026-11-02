from html.parser import HTMLParser
from pathlib import Path
from collections import Counter
import hashlib
sha=lambda b:hashlib.sha256(b).hexdigest()
e1=Path('modulos/e1-termodinamica.html').read_bytes();e2=Path('modulos/e2-transferencia-de-calor.html').read_bytes()
assert sha(e1)=='ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f'
assert sha(e2)=='fc4f05c6569aa7074811d1fe9f21e3b3641beba267f19125ce9f8d784ee53d14'
class Links(HTMLParser):
 def __init__(self):super().__init__();self.article=0;self.active=None;self.links=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='article': self.article+=1
  if t=='a' and d.get('href','').startswith('e2-transferencia-de-calor.html#'): self.active=[d['href'],'',self.article]
 def handle_data(self,d):
  if self.active is not None:self.active[1]+=d
 def handle_endtag(self,t):
  if t=='a' and self.active is not None:self.links.append(self.active);self.active=None
  if t=='article':self.article-=1
class IDs(HTMLParser):
 def __init__(self):super().__init__();self.ids=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append((d['id'],t))
a=Links();a.feed(e1.decode());b=IDs();b.feed(e2.decode());wanted={'conducao','conveccao','trocadores','radiacao'}
assert len(a.links)==4 and {x[0].split('#')[1] for x in a.links}==wanted
for href,text,depth in a.links:
 target=href.split('#')[1];assert depth==0 and Counter(x[0] for x in b.ids)[target]==1 and (target,'section') in b.ids
 print(f'{href} | {text} | fora de article')
print('ok: SHA E1/E2, quatro links únicos, IDs de seção únicos; sem navegador')
