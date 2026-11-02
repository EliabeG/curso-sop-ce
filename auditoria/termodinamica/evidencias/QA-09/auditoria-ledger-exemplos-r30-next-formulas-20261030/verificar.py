from pathlib import Path
from hashlib import sha256
import json
Q=Path('auditoria/termodinamica/evidencias/QA-09');D=Q/'ledger-exemplos-r30-r1'; H=lambda b:sha256(b).hexdigest(); ledger=json.loads((D/'ledger.json').read_text()); notes=json.loads((D/'notas.json').read_text()); report=(D/'reconciliacao.md').read_text(); tri=json.loads((Q/'ledger-exemplos-r30-triagem-r1/triagem.json').read_text()); old=json.loads((Q/'ledger-r30-direto-r2/ledger.json').read_text()); assert len(ledger['exemplos'])==len(notes)==len(tri['exemplos'])==50
snap={17:Q/'aplicacao-intercooling-r17-r1/resultado/depois-aula.html',20:Q/'aplicacao-mistura-fase-r20-r1/resultado/depois-aula.html',25:Q/'aplicacao-fun01-fases-r25-r1/resultado/depois-aula.html',30:Q/'aplicacao-precisao-r30/resultado/depois-aula.html'}; docs={v:p.read_text().encode('utf-16-le') for v,p in snap.items()}; frag=lambda v,x:docs[v][x['inicio_utf16']*2:x['fim_utf16']*2].decode('utf-16-le').encode();maps={}
for v in range(17,30):
 a=json.loads((Q/f'mapa-correspondencia-inventario-r{v}-r{v+1}-r1.json').read_text())['pares'];d={x.get(f'id_r{v}'):x for x in a if x.get(f'id_r{v}')};assert len(d)==sum(bool(x.get(f'id_r{v}')) for x in a);maps[v]=d
prior={x['id']:x for x in old['objetos']}; added=0; changed=[];contexts=[]
for i,(r,n,t) in enumerate(zip(ledger['exemplos'],notes,tri['exemplos']),1):
 assert r['id']==n['id']==t['id']==f'EX-{i:03d}' and r['juizo']==n and r['estado']=='revalidado_pelo_integrador_pendente_de_auditoria_independente';assert '| '+r['id']+' | '+n['juizo_local']+' | '+n['efeito_das_alteracoes']+' |' in report
 assert H(frag(30,r['r30']))==r['r30']['sha256']
 if r['integrado_na_base']:
  assert r['id'] in prior and prior[r['id']]['r30']['sha256']==r['r30']['sha256'] and n['juizo_local']==prior[r['id']]['juizo_r30']['juizo_local_r30']
 else:
  added+=1;v=int(r['fonte_historica'][1:]);o=r['r_anterior'];assert H(frag(v,o))==o['sha256'];ident=o['id'];digest=o['sha256'];trace=[]
  for v2 in range(v,30):
   x=maps[v2][ident];assert x[f'sha256_r{v2}']==digest;new=x[f'sha256_r{v2+1}'];ident=x[f'id_r{v2+1}'];assert new and ident
   if new!=digest:trace.append({'de':f'r{v2}','para':f'r{v2+1}','estado':x['estado'],'sha256_antes':digest,'sha256_depois':new})
   digest=new
  assert ident==r['r30']['id'] and digest==r['r30']['sha256'] and trace==r['alteracoes_mapa']
  assert r['fragmento_alterado']==(o['sha256']!=digest)
 if r['fragmento_alterado']:changed.append(r['id'])
 if r['contexto_alterado']:contexts.append(r['id'])
 for name in ['parecer_origem']:
  f=r[name];assert H(Path(f['arquivo']).read_bytes())==f['sha256']
 for f in r['pareceres_aplicacao_e_contexto']:assert H(Path(f['arquivo']).read_bytes())==f['sha256']
assert added==35 and changed==['EX-010','EX-027','EX-028','EX-044','EX-046'] and contexts==['EX-010','EX-027','EX-028','EX-044','EX-046','EX-050'];assert all(c['estado_padrao']=='pendente_de_integracao' for c in ledger['colecoes'].values());print(json.dumps({'ok':True,'exemplos':50,'anteriores':50-added,'adicionados':added,'mapas':len(maps),'fragmentos_alterados':changed,'contextos_alterados':contexts,'limites':'Contextos sao conferidos por script da triagem, nao reextraidos por este script; pareceres por hash nao conferem autoria ou merito cientifico.'},ensure_ascii=False))
