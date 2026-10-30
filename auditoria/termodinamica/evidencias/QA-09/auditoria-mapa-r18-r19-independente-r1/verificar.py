#!/usr/bin/env python3
"""Revisão estrutural do mapa efetivo, sem escrita nos dados examinados."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,subprocess
Q=Path('auditoria/termodinamica/evidencias/QA-09');P=Q/'aplicacao-notacao-fichas-r19-r1/resultado'
def digest(b):return sha256(b).hexdigest()
def read(p,expected):
 b=Path(p).read_bytes();assert digest(b)==expected,p;return b
A=Q/'inventario-r18.json';B=Q/'inventario-r19.json';MP=Q/'mapa-correspondencia-inventario-r18-r19-r1.json'
a=json.loads(read(A,'717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc'));b=json.loads(read(B,'ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f'));m=json.loads(read(MP,'42c39e8093294c19a12526262140056fc0e2da71120c48e142cab3cd06ed9be5')); edits=json.loads(read(P/'edicoes-aplicadas.json','925a4ab4981eb855569c2f8e065501091b8190e177594428130e40a6d3fdd610'));assert m['edicoes']==edits and m['base_r18']==digest(A.read_bytes()) and m['base_r19']==digest(B.read_bytes())
assert len(edits)==3 and len(a['ocorrencias'])==11400 and len(b['ocorrencias'])==11400
files={'modulos/e1-termodinamica.html':('antes-aula.html','depois-aula.html','7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca','9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65'),'formulas/termodinamica.html':('antes-formulario.html','depois-formulario.html','463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895','694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58')}
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
 st=r['estado'];counts[st]+=1;ia=r.get('id_r18');ib=r.get('id_r19');oa=x.get(ia);ob=y.get(ib)
 if ia:assert ia in x and ia not in useda and r['sha256_r18']==oa['sha256_fragmento'];useda.add(ia)
 if ib:assert ib in y and ib not in usedb and r['sha256_r19']==ob['sha256_fragmento'];usedb.add(ib)
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
assert counts=={'PAREADO_EXTERNO':11279,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':3,'PAREADO_INTERNO_CONFERIR':118}
assert len(changed)==10 and len(added)==0
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
js='''import fs from 'node:fs';import {parseHtml,isInventoryArticle} from './auditoria/termodinamica/inventario/validar-inventario.mjs';let p='auditoria/termodinamica/evidencias/QA-09/aplicacao-notacao-fichas-r19-r1/resultado/';let a=fs.readFileSync(p+'antes-aula.html','utf8'),b=fs.readFileSync(p+'depois-aula.html','utf8'),x=parseHtml(a),y=parseHtml(b);if(x.errors.length||y.errors.length)throw Error('parser');let A=x.nodes.filter(isInventoryArticle),B=y.nodes.filter(isInventoryArticle);if(A.length!==197||B.length!==197||A.some((v,i)=>v.attrs.id!==B[i].attrs.id||a.slice(v.start,v.end)!==b.slice(B[i].start,B[i].end)))throw Error('artigos');let M=x.nodes.filter(v=>v.tag==='math'),N=y.nodes.filter(v=>v.tag==='math');if(M.length!==734||N.length!==734||M.some((v,i)=>a.slice(v.start,v.end)!==b.slice(N[i].start,N[i].end)))throw Error('MathML');console.log('OK')'''
assert subprocess.check_output(['node','--input-type=module','-e',js],text=True).strip()=='OK'
js2=r"""import fs from 'node:fs';import {parseHtml} from './auditoria/termodinamica/inventario/validar-inventario.mjs';let p='auditoria/termodinamica/evidencias/QA-09/aplicacao-notacao-fichas-r19-r1/resultado/';let a=fs.readFileSync(p+'antes-formulario.html','utf8'),b=fs.readFileSync(p+'depois-formulario.html','utf8'),x=parseHtml(a),y=parseHtml(b);let cards=d=>d.nodes.filter(n=>n.tag==='article'&&(n.attrs.class||'').split(/\s+/).includes('formula-card')),u=cards(x),v=cards(y);if(u.length!==100||v.length!==100)throw Error('quantidade');let changed=[];for(let i=0;i<100;i++){if(u[i].attrs.id!==v[i].attrs.id)throw Error('ordem');if(a.slice(u[i].start,u[i].end)!==b.slice(v[i].start,v[i].end))changed.push(u[i].attrs.id)}if(JSON.stringify(changed)!==JSON.stringify(['formula-carnot','formula-brayton-liquido']))throw Error('fichas');let M=x.nodes.filter(n=>n.tag==='math'),N=y.nodes.filter(n=>n.tag==='math');if(M.length!==191||N.length!==191||M.some((n,i)=>a.slice(n.start,n.end)!==b.slice(N[i].start,N[i].end)))throw Error('MathML');console.log('OK')"""
assert subprocess.check_output(['node','--input-type=module','-e',js2],text=True).strip()=='OK'

oldofficial=json.loads((P/'inventario-oficial-antes.json').read_bytes());new=json.loads(Path('auditoria/termodinamica/inventario/inventario-questoes.json').read_bytes());assert oldofficial['itens']==new['itens'] and len(new['itens'])==197 and new['fonte']['sha256']==files['modulos/e1-termodinamica.html'][3]
print(json.dumps({'ok':True,'contagens':counts,'pares_internos_hash_diferente':len(changed),'mudancas_internas':changed,'adicionados':added,'refs':816,'recursos':138,'artigos':197,'limite':'Pares estruturais não transferem aceites; comparação de contexto não é avaliação científica.'},ensure_ascii=False,indent=2))
