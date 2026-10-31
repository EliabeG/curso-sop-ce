#!/usr/bin/env python3
"""Apoio estrutural: recompõe r26 e verifica o mapa; somente leitura."""
import collections,hashlib,json,re
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=r/(q+'aplicacao-fun02-ficha59-ex010-r26-r1/resultado');rd=lambda x:(r/x).read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html';before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()};after={A:rd(A),F:rd(F)}
for doc,old,new in [(A,'ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e','afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2'),(F,'694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58','16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02')]:
 assert sha(before[doc])==old and sha(after[doc])==new and after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes();assert sha(edb)=='49161293439d1c4cdcce5f38efb81b3af90854a33e5a6acf6af5f5e72b5c2f5f';ed=json.loads(edb)
candidates={}
hashes={'candidata-fun02-escala-r25-next-theory-20261030':'89c37950a565509a6e0d7d54e657f4fd9b6cb174a30429108bfd943e60f8ac89','candidata-fun02-parciais-r25-next-theory-20261030':'ef267f6481e3377334309a593ae70b7853fff7254c653b294896c03ba3574e37','candidata-fun02-trabalho-r25-next-theory-20261030':'5fee9a61920cfd5a93c0ed47049fbdd3de55676dc0742567ab77a4291d7c2960','candidata-fun02-fator-r25-next-theory-20261030':'5bfadef7a0fb1052ffb7c1e09fdf78719464ec6ba61a5f040a4b969e6ed5c21b','candidata-ficha59-r25-20261030':'228c16439f800be7b4753b728c42f4a856f88c18b2528b18d8b588c53c82743e','candidata-ex010-equipamentos-r25-next-examples-20261030':'9374290e0e6203e356e71b3d87b4e8df9aa714e4c5f04556a9aa2113f01c2da7'}
assert len(ed)==6 and {e['origem'] for e in ed}==set(hashes)
for e in ed:
 d=r/(q+e['origem']);mb=(d/'manifesto.json').read_bytes();assert sha(mb)==hashes[e['origem']];m=json.loads(mb);candidates[e['id']]=d/'candidata.html'
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
ib=rd(q+'inventario-r25.json');ic=rd(q+'inventario-r26.json');mp=rd(q+'mapa-correspondencia-inventario-r25-r26-r1.json')
assert sha(ib)=='6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116' and sha(ic)=='d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241' and sha(mp)=='4cf2e325012929faa2f16c3a01bb8710847cb6f302aef74f2c012dfce8decc9d'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197 and m['edicoes']==ed
for x in a['artigos_excluidos']: assert aa[x['id'].encode()]==ab[x['id'].encode()] and sha(aa[x['id'].encode()])==x['sha256_fragmento']
assert len(fa)==len(fbb)==100 and fa.keys()==fbb.keys()
assert sum(fa[k]!=fbb[k] for k in fa)==1 and fa[b'formula-cop-refrigerador']!=fbb[b'formula-cop-refrigerador']
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};useda=[];usedb=[];changed=collections.Counter();internal=collections.Counter()
for row in m['pares']:
 x=old.get(row['id_r25']);y=new.get(row['id_r26']);state=row['estado'];assert x is not None or y is not None
 if x:useda.append(x['id']);assert row['sha256_r25']==x['sha256_fragmento']
 if y:usedb.append(y['id']);assert row['sha256_r26']==y['sha256_fragmento']
 if state=='PAREADO_EXTERNO':assert x and y and x['sha256_fragmento']==y['sha256_fragmento']
 elif state=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':assert x and y and x['sha256_fragmento']!=y['sha256_fragmento'] and any(z['documento']==x['arquivo'] and x['inicio_utf16']<=z['inicio'] and x['fim_utf16']>=z['fim'] for z in ed)
 elif state=='PAREADO_INTERNO_CONFERIR':
  assert x and y;e=next(z for z in ed if z['id']==row['edicao']);assert x['arquivo']==y['arquivo']==e['documento'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
  assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);internal[e['id']]+=1
  if x['sha256_fragmento']!=y['sha256_fragmento']:changed[e['id']]+=1
 elif state in ('ADICIONADO_OU_REESTRUTURADO','REMOVIDO_OU_REESTRUTURADO'):
  assert (x is None)!=(y is None);e=next(z for z in ed if z['id']==row['edicao']);v=x or y;lo,hi=(e['inicio'],e['fim']) if x else (e['inicio_novo'],e['fim_novo']);assert v['arquivo']==e['documento'] and lo<=v['inicio_utf16']<v['fim_utf16']<=hi
 else:raise AssertionError(state)
assert len(useda)==len(set(useda))==len(old)==11405 and len(usedb)==len(set(usedb))==len(new)==11407
counts=collections.Counter(z['estado'] for z in m['pares']);assert counts=={'PAREADO_EXTERNO':11011,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':3,'PAREADO_INTERNO_CONFERIR':391,'ADICIONADO_OU_REESTRUTURADO':2}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());now=json.loads(rd('auditoria/termodinamica/inventario/inventario-questoes.json'));assert len(io['itens'])==197 and io['itens']==now['itens'] and all(io[k]==now[k] for k in io if k!='fonte') and now['fonte']['sha256']==sha(after[A])
assert rd('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith((p/'inventario-oficial-antes.md').read_bytes())
print(json.dumps({'ok':True,'edicoes':6,'artigos':197,'fichas_nao_alvo':99,'mathml':[734,191],'pares':counts,'internos_por_edicao':internal,'alterados':changed,'referencias':816,'recursos':138},ensure_ascii=False))
