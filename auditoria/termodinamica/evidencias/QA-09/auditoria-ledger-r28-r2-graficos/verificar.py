#!/usr/bin/env python3
"""Reextração independente dos 78 registros e contextos; negativos em /tmp."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from collections import Counter
import copy,json,re,subprocess,tempfile
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';d=q/'ledger-r28-parcial-r2';p=q/'aplicacao-conjunta-r28/resultado';sha=lambda b:sha256(b).hexdigest()
for f,h in [(d/'LEIA-ME.md','a530f9622f79e1ffa3bc4a318317a5c2167045f5b8742841750af7a1805c5b1c'),(d/'ledger.json','518e6b952254773be5d95ba31e06607ba0a34562d6d90162f9b95d36f6fba000'),(d/'ledger.mjs','a2692e9afa7ceedc969095cdab84f96f19c69c32380fca0175c48c94bc18a498'),(d/'reconciliacao.md','a0f53441b052372a3d7f2df12a3b9b02218a0fbf1ef7032f4c70cbf38b812af1'),(d/'juizos.json','4e3a566c41cd21b057af57a194b596d7fa85e60f0ca6b7e9eae181fdc16cf908')]:assert sha(f.read_bytes())==h
j=json.loads((d/'ledger.json').read_bytes());prev=json.loads((q/'ledger-r27-expandido-r3/ledger.json').read_bytes());rows=j['objetos'];assert len(rows)==78 and len({x['id'] for x in rows})==78
assert [x['id'] for x in rows]==[x['id_local'] for x in prev['registros_explicitamente_revisados']]+[x['id'] for x in prev['registros_adicionais_por_recorte']]
assert Counter(x['tipo'] for x in rows)=={'base':18,'ficha':22,'bloco_teoria':6,'figura_svg':4,'artigo_grafico':3,'diagnostico':15,'exemplo':10}
docs={}
for doc,stem in [('modulos/e1-termodinamica.html','aula'),('formulas/termodinamica.html','formulario')]:
 docs[doc]={}
 for version,pre in [('r27','antes'),('r28','depois')]:
  b=(p/f'{pre}-{stem}.html').read_bytes();docs[doc][version]=(b.decode(),b.decode().encode('utf-16-le'))
expected={('modulos/e1-termodinamica.html','r27'):'9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49',('modulos/e1-termodinamica.html','r28'):'d7294e8ed772cf4530788586d693a6cdfbf1ef6fa05c69afbc984efc46e353d8',('formulas/termodinamica.html','r27'):'16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02',('formulas/termodinamica.html','r28'):'3157c9b114f3156e5517440d30b91ee8a4efdebcd95be8bd0c7a588f04dead46'}
for (doc,ver),digest in expected.items():assert sha(docs[doc][ver][0].encode())==digest
class End(HTMLParser):
 def __init__(self,text,tag):super().__init__();self.depth=0;self.end=None;self.tag=tag;self.lines=[0]+[m.end() for m in re.finditer('\n',text)]
 def handle_starttag(self,t,a):
  if t==self.tag:self.depth+=1
 def handle_endtag(self,t):
  if t==self.tag:
   self.depth-=1
   if self.depth==0 and self.end is None:self.end=self.lines[self.getpos()[0]-1]+self.getpos()[1]+len('</'+t+'>')
def ctx(text,id):
 if id=='titulo-ex004':needle='Título a partir da entalpia'
 else:needle='id="'+id+'"'
 assert text.count(needle)==1,(id,text.count(needle));pos=text.index(needle)
 if id=='substancias':start=text.rfind('<section ',0,pos);tag='section'
 else:start=text.rfind('<div class="bloco-aula">',0,pos);tag='div'
 assert start>=0;part=text[start:];parser=End(part,tag);parser.feed(part);assert parser.end is not None;res=part[:parser.end];assert needle in res;return res
cached={};changed=[]
for x in rows:
 frag=[]
 for ver in ['r27','r28']:
  val=x[ver];text,u=docs[x['arquivo']][ver];a,z=val['inicio_utf16'],val['fim_utf16'];f=u[2*a:2*z].decode('utf-16-le');assert sha(f.encode())==val['sha256'];frag.append(f)
 assert frag[0]==frag[1] and x['estado']=='revalidado_pelo_integrador_pendente_de_auditoria_independente'
 for c in x['contextos']:
  key=c['id']
  if key not in cached:cached[key]=[ctx(docs['modulos/e1-termodinamica.html'][ver][0],key) for ver in ('r27','r28')]
  a,b=cached[key];assert sha(a.encode())==c['sha256_r27'] and sha(b.encode())==c['sha256_r28'] and c['alterado']==(a!=b)
  if a!=b:changed.append((x['id'],key))
assert Counter(c for _,c in changed)=={'base-leitura-matematica':9,'substancias':3} and len(changed)==12
ix=[]
for version in ('r27','r28'):
 v=json.loads((q/f'inventario-{version}.json').read_bytes());ix.append({x['id']:x for x in v['ocorrencias']})
mp=json.loads((q/'mapa-correspondencia-inventario-r27-r28-r1.json').read_bytes());assert sha((q/'mapa-correspondencia-inventario-r27-r28-r1.json').read_bytes())=='0e219e8d2863e3d7ced3af4857ce462ca5827bda38276da2a005e5f39e23eca2'
seen=[[],[]]
for row in mp['pares']:
 for k,ver in enumerate(('r27','r28')):
  id=row.get('id_'+ver)
  if id:assert id in ix[k] and ix[k][id]['sha256_fragmento']==row['sha256_'+ver];seen[k].append(id)
assert len(seen[0])==len(set(seen[0]))==len(ix[0])==11407 and len(seen[1])==len(set(seen[1]))==len(ix[1])==11409
for x in rows[:18]:
 pair=x['par_inventario'];a=ix[0][pair['id_r27']];b=ix[1][pair['id_r28']];assert a['sha256_fragmento']==b['sha256_fragmento']==x['r27']['sha256'] and b['inicio_utf16']==x['r28']['inicio_utf16']
assert all(v['estado_padrao']=='pendente_de_integracao' for v in j['colecoes'].values())
with tempfile.TemporaryDirectory(prefix='qa-ledger-r28-audit-') as tmp:
 f=Path(tmp)/'test.json';cmd=['node',str(d/'ledger.mjs'),'--verificar',str(f)]
 def run(v):f.write_text(json.dumps(v,ensure_ascii=False));return subprocess.run(cmd,cwd=r,capture_output=True).returncode
 assert run(j)==0
 for change in (lambda z:z['objetos'][0]['r28'].update(sha256='0'*64),lambda z:z['objetos'][0]['r28'].update(inicio_utf16=0),lambda z:z['objetos'].pop(),lambda z:z['colecoes']['ocorrencias'].update(estado_padrao='aprovado'),lambda z:z['objetos'][0]['contextos'][0].update(sha256_r28='0'*64),lambda z:z['objetos'][0]['par_inventario'].update(id_r28='falso'),lambda z:z['objetos'][0]['juizo'].update(juizo_local='falso')):
  v=copy.deepcopy(j);change(v);assert run(v)!=0
print(json.dumps({'ok':True,'objetos':len(rows),'contextos_distintos':len(cached),'associacoes_alteradas':12,'mapa_r27':len(seen[0]),'mapa_r28':len(seen[1]),'testes_negativos':7,'sem_escrita_em_produto':True}))
