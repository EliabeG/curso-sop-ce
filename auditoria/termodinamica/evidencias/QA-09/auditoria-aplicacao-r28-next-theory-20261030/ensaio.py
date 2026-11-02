#!/usr/bin/env python3
"""Repete a aplicação numa fixture descartável, sem editar a árvore de trabalho."""
from pathlib import Path
import subprocess, uuid, shutil, hashlib
r=Path.cwd();q=Path('auditoria/termodinamica/evidencias/QA-09');p=q/'aplicacao-conjunta-r28/resultado';d=Path('/tmp')/('qa28-auditor-'+uuid.uuid4().hex);script=d.with_suffix('.py')
try:
 s=(r/q/'aplicacao-conjunta-r28/montar-fixture.py').read_text();assert s.count('shutil.copytree(a,b)')==2
 script.write_text(s.replace('shutil.copytree(a,b)','shutil.copytree(a,b,dirs_exist_ok=True)'))
 subprocess.run(['python3',str(script),str(d)],check=True)
 for a,b in [('antes-aula.html','modulos/e1-termodinamica.html'),('antes-formulario.html','formulas/termodinamica.html'),('inventario-oficial-antes.json','auditoria/termodinamica/inventario/inventario-questoes.json'),('inventario-oficial-antes.md','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md')]:shutil.copy2(r/p/a,d/b)
 shutil.rmtree(d/p)
 for n in ['inventario-r28.json','mapa-correspondencia-inventario-r27-r28-r1.json']:(d/q/n).unlink(missing_ok=True)
 subprocess.run(['node',str(q/'aplicacao-conjunta-r28/aplicar.mjs'),'--apply'],cwd=d,check=True)
 for f in ['modulos/e1-termodinamica.html','formulas/termodinamica.html',str(q/'inventario-r28.json'),str(q/'mapa-correspondencia-inventario-r27-r28-r1.json'),'auditoria/termodinamica/inventario/inventario-questoes.json','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md']:
  x=hashlib.sha256((d/f).read_bytes()).hexdigest();y=hashlib.sha256((r/f).read_bytes()).hexdigest();assert x==y,(f,x,y);print('idêntico',f,x)
finally:
 script.unlink(missing_ok=True)
 if d.exists():shutil.rmtree(d)
