#!/usr/bin/env python3
"""Confere o ledger em cópia mínima descartável; altera apenas arquivos da cópia."""
from pathlib import Path
from hashlib import sha256
from tempfile import TemporaryDirectory
import subprocess, json
root=Path('.').resolve()
P=Path('auditoria/termodinamica/evidencias/QA-09/ledger-r15-parcial-r1')
files=[Path('modulos/e1-termodinamica.html'),Path('formulas/termodinamica.html'),Path('auditoria/termodinamica/evidencias/QA-09/inventario-r15.json'),Path('auditoria/termodinamica/pareceres/QA-09-aplicacao-wika-r15-auditoria-independente-20261030.md'),Path('auditoria/termodinamica/evidencias/QA-09/aplicacao-wika-r15-r1/entrega-r1.md'),P/'ledger.py',P/'ledger.json']
with TemporaryDirectory(prefix='auditar-ledger-r15-') as t:
 tmp=Path(t)
 for p in files:
  dst=tmp/p;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((root/p).read_bytes())
 def run():return subprocess.run(['python3',str(P/'ledger.py'),'--verificar',str(P/'ledger.json')],cwd=tmp,capture_output=True,text=True)
 first=run();assert first.returncode==0,first.stderr
 obj=json.loads(first.stdout);assert obj['ok'] and obj['registros_integrados']==1 and obj['padrao']=='pendente_de_integracao'
 changes={}
 for p in files:
  if p==P/'ledger.py': continue
  path=tmp/p; b=path.read_bytes()
  if p==P/'ledger.json':
   x=json.loads(b);x['registros_explicitamente_revisados'][0]['estado']='aprovado_global';path.write_text(json.dumps(x),encoding='utf-8')
  else:path.write_bytes(b+b'\nTESTE DE ALTERACAO\n')
  result=run();assert result.returncode!=0,(str(p),result.stdout)
  changes[str(p)]={'rejeitado':True,'motivo':result.stderr.strip()}
  path.write_bytes(b)
 assert run().returncode==0
 print(json.dumps({'ok':True,'casos_rejeitados':changes,'fonte_intocada':True,'escopo':'Somente arquivos e mutações declarados; não comprova ausência de todas as falhas.'},ensure_ascii=False,indent=2))
