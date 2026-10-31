import pathlib,json,hashlib,collections
root=pathlib.Path('.');Q=root/'auditoria/termodinamica/evidencias/QA-09';P=Q/'aplicacao-pressao-fichas-r10-r1';a=json.loads((Q/'inventario-r9.json').read_text());b=json.loads((Q/'inventario-r10.json').read_text());m=json.loads((Q/'mapa-correspondencia-inventario-r9-r10-r1.json').read_text());ed=json.loads((P/'edicoes-aplicadas.json').read_text());digest=lambda v:hashlib.sha256(v).hexdigest()
assert digest((Q/'inventario-r9.json').read_bytes())==m['base_r9']=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
assert digest((Q/'inventario-r10.json').read_bytes())==m['base_r10']=='3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c'
assert digest((Q/'mapa-correspondencia-inventario-r9-r10-r1.json').read_bytes())=='d882301bb56ec469da5bb9b6f0b42f02e908c7dfcbdacaa048d6d0caff552a62'; assert ed==m['edicoes']
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']}; assert len(old)==len(new)==11397 and len(m['pares'])==11397
seenA=set();seenB=set();C=collections.Counter()
for row in m['pares']:
 x=old[row['id_r9']];y=new[row['id_r10']];assert row['id_r9'] not in seenA and row['id_r10'] not in seenB;seenA.add(row['id_r9']);seenB.add(row['id_r10']); assert row['sha256_r9']==x['sha256_fragmento'] and row['sha256_r10']==y['sha256_fragmento']
 assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);inside=[e for e in ed if e['documento']==x['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim']]
 if inside:
  assert len(inside)==1 and row['estado']=='PAREADO_INTERNO_CONFERIR' and row['edicao']==inside[0]['id']; e=inside[0];assert e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
 else:
  assert row['estado']=='PAREADO_EXTERNO'; shift=sum(e['delta'] for e in ed if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim']);assert y['inicio_utf16']==x['inicio_utf16']+shift
 C[(row['estado'],x['sha256_fragmento']==y['sha256_fragmento'])]+=1
assert len(seenA)==len(seenB)==11397
for e in ed:
 rows=[r for r in m['pares'] if r['estado']=='PAREADO_INTERNO_CONFERIR' and r['edicao']==e['id']]
 old_order=sorted(rows,key=lambda r: list(old).index(r['id_r9']));new_order=sorted(rows,key=lambda r: list(new).index(r['id_r10']));assert [r['id_r9'] for r in old_order]==[r['id_r9'] for r in new_order],e['id']
assert len(a['referencias'])==len(b['referencias'])==815 and len(a['recursos'])==len(b['recursos'])==138
changed=[]
for x,y in zip(a['referencias'],b['referencias']):
 assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo']);inside=[e for e in ed if e['documento']==x['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim']]
 if not inside:
  assert x['valor']==y['valor'] and x['texto']==y['texto'];shift=sum(e['delta'] for e in ed if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim']);assert x['inicio_utf16']+shift==y['inicio_utf16']
 elif x['valor']!=y['valor'] or x['texto']!=y['texto']:changed.append((x['valor'],y['valor']))
assert changed==[('../modulos/e1-termodinamica.html#substancias','../modulos/e1-termodinamica.html#base-entropia')]
assert 'id="base-entropia"' in (root/'modulos/e1-termodinamica.html').read_text()
resources_changed=[];source_hashes={x['arquivo']:(x['sha256'],y['sha256']) for x,y in zip(a['documentos'],b['documentos'])}
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','arquivo','papel','estado']);
 if x['referencia']!=y['referencia']:resources_changed.append((x['referencia'],y['referencia']))
 if x['arquivo'] in source_hashes:assert (x['sha256'],y['sha256'])==source_hashes[x['arquivo']]
 else:assert x['sha256']==y['sha256']
assert resources_changed==changed;assert a['ativos_especificos']==b['ativos_especificos'] and len(a['ativos_especificos'])==6;assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
print(json.dumps({'ok':True,'pares':len(m['pares']),'categorias':{str(k):v for k,v in C.items()},'referencias':815,'referencias_mudadas':changed,'recursos':138,'ativos':6,'artigos':197,'limite':'A associação interna é por ordem/contexto; igualdade de hash não herda automaticamente prova científica.'},ensure_ascii=False,indent=2))
