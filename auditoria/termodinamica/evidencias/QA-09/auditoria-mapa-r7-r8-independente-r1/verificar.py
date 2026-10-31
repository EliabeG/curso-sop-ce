#!/usr/bin/env python3
"""Verificação independente em modo leitura de r7→r8; sem gravar evidências."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import json,re
from html.parser import HTMLParser
D=Path('auditoria/termodinamica/evidencias/QA-09'); P=D/'aplicacao-razao-percentual-r1'
def raw(path): return Path(path).read_bytes()
def digest(path): return sha256(raw(path)).hexdigest()
H0='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f';H1='57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c'; I0='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a';I1='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687';M='37d48a92165de1e29573b3ed5af992bd16df9a5da71b8372576fd84f0e6657fc'
assert digest(P/'antes.html')==H0 and digest(P/'depois.html')==H1 and digest('modulos/e1-termodinamica.html')==H1
assert digest(D/'inventario-r7.json')==I0 and digest(D/'inventario-r8.json')==I1 and digest(D/'mapa-correspondencia-inventario-r7-r8-r1.json')==M
old=raw(P/'antes.html').decode();new=raw(P/'depois.html').decode();old16=old.encode('utf-16-le');new16=new.encode('utf-16-le')
A=json.loads(raw(D/'inventario-r7.json'));B=json.loads(raw(D/'inventario-r8.json'));mp=json.loads(raw(D/'mapa-correspondencia-inventario-r7-r8-r1.json'));edits=json.loads(raw(P/'edicoes-aplicadas.json'))
assert len(edits)==4 and all(edits[i]['fim']<=edits[i+1]['inicio'] for i in range(3))
parts=[];cursor=0
for e in edits:
 o=raw(e['original']).decode().removesuffix('\n');n=raw(e['candidata']).decode().removesuffix('\n')
 assert sha256(o.encode()).hexdigest()==e['original_sha256'] and sha256(n.encode()).hexdigest()==e['candidata_sha256']
 assert old.count(o)==1 and new.count(n)==1 and old16[2*e['inicio']:2*e['fim']].decode('utf-16-le')==o
 assert len(n.encode('utf-16-le'))//2-len(o.encode('utf-16-le'))//2==e['delta']
 parts.extend([old16[2*cursor:2*e['inicio']],n.encode('utf-16-le')]);cursor=e['fim']
assert b''.join(parts)+old16[2*cursor:]==new16
assert len(A['ocorrencias'])==len(B['ocorrencias'])==len(mp['correspondencias'])==11396
assert len({x['id'] for x in A['ocorrencias']})==len(A['ocorrencias']) and len({x['id'] for x in B['ocorrencias']})==len(B['ocorrencias'])
offset=lambda p:sum(e['delta'] for e in edits if p>=e['fim'])
inside=lambda p:any(e['inicio']<=p<e['fim'] for e in edits)
changed=[];inner=[];fullhash=0
for i,(x,y,z) in enumerate(zip(A['ocorrencias'],B['ocorrencias'],mp['correspondencias'])):
 for key in ('arquivo','tipo','tag','secao','ancora'): assert x[key]==y[key]==z[key],(i,key)
 assert z['id_r7']==x['id'] and z['id_r8']==y['id'] and z['inicio_r7']==x['inicio_utf16'] and z['inicio_r8']==y['inicio_utf16']
 assert z['sha256_fragmento_r7']==x['sha256_fragmento'] and z['sha256_fragmento_r8']==y['sha256_fragmento']
 affected=x['arquivo']=='modulos/e1-termodinamica.html' and inside(x['inicio_utf16'])
 assert z['dentro_do_bloco_editado']==affected
 if affected: inner.append(i)
 else: assert y['inicio_utf16']==x['inicio_utf16']+(offset(x['inicio_utf16']) if x['arquivo']=='modulos/e1-termodinamica.html' else 0),(i,'inicio')
 different=x['sha256_fragmento']!=y['sha256_fragmento']; assert z['correspondencia']==('CONTEUDO_ALTERADO_OU_ANCESTRAL' if different else 'CONTEUDO_IDENTICO')
 if different: changed.append((i,x['id'],y['id'],x['tipo']))
 if x['arquivo']=='modulos/e1-termodinamica.html' and x['tipo'] not in ('texto_direto','atributos_significativos'):
  assert sha256(old16[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le').encode()).hexdigest()==x['sha256_fragmento']
  assert sha256(new16[2*y['inicio_utf16']:2*y['fim_utf16']].decode('utf-16-le').encode()).hexdigest()==y['sha256_fragmento'];fullhash+=1
# Hash do texto direto dos quatro nós alterados: extrai as partes entre filhos,
# sem usar o gerador de inventário. Esses quatro fragmentos não contêm quebras de linha.
class DirectText(HTMLParser):
 def __init__(self,fragment):
  super().__init__(convert_charrefs=False);self.fragment=fragment;self.depth=0;self.children=[];self.child=None;self.openend=None;self.end=None
 def handle_starttag(self,tag,attrs):
  pos=self.getpos()[1]; end=pos+len(self.get_starttag_text())
  if self.depth==0:self.openend=end
  elif self.depth==1:self.child=pos
  self.depth+=1
 def handle_endtag(self,tag):
  pos=self.getpos()[1];end=self.fragment.find('>',pos)+1;self.depth-=1
  if self.depth==1:self.children.append((self.child,end));self.child=None
  if self.depth==0:self.end=pos
 def extract(self):
  self.feed(self.fragment);pos=self.openend;pieces=[]
  for start,end in self.children:
   if start>pos:pieces.append(self.fragment[pos:start])
   pos=end
  if self.end>pos:pieces.append(self.fragment[pos:self.end])
  return ' '.join(pieces)
for idx in (513,1426,1586,4298):
 for inv,h in ((A,old16),(B,new16)):
  x=inv['ocorrencias'][idx];fragment=h[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le')
  assert x['tipo']=='texto_direto' and '\n' not in fragment
  assert sha256(DirectText(fragment).extract().encode()).hexdigest()==x['sha256_fragmento']
assert len(changed)==mp['hash_diferente']==8 and len(inner)==mp['dentro_dos_blocos']==18
assert sum(x['id']!=y['id'] for x,y in zip(A['ocorrencias'],B['ocorrencias']))==mp['ids_deslocados']==7186
assert len(A['referencias'])==len(B['referencias'])==815
inside_refs=[]
for i,(x,y) in enumerate(zip(A['referencias'],B['referencias'])):
 for k in ('arquivo','secao','ancora','tag','atributo','valor','texto'):assert x[k]==y[k],(i,k)
 active=x['arquivo']=='modulos/e1-termodinamica.html'; affected=active and inside(x['inicio_utf16'])
 if affected:inside_refs.append(i)
 else:assert y['inicio_utf16']==x['inicio_utf16']+(offset(x['inicio_utf16']) if active else 0),(i,'referencia')
assert len(A['recursos'])==len(B['recursos'])==138
resource_changed=[]
for i,(x,y) in enumerate(zip(A['recursos'],B['recursos'])):
 for k in ('origem','referencia','arquivo','papel','estado'):assert x[k]==y[k],(i,k)
 if x['arquivo']=='modulos/e1-termodinamica.html':
  assert x['sha256']==H0 and y['sha256']==H1;resource_changed.append(i)
 else:assert x['sha256']==y['sha256'],(i,'recurso')
assert A['ativos_especificos']==B['ativos_especificos'] and len(A['ativos_especificos'])==6
for item in B['ativos_especificos']+B['recursos']:
 assert digest(item['arquivo'])==item['sha256'],item['arquivo']
assert A['artigos_excluidos']==B['artigos_excluidos'] and len(A['artigos_excluidos'])==197
art=lambda h: re.findall(r'<article\b[^>]*>.*?</article\s*>',h,re.S|re.I)
aa,bb=art(old),art(new);assert len(aa)==len(bb)==197 and aa==bb and not any(re.search(r'<article\b',v[1:],re.I) for v in aa)
assert [sha256(x.encode()).hexdigest() for x in aa]==[x['sha256_fragmento'] for x in A['artigos_excluidos']]
off0=json.loads(raw(P/'inventario-oficial-antes.json'));off1=json.loads(raw('auditoria/termodinamica/inventario/inventario-questoes.json'))
keys=[k for k in set(off0)|set(off1) if off0.get(k)!=off1.get(k)];assert keys==['fonte'];assert off0['fonte']['sha256']==H0 and off1['fonte']['sha256']==H1
ledger=json.loads(raw(D/'ledger-r7-parcial-r1/ledger.json'));mapped={r['id_r7']:r for r in mp['correspondencias']};unchanged=[]
for e in ledger['registros_explicitamente_revisados']:
 z=mapped[e['id_inventario']]; assert z['sha256_fragmento_r7']==e['sha256_fragmento'];unchanged.append({'id':e['id_historico'],'same_fragment':z['sha256_fragmento_r7']==z['sha256_fragmento_r8'],'id_r8':z['id_r8']})
assert len(unchanged)==12 and all(e['same_fragment'] for e in unchanged)
print(json.dumps({'reconstrucao_bytes':True,'ocorrencias':len(A['ocorrencias']),'pares_com_hash_alterado':changed,'posicoes_internas_a_edicoes':len(inner),'hashes_de_objetos_recalculados_no_html':fullhash,'textos_diretos_alterados_verificados':4,'referencias':len(A['referencias']),'referencias_que_comecam_dentro_das_edicoes':inside_refs,'recursos':len(A['recursos']),'recursos_que_apontam_para_html_modificado':resource_changed,'ativos_especificos':len(A['ativos_especificos']),'artigos_byte_a_byte':len(aa),'inventario_oficial_campos_alterados':keys,'ledger_r7_entradas_com_fragmento_inalterado':unchanged,'limites':'Pareamento estrutural, não prova científica de dependências nem aprovação automática. Os quatro textos diretos alterados tiveram hashes reextraídos por parser independente; outros textos diretos e atributos foram comparados pelos metadados dos inventários. Referências externas não foram abertas.'},ensure_ascii=False,indent=2))
