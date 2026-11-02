#!/usr/bin/env python3
"""Testa pré-condições em fixture mínima temporária. Não altera nenhum produto."""
from pathlib import Path
import hashlib,shutil,subprocess,tempfile
root=Path.cwd().resolve();q='auditoria/termodinamica/evidencias/QA-09/';p=q+'aplicacao-pressao-r28/'
files=['modulos/e1-termodinamica.html','formulas/termodinamica.html','auditoria/termodinamica/inventario/validar-inventario.mjs','auditoria/termodinamica/inventario/inventario-questoes.json','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md',q+'inventario-r27.json',q+'inventariar-r28.mjs',p+'aplicar.mjs',p+'mapear.py','auditoria/termodinamica/pareceres/QA-09-aplicacao-carnot-flashcards-r27-auditoria-independente-20261030.md',q+'auditoria-candidata-pressao-r28/parecer.md',q+'candidata-pressao-media-r28/manifesto.json',q+'candidata-pressao-media-r28/original.html',q+'candidata-pressao-media-r28/candidata.html']
with tempfile.TemporaryDirectory(prefix='ensaio-pressao-r28-') as tmp:
 dest=Path(tmp)
 for name in files:
  out=dest/name;out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/name,out)
 cmd=['node',p+'aplicar.mjs','--ensaio']
 ok=subprocess.run(cmd,cwd=dest,text=True,capture_output=True);assert ok.returncode==0,(ok.stdout,ok.stderr);assert '3486b562ad7e8ec563fbf191775642628617f0436fe831b5e3a91e4f503bf49c' in ok.stdout
 print('versão íntegra: simulação passou, sem gravação')
 blocked=subprocess.run(['node',p+'aplicar.mjs','--apply'],cwd=dest,text=True,capture_output=True)
 assert blocked.returncode and 'APLICAÇÃO BLOQUEADA' in blocked.stderr
 assert not (dest/(p+'resultado')).exists()
 print('aplicação bloqueada enquanto aguardamos integração e sinal')
 cases=[('aula','modulos/e1-termodinamica.html','SHA divergente'),('manifesto',q+'candidata-pressao-media-r28/manifesto.json','SHA divergente'),('candidata',q+'candidata-pressao-media-r28/candidata.html','identidade'),('parecer',q+'auditoria-candidata-pressao-r28/parecer.md','SHA divergente')]
 for label,name,message in cases:
  file=dest/name;before=file.read_bytes()
  try:
   file.write_bytes(before+b'alterado')
   r=subprocess.run(cmd,cwd=dest,text=True,capture_output=True)
   assert r.returncode and message in r.stderr,(label,r.stdout,r.stderr)
   assert not (dest/(p+'resultado')).exists()
   assert not (dest/(q+'inventario-r28.json')).exists()
   print(label+': adulteração rejeitada antes de escrita')
  finally:file.write_bytes(before)
