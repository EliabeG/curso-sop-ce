#!/usr/bin/env python3
"""Auditoria estrutural dos recortes e guardas; mutações só em /tmp."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import tempfile,subprocess,copy,json
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';d=q/'ledger-r27-expandido-r3';sha=lambda x:sha256(x).hexdigest()
for path,digest in [(d/'LEIA-ME.md','9a16a7760003a08aa2ce11ee5a7f49211eee3418a8353f0b09209b1aeb2e5241'),(d/'ledger.json','b2a8f5bd94e00d441e6d2386f84e414cf8f3d7d6a46a653214c6a2064ced2593'),(d/'ledger.py','dbbca9553821b0496f9a6accacc6e92249aabd815a288fba6b9a670ea9ff0614')]:assert sha(path.read_bytes())==digest
j=json.loads((d/'ledger.json').read_bytes());base=json.loads((q/'ledger-r27-parcial-r1/ledger.json').read_bytes());r1=json.loads((q/'ledger-r27-expandido-r1/ledger.json').read_bytes());r2=json.loads((q/'ledger-r27-expandido-r2/ledger.json').read_bytes());rows=j['registros_adicionais_por_recorte'];assert len(rows)==60 and len(j['registros_explicitamente_revisados'])==18
assert j['registros_explicitamente_revisados']==base['registros_explicitamente_revisados'] and j['colecoes']==base['colecoes'] and j['fotografia']==base['fotografia']
assert rows[:45]==r1['registros_adicionais_por_recorte'] and rows[:50]==r2['registros_adicionais_por_recorte']
counts=Counter(x['tipo'] for x in rows);assert counts=={'ficha':22,'bloco_teoria':6,'figura_svg':4,'artigo_grafico':3,'diagnostico':15,'exemplo':10}
assert {x['id'] for x in rows if x['tipo']=='diagnostico'}=={f'D{x:02}' for x in list(range(1,11))+list(range(21,26))};assert {x['id'] for x in rows if x['tipo']=='exemplo'}=={f'EX-{x:03}' for x in range(31,41)}
assert [x['numero_ficha'] for x in rows if x['tipo']=='ficha']==list(range(1,23));assert len({(x['arquivo'],x['inicio_utf16'],x['fim_utf16']) for x in rows})==60
cache={p:(r/p).read_bytes().decode().encode('utf-16-le') for p in ['modulos/e1-termodinamica.html','formulas/termodinamica.html']}
for x in rows:
 assert x['estado']=='conferido_no_escopo_localizado' and x['escopo']
 u=cache[x['arquivo']];a=x['inicio_utf16'];b=x['fim_utf16'];assert 0<=a<b<=len(u)//2 and sha(u[2*a:2*b].decode('utf-16-le').encode())==x['sha256_fragmento']
 for key in ('entrega','parecer_independente'):
  v=x[key];assert sha((r/v['arquivo']).read_bytes())==v['sha256']
 if 'ativo' in x:assert sha((r/x['ativo']['arquivo']).read_bytes())==x['ativo']['sha256']
 if 'contexto' in x:
  c=x['contexto'];assert c['inicio']<=a<b<=c['fim'] and sha(u[2*c['inicio']:2*c['fim']].decode('utf-16-le').encode())==c['sha256']
 if 'links' in x:
  for link in x['links']:assert u.decode('utf-16-le').count('id="'+link+'"')==1
assert all(x['estado_padrao']=='pendente_de_integracao' for x in j['colecoes'].values()) and j['estado_global']=='QA09_EM_CORRECAO_NAO_APROVADO'
with tempfile.TemporaryDirectory(prefix='qa-ledger-r27-r3-') as tmp:
 dest=Path(tmp)/'alterado.json';cmd=['python3',str(d/'ledger.py'),'--verificar',str(dest)]
 def run(obj):dest.write_text(json.dumps(obj,ensure_ascii=False));return subprocess.run(cmd,cwd=r,stdout=subprocess.PIPE,stderr=subprocess.PIPE).returncode
 assert run(j)==0
 for change in (lambda z:z['registros_adicionais_por_recorte'][0].update(sha256_fragmento='0'*64),lambda z:z['registros_adicionais_por_recorte'][0].update(inicio_utf16=0),lambda z:z['registros_adicionais_por_recorte'].pop(),lambda z:z['colecoes']['referencias'].update(estado_padrao='aprovado'),lambda z:next(a for a in z['registros_adicionais_por_recorte'] if a['tipo']=='diagnostico')['links'].append('ficticio'),lambda z:next(a for a in z['registros_adicionais_por_recorte'] if a['tipo']=='exemplo')['contexto'].update(sha256='0'*64)):
  k=copy.deepcopy(j);change(k);assert run(k)!=0
print(json.dumps({'ok':True,'base':18,'adicionais':dict(counts),'estados_pendentes':True,'testes_negativos':6,'sem_escrita_em_produto':True},ensure_ascii=False))
