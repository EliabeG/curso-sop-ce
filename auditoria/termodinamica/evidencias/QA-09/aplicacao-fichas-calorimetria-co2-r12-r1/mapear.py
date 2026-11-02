#!/usr/bin/env python3
"""Reconcilia r11→r12 por posição fora dos deltas e por ordem/contexto dentro deles."""
import json,pathlib,hashlib,difflib
D=pathlib.Path('auditoria/termodinamica/evidencias/QA-09'); P=D/'aplicacao-fichas-calorimetria-co2-r12-r1/resultado'; out=D/'mapa-correspondencia-inventario-r11-r12-r1.json'
if out.exists():raise SystemExit('Destino já existe')
a=json.loads((D/'inventario-r11.json').read_text()); b=json.loads((D/'inventario-r12.json').read_text()); edits=json.loads((P/'edicoes-aplicadas.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inside(e,x,version):return x['arquivo']==e['documento'] and (e['inicio']<=x['inicio_utf16']<e['fim'] if version==11 else e['inicio_novo']<=x['inicio_utf16']<e['fim_novo'])
def outside(x,version):return not any(inside(e,x,version) for e in edits)
def desloc(x):return sum(e['delta'] for e in edits if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim'])
def key(x):return (x['arquivo'],x['inicio_utf16'],x['tipo'],x['tag'],x.get('secao'),x.get('ancora'))
def context(x):return (x['arquivo'],x['tipo'],x['tag'],x.get('secao'),x.get('ancora'))
remaining={key(y):y for y in b['ocorrencias'] if outside(y,12)}
assert len(remaining)==sum(outside(y,12) for y in b['ocorrencias'])
rows=[]
for x in a['ocorrencias']:
 if outside(x,11):
  k=(x['arquivo'],x['inicio_utf16']+desloc(x),x['tipo'],x['tag'],x.get('secao'),x.get('ancora'));y=remaining.pop(k,None);assert y is not None,(x['id'],k)
  rows.append({'estado':'PAREADO_EXTERNO','id_r11':x['id'],'id_r12':y['id'],'sha256_r11':x['sha256_fragmento'],'sha256_r12':y['sha256_fragmento']})
assert not remaining, 'Ocorrências externas novas não mapeadas'
for e in edits:
 old=[x for x in a['ocorrencias'] if inside(e,x,11)];new=[y for y in b['ocorrencias'] if inside(e,y,12)]
 sm=difflib.SequenceMatcher(a=[context(x) for x in old],b=[context(x) for x in new],autojunk=False)
 for op,i,j,k,l in sm.get_opcodes():
  if op=='equal':
   for x,y in zip(old[i:j],new[k:l]):rows.append({'estado':'PAREADO_INTERNO_CONFERIR','edicao':e['id'],'id_r11':x['id'],'id_r12':y['id'],'sha256_r11':x['sha256_fragmento'],'sha256_r12':y['sha256_fragmento']})
  else:
   for x in old[i:j]:rows.append({'estado':'REMOVIDO_OU_REESTRUTURADO','edicao':e['id'],'id_r11':x['id'],'id_r12':None,'sha256_r11':x['sha256_fragmento']})
   for y in new[k:l]:rows.append({'estado':'ADICIONADO_OU_REESTRUTURADO','edicao':e['id'],'id_r11':None,'id_r12':y['id'],'sha256_r12':y['sha256_fragmento']})
assert len([x for x in rows if x.get('id_r11')])==len(a['ocorrencias']) and len([x for x in rows if x.get('id_r12')])==len(b['ocorrencias'])
assert len(a['referencias'])==len(b['referencias'])
referencias_mudadas=[]
for x,y in zip(a['referencias'],b['referencias']):
 campos=['arquivo','secao','ancora','tag','atributo','valor','texto']
 if outside(x,11):
  assert all(x.get(k)==y.get(k) for k in campos),(x,y)
  assert x['inicio_utf16']+desloc(x)==y['inicio_utf16']
 else:
  assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo']),(x,y)
  dif={k:[x.get(k),y.get(k)] for k in ['valor','texto'] if x.get(k)!=y.get(k)}
  if dif: referencias_mudadas.append({'origem':x,'destino':y,'mudancas':dif})
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
out.write_text(json.dumps({'estado':'MAPEAMENTO_ESTRUTURAL','base_r11':sha(D/'inventario-r11.json'),'base_r12':sha(D/'inventario-r12.json'),'edicoes':edits,'pares':rows,'total_r11':len(a['ocorrencias']),'total_r12':len(b['ocorrencias']),'referencias':len(a['referencias']),'recursos':len(a['recursos']),'referencias_mudadas':referencias_mudadas,'recursos_mudados':recursos_mudados,'limite':'Dentro de cada bloco a correspondência é por sequência de tipo/tag/contexto; nós novos/removidos são destacados, sem transferência automática de aceite. Comparação de recursos e referências é estrutural, não comprova conteúdo visual ou validação pedagógica.'},ensure_ascii=False,indent=2)+'\n')
from collections import Counter
print(json.dumps({'status':'ok','r11':len(a['ocorrencias']),'r12':len(b['ocorrencias']),'referencias':len(a['referencias']),'recursos':len(a['recursos']),'classificacao':dict(Counter(x['estado'] for x in rows))},ensure_ascii=False))
