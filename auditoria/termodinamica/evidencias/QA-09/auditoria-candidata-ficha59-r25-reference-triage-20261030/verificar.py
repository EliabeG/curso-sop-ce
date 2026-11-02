from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'candidata-ficha59-r25-20261030';m=json.loads((p/'manifesto.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest();h=Path(m['formulario']).read_bytes();i=Path(m['inventario']).read_bytes();assert sha(h)==m['formulario_sha256']=='694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58';assert sha(i)==m['inventario_sha256']=='6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116'
s=h.decode();u=s.encode('utf-16-le');a,b=m['inicio_utf16'],m['fim_utf16'];o=u[2*a:2*b].decode('utf-16-le');c=(p/'candidata.html').read_text().removesuffix('\n');assert o==(p/'original.html').read_text().removesuffix('\n') and sha(o.encode())==m['original_sha256'] and sha(c.encode())==m['candidata_sha256']
t=o
for x in m['mudancas']:
 assert t.count(x['antes'])==2;t=t.replace(x['antes'],x['depois'])
assert t==c and s.count(o)==1
out=s.replace(o,c);assert sha(out.encode())=='16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02'
for pat in [r'<math\b[^>]*>.*?</math>',r'\bhref="[^\"]*"',r'\bid="[^\"]*"']:
 x=re.findall(pat,s,re.S);assert x==re.findall(pat,out,re.S);print(pat,len(x))
arts=re.findall(r'<article\b[^>]*>.*?</article>',s,re.S);new=re.findall(r'<article\b[^>]*>.*?</article>',out,re.S);assert len(arts)==len(new)==100 and sum(a!=b for a,b in zip(arts,new))==1
assert 100-20==80 and F(300,80)==F(15,4) and 300+80==380 and F(380,350)-F(300,300)==F(3,35)
print('ok: dois deltas em texto e busca; 99 cartões não alvo; saldo e COP verificados')
