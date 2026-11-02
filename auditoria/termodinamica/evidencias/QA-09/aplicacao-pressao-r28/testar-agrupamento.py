#!/usr/bin/env python3
"""Testa simulação e proteção contra sobreposição em fixture mínima descartável."""
from pathlib import Path
import json,shutil,subprocess,tempfile
root=Path.cwd().resolve();q='auditoria/termodinamica/evidencias/QA-09/';p=q+'aplicacao-pressao-r28/'
files=['modulos/e1-termodinamica.html','formulas/termodinamica.html','auditoria/termodinamica/inventario/validar-inventario.mjs',q+'inventario-r27.json',p+'agrupamento.json',p+'simular-agrupamento.mjs',q+'auditoria-candidata-pressao-r28/parecer.md',q+'candidata-pressao-media-r28/manifesto.json',q+'candidata-pressao-media-r28/original.html',q+'candidata-pressao-media-r28/candidata.html']
with tempfile.TemporaryDirectory(prefix='agrupa-pressao-r28-') as tmp:
 dest=Path(tmp)
 for name in files:
  out=dest/name;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/name,out)
 cmd=['node',p+'simular-agrupamento.mjs'];r=subprocess.run(cmd,cwd=dest,text=True,capture_output=True);assert r.returncode==0,(r.stdout,r.stderr);print('configuração parcial válida: simulação sem escrita')
 cfg=dest/(p+'agrupamento.json'); data=json.loads(cfg.read_text());data['candidatas'].append(data['candidatas'][0]);cfg.write_text(json.dumps(data));r=subprocess.run(cmd,cwd=dest,text=True,capture_output=True);assert r.returncode and 'sobreposição' in r.stderr,(r.stdout,r.stderr);print('candidata duplicada: sobreposição rejeitada')
 assert not (dest/(q+'inventario-r28.json')).exists() and not (dest/(p+'resultado')).exists()
