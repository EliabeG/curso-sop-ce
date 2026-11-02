from pathlib import Path
from decimal import Decimal as D
from fractions import Fraction as F
import hashlib,json,re
r=Path('auditoria/termodinamica/evidencias/QA-09');ps=['candidata-fun01-gases-r23-next-theory-20261030','candidata-fun01-liquido-r23-next-theory-20261030','candidata-fun01-gravidade-r23-next-theory-20261030'];sha=lambda b:hashlib.sha256(b).hexdigest()
h=(r/'aplicacao-resumo-glossario-r23-r1/resultado/depois-aula.html').read_bytes();i=(r/'inventario-r23.json').read_bytes();assert sha(h)=='f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d' and sha(i)=='ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e'
s=h.decode();u=s.encode('utf-16-le');o=u[2*107020:2*111548].decode('utf-16-le');assert sha(o.encode())=='6a58642fcfbbe49b936c53ea8be9c679fa45607ac3e200fcaf836e12bd1c7a2e'
subs=[]
for p in ps:
 p=r/p;m=json.loads((p/'manifesto.json').read_text());c=(p/'candidata.html').read_text().removesuffix('\n');assert (p/'original.html').read_text().removesuffix('\n')==o and sha(c.encode())==m['candidata_sha256'];t=o
 for x in m['substituicoes']:
  assert o.count(x['antes'])==1 and t.count(x['antes'])==1
  pos=o.index(x['antes']);subs.append((pos,pos+len(x['antes']),x['antes'],x['depois']));t=t.replace(x['antes'],x['depois'])
 assert t==c
subs.sort();assert all(subs[k][1]<=subs[k+1][0] for k in range(len(subs)-1))
t=o
for _,_,a,b in subs: assert t.count(a)==1;t=t.replace(a,b)
assert s.count(o)==1;out=s.replace(o,t)
for pat in [r'<math\b[^>]*>.*?</math>',r'<article\b[^>]*>.*?</article>',r'\bhref="[^"]*"',r'\bid="[^"]*"']:
 x=re.findall(pat,s,re.S);assert x==re.findall(pat,out,re.S);print(pat,len(x))
assert D(80)*D('.25')==D(160)*D('.125')==20
assert F(10)/(F(50,30))==6 and F(10)!=6
assert -1+D('.1')*10*2==1
print('alterações não sobrepostas:',len(subs));print('sha bloco combinado',sha(t.encode()));print('sha HTML combinado',sha(out.encode()));print('ok: identidade e combinação sem gravação')
