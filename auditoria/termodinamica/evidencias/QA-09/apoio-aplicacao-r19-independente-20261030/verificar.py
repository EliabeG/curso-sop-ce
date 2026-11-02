#!/usr/bin/env python3
"""Apoio estrutural: recompõe r19 e verifica o mapa; somente leitura."""
import collections,hashlib,json,re
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=r/(q+'aplicacao-notacao-fichas-r19-r1/resultado');rd=lambda x:(r/x).read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html';before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()};after={A:rd(A),F:rd(F)}
for doc,old,new in [(A,'7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca','9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65'),(F,'463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58')]:
 assert sha(before[doc])==old and sha(after[doc])==new and after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes();assert sha(edb)=='925a4ab4981eb855569c2f8e065501091b8190e177594428130e40a6d3fdd610';ed=json.loads(edb)
nd=r/(q+'candidata-notacao-propriedades-r18-20261030');fd=r/(q+'candidatas-fichas-61-80-r18-20261030')
nb=(nd/'manifesto.json').read_bytes();fb=(fd/'manifesto.json').read_bytes();assert sha(nb)=='ea6eb91f1015d78362f6b0ba192d299ec3c75198f1867bc3ea60ffc6cfa3e092' and sha(fb)=='dfa6ca4b00e704e3eee4c909dc09561a011dd429bdadb77b21efa908bf9cb521'
nm,fm=json.loads(nb),json.loads(fb);candidates={nm['ancora']:nd/'candidata.html'};candidates.update({x['id']:fd/(str(x['ficha'])+'-candidata.html') for x in fm['itens']})
assert len(ed)==3 and set(candidates)=={e['id'] for e in ed}
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
ib=rd(q+'inventario-r18.json');ic=rd(q+'inventario-r19.json');mp=rd(q+'mapa-correspondencia-inventario-r18-r19-r1.json')
assert sha(ib)=='717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc' and sha(ic)=='ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f' and sha(mp)=='42c39e8093294c19a12526262140056fc0e2da71120c48e142cab3cd06ed9be5'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197 and m['edicoes']==ed
for x in a['artigos_excluidos']: assert aa[x['id'].encode()]==ab[x['id'].encode()] and sha(aa[x['id'].encode()])==x['sha256_fragmento']
assert len(fa)==len(fbb)==100 and fa.keys()==fbb.keys()
assert all(fa[k]==fbb[k] for k in fa if k not in (b'formula-carnot',b'formula-brayton-liquido'))
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};useda=[];usedb=[];changed=collections.Counter();internal=collections.Counter()
for row in m['pares']:
 x=old[row['id_r18']];y=new[row['id_r19']];useda.append(x['id']);usedb.append(y['id']);assert row['sha256_r18']==x['sha256_fragmento'] and row['sha256_r19']==y['sha256_fragmento']
 if row['estado']=='PAREADO_EXTERNO':assert x['sha256_fragmento']==y['sha256_fragmento']
 if row['estado']=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':
  assert x['sha256_fragmento']!=y['sha256_fragmento'] and any(z['documento']==x['arquivo'] and x['inicio_utf16']<=z['inicio'] and x['fim_utf16']>=z['fim'] for z in ed)
 if row['estado']=='PAREADO_INTERNO_CONFERIR':
  e=next(z for z in ed if z['id']==row['edicao']);assert x['arquivo']==y['arquivo']==e['documento'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
  assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);internal[e['id']]+=1
  if x['sha256_fragmento']!=y['sha256_fragmento']:changed[e['id']]+=1
assert len(useda)==len(set(useda))==len(old)==11400 and len(usedb)==len(set(usedb))==len(new)==11400
counts=collections.Counter(z['estado'] for z in m['pares']);assert counts=={'PAREADO_EXTERNO':11279,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':3,'PAREADO_INTERNO_CONFERIR':118}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());now=json.loads(rd('auditoria/termodinamica/inventario/inventario-questoes.json'));assert len(io['itens'])==197 and io['itens']==now['itens'] and all(io[k]==now[k] for k in io if k!='fonte') and now['fonte']['sha256']==sha(after[A])
assert rd('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith((p/'inventario-oficial-antes.md').read_bytes())
print(json.dumps({'ok':True,'edicoes':3,'artigos':197,'fichas_nao_alvo':98,'mathml':[734,191],'pares':counts,'internos_por_edicao':internal,'alterados':changed,'referencias':816,'recursos':138},ensure_ascii=False))
