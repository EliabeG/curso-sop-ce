#!/usr/bin/env python3
"""Reconcilia r16→r17 por posição fora dos deltas e por ordem/contexto dentro deles."""
import json,pathlib,hashlib,difflib
D=pathlib.Path('auditoria/termodinamica/evidencias/QA-09'); P=D/'aplicacao-intercooling-r17-r1/resultado'; out=D/'mapa-correspondencia-inventario-r16-r17-r1.json'
if out.exists():raise SystemExit('Destino já existe')
a=json.loads((D/'inventario-r16.json').read_text()); b=json.loads((D/'inventario-r17.json').read_text()); edits=json.loads((P/'edicoes-aplicadas.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inside(e,x,version):return x['arquivo']==e['documento'] and (e['inicio']<=x['inicio_utf16']<e['fim'] if version==16 else e['inicio_novo']<=x['inicio_utf16']<e['fim_novo'])
def outside(x,version):return not any(inside(e,x,version) for e in edits)
def desloc(x):return sum(e['delta'] for e in edits if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim'])
def key(x):return (x['arquivo'],x['inicio_utf16'],x['tipo'],x['tag'],x.get('secao'),x.get('ancora'))
def context(x):return (x['arquivo'],x['tipo'],x['tag'],x.get('secao'),x.get('ancora'))
remaining={key(y):y for y in b['ocorrencias'] if outside(y,17)}
assert len(remaining)==sum(outside(y,17) for y in b['ocorrencias'])
rows=[]
for x in a['ocorrencias']:
 if outside(x,16):
  k=(x['arquivo'],x['inicio_utf16']+desloc(x),x['tipo'],x['tag'],x.get('secao'),x.get('ancora'));y=remaining.pop(k,None);assert y is not None,(x['id'],k)
  estado='PAREADO_EXTERNO'
  if x['sha256_fragmento']!=y['sha256_fragmento']:
   assert any(e['documento']==x['arquivo'] and x['inicio_utf16']<=e['inicio'] and x['fim_utf16']>=e['fim'] for e in edits),(x['id'], 'hash externo divergente')
   estado='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR'
  rows.append({'estado':estado,'id_r16':x['id'],'id_r17':y['id'],'sha256_r16':x['sha256_fragmento'],'sha256_r17':y['sha256_fragmento']})
assert not remaining, 'Ocorrências externas novas não mapeadas'
for e in edits:
 old=[x for x in a['ocorrencias'] if inside(e,x,16)];new=[y for y in b['ocorrencias'] if inside(e,y,17)]
 sm=difflib.SequenceMatcher(a=[context(x) for x in old],b=[context(x) for x in new],autojunk=False)
 for op,i,j,k,l in sm.get_opcodes():
  if op=='equal':
   for x,y in zip(old[i:j],new[k:l]):rows.append({'estado':'PAREADO_INTERNO_CONFERIR','edicao':e['id'],'id_r16':x['id'],'id_r17':y['id'],'sha256_r16':x['sha256_fragmento'],'sha256_r17':y['sha256_fragmento']})
  else:
   for x in old[i:j]:rows.append({'estado':'REMOVIDO_OU_REESTRUTURADO','edicao':e['id'],'id_r16':x['id'],'id_r17':None,'sha256_r16':x['sha256_fragmento']})
   for y in new[k:l]:rows.append({'estado':'ADICIONADO_OU_REESTRUTURADO','edicao':e['id'],'id_r16':None,'id_r17':y['id'],'sha256_r17':y['sha256_fragmento']})
assert len([x for x in rows if x.get('id_r16')])==len(a['ocorrencias']) and len([x for x in rows if x.get('id_r17')])==len(b['ocorrencias'])
# Parear referências na mesma ordem, preservando os valores.
assert len(a['referencias'])==len(b['referencias'])
referencias_mudadas=[];referencias_novas=[]
for x,y in zip(a['referencias'],b['referencias']):
 campos=['arquivo','secao','ancora','tag','atributo','valor','texto']
 if outside(x,16):
  assert all(x.get(k)==y.get(k) for k in campos) and x['inicio_utf16']+desloc(x)==y['inicio_utf16']
 else:
  assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','texto'])
  assert x['valor']==y['valor']
assert not referencias_mudadas
assert len(a['recursos'])==len(b['recursos'])
recursos_mudados=[]
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','arquivo','papel','estado'])
 if x['referencia']!=y['referencia']:
  assert any(q['origem']['valor']==x['referencia'] and q['destino']['valor']==y['referencia'] for q in referencias_mudadas)
  recursos_mudados.append({'origem':x['referencia'],'destino':y['referencia'],'arquivo':x['arquivo']})
 if x['arquivo'] in ['modulos/e1-termodinamica.html','formulas/termodinamica.html']:
  assert x['sha256']==sha(P/('antes-aula.html' if x['arquivo'].startswith('modulos') else 'antes-formulario.html')) and y['sha256']==sha(pathlib.Path(x['arquivo']))
 else:assert x['sha256']==y['sha256']
assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
out.write_text(json.dumps({'estado':'MAPEAMENTO_ESTRUTURAL','base_r16':sha(D/'inventario-r16.json'),'base_r17':sha(D/'inventario-r17.json'),'edicoes':edits,'pares':rows,'total_r16':len(a['ocorrencias']),'total_r17':len(b['ocorrencias']),'referencias':len(a['referencias']),'recursos':len(a['recursos']),'referencias_mudadas':referencias_mudadas,'referencias_novas':referencias_novas,'recursos_mudados':recursos_mudados,'limite':'Dentro de cada bloco a correspondência é por sequência de tipo/tag/contexto; nós novos/removidos são destacados, sem transferência automática de aceite. Comparação de recursos e referências é estrutural, não comprova conteúdo visual ou validação pedagógica.'},ensure_ascii=False,indent=2)+'\n')
from collections import Counter
print(json.dumps({'status':'ok','r16':len(a['ocorrencias']),'r17':len(b['ocorrencias']),'referencias':len(a['referencias']),'recursos':len(a['recursos']),'referencias_novas':len(referencias_novas),'referencias_mudadas':len(referencias_mudadas),'classificacao':dict(Counter(x['estado'] for x in rows))},ensure_ascii=False))
