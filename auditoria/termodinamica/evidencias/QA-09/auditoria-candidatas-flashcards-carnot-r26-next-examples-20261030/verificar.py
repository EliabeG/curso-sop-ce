#!/usr/bin/env python3
"""Revisão somente leitura de quatro candidatas isoladas; executar da raiz."""
from pathlib import Path
import hashlib,json,re
sha=lambda x:hashlib.sha256(x).hexdigest()
q=Path('auditoria/termodinamica/evidencias/QA-09')
source=Path('modulos/e1-termodinamica.html').read_bytes(); assert sha(source)=='afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2'
assert sha((q/'inventario-r26.json').read_bytes())=='d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241'
conf=[('card-cop','76c69881ec1f788a2d35056ccb26f8677dde1c356caf94c3a9b7993dfd33503c'),('card-carnot','e7b18767b4e56951478db06e87d263b92b6b5844b707b8b601a999f1576050e5'),('card-compressor','966452a015ec5f7a782989ecaf87d7a83fbb47ee5a19f2153f6ae7aa7e7326a1'),('base-carnot','95c2e4033297a8a39ad1fde18124e505e0de489ff53f37d17fd8c31e7560816c')]
h=source.decode(); b=h.encode('utf-16-le'); edits=[]
for name,hash_ in conf:
 p=q/f'candidata-{name}-r26-next-theory-20261030';raw=(p/'manifesto.json').read_bytes();assert sha(raw)==hash_;m=json.loads(raw)
 a=(p/'original.html').read_bytes();c=(p/'candidata.html').read_bytes();assert a.endswith(b'\n') and c.endswith(b'\n');a=a[:-1];c=c[:-1]
 assert sha(a)==m['original_sha256'] and sha(c)==m['candidata_sha256']; assert b[2*m['inicio_utf16']:2*m['fim_utf16']].decode('utf-16-le')==a.decode(); assert h.count(a.decode())==1
 reconstructed=a.decode()
 for x in m['substituicoes']:
  assert reconstructed.count(x['antes'])==1;reconstructed=reconstructed.replace(x['antes'],x['depois'])
 assert reconstructed==c.decode();edits.append((m,c.decode()));print(name,'identidade e substituição conferidas',m['inicio_utf16'],m['fim_utf16'])
edits.sort(key=lambda t:t[0]['inicio_utf16']);assert all(edits[i-1][0]['fim_utf16']<=edits[i][0]['inicio_utf16'] for i in range(1,len(edits)))
for m,c in reversed(edits):b=b[:2*m['inicio_utf16']]+c.encode('utf-16-le')+b[2*m['fim_utf16']:]
out=b.decode('utf-16-le')
for pattern in [r'<article\b[\s\S]*?</article>',r'<math\b[\s\S]*?</math>',r'\b(?:id|href|src|aria-controls|aria-labelledby|aria-describedby)="[^"]*"']:
 left=re.findall(pattern,h);right=re.findall(pattern,out);assert left==right;print('padrão',pattern,'preservado:',len(left))
print('sha hipotético combinado r1 (não é aprovação):',sha(out.encode()))
print('η específico=',30/40,'razão potências com 1 e 2 kg/s=',30/80,'COP=',300/(100-20),'Carnot=',1-300/600)
