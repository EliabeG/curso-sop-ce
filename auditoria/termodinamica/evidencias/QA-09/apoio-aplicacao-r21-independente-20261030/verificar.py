#!/usr/bin/env python3
"""Apoio estrutural: recompõe r21 e verifica o mapa; somente leitura."""
import collections,hashlib,json,re
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=r/(q+'aplicacao-oficina-ex046-r21-r1/resultado');rd=lambda x:(r/x).read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html';before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()};after={A:rd(A),F:rd(F)}
for doc,old,new in [(A,'b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7','239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238'),(F,'694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58')]:
 assert sha(before[doc])==old and sha(after[doc])==new and after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes();assert sha(edb)=='7f0fe20342a1ef32aa119817ffa3710b4584b587c0761b0834e895c4596430f2';ed=json.loads(edb)
nd=r/(q+'candidata-ex046-r20-20261030-r3');fd=r/(q+'candidata-entropia-oficina-r20-20261030')
nb=(nd/'manifesto.json').read_bytes();fb=(fd/'manifesto.json').read_bytes();assert sha(nb)=='a453b56ec947c4d536ab7656543304afcb279acbb52a679cd95950a1dbc221e6' and sha(fb)=='b8a2879422c561eb2e3f42996d781e88c7896d75d9085fb8b4ddeb8172e3ac52'
fm=json.loads(fb);candidates={'ex046':nd/'candidata.html',fm['ancora']:fd/'candidata.html'}
assert len(ed)==2 and set(candidates)=={e['id'] for e in ed}
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
ib=rd(q+'inventario-r20.json');ic=rd(q+'inventario-r21.json');mp=rd(q+'mapa-correspondencia-inventario-r20-r21-r1.json')
assert sha(ib)=='e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4' and sha(ic)=='d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1' and sha(mp)=='6930666290d17dc5fc1d7c1375d4bf1a454d5a509d4578be691b58f463cdb99c'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197 and m['edicoes']==ed
for x in a['artigos_excluidos']: assert aa[x['id'].encode()]==ab[x['id'].encode()] and sha(aa[x['id'].encode()])==x['sha256_fragmento']
assert len(fa)==len(fbb)==100 and fa.keys()==fbb.keys()
assert fa==fbb and before[F]==after[F]
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};useda=[];usedb=[];changed=collections.Counter();internal=collections.Counter()
for row in m['pares']:
 x=old[row['id_r20']];y=new[row['id_r21']];useda.append(x['id']);usedb.append(y['id']);assert row['sha256_r20']==x['sha256_fragmento'] and row['sha256_r21']==y['sha256_fragmento']
 if row['estado']=='PAREADO_EXTERNO':assert x['sha256_fragmento']==y['sha256_fragmento']
 if row['estado']=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':
  assert x['sha256_fragmento']!=y['sha256_fragmento'] and any(z['documento']==x['arquivo'] and x['inicio_utf16']<=z['inicio'] and x['fim_utf16']>=z['fim'] for z in ed)
 if row['estado']=='PAREADO_INTERNO_CONFERIR':
  e=next(z for z in ed if z['id']==row['edicao']);assert x['arquivo']==y['arquivo']==e['documento'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
  assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);internal[e['id']]+=1
  if x['sha256_fragmento']!=y['sha256_fragmento']:changed[e['id']]+=1
assert len(useda)==len(set(useda))==len(old)==11400 and len(usedb)==len(set(usedb))==len(new)==11400
counts=collections.Counter(z['estado'] for z in m['pares']);assert counts=={'PAREADO_EXTERNO':11380,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':2,'PAREADO_INTERNO_CONFERIR':18}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());now=json.loads(rd('auditoria/termodinamica/inventario/inventario-questoes.json'));assert len(io['itens'])==197 and io['itens']==now['itens'] and all(io[k]==now[k] for k in io if k!='fonte') and now['fonte']['sha256']==sha(after[A])
assert rd('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith((p/'inventario-oficial-antes.md').read_bytes())
print(json.dumps({'ok':True,'edicoes':2,'artigos':197,'formulario_preservado':True,'mathml':[734,191],'pares':counts,'internos_por_edicao':internal,'alterados':changed,'referencias':816,'recursos':138},ensure_ascii=False))
