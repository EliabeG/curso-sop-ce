#!/usr/bin/env python3
"""Checagem independente somente leitura; não decide sozinho interpretação textual."""
from pathlib import Path
import hashlib,json,math
sha=lambda b:hashlib.sha256(b).hexdigest()
q=Path('auditoria/termodinamica/evidencias/QA-09');d=q/'revisao-r28-reference-2'
h=Path('modulos/e1-termodinamica.html').read_bytes();assert sha(h)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'
assert sha((q/'inventario-r27.json').read_bytes())=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
a=(d/'identidades.json').read_bytes();assert sha(a)=='a2d2c205016a3d2fdc1e73b3e0ecd358d447cc66573a71f48ddeb8b3ff24b6b8';rows=json.loads(a);u=h.decode().encode('utf-16-le')
assert len(rows)==4
for r in rows:
 s=u[2*r['start']:2*r['end']].decode('utf-16-le').encode();assert sha(s)==r['sha'];print(r['id'],r['start'],r['end'],r['sha'])
F1,F2=10000*.005,30000*.005;average=(F1+F2)/.01
assert (F1,F2,average)==(50,150,20000)
cv,cp,dt=.718,1.005,100
assert abs(cv*dt-71.8)<1e-10 and abs(cp*dt-100.5)<1e-10
sgen=.287*math.log(2);assert abs(sgen-.1989332408207043)<1e-12
print('forças N, pressão média Pa:',F1,F2,average)
print('calor em kJ, isocórico/isobárico:',cv*dt,cp*dt)
print('entropia kJ/K:',sgen)
