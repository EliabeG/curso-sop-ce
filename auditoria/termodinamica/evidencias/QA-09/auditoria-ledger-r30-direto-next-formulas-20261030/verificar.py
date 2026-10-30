from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
Q=Path('auditoria/termodinamica/evidencias/QA-09');D=Q/'ledger-r30-direto-r2';L=json.loads((D/'ledger.json').read_text());J=json.loads((D/'juizos.json').read_text());R=(D/'reconciliacao.md').read_text();P=Q/'aplicacao-refrigeracao-r29/resultado';T=Q/'aplicacao-precisao-r30/resultado'
files={28:(P/'antes-aula.html',P/'antes-formulario.html'),29:(P/'depois-aula.html',P/'depois-formulario.html'),30:(T/'depois-aula.html',T/'depois-formulario.html')}
docs={v:{'modulos/e1-termodinamica.html':a.read_text().encode('utf-16-le'),'formulas/termodinamica.html':b.read_text().encode('utf-16-le')} for v,(a,b) in files.items()}; inv={v:json.loads((Q/f'inventario-r{v}.json').read_text()) for v in (28,29,30)}
H=lambda b:sha256(b).hexdigest(); frag=lambda doc,a,b:doc[2*a:2*b].decode('utf-16-le').encode()
for v in (28,29,30):
 rows=inv[v]['ocorrencias'];assert len(rows)==11409 and len({r['id'] for r in rows})==11409
 for r in rows:
  if r['tipo'] not in ('texto_direto','atributos_significativos'):assert H(frag(docs[v][r['arquivo']],r['inicio_utf16'],r['fim_utf16']))==r['sha256_fragmento'],(v,r['id'])
indices={v:{r['id']:r for r in inv[v]['ocorrencias']} for v in (28,29,30)};maps={}
for a,b in ((28,29),(29,30)):
 m=json.loads((Q/f'mapa-correspondencia-inventario-r{a}-r{b}-r1.json').read_text());pairs=m['pares'];assert len(pairs)==11409
 assert len({x[f'id_r{a}'] for x in pairs})==len({x[f'id_r{b}'] for x in pairs})==11409
 for x in pairs:
  for v in (a,b):assert indices[v][x[f'id_r{v}']]['sha256_fragmento']==x[f'sha256_r{v}']
 maps[a]={x[f'id_r{a}']:x for x in pairs}
assert len(L['objetos'])==len(J)==78 and len({x['id'] for x in L['objetos']})==78
ctx=[];mapped=0
for x,j in zip(L['objetos'],J):
 assert x['id']==j['id'] and x['juizo_r30']==j and x['juizo_r28']['juizo_local']==j['juizo_local_r30']
 assert '| '+j['id']+' | '+j['juizo_local_r30']+' | '+j['efeito_deltas_r29_r30']+' |' in R
 data=[]
 for v in (28,29,30):
  t=x[f'r{v}'];b=frag(docs[v][x['arquivo']],t['inicio_utf16'],t['fim_utf16']);assert H(b)==t['sha256'];data.append(b)
 assert data[0]==data[1]==data[2]
 for c in x['contextos']:
  assert c['sha256_r28']==c['sha256_r29']==c['sha256_r30'] and c['alterado_r28_r30'] is False;ctx.append(c['id'])
 if 'par_inventario' in x:
  z=x['par_inventario'];p=maps[28][z['id_r28']];q=maps[29][p['id_r29']];assert p['id_r29']==z['id_r29'] and q['id_r30']==z['id_r30'];mapped+=1
 if 'contexto_figura' in x:
  f=x['contexto_figura'];assert f['sha256_r28']==f['sha256_r29']==f['sha256_r30'] and not f['alterado_r28_r30']
assert len(ctx)==93 and len(set(ctx))==43 and mapped==18 and sum('contexto_figura' in x for x in L['objetos'])==4
assert all(v['estado_padrao']=='pendente_de_integracao' for v in L['colecoes'].values())
print(json.dumps({'ok':True,'fragmentos_reextraidos':78,'ocorrencias_conferidas_por_tipo':{v:dict(Counter(r['tipo'] for r in inv[v]['ocorrencias'])) for v in inv},'mapas_verificados':2,'pares_compostos':mapped,'contextos_entradas':len(ctx),'contextos_distintos':len(set(ctx)),'figuras':4,'juizos_confrontados':len(J),'limite':'Para atributos significativos e texto direto só compara manifesto/mapas; demais tipos reextraídos da foto. Compara hashes dos contextos registrados; a reextração dos contextos é feita pelo verificador da ponte. Não reavalia ciência.'},ensure_ascii=False))
