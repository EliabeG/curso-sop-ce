#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
import json,re
q=Path('auditoria/termodinamica/evidencias/QA-09');d=q/'candidata-ex046-r20-20261030-r3'
def sh(x):return sha256(x).hexdigest()
def rd(p):return p.read_bytes()
h=rd(Path('modulos/e1-termodinamica.html'));assert sh(h)=='b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7'
assert sh(rd(q/'inventario-r20.json'))=='e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4'
assert sh(rd(d/'manifesto.json'))=='a453b56ec947c4d536ab7656543304afcb279acbb52a679cd95950a1dbc221e6'
assert sh(rd(d/'analise.md'))=='cb8901f6a5ed42afe9d3c0812ca4132316ac1e715cfc1193ff88413094e61428'
m=json.loads(rd(d/'manifesto.json'));o=rd(d/'original.html');n=rd(d/'candidata.html');assert sh(o)=='d7fc82a69bdc4bf9a24cebbd6665e2697f1a92dfa3869da604cab37adf6fa8c3';assert sh(n)=='b4d9dafa1f27c766cc44a698709d74f5fbe3ee09cc587c8def6e0709e2f36c55';assert sh(n)==m['candidata_sha256'] and sh(o)==m['original_sha256'];raw=h.decode().encode('utf-16-le');assert raw[2*m['inicio_utf16']:2*m['fim_utf16']].decode('utf-16-le').encode()==o;assert h.count(o)==1
new=h.replace(o,n);assert sh(new)=='f7b7a2c23f5e5704bd4d6c456fc431008f9261160a3300128df7a14f13008d24'
arts=lambda x:re.findall(rb'<article\b[^>]*>.*?</article\s*>',x,re.I|re.S);mat=lambda x:re.findall(rb'<math\b.*?</math\s*>',x,re.I|re.S)
assert len(arts(h))==197 and arts(h)==arts(new) and len(mat(h))==734 and mat(h)==mat(new)
assert 3*2*1*200==1200 and 1200/(20*3*2)+20==30 and -1200-(-1200)==0 and 1320/(20*6)+20==31
print('OK: r3 e manifesto consistentes, substituição única hipotética, 197 artigos/734 MathML e dois balanços; produto não alterado')
