import pathlib,json,hashlib,collections
root=pathlib.Path('.');Q=root/'auditoria/termodinamica/evidencias/QA-09';P=Q/'aplicacao-fichas-calorimetria-co2-r12-r1/resultado';a=json.loads((Q/'inventario-r11.json').read_text());b=json.loads((Q/'inventario-r12.json').read_text());m=json.loads((Q/'mapa-correspondencia-inventario-r11-r12-r1.json').read_text());ed=json.loads((P/'edicoes-aplicadas.json').read_text());digest=lambda v:hashlib.sha256(v).hexdigest()
assert digest((Q/'inventario-r11.json').read_bytes())==m['base_r11']=='720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7';assert digest((Q/'inventario-r12.json').read_bytes())==m['base_r12']=='457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e';assert digest((Q/'mapa-correspondencia-inventario-r11-r12-r1.json').read_bytes())=='1c67bdda8f5996c6a230e4556277dbbfac270e64ec5b2ac0cabccdee4b3680ef';assert ed==m['edicoes']
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};assert len(old)==len(new)==len(m['pares'])==11397
seenA=set();seenB=set();C=collections.Counter();changed=[]
for row in m['pares']:
 x=old[row['id_r11']];y=new[row['id_r12']];assert row['id_r11'] not in seenA and row['id_r12'] not in seenB;seenA.add(row['id_r11']);seenB.add(row['id_r12']); assert row['sha256_r11']==x['sha256_fragmento'] and row['sha256_r12']==y['sha256_fragmento'];assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);inside=[e for e in ed if e['documento']==x['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim']]
 if inside:
  assert len(inside)==1 and row['estado']=='PAREADO_INTERNO_CONFERIR' and row['edicao']==inside[0]['id'];e=inside[0];assert e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
 else:
  assert row['estado']=='PAREADO_EXTERNO';shift=sum(e['delta'] for e in ed if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim']);assert y['inicio_utf16']==x['inicio_utf16']+shift
 C[(row['estado'],x['sha256_fragmento']==y['sha256_fragmento'])]+=1
 if x['sha256_fragmento']!=y['sha256_fragmento']:changed.append((row['estado'],x['tipo'],x['secao'],x['ancora'],x['inicio_utf16']))
for e in ed:
 rows=[r for r in m['pares'] if r['estado']=='PAREADO_INTERNO_CONFERIR' and r['edicao']==e['id']]; old_order=sorted(rows,key=lambda r: list(old).index(r['id_r11']));new_order=sorted(rows,key=lambda r: list(new).index(r['id_r12']));assert [r['id_r11'] for r in old_order]==[r['id_r11'] for r in new_order]
assert len(seenA)==len(seenB)==11397; assert C=={('PAREADO_EXTERNO',True):11236,('PAREADO_EXTERNO',False):2,('PAREADO_INTERNO_CONFERIR',True):144,('PAREADO_INTERNO_CONFERIR',False):15}
assert len(a['referencias'])==len(b['referencias'])==815 and len(a['recursos'])==len(b['recursos'])==138
doc_pairs={
 'modulos/e1-termodinamica.html':((P/'antes-aula.html').read_text().encode('utf-16-le'),(root/'modulos/e1-termodinamica.html').read_text().encode('utf-16-le')),
 'formulas/termodinamica.html':((P/'antes-formulario.html').read_text().encode('utf-16-le'),(root/'formulas/termodinamica.html').read_text().encode('utf-16-le'))}
for x,y in zip(a['referencias'],b['referencias']):
 original,current=doc_pairs[x['arquivo']];assert original[x['inicio_utf16']*2:x['fim_utf16']*2]==current[y['inicio_utf16']*2:y['fim_utf16']*2]
 assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto']);inside=[e for e in ed if e['documento']==x['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim']]
 if not inside:
  shift=sum(e['delta'] for e in ed if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim']);assert x['inicio_utf16']+shift==y['inicio_utf16']
source_hashes={x['arquivo']:(x['sha256'],y['sha256']) for x,y in zip(a['documentos'],b['documentos'])};updated=0
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in source_hashes:
  assert (x['sha256'],y['sha256'])==source_hashes[x['arquivo']];updated+=x['sha256']!=y['sha256']
 else:assert x['sha256']==y['sha256']
assert a['ativos_especificos']==b['ativos_especificos'] and len(a['ativos_especificos'])==6;assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
print(json.dumps({'ok':True,'pares':len(m['pares']),'categorias':{str(k):v for k,v in C.items()},'alterados':changed,'referencias':815,'recursos':138,'recursos_hash_atualizado':updated,'ativos':6,'artigos_excluidos':197,'limite':'Pares internos por ordem e contexto; correspondência não transfere automaticamente revisão científica.'},ensure_ascii=False,indent=2))
