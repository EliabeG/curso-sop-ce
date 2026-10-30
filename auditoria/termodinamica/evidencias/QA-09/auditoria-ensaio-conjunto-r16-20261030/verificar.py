#!/usr/bin/env python3
"""Copia isolada em /tmp, testes de guardas e conferência independente do mapa."""
import collections, hashlib, json, pathlib, re, shutil, subprocess, tempfile
root=pathlib.Path(__file__).resolve().parents[5]
rel='auditoria/termodinamica/evidencias/QA-09/'
P=rel+'aplicacao-conjunta-r16-r1/'
sha=lambda b: hashlib.sha256(b).hexdigest()
assert sha((root/(P+'ensaio.mjs')).read_bytes())=='2e91bce9d697189a629797e3371d1afef2a46dc03313c06a71404ba9e67b81ba'
expected_map=(root/(P+'mapa-ensaio.json')).read_bytes()
assert sha(expected_map)=='a3edb9fab577c58e5b3df4831ee8cfb09d8e8b39bf92d1efcd5e0a5f39b2d4d0'
def run(cwd): return subprocess.run(['node',P+'ensaio.mjs'],cwd=cwd,text=True,capture_output=True)
assert not str(root).startswith('/tmp/')
r=run(root);assert r.returncode and 'Somente cópia /tmp' in r.stderr
with tempfile.TemporaryDirectory(prefix='qa-r16-independente-',dir='/tmp') as tmp:
 c=pathlib.Path(tmp)/'repo'
 shutil.copytree(root,c,ignore=shutil.ignore_patterns('.git'))
 out=c/(rel+'inventario-r16.json');assert not out.exists();out.write_text('destino-protegido')
 r=run(c);assert r.returncode and 'Destino existe' in r.stderr and out.read_text()=='destino-protegido';out.unlink()
 f=c/'formulas/termodinamica.html';orig=f.read_bytes();f.write_bytes(orig+b'\n')
 r=run(c);assert r.returncode and 'SHA divergente' in r.stderr;f.write_bytes(orig)
 r=run(c); assert r.returncode==0,(r.stderr,r.stdout)
 result=json.loads(r.stdout); generated=(c/(rel+'mapa-correspondencia-inventario-r15-r16-r1.json')).read_bytes()
 assert generated==expected_map and result==json.loads((root/(P+'resultado-ensaio.json')).read_bytes())
 map=json.loads(generated); a=json.loads((c/(rel+'inventario-r15.json')).read_bytes());b=json.loads(out.read_bytes())
 assert len(map['pares'])==11400 and len(a['ocorrencias'])==11399 and len(b['ocorrencias'])==11400
 old={x['id']:x for x in a['ocorrencias']}; new={x['id']:x for x in b['ocorrencias']}
 assert len(old)==11399 and len(new)==11400
 refs15=[];refs16=[];tot=collections.Counter();by_edit=collections.Counter();changed=collections.Counter();added=[];differences=[]
 for p in map['pares']:
  state=p['estado'];tot[state]+=1
  x=old[p['id_r15']] if p.get('id_r15') else None
  y=new[p['id_r16']] if p.get('id_r16') else None
  if x: refs15.append(x['id']);assert p['sha256_r15']==x['sha256_fragmento']
  if y: refs16.append(y['id']);assert p['sha256_r16']==y['sha256_fragmento']
  if state=='PAREADO_EXTERNO': assert x and y and x['sha256_fragmento']==y['sha256_fragmento']
  if state=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':
   assert x and y and x['sha256_fragmento']!=y['sha256_fragmento']
   assert any(e['documento']==x['arquivo'] and x['inicio_utf16']<=e['inicio'] and x['fim_utf16']>=e['fim'] for e in map['edicoes'])
  if state=='PAREADO_INTERNO_CONFERIR':
   assert x and y and all(x.get(k)==y.get(k) for k in ['arquivo','tipo','tag','secao','ancora'])
   e=next(e for e in map['edicoes'] if e['id']==p['edicao'])
   assert x['arquivo']==e['documento']==y['arquivo'] and e['inicio']<=x['inicio_utf16']<e['fim'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
   by_edit[e['id']]+=1
   if x['sha256_fragmento']!=y['sha256_fragmento']:
    changed[e['id']]+=1
    differences.append({'edicao':e['id'],'tipo':x['tipo'],'tag':x['tag'],'id_r15':x['id'],'id_r16':y['id'],'texto_r15':x.get('texto'),'texto_r16':y.get('texto')})
  if state=='ADICIONADO_OU_REESTRUTURADO':
   assert not x and y
   e=next(e for e in map['edicoes'] if e['id']==p['edicao'])
   assert y['arquivo']==e['documento'] and e['inicio_novo']<=y['inicio_utf16']<e['fim_novo']
   added.append({'edicao':p['edicao'],'id':y['id'],'texto':y.get('texto')})
 assert len(refs15)==len(set(refs15))==len(old) and len(refs16)==len(set(refs16))==len(new)
 assert tot=={'PAREADO_EXTERNO':11021,'PAREADO_INTERNO_CONFERIR':375,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':3,'ADICIONADO_OU_REESTRUTURADO':1}
 assert len(a['referencias'])==len(b['referencias'])==816
 for x,y in zip(a['referencias'],b['referencias']):
  assert all(x.get(k)==y.get(k) for k in ['arquivo','secao','ancora','tag','atributo','valor','texto'])
 assert len(a['recursos'])==len(b['recursos'])==138
 for x,y in zip(a['recursos'],b['recursos']):
  assert all(x.get(k)==y.get(k) for k in ['origem','referencia','arquivo','papel','estado'])
  if x['arquivo'] not in ('modulos/e1-termodinamica.html','formulas/termodinamica.html'): assert x['sha256']==y['sha256']
 assert a['artigos_excluidos']==b['artigos_excluidos'] and len(a['artigos_excluidos'])==197
 before=(c/(P+'resultado/antes-aula.html')).read_text();after=(c/'modulos/e1-termodinamica.html').read_text()
 def artigos(h):
  found={}
  for m in re.finditer(r'<article\b[^>]*>.*?</article>',h,re.S):
   id_match=re.search(r'\bid="([^"]+)"',m.group().split('>',1)[0])
   if id_match:
    assert id_match.group(1) not in found
    found[id_match.group(1)]=m.group()
  return found
 ba,aa=artigos(before),artigos(after)
 for x in a['artigos_excluidos']:
  assert x['id'] in ba and x['id'] in aa and ba[x['id']]==aa[x['id']] and sha(ba[x['id']].encode())==x['sha256_fragmento']
 assert all(map[k]==[] for k in ['referencias_mudadas','referencias_novas','recursos_mudados'])
 print(json.dumps({'ok':True,'guardas':['cwd','destino','sha_formulario'],'mapa_idêntico':True,'classificacao':tot,'internos_por_edicao':by_edit,'hashes_internos_diferentes':changed,'diferencas':differences,'novo':added,'limite':'pareamento por contexto/ordem não valida significado nem navegador'},ensure_ascii=False,indent=2))
