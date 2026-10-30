#!/usr/bin/env python3
"""Candidatas 89–90: ensaio independente em memória, somente leitura."""
import hashlib, json, math, re
from pathlib import Path
root=Path(__file__).resolve().parents[5]
base=root/'auditoria/termodinamica/evidencias/QA-09/candidatas-fichas-89-90-r15-20261030'
sha=lambda s:hashlib.sha256(s).hexdigest()
h=(root/'formulas/termodinamica.html').read_bytes()
assert sha(h)=='3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce'
mb=(base/'manifesto.json').read_bytes(); assert sha(mb)=='093609d634e7e875aa51e5999494fa3ec2642be5c63c91e8a8c3a58de6a13cdf'
m=json.loads(mb); result=h.decode(); old=[]; new=[]
for i in m['itens']:
 a=(base/f"{i['ficha']}-original.html").read_bytes().removesuffix(b'\n').decode()
 b=(base/f"{i['ficha']}-candidata.html").read_bytes().removesuffix(b'\n').decode()
 assert sha(a.encode())==i['original_sha256'] and sha(b.encode())==i['candidata_sha256']
 u=h.decode().encode('utf-16-le'); assert u[2*i['inicio_utf16']:2*i['fim_utf16']].decode('utf-16-le')==a
 assert result.count(a)==1 and a.count('class="formula-card"')==1 and b.count('class="formula-card"')==1
 changed=a
 for d in i['mudancas']:
  assert changed.count(d['antes'])==2
  changed=changed.replace(d['antes'],d['depois'])
 assert changed==b
 assert re.findall(r'<math\b.*?</math>',a,re.S)==re.findall(r'<math\b.*?</math>',b,re.S)
 old.append(a);new.append(b);result=result.replace(a,b,1)
assert sha(result.encode())=='dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d'
for a,b in zip(old,new): assert result.count(b)==1;result=result.replace(b,a,1)
assert result.encode()==h
rt=.287*300
for n,expected in [(2,172.2),(.5,64.575)]:
 w=n/(n-1)*rt*(4**((n-1)/n)-1)
 assert abs(w-expected)<1e-10
iso=rt*math.log(4)
assert abs(iso-119.35994449242257)<1e-10
for n in (.999999,1.000001): assert abs(n/(n-1)*rt*(4**((n-1)/n)-1)-iso)<.0001
assert abs((iso-30)+30-iso)<1e-12 and abs(-iso/300+.287*math.log(4))<1e-12
print(json.dumps({'ok':True,'candidatas':2,'resultado_reversivel_em_memoria':True,'isotermica_kJkg':iso}))
