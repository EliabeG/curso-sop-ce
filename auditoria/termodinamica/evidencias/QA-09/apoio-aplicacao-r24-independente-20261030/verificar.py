#!/usr/bin/env python3
"""Apoio estrutural: recompõe r24 e verifica o mapa; somente leitura."""
import collections,hashlib,json,re
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=r/(q+'aplicacao-fun01-combinada-r24-r1/resultado');rd=lambda x:(r/x).read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html';before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()};after={A:rd(A),F:rd(F)}
for doc,old,new in [(A,'f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d','2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9'),(F,'694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58')]:
 assert sha(before[doc])==old and sha(after[doc])==new and after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes();assert sha(edb)=='b28075447ebfbcc0fddfb74950260598a661061c91341339b94d5bd490c80e16';ed=json.loads(edb)
assert len(ed)==1 and ed[0]['id']=='fun01-preparacao-equilibrio'
e=ed[0];u=before[A].decode().encode('utf-16-le');start,end=e['inicio'],e['fim'];orig=u[2*start:2*end].decode('utf-16-le');assert sha(orig.encode())==e['original_sha256']
expected={'gases':'797fe338ed7108cf2e3644868ffea7d7ce900bd88511dff26df8c79c6a996e1c','liquido':'129a789ff993feb9419ea2a327bee46a83fd9acdb595f03d0ddde73a7246b027','gravidade':'a6be90eb5c2cc40229f7807bacd90afc5e7d8db9d8807e4c4bdf4e5f5f6e2a61'}
allsubs=[]
for name,digest in expected.items():
 d=r/(q+'candidata-fun01-'+name+'-r23-next-theory-20261030');mb=(d/'manifesto.json').read_bytes();assert sha(mb)==digest
 m=json.loads(mb);assert (d/'original.html').read_bytes().removesuffix(b'\n')==orig.encode();candidate=orig
 for z in m['substituicoes']:
  assert candidate.count(z['antes'])==1;candidate=candidate.replace(z['antes'],z['depois'],1);allsubs.append((z['antes'],z['depois'],d.name))
 assert candidate.encode()==(d/'candidata.html').read_bytes().removesuffix(b'\n')
subs=e['substituicoes'];assert len(subs)==6 and sorted(allsubs)==sorted((z['antes'],z['depois'],z['origem']) for z in subs)
units=orig.encode('utf-16-le');last=0
for z in sorted(subs,key=lambda x:x['pos']):
 assert z['pos']>=last and units[2*z['pos']:2*z['end']].decode('utf-16-le')==z['antes'];last=z['end']
for z in sorted(subs,key=lambda x:x['pos'],reverse=True):units=units[:2*z['pos']]+z['depois'].encode('utf-16-le')+units[2*z['end']:]
combined=units.decode('utf-16-le').encode();assert sha(combined)==e['candidata_sha256'];assert (u[:2*start]+units+u[2*end:]).decode('utf-16-le').encode()==after[A];assert before[F]==after[F]
for doc in (A,F):
 x=re.findall(rb'<math\b.*?</math>',before[doc],re.S);y=re.findall(rb'<math\b.*?</math>',after[doc],re.S);assert x==y and len(x)==({A:734,F:191}[doc])
def articles(raw):
 out={}
 for m in re.finditer(rb'<article\b[^>]*>.*?</article>',raw,re.S):
  match=re.search(rb'\bid="([^"]+)"',m.group().split(b'>',1)[0])
  if match:assert match.group(1) not in out;out[match.group(1)]=m.group()
 return out
aa,ab=articles(before[A]),articles(after[A]);fa,fbb=articles(before[F]),articles(after[F])
ib=rd(q+'inventario-r23.json');ic=rd(q+'inventario-r24.json');mp=rd(q+'mapa-correspondencia-inventario-r23-r24-r1.json')
assert sha(ib)=='ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e' and sha(ic)=='469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf' and sha(mp)=='63b3b5fc54566c617eb025458fec7dce979369dc180d01ec3bdc4a0ff31c9044'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197 and m['edicoes']==ed
for x in a['artigos_excluidos']: assert aa[x['id'].encode()]==ab[x['id'].encode()] and sha(aa[x['id'].encode()])==x['sha256_fragmento']
assert len(fa)==len(fbb)==100 and fa.keys()==fbb.keys()
assert fa==fbb and before[F]==after[F]
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};useda=[];usedb=[];changed=collections.Counter();internal=collections.Counter()
for row in m['pares']:
 x=old[row['id_r23']];y=new[row['id_r24']];useda.append(x['id']);usedb.append(y['id']);assert row['sha256_r23']==x['sha256_fragmento'] and row['sha256_r24']==y['sha256_fragmento']
 if row['estado']=='PAREADO_EXTERNO':assert x['sha256_fragmento']==y['sha256_fragmento']
 if row['estado']=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':
  assert x['sha256_fragmento']!=y['sha256_fragmento'] and any(z['documento']==x['arquivo'] and x['inicio_utf16']<=z['inicio'] and x['fim_utf16']>=z['fim'] for z in ed)
 if row['estado']=='PAREADO_INTERNO_CONFERIR':
  e=next(z for z in ed if z['id']==row['edicao']);assert x['arquivo']==y['arquivo']==e['documento'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
  assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);internal[e['id']]+=1
  if x['sha256_fragmento']!=y['sha256_fragmento']:changed[e['id']]+=1
assert len(useda)==len(set(useda))==len(old)==11400 and len(usedb)==len(set(usedb))==len(new)==11400
counts=collections.Counter(z['estado'] for z in m['pares']);assert counts=={'PAREADO_EXTERNO':11381,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':1,'PAREADO_INTERNO_CONFERIR':18}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());now=json.loads(rd('auditoria/termodinamica/inventario/inventario-questoes.json'));assert len(io['itens'])==197 and io['itens']==now['itens'] and all(io[k]==now[k] for k in io if k!='fonte') and now['fonte']['sha256']==sha(after[A])
assert rd('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith((p/'inventario-oficial-antes.md').read_bytes())
print(json.dumps({'ok':True,'edicoes':1,'artigos':197,'formulario_preservado':True,'mathml':[734,191],'pares':counts,'internos_por_edicao':internal,'alterados':changed,'referencias':816,'recursos':138},ensure_ascii=False))
