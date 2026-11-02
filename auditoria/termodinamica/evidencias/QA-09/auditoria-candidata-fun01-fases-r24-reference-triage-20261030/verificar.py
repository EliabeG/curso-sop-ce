from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'candidata-fun01-fases-r24-next-theory-20261030';m=json.loads((p/'manifesto.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
h=Path(m['fonte']).read_bytes();i=Path(m['inventario']).read_bytes();assert sha(h)==m['fonte_sha256']=='2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9';assert sha(i)==m['inventario_sha256']=='469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf'
s=h.decode();u=s.encode('utf-16-le');a,b=m['inicio_utf16'],m['fim_utf16'];o=u[2*a:2*b].decode('utf-16-le');c=(p/'candidata.html').read_text().removesuffix('\n')
assert (p/'original.html').read_text().removesuffix('\n')==o and sha(o.encode())==m['original_sha256'] and sha(c.encode())==m['candidata_sha256']
assert o.count(m['antes'])==1 and o.replace(m['antes'],m['depois'])==c and s.count(o)==1
out=s.replace(o,c);assert sha(out.encode())=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e'
for pat in [r'<math\b[^>]*>.*?</math>',r'<article\b[^>]*>.*?</article>',r'\bhref="[^"]*"',r'\bid="[^"]*"']:
 x=re.findall(pat,s,re.S);assert x==re.findall(pat,out,re.S);print(pat,len(x))
xa,ya=F(1,6),F(4,9)
assert (xa-xa)/(ya-xa)==0 and (ya-xa)/(ya-xa)==1
assert (F(1,4)-xa)/(ya-xa)==F(3,10)
for beta in (F(1,5),F(3,4)):
 assert (1-beta)*0+beta*0==0
assert (1-F(1,2))*0+F(1,2)*0!=F(1,4)
assert (F(5,2)-1)/(4-1)==F(1,2)
print('ok: identidade, troca literal, condições 0/0, inconsistência, fase incipiente e propriedade global')
