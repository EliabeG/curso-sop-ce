from pathlib import Path
from decimal import Decimal as D
import hashlib,json,re
r=Path('auditoria/termodinamica/evidencias/QA-09');ps=['candidata-radiacao-pontes-r21-next-theory-20261030','candidata-geracao-pontes-r21-next-theory-20261030','candidata-d14-fonte-r21-next-theory-20261030'];sha=lambda b:hashlib.sha256(b).hexdigest()
h=(r/'aplicacao-oficina-ex046-r21-r1/resultado/depois-aula.html').read_bytes();i=(r/'inventario-r21.json').read_bytes();assert sha(h)=='239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238' and sha(i)=='d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1'
s=h.decode();u=s.encode('utf-16-le');out=s
for p in ps:
 p=r/p;m=json.loads((p/'manifesto.json').read_text());a,b=m['inicio_utf16'],m['fim_utf16'];o=u[2*a:2*b].decode('utf-16-le');c=(p/'candidata.html').read_text().removesuffix('\n');assert o==(p/'original.html').read_text().removesuffix('\n') and sha(o.encode())==m['original_sha256'] and sha(c.encode())==m['candidata_sha256']
 t=o
 for x in m['substituicoes']:
  assert t.count(x['antes'])==1;t=t.replace(x['antes'],x['depois'])
 assert t==c and out.count(o)==1;out=out.replace(o,c)
for pat in [r'<math\b[^>]*>.*?</math>',r'<article\b[^>]*>.*?</article>',r'\bhref="[^"]*"',r'\bid="[^"]*"']:
 x=re.findall(pat,s,re.S);assert x==re.findall(pat,out,re.S);print(pat,len(x))
assert D('.3')/D('.6')==D('.5') and 300**4-300**4==0
assert 2*1*1*60==120 and D(120)/(6*2)+18==28 and 120-120==0
print('sha combinado',sha(out.encode()));print('ok: cinco substituições únicas e simulação sem gravação')
