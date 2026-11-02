#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');d=q/'candidata-ex010-equipamentos-r25-next-examples-20261030'
def rd(p):return p.read_bytes()
def sh(x):return sha256(x).hexdigest()
a=rd(Path('modulos/e1-termodinamica.html'));assert sh(a)=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e';assert sh(rd(q/'inventario-r25.json'))=='6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116'
mb=rd(d/'manifesto.json');assert sh(mb)=='9374290e0e6203e356e71b3d87b4e8df9aa714e4c5f04556a9aa2113f01c2da7';m=json.loads(mb);old=rd(d/'original.html');new=rd(d/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1];assert sh(old)==m['original_sha256'] and sh(new)==m['candidata_sha256'];u=a.decode().encode('utf-16-le');assert u[2*m['inicio_utf16']:2*m['fim_utf16']].decode('utf-16-le').encode()==old
assert len(m['substituicoes'])==9;tmp=old
for z in m['substituicoes']:
 x=z['antes'].encode();y=z['depois'].encode();assert tmp.count(x)==1;tmp=tmp.replace(x,y)
assert tmp==new and a.count(old)==1;b=a.replace(old,new);assert sh(b)=='a05528748cf34195eeb5366484b16ce6f19f9668e91c5a1915ff5afe5a1cad36'
arts=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S);maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
assert len(arts(a))==197 and arts(a)==arts(b) and len(maths(a))==734 and maths(a)==maths(b)
class H(HTMLParser):
 def __init__(self):super().__init__();self.attr=[]
 def handle_starttag(self,tag,attrs):
  z=tuple((k,v) for k,v in attrs if k in ('id','href','src') or k.startswith('aria-'))
  if z:self.attr.append((tag,z))
x=H();y=H();x.feed(a.decode());y.feed(b.decode());assert x.attr==y.attr
assert 3000-2600==400 and 2*400==800 and 2*3000-2600-2000==1400
assert 1*(-100)+2*50==0
print('OK: nove substituições reproduzem candidata e HTML hipotético; 197 artigos, 734 MathML, ids/links/ARIA; balanços turbina e trocador')
