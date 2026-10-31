#!/usr/bin/env python3
"""Apoio estrutural: recompõe r23 e verifica o mapa; somente leitura."""
import collections,hashlib,json,re
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=r/(q+'aplicacao-resumo-glossario-r23-r1/resultado');rd=lambda x:(r/x).read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
A='modulos/e1-termodinamica.html';F='formulas/termodinamica.html';before={A:(p/'antes-aula.html').read_bytes(),F:(p/'antes-formulario.html').read_bytes()};after={A:rd(A),F:rd(F)}
for doc,old,new in [(A,'ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f','f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d'),(F,'694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58')]:
 assert sha(before[doc])==old and sha(after[doc])==new and after[doc]==(p/('depois-aula.html' if doc==A else 'depois-formulario.html')).read_bytes()
edb=(p/'edicoes-aplicadas.json').read_bytes();assert sha(edb)=='2d02029dd9bbcde19e147be8c850147e8dc9cb8e9c0b383369e67b83195e03db';ed=json.loads(edb)
candidates={}
for name,expected in [('resumo','c893fbd1e95582add646f384f187d601993286a078455736d1a12b090befdbe9'),('glossario','1c6fbe50b85c9e4dd7be36c864af7767781c9748324748548d0e1e4fc98aacbd')]:
 d=r/(q+'candidata-'+name+'-r22-next-theory-20261030'); mb=(d/'manifesto.json').read_bytes(); assert sha(mb)==expected
 manifest=json.loads(mb); candidates[manifest['ancora']]=d/'candidata.html'
assert len(ed)==2 and set(candidates)=={e['id'] for e in ed}
e0,e1=sorted(ed,key=lambda e:e['inicio']);assert e1['inicio']-e0['fim']==1 and e1['inicio_novo']-e0['fim_novo']==1
oldbytes=before[A].decode().encode('utf-16-le');newbytes=after[A].decode().encode('utf-16-le');assert oldbytes[2*e0['fim']:2*e1['inicio']]==newbytes[2*e0['fim_novo']:2*e1['inicio_novo']]
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
ib=rd(q+'inventario-r22.json');ic=rd(q+'inventario-r23.json');mp=rd(q+'mapa-correspondencia-inventario-r22-r23-r1.json')
assert sha(ib)=='6e68d5a9e5cfec73aa2a5ce24121ede1c3a155ca2a5783cf6f17ca95eee8061b' and sha(ic)=='ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e' and sha(mp)=='9a3c42d4f075f6a686b969a34d82ae439270fd50d49f25458b1d494caa205dd0'
a,b,m=map(json.loads,(ib,ic,mp));assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197 and m['edicoes']==ed
for x in a['artigos_excluidos']: assert aa[x['id'].encode()]==ab[x['id'].encode()] and sha(aa[x['id'].encode()])==x['sha256_fragmento']
assert len(fa)==len(fbb)==100 and fa.keys()==fbb.keys()
assert fa==fbb and before[F]==after[F]
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};useda=[];usedb=[];changed=collections.Counter();internal=collections.Counter()
for row in m['pares']:
 x=old[row['id_r22']];y=new[row['id_r23']];useda.append(x['id']);usedb.append(y['id']);assert row['sha256_r22']==x['sha256_fragmento'] and row['sha256_r23']==y['sha256_fragmento']
 if row['estado']=='PAREADO_EXTERNO':assert x['sha256_fragmento']==y['sha256_fragmento']
 if row['estado']=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':
  assert x['sha256_fragmento']!=y['sha256_fragmento'] and any(z['documento']==x['arquivo'] and x['inicio_utf16']<=z['inicio'] and x['fim_utf16']>=z['fim'] for z in ed)
 if row['estado']=='PAREADO_INTERNO_CONFERIR':
  e=next(z for z in ed if z['id']==row['edicao']);assert x['arquivo']==y['arquivo']==e['documento'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
  assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);internal[e['id']]+=1
  if x['sha256_fragmento']!=y['sha256_fragmento']:changed[e['id']]+=1
assert len(useda)==len(set(useda))==len(old)==11400 and len(usedb)==len(set(usedb))==len(new)==11400
counts=collections.Counter(z['estado'] for z in m['pares']);assert counts=={'PAREADO_EXTERNO':11104,'PAREADO_INTERNO_CONFERIR':296}
assert len(a['referencias'])==len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
for x,y in zip(a['referencias'],b['referencias']):assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in (A,F):assert x['sha256']==sha(before[x['arquivo']]) and y['sha256']==sha(after[y['arquivo']])
 else:assert x['sha256']==y['sha256']
io=json.loads((p/'inventario-oficial-antes.json').read_bytes());now=json.loads(rd('auditoria/termodinamica/inventario/inventario-questoes.json'));assert len(io['itens'])==197 and io['itens']==now['itens'] and all(io[k]==now[k] for k in io if k!='fonte') and now['fonte']['sha256']==sha(after[A])
assert rd('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').startswith((p/'inventario-oficial-antes.md').read_bytes())
print(json.dumps({'ok':True,'edicoes':2,'artigos':197,'formulario_preservado':True,'mathml':[734,191],'pares':counts,'internos_por_edicao':internal,'alterados':changed,'referencias':816,'recursos':138},ensure_ascii=False))
