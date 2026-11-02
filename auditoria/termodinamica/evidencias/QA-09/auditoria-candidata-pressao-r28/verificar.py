#!/usr/bin/env python3
"""Independente, somente leitura; não testa apresentação ou ciência por si."""
from pathlib import Path
import hashlib,json,re
s=lambda b:hashlib.sha256(b).hexdigest()
q=Path('auditoria/termodinamica/evidencias/QA-09');d=q/'candidata-pressao-media-r28'; raw=(d/'manifesto.json').read_bytes();assert s(raw)=='70a4aa3e86d7604ee1281d493d702db8678b6517d88e8fbc9f61b7acde61e718';m=json.loads(raw)
h=Path(m['fonte']).read_bytes();assert s(h)==m['fonte_sha256']=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49';assert s(Path(m['inventario']).read_bytes())==m['inventario_sha256']=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
a=(d/'original.html').read_bytes();b=(d/'candidata.html').read_bytes();assert a.endswith(b'\n') and b.endswith(b'\n');a=a[:-1];b=b[:-1];assert s(a)==m['original_sha256'];assert s(b)==m['candidata_sha256'];text=h.decode();u=text.encode('utf-16-le');assert u[2*m['inicio_utf16']:2*m['fim_utf16']].decode('utf-16-le')==a.decode();assert text.count(a.decode())==1;assert a.decode().count(m['antes'])==1;assert a.decode().replace(m['antes'],m['depois'])==b.decode()
out=(u[:2*m['inicio_utf16']]+b.decode().encode('utf-16-le')+u[2*m['fim_utf16']:]).decode('utf-16-le');assert s(out.encode())=='3486b562ad7e8ec563fbf191775642628617f0436fe831b5e3a91e4f503bf49c'
for pattern in (r'<article\b[\s\S]*?</article>',r'<math\b[\s\S]*?</math>',r'\b(?:id|href|src|aria-controls|aria-labelledby|aria-describedby)="[^"]*"'):
 old=re.findall(pattern,text);new=re.findall(pattern,out);assert old==new;print('preservados:',len(old),pattern)
assert 200/.01==20000 and (10000*.005+30000*.005)/.01==20000
print('ok: contêiner, substituição, hipotético, pressão média e contramodelo; sem gravação do produto')
