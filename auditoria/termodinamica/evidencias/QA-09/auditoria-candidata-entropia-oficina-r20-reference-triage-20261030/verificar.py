from pathlib import Path
from decimal import Decimal as D
import hashlib,json,re
r=Path('auditoria/termodinamica/evidencias/QA-09');p=r/'candidata-entropia-oficina-r20-20261030';m=json.loads((p/'manifesto.json').read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
h=Path(m['fonte']).read_bytes();i=Path(m['inventario']).read_bytes();assert sha(h)==m['fonte_sha256']=='b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7';assert sha(i)==m['inventario_sha256']=='e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4'
s=h.decode();u=s.encode('utf-16-le');a,b=m['inicio_utf16'],m['fim_utf16'];o=u[2*a:2*b].decode('utf-16-le');c=(p/'candidata.html').read_text().removesuffix('\n')
assert o==(p/'original.html').read_text().removesuffix('\n') and sha(o.encode())==m['original_sha256'] and sha(c.encode())==m['candidata_sha256']
t=o
for x in m['substituicoes']:
 assert t.count(x['antes'])==1;t=t.replace(x['antes'],x['depois'])
assert t==c and s.count(o)==1
out=s.replace(o,c);assert sha(out.encode())=='ac3b482a49801e125a6e6ff1792a63d5f4cd1406430d29a633c863da91f44c21'
for pattern in [r'<math\b[^>]*>.*?</math>',r'<article\b[^>]*>.*?</article>',r'\bhref="[^"]*"',r'\bid="[^"]*"']:
 a=re.findall(pattern,s,re.S);assert a==re.findall(pattern,out,re.S);print(pattern,len(a))
assert -D(900)/500==D('-1.8') and D(600)/300==2 and D(600)/300-D(900)/500==D('.2')
assert D(300)/900 < 1-D(300)/500
print('ok: três substituições, somas, estruturas e documento hipotético; sem gravar produto')
