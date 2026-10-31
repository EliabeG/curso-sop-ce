from pathlib import Path
import hashlib,json,re
root=Path('auditoria/termodinamica/evidencias/QA-09')
paths=['candidata-mistura-termica-r19-20261030','candidata-fase-calorimetria-r19-20261030']
sha=lambda x:hashlib.sha256(x).hexdigest()
s=(root/'aplicacao-notacao-fichas-r19-r1/resultado/depois-aula.html').read_text();src=s.encode('utf-16-le')
assert sha(s.encode())=='9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65'
assert sha((root/'inventario-r19.json').read_bytes())=='ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f'
out=s
for path in paths:
 p=root/path;m=json.loads((p/'manifesto.json').read_text());a,b=m['inicio_utf16'],m['fim_utf16'];original=src[2*a:2*b].decode('utf-16-le');candidate=(p/'candidata.html').read_text().removesuffix('\n')
 assert (p/'original.html').read_text().removesuffix('\n')==original and sha(original.encode())==m['original_sha256'] and sha(candidate.encode())==m['candidata_sha256']
 t=original
 for x in m['substituicoes']:
  assert t.count(x['antes'])==1;t=t.replace(x['antes'],x['depois'])
 assert t==candidate and out.count(original)==1
 out=out.replace(original,candidate)
for pattern in [r'<math\b[^>]*>.*?</math>',r'<article\b[^>]*>.*?</article>',r'\bhref="[^"]*"',r'\bid="[^"]*"']:
 old=re.findall(pattern,s,re.S);assert old==re.findall(pattern,out,re.S);print(pattern,len(old))
print('sha combinado:',sha(out.encode()));print('ok: ambos os blocos alterados apenas como manifesto; simulação sem gravação')
