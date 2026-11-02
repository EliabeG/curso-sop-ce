#!/usr/bin/env python3
"""Auditoria estrutural somente leitura da aplicação efetiva r16."""
import collections, hashlib, json, re
from pathlib import Path
r=Path(__file__).resolve().parents[5]; q='auditoria/termodinamica/evidencias/QA-09/'
p=r/(q+'aplicacao-conjunta-r16-r1/resultado'); sha=lambda b:hashlib.sha256(b).hexdigest()
read=lambda s:(r/s).read_bytes()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html'
before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()}
after={A:read(A),F:read(F)}
for doc,old,new in [(A,'f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e','55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23'),(F,'3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce','dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d')]:
 assert sha(before[doc])==old and sha(after[doc])==new
 assert after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes(); assert sha(edb)=='544ea43568eed6ef44aaf6710a81cd11b815bc6bf7bf8da3a36c6f96b4a449b7';ed=json.loads(edb)
theory=r/(q+'candidatas-teoria-ciclos-r15-20261030');forms=r/(q+'candidatas-fichas-89-90-r15-20261030')
tb=(theory/'manifesto.json').read_bytes();fmb=(forms/'manifesto.json').read_bytes()
assert sha(tb)=='2f2976954c12c58cf14a487922082361d305de584a9127b431f426551310ebab' and sha(fmb)=='093609d634e7e875aa51e5999494fa3ec2642be5c63c91e8a8c3a58de6a13cdf'
tm=json.loads(tb);fm=json.loads(fmb)
candidates={x['id']:theory/(x['id']+'-candidata.html') for x in tm['itens']}
candidates.update({x['ancora']:forms/(str(x['ficha'])+'-candidata.html') for x in fm['itens']})
assert len(ed)==5 and set(candidates)=={x['id'] for x in ed}
for doc in (A,F):
 u=before[doc].decode().encode('utf-16-le')
 for e in sorted((x for x in ed if x['documento']==doc),key=lambda x:x['inicio'],reverse=True):
  old=u[e['inicio']*2:e['fim']*2].decode('utf-16-le').encode();new=candidates[e['id']].read_bytes().removesuffix(b'\n')
  assert sha(old)==e['original_sha256'] and sha(new)==e['candidata_sha256']
  u=u[:e['inicio']*2]+new.decode().encode('utf-16-le')+u[e['fim']*2:]
 assert u.decode('utf-16-le').encode()==after[doc]
 def maths(b):return re.findall(rb'<math\b.*?</math>',b,re.S)
 assert maths(before[doc])==maths(after[doc])
 assert len(maths(after[doc]))==({A:734,F:191}[doc])
def articles(raw):
 out={}
 for m in re.finditer(rb'<article\b[^>]*>.*?</article>',raw,re.S):
  tag=m.group().split(b'>',1)[0];match=re.search(rb'\bid="([^"]+)"',tag)
  if match: out[match.group(1).decode()]=m.group()
 return out
aa,ab=articles(before[A]),articles(after[A]);fa,fb=articles(before[F]),articles(after[F])
ib=read(q+'inventario-r15.json');ic=read(q+'inventario-r16.json');mp=read(q+'mapa-correspondencia-inventario-r15-r16-r1.json')
assert sha(ib)=='c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c' and sha(ic)=='2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd' and sha(mp)=='a3edb9fab577c58e5b3df4831ee8cfb09d8e8b39bf92d1efcd5e0a5f39b2d4d0'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
assert m['edicoes']==ed and m['base_r15']==sha(ib) and m['base_r16']==sha(ic)
for x in a['artigos_excluidos']:assert aa[x['id']]==ab[x['id']] and sha(aa[x['id']])==x['sha256_fragmento']
assert len(fa)==len(fb)==100 and set(fa)==set(fb)
assert all(fa[k]==fb[k] for k in fa if k not in ('formula-politropico','formula-compressao-isotermica'))
oa={x['id']:x for x in a['ocorrencias']};ob={x['id']:x for x in b['ocorrencias']};seen_a=[];seen_b=[]
for row in m['pares']:
 if row.get('id_r15'):x=oa[row['id_r15']];seen_a.append(x['id']);assert x['sha256_fragmento']==row['sha256_r15']
 if row.get('id_r16'):y=ob[row['id_r16']];seen_b.append(y['id']);assert y['sha256_fragmento']==row['sha256_r16']
assert len(seen_a)==len(set(seen_a))==len(oa)==11399 and len(seen_b)==len(set(seen_b))==len(ob)==11400
counts=collections.Counter(x['estado'] for x in m['pares']);assert counts=={'PAREADO_EXTERNO':11021,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':3,'PAREADO_INTERNO_CONFERIR':375,'ADICIONADO_OU_REESTRUTURADO':1}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());inow=json.loads(read('auditoria/termodinamica/inventario/inventario-questoes.json'))
assert len(io['itens'])==197 and io['itens']==inow['itens']
assert all(io[k]==inow[k] for k in io if k!='fonte')
assert inow['fonte']['sha256']==sha(after[A]) and inow['fonte']['snapshot']==str((p/'depois-aula.html').relative_to(r))
note=(p/'inventario-oficial-antes.md').read_bytes();assert read('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith(note)
print(json.dumps({'ok':True,'cinco_deltas':5,'artigos':197,'fichas_nao_alvo':98,'mathml':[734,191],'classificacao':counts,'referencias':816,'recursos':138},ensure_ascii=False))
