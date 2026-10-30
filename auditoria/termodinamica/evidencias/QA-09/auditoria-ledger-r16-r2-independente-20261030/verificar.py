#!/usr/bin/env python3
"""Confere ledger r2 sobre snapshot r16 e mutações em cópia mínima."""
import collections,copy,hashlib,json,shutil,subprocess,tempfile
from fractions import Fraction as F
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';l=q+'ledger-r16-parcial-r2/';a=q+'ledger-r16-parcial-r1/'
sha=lambda b:hashlib.sha256(b).hexdigest(); read=lambda p:(r/p).read_bytes(); load=lambda p:json.loads(read(p))
fixed={l+'ledger.json':'ae68437b7c45ce6410a37b3b31c03cbb239a0f2e2d2342385e6f5c161abe029f',l+'ledger.mjs':'e3f1c05c57b43a151b9850c65965b8c18b1f37716e1b1a76be8cc9cb97441ba1',l+'reconciliacao-d11-20.md':'57ac4af5846a53853be36593a71777239f21d97239d0eb0b916bdb5dea12c8c8',a+'ledger.json':'1e538c61bbee7972972d82419c4237de4f5f91728e4cf95cabb53724021d65a5',q+'inventario-r16.json':'2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd',q+'aplicacao-conjunta-r16-r1/resultado/depois-aula.html':'55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23'}
for p,digest in fixed.items():assert sha(read(p))==digest
ledger=load(l+'ledger.json');base=load(a+'ledger.json');v12=load(q+'inventario-r12.json');v16=load(q+'inventario-r16.json')
assert ledger['registros_r1']==base['registros_explicitamente_revisados'] and len(ledger['registros_r1'])==8
assert ledger['colecoes']==base['colecoes'] and all(c['estado_padrao']=='pendente_de_integracao' for c in ledger['colecoes'].values())
assert ledger['estado_global']=='QA09_EM_CORRECAO_NAO_APROVADO'
old=read(q+'aplicacao-energyplus-fichas-r13-r1/resultado/antes-aula.html').decode().encode('utf-16-le')
cur=read(q+'aplicacao-conjunta-r16-r1/resultado/depois-aula.html').decode().encode('utf-16-le')
rows=ledger['registros_adicionais'];assert [x['id_local'] for x in rows]==[f'D{n}' for n in range(11,21)]
for row in rows:
 x=row['identidade_r12'];y=row['identidade_r16'];assert v16['ocorrencias'][row['indice_base_zero']]==y
 assert len([i for i in v12['ocorrencias'] if i==x])==1
 p=old[2*x['inicio_utf16']:2*x['fim_utf16']];z=cur[2*y['inicio_utf16']:2*y['fim_utf16']]
 assert p==z and sha(p.decode('utf-16-le').encode())==x['sha256_fragmento']==y['sha256_fragmento']
 assert row['estado']=='conferido_no_escopo_localizado' and row['auditor_historico']=='/root/next_examples' and row['responsavel_revalidacao']=='/root/planning'
 assert sha(read(row['parecer_historico']))==row['parecer_historico_sha256'] and sha(read(row['reconciliacao']))==row['reconciliacao_sha256']
contexts={c['id']:(c['sha256_r12'],c['sha256_r16']) for row in rows for c in row['contextos']}
assert len(contexts)==14 and sum(x!=y for x,y in contexts.values())==1
assert contexts['base-brayton-real']==('ff66d7377eff5357668aae739c6390e23a38ad954acdd1b6af92447575e944a0','9795a00e2a3363aff4d55a6ae06aef91b45a2fe328ae327d42865aeaf685f94c')
assert F(140-50,300)==F(3,10) and F(6,8)==F(3,4) and F(7,10)==1-F(3,10)
assert 2*60==120 and 18+F(120,6*2)==28
assert F(12+24+36,3)==24 and F(2*90+6*30,8)==45 and F(4*80+4*20+2*20-20,10)==42
assert F(1,2)*F(42,10)*20==42 and F(2,10)*334==F(668,10)
assert abs(F(42,334)-F(126,1000))<F(1,2000) and abs(F(2,10)-F(42,334)-F(74,1000))<F(1,2000)
assert F(20*300*60,10**6)/F(500,10**6)==720
assert F(36,3600)==F(1,100) and 1000*10*F(1,100)*15==1500 and F(1500,3000)==F(1,2)
paths=[*fixed,a+'ledger.mjs',a+'reconciliacao-ex001-005-d26-28.md',q+'inventario-r9.json',q+'inventario-r12.json',q+'aplicacao-pressao-fichas-r10-r1/antes-aula.html',q+'aplicacao-energyplus-fichas-r13-r1/resultado/antes-aula.html','formulas/termodinamica.html','auditoria/termodinamica/inventario/validar-inventario.mjs','auditoria/termodinamica/pareceres/QA-09-ledger-r16-parcial-r1-auditoria-independente-20261030.md','auditoria/termodinamica/pareceres/QA-09-diagnosticos11-20-r12-auditoria-independente-20261030.md','auditoria/termodinamica/pareceres/QA-09-aplicacao-conjunta-ciclos-r16-auditoria-independente-20261030.md','auditoria/termodinamica/pareceres/QA-09-exemplos001-005-diagnosticos26-28-r9-auditoria-independente-20261030.md']
with tempfile.TemporaryDirectory(prefix='qa-ledger-r16-r2-') as temp:
 t=Path(temp)
 for p in set(paths):
  dest=t/p;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(r/p,dest)
 dest=t/'modulos/e1-termodinamica.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(read(q+'aplicacao-conjunta-r16-r1/resultado/depois-aula.html'))
 def run():return subprocess.run(['node',l+'ledger.mjs','--verificar',l+'ledger.json'],cwd=t,capture_output=True,text=True)
 assert run().returncode==0
 f=t/(l+'ledger.json')
 for mutate in (lambda x:x['registros_adicionais'][1].update(estado='aprovado_globalmente'),lambda x:x['registros_adicionais'].pop(),lambda x:x['colecoes']['referencias'].update(estado_padrao='aprovado')):
  v=copy.deepcopy(ledger);mutate(v);f.write_text(json.dumps(v));assert run().returncode!=0
 f.write_bytes(read(l+'ledger.json'))
 for p in ('modulos/e1-termodinamica.html',l+'reconciliacao-d11-20.md',a+'ledger.json'):
  dest=t/p;v=dest.read_bytes();dest.write_bytes(v+b'\n');result=run();assert result.returncode!=0 and 'SHA divergente' in result.stderr;dest.write_bytes(v)
 assert run().returncode==0
print(json.dumps({'ok':True,'base_r1':8,'novos':10,'contextos':len(contexts),'contexto_alterado':'base-brayton-real','testes_negativos':6,'ambiente':'snapshot r16 em cópia temporária'},ensure_ascii=False))
