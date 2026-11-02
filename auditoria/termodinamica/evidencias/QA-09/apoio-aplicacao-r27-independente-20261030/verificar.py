#!/usr/bin/env python3
"""Apoio estrutural: recompõe r27 e verifica o mapa; somente leitura."""
import collections,hashlib,json,re
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=r/(q+'aplicacao-carnot-flashcards-r27-r1/resultado');rd=lambda x:(r/x).read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html';before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()};after={A:rd(A),F:rd(F)}
for doc,old,new in [(A,'afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2','9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'),(F,'16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02','16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02')]:
 assert sha(before[doc])==old and sha(after[doc])==new and after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes();assert sha(edb)=='24ecb7389b8e7dc215108420a798206d158af3afdbcc97b281b093b3eca9468f';ed=json.loads(edb)
candidates={}
hashes={'candidata-base-carnot-r26-next-theory-20261030':'95c2e4033297a8a39ad1fde18124e505e0de489ff53f37d17fd8c31e7560816c','candidata-card-cop-r26-next-theory-20261030':'76c69881ec1f788a2d35056ccb26f8677dde1c356caf94c3a9b7993dfd33503c','candidata-card-carnot-r26-next-theory-20261030':'e7b18767b4e56951478db06e87d263b92b6b5844b707b8b601a999f1576050e5','candidata-card-compressor-r26-next-theory-20261030-r2':'6752eb3cb1ebed8ec8cddbdac888ddb1f86a557d233525234298623875006f45'}
assert len(ed)==4 and {e['id'] for e in ed}=={'QA-09-'+x for x in hashes}
for e in ed:
 d=r/(q+e['id'].removeprefix('QA-09-'));mb=(d/'manifesto.json').read_bytes();assert sha(mb)==hashes[d.name];candidates[e['id']]=d/'candidata.html'
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
ib=rd(q+'inventario-r26.json');ic=rd(q+'inventario-r27.json');mp=rd(q+'mapa-correspondencia-inventario-r26-r27-r1.json')
assert sha(ib)=='d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241' and sha(ic)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c' and sha(mp)=='2eff0a63420831284ca726ed4efaadb436ffc6c976de151d2f70eb9e2e9790b4'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197 and m['edicoes']==ed
for x in a['artigos_excluidos']: assert aa[x['id'].encode()]==ab[x['id'].encode()] and sha(aa[x['id'].encode()])==x['sha256_fragmento']
assert len(fa)==len(fbb)==100 and fa.keys()==fbb.keys()
assert fa==fbb and before[F]==after[F]
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};useda=[];usedb=[];changed=collections.Counter();internal=collections.Counter()
for row in m['pares']:
 x=old.get(row['id_r26']);y=new.get(row['id_r27']);state=row['estado'];assert x is not None or y is not None
 if x:useda.append(x['id']);assert row['sha256_r26']==x['sha256_fragmento']
 if y:usedb.append(y['id']);assert row['sha256_r27']==y['sha256_fragmento']
 if state=='PAREADO_EXTERNO':assert x and y and x['sha256_fragmento']==y['sha256_fragmento']
 elif state=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':assert x and y and x['sha256_fragmento']!=y['sha256_fragmento'] and any(z['documento']==x['arquivo'] and x['inicio_utf16']<=z['inicio'] and x['fim_utf16']>=z['fim'] for z in ed)
 elif state=='PAREADO_INTERNO_CONFERIR':
  assert x and y;e=next(z for z in ed if z['id']==row['edicao']);assert x['arquivo']==y['arquivo']==e['documento'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
  assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);internal[e['id']]+=1
  if x['sha256_fragmento']!=y['sha256_fragmento']:changed[e['id']]+=1
 elif state in ('ADICIONADO_OU_REESTRUTURADO','REMOVIDO_OU_REESTRUTURADO'):
  assert (x is None)!=(y is None);e=next(z for z in ed if z['id']==row['edicao']);v=x or y;lo,hi=(e['inicio'],e['fim']) if x else (e['inicio_novo'],e['fim_novo']);assert v['arquivo']==e['documento'] and lo<=v['inicio_utf16']<v['fim_utf16']<=hi
 else:raise AssertionError(state)
assert len(useda)==len(set(useda))==len(old)==11407 and len(usedb)==len(set(usedb))==len(new)==11407
counts=collections.Counter(z['estado'] for z in m['pares']);assert counts=={'PAREADO_EXTERNO':11206,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':2,'PAREADO_INTERNO_CONFERIR':199}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());now=json.loads(rd('auditoria/termodinamica/inventario/inventario-questoes.json'));assert len(io['itens'])==197 and io['itens']==now['itens'] and all(io[k]==now[k] for k in io if k!='fonte') and now['fonte']['sha256']==sha(after[A])
assert rd('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith((p/'inventario-oficial-antes.md').read_bytes())
print(json.dumps({'ok':True,'edicoes':4,'artigos':197,'formulario_preservado':True,'mathml':[734,191],'pares':counts,'internos_por_edicao':internal,'alterados':changed,'referencias':816,'recursos':138},ensure_ascii=False))
