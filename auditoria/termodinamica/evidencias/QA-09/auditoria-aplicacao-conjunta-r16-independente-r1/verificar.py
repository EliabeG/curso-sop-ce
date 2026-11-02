#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,math
q=Path('auditoria/termodinamica/evidencias/QA-09'); r=q/'aplicacao-conjunta-r16-r1/resultado'; t=q/'candidatas-teoria-ciclos-r15-20261030'; f=q/'candidatas-fichas-89-90-r15-20261030'
def sh(b): return hashlib.sha256(b).hexdigest()
def read(p): return p.read_bytes()
a,aa=read(r/'antes-aula.html'),read(r/'depois-aula.html'); b,bb=read(r/'antes-formulario.html'),read(r/'depois-formulario.html')
assert sh(a)=='f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e'
assert sh(aa)=='55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23' and aa==read(Path('modulos/e1-termodinamica.html'))
assert sh(b)=='3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce'
assert sh(bb)=='dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d' and bb==read(Path('formulas/termodinamica.html'))
ed=json.loads(read(r/'edicoes-aplicadas.json')); assert len(ed)==5
for e in ed:
 id=e['id']; p=t if id.startswith('base-') else f; name=id if id.startswith('base-') else ('89' if id=='formula-politropico' else '90')
 old=read(p/(name+'-original.html')); new=read(p/(name+'-candidata.html')); assert old.endswith(b'\n') and new.endswith(b'\n'); old=old[:-1]; new=new[:-1]
 assert sh(old)==e['original_sha256'] and sh(new)==e['candidata_sha256']
 if p==t: assert a.count(old)==1; a=a.replace(old,new)
 else: assert b.count(old)==1; b=b.replace(old,new)
assert a==aa and b==bb
article=lambda x:re.findall(rb'<article\b[^>]*>.*?</article\s*>',x,re.I|re.S)
r0=read(r/'antes-aula.html'); assert len(article(r0))==197 and article(r0)==article(aa)
c0=article(read(r/'antes-formulario.html')); c1=article(bb); assert len(c0)==len(c1)==100
assert sum(x!=y for x,y in zip(c0,c1))==2
for raw,new,count in [(r0,aa,734),(read(r/'antes-formulario.html'),bb,191)]:
 m0=re.findall(rb'<math\b.*?</math\s*>',raw,re.I|re.S); m1=re.findall(rb'<math\b.*?</math\s*>',new,re.I|re.S); assert len(m0)==count and m0==m1
io=json.loads(read(r/'inventario-oficial-antes.json')); inn=json.loads(read(Path('auditoria/termodinamica/inventario/inventario-questoes.json'))); assert len(io['itens'])==197 and io['itens']==inn['itens']
assert io['fonte']['sha256']==sh(r0) and inn['fonte']['sha256']==sh(aa)
assert sh(read(q/'inventario-r16.json'))=='2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd'
assert sh(read(q/'mapa-correspondencia-inventario-r15-r16-r1.json'))=='a3edb9fab577c58e5b3df4831ee8cfb09d8e8b39bf92d1efcd5e0a5f39b2d4d0'
R=.287;T=300;ratio=4;n=1.3;w=n/(n-1)*R*T*(ratio**((n-1)/n)-1); wi=R*T*math.log(ratio)
assert abs(w-140.662226)<.001 and abs(wi-119.359944)<.00001
assert abs((400-300)/400-.25)<1e-12 and 120/400==.3 and 120/300==.4
assert 300/(400-300)==3 and 20/(100-20)==.25
print('OK: cinco candidatas reproduzem as duas páginas; 197 artigos e registros, 98 fichas, 734/191 MathML; exemplos e hipóteses numéricas conferidos; w_p=%.6f e w_iso=%.6f kJ/kg'%(w,wi))
