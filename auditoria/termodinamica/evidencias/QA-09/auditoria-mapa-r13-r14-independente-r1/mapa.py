import pathlib,json,hashlib,collections
root=pathlib.Path('.');Q=root/'auditoria/termodinamica/evidencias/QA-09';P=Q/'aplicacao-conjunta-r14-seis-r1/resultado';a=json.loads((Q/'inventario-r13.json').read_text());b=json.loads((Q/'inventario-r14.json').read_text());m=json.loads((Q/'mapa-correspondencia-inventario-r13-r14-r1.json').read_text());ed=json.loads((P/'edicoes-aplicadas.json').read_text());digest=lambda v:hashlib.sha256(v).hexdigest()
assert digest((Q/'inventario-r13.json').read_bytes())==m['base_r13']=='0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b';assert digest((Q/'inventario-r14.json').read_bytes())==m['base_r14']=='6505b06f3f3ef15bc2904f8a604f6e1f0fa6cf22af822394b2c2a871437b6175';assert digest((Q/'mapa-correspondencia-inventario-r13-r14-r1.json').read_bytes())=='a43156dad32d5529850bdd4c40209c68a772fee45cfd8651e3f9b0becaa1ff07';assert ed==m['edicoes']
old={x['id']:x for x in a['ocorrencias']};new={x['id']:x for x in b['ocorrencias']};assert len(old)==11397 and len(new)==11399 and len(m['pares'])==11399
seenA=set();seenB=set();C=collections.Counter();added=[];changed=[]
for row in m['pares']:
 if row['id_r13'] is None:
  y=new[row['id_r14']]; assert row['estado']=='ADICIONADO_OU_REESTRUTURADO' and row['id_r14'] not in seenB and row['sha256_r14']==y['sha256_fragmento'];seenB.add(row['id_r14']);added.append((row['edicao'],y['id']));C[(row['estado'],False)]+=1;continue
 x=old[row['id_r13']];y=new[row['id_r14']];assert row['id_r13'] not in seenA and row['id_r14'] not in seenB;seenA.add(row['id_r13']);seenB.add(row['id_r14']);assert row['sha256_r13']==x['sha256_fragmento'] and row['sha256_r14']==y['sha256_fragmento'];assert all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora']);inside=[e for e in ed if e['documento']==x['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim']]
 if inside:
  assert len(inside)==1 and row['estado']=='PAREADO_INTERNO_CONFERIR' and row['edicao']==inside[0]['id'];e=inside[0];assert e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
 else:
  shift=sum(e['delta'] for e in ed if e['documento']==x['arquivo'] and x['inicio_utf16']>=e['fim']);assert y['inicio_utf16']==x['inicio_utf16']+shift
  ancestor=x['tipo'] not in ('atributos_significativos','texto_direto') and any(e['documento']==x['arquivo'] and x['inicio_utf16']<=e['inicio'] and e['fim']<=x['fim_utf16'] for e in ed)
  assert row['estado']==('PAREADO_CONTEXTO_ANCESTRAL_CONFERIR' if ancestor else 'PAREADO_EXTERNO')
 same=x['sha256_fragmento']==y['sha256_fragmento'];C[(row['estado'],same)]+=1
 if not same:changed.append((row['estado'],x['tipo'],x['secao'],x['ancora']))
for e in ed:
 rows=[r for r in m['pares'] if r['estado']=='PAREADO_INTERNO_CONFERIR' and r['edicao']==e['id']]; old_order=sorted(rows,key=lambda r:list(old).index(r['id_r13']));new_order=sorted(rows,key=lambda r:list(new).index(r['id_r14']));assert [r['id_r13'] for r in old_order]==[r['id_r13'] for r in new_order]
assert len(seenA)==11397 and len(seenB)==11399; assert C=={('PAREADO_EXTERNO',True):11178,('PAREADO_CONTEXTO_ANCESTRAL_CONFERIR',False):5,('PAREADO_INTERNO_CONFERIR',True):198,('PAREADO_INTERNO_CONFERIR',False):16,('ADICIONADO_OU_REESTRUTURADO',False):2}
assert len(a['referencias'])==815 and len(b['referencias'])==816 and len(a['recursos'])==len(b['recursos'])==138
fields=['arquivo','secao','ancora','tag','atributo','valor','texto'];i=0;refs_new=[]
for x in b['referencias']:
 if i<len(a['referencias']) and all(a['referencias'][i].get(k)==x.get(k) for k in fields):i+=1
 else:refs_new.append(x)
assert i==815 and len(refs_new)==1 and refs_new[0]['valor']=='https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node33.html';assert refs_new==m['referencias_novas'] and not m['referencias_mudadas']
source_hashes={x['arquivo']:(x['sha256'],y['sha256']) for x,y in zip(a['documentos'],b['documentos'])};updated=collections.Counter()
for x,y in zip(a['recursos'],b['recursos']):
 assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
 if x['arquivo'] in source_hashes:
  assert (x['sha256'],y['sha256'])==source_hashes[x['arquivo']];updated[x['arquivo']]+=x['sha256']!=y['sha256']
 else:assert x['sha256']==y['sha256']
assert a['ativos_especificos']==b['ativos_especificos'] and len(a['ativos_especificos'])==6;assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
print(json.dumps({'ok':True,'r13':len(old),'r14':len(new),'categorias':{str(k):v for k,v in C.items()},'adicionados':added,'referencias_anteriores':i,'novas':refs_new,'recursos':138,'hashes_atualizados':dict(updated),'ativos':6,'artigos_excluidos':197,'limite':'Associações internas por ordem/contexto; não transfere automaticamente revisão científica.'},ensure_ascii=False,indent=2))
