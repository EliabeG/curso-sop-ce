import pathlib,json,hashlib,collections
D=pathlib.Path('auditoria/termodinamica/evidencias/QA-09');P=D/'aplicacao-conjunta-r18-r1/resultado';a=json.loads((D/'inventario-r17.json').read_text());b=json.loads((D/'inventario-r18.json').read_text());m=json.loads((D/'mapa-correspondencia-inventario-r17-r18-r1.json').read_text());ed=json.loads((P/'edicoes-aplicadas.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'inventario-r17.json')==m['base_r17']=='b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b';assert sha(D/'inventario-r18.json')==m['base_r18']=='717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc';assert sha(D/'mapa-correspondencia-inventario-r17-r18-r1.json')=='54ef57e0479f4a8143fd5c7fde4021e45330d0125da939b02bc08fe3855ac1a7';assert ed==m['edicoes']
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};assert len(old)==len(new)==len(m['pares'])==11400;sa=set();sb=set();c=collections.Counter();changed=[]
for r in m['pares']:
 x=old[r['id_r17']];y=new[r['id_r18']];assert x['id'] not in sa and y['id'] not in sb;sa.add(x['id']);sb.add(y['id']);assert r['sha256_r17']==x['sha256_fragmento'] and r['sha256_r18']==y['sha256_fragmento'];assert all(x.get(k)==y.get(k) for k in ('arquivo','tipo','tag','secao','ancora'))
 inside=[e for e in ed if e['documento']==x['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim']]
 if inside:
  assert len(inside)==1 and r['estado']=='PAREADO_INTERNO_CONFERIR' and r['edicao']==inside[0]['id'];e=inside[0];assert e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
 else:
  shift=sum(e['delta'] for e in ed if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim']);assert y['inicio_utf16']==x['inicio_utf16']+shift
  if x['sha256_fragmento']!=y['sha256_fragmento']:
   assert r['estado']=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR' and any(e['documento']==x['arquivo'] and x['inicio_utf16']<=e['inicio'] and x['fim_utf16']>=e['fim'] for e in ed)
  else:assert r['estado']=='PAREADO_EXTERNO'
 same=x['sha256_fragmento']==y['sha256_fragmento'];c[(r['estado'],same)]+=1
 if not same:changed.append({'tipo':x['tipo'],'id':x['id'],'estado':r['estado']})
assert len(sa)==len(sb)==11400;assert sum(v for (k,_),v in c.items() if k=='PAREADO_INTERNO_CONFERIR')==427 and sum(v for (k,_),v in c.items() if k=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR')==4 and sum(v for (k,_),v in c.items() if k=='PAREADO_EXTERNO')==10969
for e in ed:
 rows=[r for r in m['pares'] if r['estado']=='PAREADO_INTERNO_CONFERIR' and r['edicao']==e['id']];assert [r['id_r17'] for r in sorted(rows,key=lambda r:old[r['id_r17']]['inicio_utf16'])]==[r['id_r17'] for r in sorted(rows,key=lambda r:new[r['id_r18']]['inicio_utf16'])]
fields=['arquivo','secao','ancora','tag','atributo','valor','texto'];assert len(a['referencias'])==len(b['referencias'])==816
for x,y in zip(a['referencias'],b['referencias']):
 assert all(x.get(k)==y.get(k) for k in fields)
 if not any(e['documento']==x['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim'] for e in ed):assert y['inicio_utf16']==x['inicio_utf16']+sum(e['delta'] for e in ed if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim'])
assert len(a['recursos'])==len(b['recursos'])==138;source={x['arquivo']:(x['sha256'],y['sha256']) for x,y in zip(a['documentos'],b['documentos'])}
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ('origem','referencia','arquivo','papel','estado'))
 assert (x['sha256'],y['sha256'])==source[x['arquivo']] if x['arquivo'] in source else x['sha256']==y['sha256']
assert a['ativos_especificos']==b['ativos_especificos'];assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
print(json.dumps({'ok':True,'pares':len(sa),'classificacao':{str(k):v for k,v in c.items()},'mudancas':changed,'referencias':816,'recursos':138,'limite':'Pares internos por sequência/contexto; não transfere mérito nem auditoria científica.'},ensure_ascii=False,indent=2))
