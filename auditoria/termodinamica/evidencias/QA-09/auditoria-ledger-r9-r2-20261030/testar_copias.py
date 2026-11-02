#!/usr/bin/env python3
"""Replica apenas dependências em diretório temporário e testa violações sem editar fontes."""
import json,shutil,subprocess,tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[5]; d='auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r2/';r1='auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r1/';a='auditoria/termodinamica/evidencias/QA-09/aplicacao-flashcards-ficha80-r1/'
sel=json.loads((root/d/'selecoes.json').read_text()); edits=json.loads((root/a/'edicoes-aplicadas.json').read_text())
files={d+'ledger.py',d+'ledger.json',d+'selecoes.json',d+'verificar-textos.mjs',r1+'ledger.py',r1+'ledger.json',a+'config-r2.json',a+'edicoes-aplicadas.json','auditoria/termodinamica/evidencias/QA-09/inventario-r9.json','auditoria/termodinamica/inventario/validar-inventario.mjs','auditoria/termodinamica/pareceres/QA-09-ledger-r9-parcial-auditoria-independente-20261030.md','auditoria/termodinamica/pareceres/QA-09-aplicacao-flashcards-ficha80-auditoria-independente-20261030.md','modulos/e1-termodinamica.html','formulas/termodinamica.html'}
files.update(e['candidata'] for e in edits);files.update(x['parecer'] for x in sel['registros']);files.update(x['identidade_r9']['arquivo'] for x in sel['registros'] if x['colecao']=='ativos_especificos')
with tempfile.TemporaryDirectory(prefix='qa09-ledger-test-') as t:
 tmp=Path(t)
 for f in files:
  target=tmp/f;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/f,target)
 cmd=['python3',d+'ledger.py','--verificar',d+'ledger.json']
 def run():return subprocess.run(cmd,cwd=tmp,text=True,capture_output=True)
 assert run().returncode==0
 tests=[('ledger',d+'ledger.json'),('selecao',d+'selecoes.json'),('aula','modulos/e1-termodinamica.html'),('formulario','formulas/termodinamica.html'),('parecer','auditoria/termodinamica/pareceres/QA-09-fichas-gases-fases-r9-auditoria-independente-20261030.md'),('ativo','assets/termodinamica/fun02-caminhos-v1.svg'),('script_textos',d+'verificar-textos.mjs')]
 results=[]
 for label,name in tests:
  p=tmp/name;old=p.read_bytes()
  try:
   if label=='ledger':
    j=json.loads(old);j['registros_adicionais'][0]['estado']='achado_aberto';p.write_text(json.dumps(j,ensure_ascii=False))
   else:p.write_bytes(old+b' ')
   z=run();assert z.returncode!=0,label;results.append({'teste':label,'rejeitado':True,'erro':z.stderr.splitlines()[-1] if z.stderr else ''})
  finally:p.write_bytes(old)
 assert run().returncode==0
 print(json.dumps({'ok':True,'copias_alteradas_rejeitadas':results,'original_alterado':False},ensure_ascii=False,indent=2))
