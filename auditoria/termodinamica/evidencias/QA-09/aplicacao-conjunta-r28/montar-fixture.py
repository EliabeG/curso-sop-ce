#!/usr/bin/env python3
"""Copia ao /tmp somente produto e dependências locais do inventário; nunca produto real."""
from pathlib import Path
import json,shutil,sys
root=Path.cwd().resolve();dst=Path(sys.argv[1]).resolve();assert dst.parent==Path('/tmp') and not dst.exists();dst.mkdir()
for name in ['modulos','formulas','assets','auditoria/termodinamica/inventario']:
 a=root/name;b=dst/name;b.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(a,b)
q='auditoria/termodinamica/evidencias/QA-09/'
files={'index.html','auditoria/termodinamica/pareceres/QA-09-aplicacao-carnot-flashcards-r27-auditoria-independente-20261030.md',q+'inventario-r27.json',q+'inventariar-r28.mjs'}
def collect(x):
 if isinstance(x,dict):
  for v in x.values():collect(v)
 elif isinstance(x,list):
  for v in x:collect(v)
 elif isinstance(x,str) and x.startswith(('downloads/','auditoria/')):
  path=x.split('#')[0].split('?')[0]
  if (root/path).is_file():files.add(path)
collect(json.loads((root/'auditoria/termodinamica/inventario/inventario-questoes.json').read_text()))
for name in files:
 a=root/name;b=dst/name;b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(a,b)
for name in ['aplicacao-conjunta-r28','candidata-pressao-media-r28','candidata-substancias-ciclos-r28','candidata-fichas-maquinas-r28-20261030','auditoria-candidata-pressao-r28','auditoria-candidata-substancias-r28','auditoria-candidata-fichas-r28']:
 a=root/q/name;b=dst/q/name;b.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(a,b)
print('fixture criada',dst,'arquivos de dependência',len(files))
