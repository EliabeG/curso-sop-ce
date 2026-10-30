#!/usr/bin/env python3
"""Verifica identidade do ledger e testes de adulteração somente em diretório temporário."""
import tempfile, pathlib, json, hashlib, shutil, subprocess
root=pathlib.Path.cwd(); ledgerp='auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r1/ledger.json'; scriptp='auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r1/ledger.py'
l=json.loads((root/ledgerp).read_text()); inv=json.loads((root/l['fotografia']['inventario']).read_text()); rows=l['registros_explicitamente_revisados']; expected={'ficha-080','cop','valvula','compressor','trocador','pressao-entrada-saida','pressao-1-3','resumo'}
assert len(rows)==8 and {x['id_edicao'] for x in rows}==expected and len({x['indice_base_zero'] for x in rows})==8
for row in rows:
 item=inv['ocorrencias'][row['indice_base_zero']]
 for a,b in [('id_inventario','id'),('arquivo','arquivo'),('secao','secao'),('ancora','ancora'),('tag','tag'),('tipo','tipo'),('inicio_utf16','inicio_utf16'),('fim_utf16','fim_utf16'),('sha256_ocorrencia','sha256_fragmento')]:assert row[a]==item[b],(row['id_edicao'],a)
 raw=(root/row['arquivo']).read_text().encode('utf-16-le'); seg=raw[row['inicio_utf16']*2:row['fim_utf16']*2].decode('utf-16-le').encode('utf-8'); assert hashlib.sha256(seg).hexdigest()==row['sha256_fragmento_html'];assert row['estado']=='conferido_no_escopo_localizado' and 'não abrange' in row['alcance']
assert len(inv['ocorrencias'])==11397 and len(inv['referencias'])==815 and len(inv['recursos'])==138 and len(inv['ativos_especificos'])==6 and len(inv['artigos_excluidos'])==197
cfg=json.loads((root/l['fontes']['configuracao']).read_text()); files={ledgerp,scriptp,l['fotografia']['inventario'],l['fontes']['configuracao'],l['fontes']['edicoes'],l['fontes']['parecer'],*l['fotografia']['documentos']}; files.update(x['candidata'] for x in cfg['edicoes'])
with tempfile.TemporaryDirectory() as tmp:
 d=pathlib.Path(tmp)
 for x in files:(d/x).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/x,d/x)
 def run():return subprocess.run(['python3',str(d/scriptp),'--verificar',ledgerp],cwd=d,text=True,capture_output=True)
 assert run().returncode==0
 def corrupt(path,mutate):
  p=d/path;original=p.read_bytes();p.write_bytes(mutate(original));r=run();p.write_bytes(original);assert r.returncode!=0,(path,r.stdout,r.stderr);return r.stderr.strip().splitlines()[-1]
 def corrupt_ledger(b):
  o=json.loads(b);o['registros_explicitamente_revisados'][0]['estado']='aprovado_integral';return json.dumps(o).encode()
 tests={'ledger_estado':corrupt(ledgerp,corrupt_ledger),'html':corrupt('modulos/e1-termodinamica.html',lambda x:x+b' '),'inventario':corrupt(l['fotografia']['inventario'],lambda x:x+b' '),'parecer':corrupt(l['fontes']['parecer'],lambda x:x+b' '),'candidata':corrupt(cfg['edicoes'][0]['candidata'],lambda x:x+b' ')}
print(json.dumps({'ok':True,'linhas':len(rows),'colecoes':[11397,815,138,6],'adulteracoes_rejeitadas':tests,'limite':'Identidade e integridade; nao revisa a ciencia nem comprova ausencia total de modificacao deliberada.'},ensure_ascii=False,indent=2))
