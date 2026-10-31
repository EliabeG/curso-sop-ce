#!/usr/bin/env python3
"""Auditoria estrutural independente r8→r9: somente leitura e saída padrão."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,re
D=Path('auditoria/termodinamica/evidencias/QA-09');P=D/'aplicacao-flashcards-ficha80-r1'
def read(p):return Path(p).read_bytes()
def sh(p):return sha256(read(p)).hexdigest()
oldhash={'modulos/e1-termodinamica.html':'57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c','formulas/termodinamica.html':'c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0'}
newhash={'modulos/e1-termodinamica.html':'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2','formulas/termodinamica.html':'cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'}
paths={'modulos/e1-termodinamica.html':('antes-aula.html','depois-aula.html'),'formulas/termodinamica.html':('antes-formulario.html','depois-formulario.html')}
assert sh(D/'inventario-r8.json')=='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687'
assert sh(D/'inventario-r9.json')=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
assert sh(D/'mapa-correspondencia-inventario-r8-r9-r1.json')=='d210e8c7efd4520e0d2036c4ebd2ec90762f684ffe8378b5fd71fdbd43d15b90'
old={};new={}
for doc,(before,after) in paths.items():
 assert sh(P/before)==oldhash[doc] and sh(P/after)==newhash[doc] and sh(doc)==newhash[doc]
 old[doc]=read(P/before).decode().encode('utf-16-le');new[doc]=read(P/after).decode().encode('utf-16-le')
A=json.loads(read(D/'inventario-r8.json'));B=json.loads(read(D/'inventario-r9.json'));mp=json.loads(read(D/'mapa-correspondencia-inventario-r8-r9-r1.json'));edits=json.loads(read(P/'edicoes-aplicadas.json'));assert len(edits)==8
for doc in paths:
 editsdoc=[e for e in edits if e['documento']==doc];editsdoc.sort(key=lambda e:e['inicio']);cursor=0;offset=0;parts=[]
 for e in editsdoc:
  o=read(e['original']).decode().removesuffix('\n');n=read(e['candidata']).decode().removesuffix('\n'); assert sha256(o.encode()).hexdigest()==e['original_sha256'] and sha256(n.encode()).hexdigest()==e['candidata_sha256']
  assert old[doc].decode('utf-16-le').count(o)==1 and new[doc].decode('utf-16-le').count(n)==1
  assert e['inicio']>=cursor and old[doc][2*e['inicio']:2*e['fim']].decode('utf-16-le')==o
  assert e['delta']==len(n.encode('utf-16-le'))//2-len(o.encode('utf-16-le'))//2
  assert e['inicio_novo']==e['inicio']+offset and e['fim_novo']==e['inicio_novo']+len(n.encode('utf-16-le'))//2
  parts.extend([old[doc][2*cursor:2*e['inicio']],n.encode('utf-16-le')]);cursor=e['fim'];offset+=e['delta']
 assert b''.join(parts)+old[doc][2*cursor:]==new[doc]
assert (len(A['ocorrencias']),len(B['ocorrencias']))==(11396,11397)
a={x['id']:x for x in A['ocorrencias']};b={x['id']:x for x in B['ocorrencias']};assert len(a)==11396 and len(b)==11397
rows=mp['pares'];ida=[r['id_r8'] for r in rows if r.get('id_r8')];idb=[r['id_r9'] for r in rows if r.get('id_r9')];assert len(set(ida))==len(ida)==len(a) and set(ida)==set(a);assert len(set(idb))==len(idb)==len(b) and set(idb)==set(b)
counter=Counter(r['estado'] for r in rows);assert counter=={'PAREADO_EXTERNO':11200,'PAREADO_INTERNO_CONFERIR':196,'ADICIONADO_OU_REESTRUTURADO':1}
inside=lambda x,e,v:x['arquivo']==e['documento'] and ((e['inicio']<=x['inicio_utf16']<e['fim']) if v==8 else (e['inicio_novo']<=x['inicio_utf16']<e['fim_novo']))
shift=lambda x:sum(e['delta'] for e in edits if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim'])
changed=[];sameinternal=[];added=[]
for r in rows:
 x=a.get(r.get('id_r8'));y=b.get(r.get('id_r9'));status=r['estado']
 if x:assert r['sha256_r8']==x['sha256_fragmento']
 if y:assert r['sha256_r9']==y['sha256_fragmento']
 if status=='ADICIONADO_OU_REESTRUTURADO':
  assert x is None and y is not None; e=next(e for e in edits if e['id']==r['edicao']);assert inside(y,e,9);added.append((r['edicao'],y['id'],y['tipo']));continue
 assert x and y
 for k in ('arquivo','tipo','tag','secao','ancora'):assert x[k]==y[k],(r,k)
 if status=='PAREADO_EXTERNO':
  assert not any(inside(x,e,8) or inside(y,e,9) for e in edits);assert y['inicio_utf16']==x['inicio_utf16']+shift(x)
 else:
  e=next(e for e in edits if e['id']==r['edicao']);assert inside(x,e,8) and inside(y,e,9)
  if x['sha256_fragmento']==y['sha256_fragmento']:
   assert old[x['arquivo']][2*x['inicio_utf16']:2*x['fim_utf16']]==new[y['arquivo']][2*y['inicio_utf16']:2*y['fim_utf16']]
   sameinternal.append((r['edicao'],x['id'],y['id']))
 if x['sha256_fragmento']!=y['sha256_fragmento']:changed.append((status,r.get('edicao'),x['id'],y['id']))
assert len(A['referencias'])==len(B['referencias'])==815
refinside=[]
for i,(x,y) in enumerate(zip(A['referencias'],B['referencias'])):
 for k in ('arquivo','secao','ancora','tag','atributo','valor','texto'):assert x[k]==y[k],(i,k)
 if any(inside(x,e,8) for e in edits):
  assert old[x['arquivo']][2*x['inicio_utf16']:2*x['fim_utf16']]==new[y['arquivo']][2*y['inicio_utf16']:2*y['fim_utf16']]
  refinside.append(i)
 else:assert y['inicio_utf16']==x['inicio_utf16']+shift(x),(i,'ref')
assert len(A['recursos'])==len(B['recursos'])==138
changedresources=Counter()
for i,(x,y) in enumerate(zip(A['recursos'],B['recursos'])):
 for k in ('origem','referencia','arquivo','papel','estado'):assert x[k]==y[k],(i,k)
 if x['arquivo'] in paths:assert x['sha256']==oldhash[x['arquivo']] and y['sha256']==newhash[x['arquivo']];changedresources[x['arquivo']]+=1
 else:assert x['sha256']==y['sha256']
 assert sh(y['arquivo'])==y['sha256']
assert A['ativos_especificos']==B['ativos_especificos'] and len(A['ativos_especificos'])==6
for x in B['ativos_especificos']:assert sh(x['arquivo'])==x['sha256']
art=lambda h:re.findall(r'<article\b[^>]*>.*?</article\s*>',h.decode('utf-16-le'),re.S|re.I)
a8,a9=art(old['modulos/e1-termodinamica.html']),art(new['modulos/e1-termodinamica.html']);assert len(a8)==len(a9)==197 and a8==a9 and not any(re.search(r'<article\b',x[1:],re.I) for x in a8+a9)
assert A['artigos_excluidos']==B['artigos_excluidos'] and [sha256(x.encode()).hexdigest() for x in a8]==[x['sha256_fragmento'] for x in A['artigos_excluidos']]
f8,f9=art(old['formulas/termodinamica.html']),art(new['formulas/termodinamica.html']);assert len(f8)==len(f9)==100 and not any(re.search(r'<article\b',x[1:],re.I) for x in f8+f9)
changedcards=[n for n,(x,y) in enumerate(zip(f8,f9),1) if x!=y];assert changedcards==[80]
e=next(e for e in edits if e['id']=='ficha-080');assert sha256(f8[79].encode()).hexdigest()==e['original_sha256'] and sha256(f9[79].encode()).hexdigest()==e['candidata_sha256']
math=lambda s:re.findall(r'<math\b[^>]*>.*?</math\s*>',s,re.S|re.I)
assert math(old['formulas/termodinamica.html'].decode('utf-16-le'))==math(new['formulas/termodinamica.html'].decode('utf-16-le'))
off0=json.loads(read(P/'inventario-oficial-antes.json'));off1=json.loads(read('auditoria/termodinamica/inventario/inventario-questoes.json'));keys=[k for k in set(off0)|set(off1) if off0.get(k)!=off1.get(k)];assert keys==['fonte'];assert off0['fonte']['sha256']==oldhash['modulos/e1-termodinamica.html'] and off1['fonte']['sha256']==newhash['modulos/e1-termodinamica.html']
print(json.dumps({'reconstrucao_documentos':True,'classificacao':dict(counter),'pares_alterados':changed,'iguais_internos_contagem':len(sameinternal),'adicionados':added,'referencias':len(A['referencias']),'refs_em_blocos':refinside,'recursos':len(A['recursos']),'recursos_apontando_a_documentos_alterados':dict(changedresources),'ativos':6,'artigos_iguais':197,'fichas':100,'fichas_modificadas':changedcards,'mathml_formulario_iguais':len(math(old['formulas/termodinamica.html'].decode('utf-16-le'))),'json_oficial_alteracoes':keys,'limite':'Associação de pares internos por contexto/ordem exige análise individual; hashes iguais não são aprovação automática. Recursos externos e apresentação não foram testados.'},ensure_ascii=False,indent=2))
