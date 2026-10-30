#!/usr/bin/env python3
"""Mapa r10→r11 para delta único dentro de artigo excluído. Grava SOMENTE novo mapa."""
import json,pathlib,hashlib
P=pathlib.Path('auditoria/termodinamica/evidencias/QA-09'); E=P/'aplicacao-fun01-p3-r11-r1/resultado'; dest=P/'mapa-correspondencia-inventario-r10-r11-r1.json'
if dest.exists():raise SystemExit('Destino de mapa já existe')
a=json.loads((P/'inventario-r10.json').read_text());b=json.loads((P/'inventario-r11.json').read_text());change=json.loads((E/'edicao.json').read_text());start,end,delta=change['inicio_utf16'],change['fim_utf16'],change['delta_utf16'];doc=change['documento']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def pos(n,field):
 v=n[field];return v+delta if n['arquivo']==doc and v>=end else v
key=lambda x:(x['arquivo'],x['inicio_utf16'],x['tipo'],x['tag'],x.get('secao'),x.get('ancora'))
nexts={key(y):y for y in b['ocorrencias']};assert len(nexts)==len(b['ocorrencias']);out=[]
for x in a['ocorrencias']:
 assert not (x['arquivo']==doc and start<=x['inicio_utf16']<end),('nó não segregado começa dentro do delta',x['id'])
 k=(x['arquivo'],pos(x,'inicio_utf16'),x['tipo'],x['tag'],x.get('secao'),x.get('ancora'));y=nexts.pop(k,None);assert y is not None,('sem par',x['id']);assert y['fim_utf16']==pos(x,'fim_utf16'),('fim divergente',x['id'])
 ancestor=x['arquivo']==doc and x['inicio_utf16']<=start and x['fim_utf16']>=end
 if x['sha256_fragmento']!=y['sha256_fragmento']:assert ancestor,('hash externo mudou',x['id'])
 out.append({'estado':'PAREADO_ANCESTRAL_CONFERIR' if ancestor and x['sha256_fragmento']!=y['sha256_fragmento'] else 'PAREADO_EXTERNO','id_r10':x['id'],'id_r11':y['id'],'sha256_r10':x['sha256_fragmento'],'sha256_r11':y['sha256_fragmento']})
assert not nexts and len(out)==len(a['ocorrencias'])==len(b['ocorrencias'])
assert len(a['referencias'])==len(b['referencias'])
for x,y in zip(a['referencias'],b['referencias']):
 assert not(x['arquivo']==doc and start<=x['inicio_utf16']<end)
 for f in ['arquivo','secao','ancora','tag','atributo','valor','texto']:assert x.get(f)==y.get(f),(f,x,y)
 assert y['inicio_utf16']==pos(x,'inicio_utf16') and y['fim_utf16']==pos(x,'fim_utf16')
assert len(a['recursos'])==len(b['recursos'])
for x,y in zip(a['recursos'],b['recursos']):
 for f in ['origem','referencia','arquivo','papel','estado']:assert x.get(f)==y.get(f),(f,x,y)
 if x['arquivo']==doc:assert x['sha256']==sha(E/'antes-aula.html') and y['sha256']==sha(pathlib.Path(doc))
 else:assert x['sha256']==y['sha256']
old=a['artigos_excluidos'];new=b['artigos_excluidos'];assert len(old)==len(new)==197;diff=[(x,y) for x,y in zip(old,new) if x!=y];assert len(diff)==1 and diff[0][0]['id']==diff[0][1]['id']=='fun01-e1-supercritico';assert diff[0][0]['sha256_fragmento']==change['artigo_antes_sha256'] and diff[0][1]['sha256_fragmento']==change['artigo_depois_sha256']
assert a['ativos_especificos']==b['ativos_especificos']
from collections import Counter
v={'estado':'MAPEAMENTO_ESTRUTURAL_SEM_TRANSFERENCIA_DE_ACEITE','base_r10':sha(P/'inventario-r10.json'),'base_r11':sha(P/'inventario-r11.json'),'delta':change,'pares':out,'referencias':len(a['referencias']),'recursos':len(a['recursos']),'artigos':[{'id':diff[0][0]['id'],'sha256_r10':diff[0][0]['sha256_fragmento'],'sha256_r11':diff[0][1]['sha256_fragmento']}],'limite':'Nós ancestrais alterados exigem exame do contexto e das dependências; igualdade de hash não transfere qualquer aceite entre versões.'};dest.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'ok':True,'pares':len(out),'classificacao':dict(Counter(x['estado'] for x in out)),'referencias':len(a['referencias']),'recursos':len(a['recursos']),'artigos_alterados':len(diff)},ensure_ascii=False))
