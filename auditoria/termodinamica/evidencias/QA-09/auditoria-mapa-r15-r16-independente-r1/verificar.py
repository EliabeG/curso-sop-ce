#!/usr/bin/env python3
"""Revisão estrutural do mapa efetivo, sem escrita nos dados examinados."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,subprocess
Q=Path('auditoria/termodinamica/evidencias/QA-09');P=Q/'aplicacao-conjunta-r16-r1/resultado'
def digest(b):return sha256(b).hexdigest()
def read(p,expected):
 b=Path(p).read_bytes();assert digest(b)==expected,p;return b
A=Q/'inventario-r15.json';B=Q/'inventario-r16.json';MP=Q/'mapa-correspondencia-inventario-r15-r16-r1.json'
a=json.loads(read(A,'c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c'));b=json.loads(read(B,'2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd'));m=json.loads(read(MP,'a3edb9fab577c58e5b3df4831ee8cfb09d8e8b39bf92d1efcd5e0a5f39b2d4d0')); edits=json.loads(read(P/'edicoes-aplicadas.json','544ea43568eed6ef44aaf6710a81cd11b815bc6bf7bf8da3a36c6f96b4a449b7'));assert m['edicoes']==edits and m['base_r15']==digest(A.read_bytes()) and m['base_r16']==digest(B.read_bytes())
assert len(edits)==5 and len(a['ocorrencias'])==11399 and len(b['ocorrencias'])==11400
files={'modulos/e1-termodinamica.html':('antes-aula.html','depois-aula.html','f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e','55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23'),'formulas/termodinamica.html':('antes-formulario.html','depois-formulario.html','3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce','dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d')}
def part(text,start,end):return text.encode('utf-16-le')[start*2:end*2].decode('utf-16-le')
for doc,(old,new,ha,hb) in files.items():
 h=read(P/old,ha).decode();n=read(P/new,hb).decode();assert read(doc,hb).decode()==n
 es=sorted([x for x in edits if x['documento']==doc],key=lambda x:x['inicio']);last=0;output=''
 for e in es:
  assert e['inicio']>=last and e['delta']==(e['fim_novo']-e['inicio_novo'])-(e['fim']-e['inicio'])
  output+=part(h,last,e['inicio']);orig=part(h,e['inicio'],e['fim']);newtext=part(n,e['inicio_novo'],e['fim_novo']);assert digest(orig.encode())==e['original_sha256'] and digest(newtext.encode())==e['candidata_sha256'];output+=newtext;last=e['fim']
 output+=part(h,last,len(h.encode('utf-16-le'))//2);assert output==n
byid=lambda i:{x['id']:x for x in i['ocorrencias']}
order_a={o['id']:i for i,o in enumerate(a['ocorrencias'])};order_b={o['id']:i for i,o in enumerate(b['ocorrencias'])};previous={}
x=byid(a);y=byid(b);assert len(x)==len(a['ocorrencias']) and len(y)==len(b['ocorrencias']);useda=set();usedb=set();counts=Counter();changed=[];added=[]
for r in m['pares']:
 st=r['estado'];counts[st]+=1;ia=r.get('id_r15');ib=r.get('id_r16');oa=x.get(ia);ob=y.get(ib)
 if ia:assert ia in x and ia not in useda and r['sha256_r15']==oa['sha256_fragmento'];useda.add(ia)
 if ib:assert ib in y and ib not in usedb and r['sha256_r16']==ob['sha256_fragmento'];usedb.add(ib)
 if oa and ob:
  assert all(oa.get(k)==ob.get(k) for k in ('arquivo','secao','ancora','tag','tipo'))
  if st=='PAREADO_EXTERNO':assert oa['sha256_fragmento']==ob['sha256_fragmento']
  elif st=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':assert oa['sha256_fragmento']!=ob['sha256_fragmento'] and any(e['documento']==oa['arquivo'] and oa['inicio_utf16']<=e['inicio'] and oa['fim_utf16']>=e['fim'] for e in edits)
  elif st=='PAREADO_INTERNO_CONFERIR':
   e=next(e for e in edits if e['id']==r['edicao']);pos=(order_a[ia],order_b[ib]);prev=previous.get(e['id'],(-1,-1));assert pos[0]>prev[0] and pos[1]>prev[1];previous[e['id']]=pos;assert e['documento']==oa['arquivo']==ob['arquivo'] and e['inicio']<=oa['inicio_utf16']<e['fim'] and e['inicio_novo']<=ob['inicio_utf16']<e['fim_novo']
   if oa['sha256_fragmento']!=ob['sha256_fragmento']:changed.append({'edicao':e['id'],'tipo':oa['tipo'],'tag':oa['tag'],'antes':oa.get('texto',oa.get('atributos')),'depois':ob.get('texto',ob.get('atributos'))})
  else:raise AssertionError(st)
 else:
  assert st=='ADICIONADO_OU_REESTRUTURADO' and oa is None and ob is not None;e=next(e for e in edits if e['id']==r['edicao']);assert e['inicio_novo']<=ob['inicio_utf16']<e['fim_novo'];added.append({'edicao':e['id'],'tipo':ob['tipo'],'tag':ob['tag'],'texto':ob.get('texto')})
assert useda==set(x) and usedb==set(y)
assert counts=={'PAREADO_EXTERNO':11021,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':3,'PAREADO_INTERNO_CONFERIR':375,'ADICIONADO_OU_REESTRUTURADO':1}
assert len(changed)==11 and len(added)==1 and added[0]['edicao']=='base-eficiencia-cop' and added[0]['tag']=='p'
assert len(a['referencias'])==len(b['referencias'])==816 and not m['referencias_mudadas'] and not m['referencias_novas']
for u,v in zip(a['referencias'],b['referencias']):
 assert all(u.get(k)==v.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
 before=(P/files[u['arquivo']][0]).read_text();after=(P/files[u['arquivo']][1]).read_text()
 assert part(before,u['inicio_utf16'],u['fim_utf16'])==part(after,v['inicio_utf16'],v['fim_utf16'])
assert len(a['recursos'])==len(b['recursos'])==138 and not m['recursos_mudados']
for u,v in zip(a['recursos'],b['recursos']):
 assert all(u.get(k)==v.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if u['arquivo'] in files:assert u['sha256']==files[u['arquivo']][2] and v['sha256']==files[u['arquivo']][3]
 else:assert u['sha256']==v['sha256']==digest(Path(u['arquivo']).read_bytes())
assert a['ativos_especificos']==b['ativos_especificos'] and a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
js='''import fs from 'node:fs';import {parseHtml,isInventoryArticle} from './auditoria/termodinamica/inventario/validar-inventario.mjs';let p='auditoria/termodinamica/evidencias/QA-09/aplicacao-conjunta-r16-r1/resultado/';let a=fs.readFileSync(p+'antes-aula.html','utf8'),b=fs.readFileSync(p+'depois-aula.html','utf8'),x=parseHtml(a),y=parseHtml(b);if(x.errors.length||y.errors.length)throw Error('parser');let A=x.nodes.filter(isInventoryArticle),B=y.nodes.filter(isInventoryArticle);if(A.length!==197||B.length!==197||A.some((v,i)=>v.attrs.id!==B[i].attrs.id||a.slice(v.start,v.end)!==b.slice(B[i].start,B[i].end)))throw Error('artigos');console.log('OK')'''
assert subprocess.check_output(['node','--input-type=module','-e',js],text=True).strip()=='OK'
oldofficial=json.loads((P/'inventario-oficial-antes.json').read_bytes());new=json.loads(Path('auditoria/termodinamica/inventario/inventario-questoes.json').read_bytes());assert oldofficial['itens']==new['itens'] and len(new['itens'])==197 and new['fonte']['sha256']==files['modulos/e1-termodinamica.html'][3]
print(json.dumps({'ok':True,'contagens':counts,'pares_internos_hash_diferente':len(changed),'mudancas_internas':changed,'adicionados':added,'refs':816,'recursos':138,'artigos':197,'limite':'Pares estruturais não transferem aceites; comparação de contexto não é avaliação científica.'},ensure_ascii=False,indent=2))
