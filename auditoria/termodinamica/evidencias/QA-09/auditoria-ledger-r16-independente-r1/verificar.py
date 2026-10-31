#!/usr/bin/env python3
"""Audita ledger r16 com testes negativos em árvore mínima temporária."""
import copy, hashlib, json, shutil, subprocess, tempfile
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[5]; Q='auditoria/termodinamica/evidencias/QA-09/';L=Q+'ledger-r16-parcial-r1/'
sha=lambda x:hashlib.sha256(x).hexdigest();load=lambda x:json.loads((root/x).read_bytes())
checks={L+'ledger.json':'1e538c61bbee7972972d82419c4237de4f5f91728e4cf95cabb53724021d65a5',L+'ledger.mjs':'5f8d7967a26d0409c90f29316e2de1018b6df67feff5ba419364e958946d847c',L+'reconciliacao-ex001-005-d26-28.md':'0d60c27750ad5fba5991881480c2c6e25f3f30444681b8aa4aada0a89e8122b6',Q+'inventario-r16.json':'2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd','modulos/e1-termodinamica.html':'55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23'}
for p,h in checks.items():assert sha((root/p).read_bytes())==h
ledger=load(L+'ledger.json');r16=load(Q+'inventario-r16.json');r9=load(Q+'inventario-r9.json')
assert [(k,ledger['colecoes'][k]['total'],ledger['colecoes'][k]['estado_padrao']) for k in ['ocorrencias','referencias','recursos','ativos_especificos']]==[(k,n,'pendente_de_integracao') for k,n in [('ocorrencias',11400),('referencias',816),('recursos',138),('ativos_especificos',6)]]
assert ledger['estado_global']=='QA09_EM_CORRECAO_NAO_APROVADO'
rows=ledger['registros_explicitamente_revisados'];assert [x['id_local'] for x in rows]==['EX-001','EX-002','EX-003','EX-004','EX-005','D26','D27','D28']
cur=(root/'modulos/e1-termodinamica.html').read_text().encode('utf-16-le')
old=(root/(Q+'aplicacao-pressao-fichas-r10-r1/antes-aula.html')).read_text().encode('utf-16-le')
for row in rows:
 a=row['identidade_r9'];b=row['identidade_r16'];assert r16['ocorrencias'][row['indice_base_zero']]==b
 assert len([x for x in r9['ocorrencias'] if x==a])==1
 fa=old[2*a['inicio_utf16']:2*a['fim_utf16']];fb=cur[2*b['inicio_utf16']:2*b['fim_utf16']]
 assert fa==fb and sha(fa.decode('utf-16-le').encode())==a['sha256_fragmento']==b['sha256_fragmento']
 assert row['estado']=='conferido_no_escopo_localizado' and row['auditor_historico']=='/root/next_graphics' and row['responsavel_revalidacao']=='/root/planning'
 assert sha((root/row['parecer_historico']).read_bytes())==row['parecer_historico_sha256'] and sha((root/row['reconciliacao']).read_bytes())==row['reconciliacao_sha256']
assert F(9,1)/F(1,100)==F(9,2)/F(5,1000)==900
assert -10+120==110 and 10+F(30,40)*(90-10)==70 and F(900-400,2400-400)==F(1,4)
assert F(82,1000)*320/F(2624,100)==1
assert abs(D('8.31446261815324')*D(320)/(D('101.325')*D('26.24'))-D('1.000699586'))<D('0.000000001')
assert 600+900-20==1480 and F(1480,3200)==F(4625,10000) and 3200-1480==1720
assert F(700-300,2300-300)==F(1,5) and (10-2)*250==2000
assert (F(2,10)+500*(F(4,10000)-F(6,10000)))/200*10**6==500
assert (F(4,10000)+F(2,10)/500)*10**6==800
paths=[*checks, 'formulas/termodinamica.html',Q+'inventario-r9.json',Q+'aplicacao-pressao-fichas-r10-r1/antes-aula.html','auditoria/termodinamica/pareceres/QA-09-exemplos001-005-diagnosticos26-28-r9-auditoria-independente-20261030.md','auditoria/termodinamica/inventario/validar-inventario.mjs']
with tempfile.TemporaryDirectory(prefix='qa-ledger-r16-') as temp:
 t=Path(temp)
 for p in set(paths):
  dest=t/p;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/p,dest)
 def run():return subprocess.run(['node',L+'ledger.mjs','--verificar',L+'ledger.json'],cwd=t,capture_output=True,text=True)
 assert run().returncode==0
 f=t/(L+'ledger.json')
 for mutate in (lambda x:x['registros_explicitamente_revisados'][0].update(estado='aprovado_globalmente'),lambda x:x['registros_explicitamente_revisados'].pop(),lambda x:x['colecoes']['recursos'].update(estado_padrao='aprovado')):
  alter=copy.deepcopy(ledger);mutate(alter);f.write_text(json.dumps(alter));assert run().returncode!=0
 f.write_bytes((root/(L+'ledger.json')).read_bytes())
 for p in ('modulos/e1-termodinamica.html',L+'reconciliacao-ex001-005-d26-28.md','auditoria/termodinamica/inventario/validar-inventario.mjs'):
  dest=t/p;v=dest.read_bytes();dest.write_bytes(v+b'\n');result=run();assert result.returncode!=0 and 'SHA divergente' in result.stderr;dest.write_bytes(v)
 assert run().returncode==0
print(json.dumps({'ok':True,'objetos':8,'negativos_ledger':3,'negativos_versao':3,'base_original_inalterada':True},ensure_ascii=False))
