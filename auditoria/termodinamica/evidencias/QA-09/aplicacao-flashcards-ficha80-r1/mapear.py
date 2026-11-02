#!/usr/bin/env python3
"""Reconcilia r8→r9 por posição fora dos deltas e por ordem/contexto dentro deles."""
import json,pathlib,hashlib,difflib
D=pathlib.Path('auditoria/termodinamica/evidencias/QA-09'); P=D/'aplicacao-flashcards-ficha80-r1'; out=D/'mapa-correspondencia-inventario-r8-r9-r1.json'
if out.exists():raise SystemExit('Destino já existe')
a=json.loads((D/'inventario-r8.json').read_text()); b=json.loads((D/'inventario-r9.json').read_text()); edits=json.loads((P/'edicoes-aplicadas.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inside(e,x,version):return x['arquivo']==e['documento'] and (e['inicio']<=x['inicio_utf16']<e['fim'] if version==8 else e['inicio_novo']<=x['inicio_utf16']<e['fim_novo'])
def outside(x,version):return not any(inside(e,x,version) for e in edits)
def desloc(x):return sum(e['delta'] for e in edits if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim'])
def key(x):return (x['arquivo'],x['inicio_utf16'],x['tipo'],x['tag'],x.get('secao'),x.get('ancora'))
def context(x):return (x['arquivo'],x['tipo'],x['tag'],x.get('secao'),x.get('ancora'))
remaining={key(y):y for y in b['ocorrencias'] if outside(y,9)}
assert len(remaining)==sum(outside(y,9) for y in b['ocorrencias'])
rows=[]
for x in a['ocorrencias']:
 if outside(x,8):
  k=(x['arquivo'],x['inicio_utf16']+desloc(x),x['tipo'],x['tag'],x.get('secao'),x.get('ancora'));y=remaining.pop(k,None);assert y is not None,(x['id'],k)
  rows.append({'estado':'PAREADO_EXTERNO','id_r8':x['id'],'id_r9':y['id'],'sha256_r8':x['sha256_fragmento'],'sha256_r9':y['sha256_fragmento']})
assert not remaining, 'Ocorrências externas novas não mapeadas'
for e in edits:
 old=[x for x in a['ocorrencias'] if inside(e,x,8)];new=[y for y in b['ocorrencias'] if inside(e,y,9)]
 sm=difflib.SequenceMatcher(a=[context(x) for x in old],b=[context(x) for x in new],autojunk=False)
 for op,i,j,k,l in sm.get_opcodes():
  if op=='equal':
   for x,y in zip(old[i:j],new[k:l]):rows.append({'estado':'PAREADO_INTERNO_CONFERIR','edicao':e['id'],'id_r8':x['id'],'id_r9':y['id'],'sha256_r8':x['sha256_fragmento'],'sha256_r9':y['sha256_fragmento']})
  else:
   for x in old[i:j]:rows.append({'estado':'REMOVIDO_OU_REESTRUTURADO','edicao':e['id'],'id_r8':x['id'],'id_r9':None,'sha256_r8':x['sha256_fragmento']})
   for y in new[k:l]:rows.append({'estado':'ADICIONADO_OU_REESTRUTURADO','edicao':e['id'],'id_r8':None,'id_r9':y['id'],'sha256_r9':y['sha256_fragmento']})
assert len([x for x in rows if x.get('id_r8')])==len(a['ocorrencias']) and len([x for x in rows if x.get('id_r9')])==len(b['ocorrencias'])
assert len(a['referencias'])==len(b['referencias'])
for x,y in zip(a['referencias'],b['referencias']):
 assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto']),(x,y)
 if outside(x,8):assert x['inicio_utf16']+desloc(x)==y['inicio_utf16']
assert len(a['recursos'])==len(b['recursos'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in ['modulos/e1-termodinamica.html','formulas/termodinamica.html']:
  assert x['sha256']==sha(P/('antes-aula.html' if x['arquivo'].startswith('modulos') else 'antes-formulario.html')) and y['sha256']==sha(pathlib.Path(x['arquivo']))
 else:assert x['sha256']==y['sha256']
assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
out.write_text(json.dumps({'estado':'MAPEAMENTO_ESTRUTURAL','base_r8':sha(D/'inventario-r8.json'),'base_r9':sha(D/'inventario-r9.json'),'edicoes':edits,'pares':rows,'total_r8':len(a['ocorrencias']),'total_r9':len(b['ocorrencias']),'referencias':len(a['referencias']),'recursos':len(a['recursos']),'limite':'Dentro de cada bloco a correspondência é por sequência de tipo/tag/contexto; nós novos/removidos são destacados, sem transferência automática de aceite. Comparação de recursos e referências é estrutural, não comprova conteúdo visual ou validação pedagógica.'},ensure_ascii=False,indent=2)+'\n')
from collections import Counter
print(json.dumps({'status':'ok','r8':len(a['ocorrencias']),'r9':len(b['ocorrencias']),'referencias':len(a['referencias']),'recursos':len(a['recursos']),'classificacao':dict(Counter(x['estado'] for x in rows))},ensure_ascii=False))
