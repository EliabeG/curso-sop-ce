#!/usr/bin/env python3
"""Cria somente entradas sintéticas de ensaio; use em cópia descartável da raiz."""
import hashlib,json,pathlib,sys
if sys.argv[1:] != ['--copia-descartavel']:
 raise SystemExit('Obrigatório --copia-descartavel, em uma cópia isolada do repositório.')
r=pathlib.Path('.'); d=r/'auditoria/termodinamica/evidencias/QA-09'; p=d/'aplicacao-razao-percentual-r1'; q=d/'candidata-razao-percentual-20261030';h=(r/'modulos/e1-termodinamica.html').read_text().encode('utf-16-le'); inv=json.loads((d/'inventario-r7.json').read_text());entries=[]
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def add(id,orig,cand):
 a=orig.read_text().removesuffix('\n');b=cand.read_text().removesuffix('\n');entries.append({'id':id,'original':str(orig),'candidata':str(cand),'original_sha256':sha(a),'candidata_sha256':sha(b)})
add('percentual',q/'original.html',q/'candidata.html')
for pos in [31291,412780]:
 rec=next(x for x in inv['ocorrencias'] if x['arquivo']=='modulos/e1-termodinamica.html' and x['tipo']=='texto_direto' and x['inicio_utf16']==pos)
 a=h[2*rec['inicio_utf16']:2*rec['fim_utf16']].decode('utf-16-le');assert a.endswith('</p>');b=a[:-4]+' [ensaio isolado]</p>'
 f=p/f'sintetico-{pos}-original.html';g=p/f'sintetico-{pos}-candidata.html'
 if f.exists() or g.exists():raise SystemExit('Ensaio já existe')
 f.write_text(a+'\n');g.write_text(b+'\n');add(f'sintetico-{pos}',f,g)
c=p/'ensaio-config.json'
if c.exists():raise SystemExit('Ensaio já existe')
c.write_text(json.dumps({'edicoes':entries},indent=2)+'\n')
print(c)
