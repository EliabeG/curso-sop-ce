#!/usr/bin/env python3
"""Apoio estrutural: recompõe r25 e verifica o mapa; somente leitura."""
import collections,hashlib,json,re
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=r/(q+'aplicacao-fun01-fases-r25-r1/resultado');rd=lambda x:(r/x).read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html';before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()};after={A:rd(A),F:rd(F)}
for doc,old,new in [(A,'2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9','ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e'),(F,'694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58')]:
 assert sha(before[doc])==old and sha(after[doc])==new and after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes();assert sha(edb)=='fc3433c9a4ab51715a678640fe3353026fa20c195c7d0bf4ec9da4a8be3631e1';ed=json.loads(edb)
candidates={}
d=r/(q+'candidata-fun01-fases-r24-next-theory-20261030');mb=(d/'manifesto.json').read_bytes();assert sha(mb)=='41acd831e5777031626f6d09f8dd0943c5a836365499b41b60e78de1c41fd6b3'
manifest=json.loads(mb); candidates[manifest['ancora']]=d/'candidata.html';assert len(ed)==1 and set(candidates)=={e['id'] for e in ed}
for doc in (A,F):
 u=before[doc].decode().encode('utf-16-le')
 for e in sorted((e for e in ed if e['documento']==doc),key=lambda e:e['inicio'],reverse=True):
  orig=u[2*e['inicio']:2*e['fim']].decode('utf-16-le').encode();cand=candidates[e['id']].read_bytes().removesuffix(b'\n')
  assert sha(orig)==e['original_sha256'] and sha(cand)==e['candidata_sha256'];u=u[:2*e['inicio']]+cand.decode().encode('utf-16-le')+u[2*e['fim']:]
 assert u.decode('utf-16-le').encode()==after[doc]
 x=re.findall(rb'<math\b.*?</math>',before[doc],re.S);y=re.findall(rb'<math\b.*?</math>',after[doc],re.S);assert x==y and len(x)==({A:734,F:191}[doc])
def articles(raw):
 out={}
 for m in re.finditer(rb'<article\b[^>]*>.*?</article>',raw,re.S):
  match=re.search(rb'\bid="([^"]+)"',m.group().split(b'>',1)[0])
  if match:assert match.group(1) not in out;out[match.group(1)]=m.group()
 return out
aa,ab=articles(before[A]),articles(after[A]);fa,fbb=articles(before[F]),articles(after[F])
ib=rd(q+'inventario-r24.json');ic=rd(q+'inventario-r25.json');mp=rd(q+'mapa-correspondencia-inventario-r24-r25-r1.json')
assert sha(ib)=='469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf' and sha(ic)=='6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116' and sha(mp)=='2b39fde214b9e058e740fb0140f6c40105d5a710fe366ac8f147ce9ba59e4100'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197 and m['edicoes']==ed
for x in a['artigos_excluidos']: assert aa[x['id'].encode()]==ab[x['id'].encode()] and sha(aa[x['id'].encode()])==x['sha256_fragmento']
assert len(fa)==len(fbb)==100 and fa.keys()==fbb.keys()
assert fa==fbb and before[F]==after[F]
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};useda=[];usedb=[];changed=collections.Counter();internal=collections.Counter()
for row in m['pares']:
 x=old.get(row['id_r24']);y=new.get(row['id_r25']);state=row['estado'];assert x is not None or y is not None
 if x:useda.append(x['id']);assert row['sha256_r24']==x['sha256_fragmento']
 if y:usedb.append(y['id']);assert row['sha256_r25']==y['sha256_fragmento']
 if state=='PAREADO_EXTERNO':assert x and y and x['sha256_fragmento']==y['sha256_fragmento']
 elif state=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':assert x and y and x['sha256_fragmento']!=y['sha256_fragmento'] and any(z['documento']==x['arquivo'] and x['inicio_utf16']<=z['inicio'] and x['fim_utf16']>=z['fim'] for z in ed)
 elif state=='PAREADO_INTERNO_CONFERIR':
  assert x and y;e=next(z for z in ed if z['id']==row['edicao']);assert x['arquivo']==y['arquivo']==e['documento'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
  assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);internal[e['id']]+=1
  if x['sha256_fragmento']!=y['sha256_fragmento']:changed[e['id']]+=1
 elif state in ('ADICIONADO_OU_REESTRUTURADO','REMOVIDO_OU_REESTRUTURADO'):
  assert (x is None)!=(y is None);e=next(z for z in ed if z['id']==row['edicao']);v=x or y;lo,hi=(e['inicio'],e['fim']) if x else (e['inicio_novo'],e['fim_novo']);assert v['arquivo']==e['documento'] and lo<=v['inicio_utf16']<v['fim_utf16']<=hi
 else:raise AssertionError(state)
assert len(useda)==len(set(useda))==len(old)==11400 and len(usedb)==len(set(usedb))==len(new)==11405
counts=collections.Counter(z['estado'] for z in m['pares']);assert counts=={'PAREADO_EXTERNO':11314,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':1,'PAREADO_INTERNO_CONFERIR':81,'REMOVIDO_OU_REESTRUTURADO':4,'ADICIONADO_OU_REESTRUTURADO':9}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());now=json.loads(rd('auditoria/termodinamica/inventario/inventario-questoes.json'));assert len(io['itens'])==197 and io['itens']==now['itens'] and all(io[k]==now[k] for k in io if k!='fonte') and now['fonte']['sha256']==sha(after[A])
assert rd('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith((p/'inventario-oficial-antes.md').read_bytes())
print(json.dumps({'ok':True,'edicoes':1,'artigos':197,'formulario_preservado':True,'mathml':[734,191],'pares':counts,'internos_por_edicao':internal,'alterados':changed,'referencias':816,'recursos':138},ensure_ascii=False))
