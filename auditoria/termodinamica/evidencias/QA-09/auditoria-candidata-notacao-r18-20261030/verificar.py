from pathlib import Path
import hashlib,json,re
root=Path('auditoria/termodinamica/evidencias/QA-09')
p=root/'candidata-notacao-propriedades-r18-20261030'
m=json.loads((p/'manifesto.json').read_text())
sha=lambda s:hashlib.sha256(s).hexdigest()
h=Path(m['fonte']).read_bytes()
assert sha(h)==m['fonte_sha256']
assert sha(Path(m['inventario']).read_bytes())==m['inventario_sha256']
s=h.decode(); su=s.encode('utf-16-le'); a,b=m['inicio_utf16'],m['fim_utf16']
orig=su[2*a:2*b].decode('utf-16-le'); cand=(p/'candidata.html').read_text().removesuffix('\n'); original=(p/'original.html').read_text().removesuffix('\n')
assert orig==original and sha(orig.encode())==m['original_sha256'] and sha(cand.encode())==m['candidata_sha256']
assert orig.count(m['antes'])==1 and cand==orig.replace(m['antes'],m['depois'])
assert s.count(orig)==1
out=s.replace(orig,cand)
assert sha(out.encode())=='9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65'
for pattern in [r'<math\b[^>]*>.*?</math>',r'<article\b[^>]*>.*?</article>',r'\bhref="[^"]*"',r'\bid="[^"]*"']:
 old=re.findall(pattern,s,re.S);new=re.findall(pattern,out,re.S);assert old==new
 print(pattern, len(old))
print('ok: alteração textual única; fontes, fórmulas, artigos, IDs e links intactos em memória')
