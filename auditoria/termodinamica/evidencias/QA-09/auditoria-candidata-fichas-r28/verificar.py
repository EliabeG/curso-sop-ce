from pathlib import Path
from html import unescape
from html.parser import HTMLParser
from xml.etree import ElementTree as E
import hashlib,json,re
p=Path('auditoria/termodinamica/evidencias/QA-09/candidata-fichas-maquinas-r28-20261030');m=json.loads((p/'manifesto.json').read_text());sha=lambda x:hashlib.sha256(x).hexdigest();h=Path(m['formulario']).read_bytes();i=Path(m['inventario']).read_bytes();assert sha(h)==m['formulario_sha256'] and sha(i)==m['inventario_sha256']
for f in m['pareceres']:assert sha(Path(f['path']).read_bytes())==f['sha256']
s=h.decode();u=s.encode('utf-16-le');out=s
for x in m['itens']:
 a,b=x['inicio_utf16'],x['fim_utf16'];o=u[2*a:2*b].decode('utf-16-le');c=(p/f'{x["ficha"]}-candidata.html').read_text().removesuffix('\n');assert (p/f'{x["ficha"]}-original.html').read_text().removesuffix('\n')==o and sha(o.encode())==x['original_sha256'] and sha(c.encode())==x['candidata_sha256'];t=o
 for d in x['mudancas']:
  assert t.count(d['antes'])==2;t=t.replace(d['antes'],d['depois'])
 assert t==c and out.count(o)==1;out=out.replace(o,c)
for pattern in [r'<math\b[^>]*>.*?</math>',r'\bhref="[^\"]*"',r'\bid="[^\"]*"',r'\baria-[\w-]+="[^\"]*"']:
 a=re.findall(pattern,s,re.S);assert a==re.findall(pattern,out,re.S);print(pattern,len(a))
old=re.findall(r'<article\b[^>]*>.*?</article>',s,re.S);new=re.findall(r'<article\b[^>]*>.*?</article>',out,re.S);assert len(old)==len(new)==100 and sum(a!=b for a,b in zip(old,new))==len(m['itens'])
print('itens',[x['ficha'] for x in m['itens']]);print('formulario hipotetico',sha(out.encode()));print('ok: substituições em cartão e busca, demais cartões e atributos preservados; nenhuma gravação de produto')
