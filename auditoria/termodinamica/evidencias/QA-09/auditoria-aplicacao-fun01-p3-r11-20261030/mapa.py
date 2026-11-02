#!/usr/bin/env python3
"""Confronto independente do mapa r10→r11, somente leitura."""
from hashlib import sha256
import json
from pathlib import Path
from collections import Counter

def read(path, expected):
    raw=Path(path).read_bytes()
    if sha256(raw).hexdigest()!=expected: raise ValueError(f'hash divergente: {path}')
    return json.loads(raw)
base='auditoria/termodinamica/evidencias/QA-09/'
old=read(base+'inventario-r10.json','3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c')
new=read(base+'inventario-r11.json','720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7')
mapping=read(base+'mapa-correspondencia-inventario-r10-r11-r1.json','3c50f64d7f5a318edfc7544c2f2c628ca8789d45efdef8dcb08c88eac027cc3a')
a={o['id']:o for o in old['ocorrencias']};b={o['id']:o for o in new['ocorrencias']}
assert len(a)==len(b)==len(mapping['pares'])==11397
assert len({p['id_r10'] for p in mapping['pares']})==len({p['id_r11'] for p in mapping['pares']})==11397
states=Counter();changed=[]
for p in mapping['pares']:
    x,y=a[p['id_r10']],b[p['id_r11']];states[p['estado']]+=1
    assert all(x.get(k)==y.get(k) for k in ('arquivo','secao','ancora','tag','tipo'))
    assert x['sha256_fragmento']==p['sha256_r10'] and y['sha256_fragmento']==p['sha256_r11']
    for k in ('inicio_utf16','fim_utf16'):
        shift=71 if x['arquivo']=='modulos/e1-termodinamica.html' and x[k]>=130109 else 0
        assert y[k]==x[k]+shift
    if x['sha256_fragmento']!=y['sha256_fragmento']:changed.append((p['estado'],x['id']))
assert states=={'PAREADO_EXTERNO':11396,'PAREADO_ANCESTRAL_CONFERIR':1}
assert len(changed)==1 and changed[0][0]=='PAREADO_ANCESTRAL_CONFERIR'
assert len(old['referencias'])==len(new['referencias'])==815
for x,y in zip(old['referencias'],new['referencias']):
    for k in ('arquivo','secao','ancora','tag','atributo','valor','texto'):assert x.get(k)==y.get(k)
    for k in ('inicio_utf16','fim_utf16'):
        shift=71 if x['arquivo']=='modulos/e1-termodinamica.html' and x[k]>=130109 else 0
        assert y[k]==x[k]+shift
assert len(old['recursos'])==len(new['recursos'])==138
changed_resource_hashes=0
for x,y in zip(old['recursos'],new['recursos']):
    for k in ('origem','referencia','arquivo','papel','estado'):assert x[k]==y[k]
    assert sha256(Path(y['arquivo']).read_bytes()).hexdigest()==y['sha256']
    if x['sha256']!=y['sha256']:
        changed_resource_hashes+=1;assert x['arquivo']=='modulos/e1-termodinamica.html'
assert changed_resource_hashes==105
assert old['ativos_especificos']==new['ativos_especificos']
items0={x['id']:x['sha256_fragmento'] for x in old['artigos_excluidos']};items1={x['id']:x['sha256_fragmento'] for x in new['artigos_excluidos']}
assert len(items0)==len(items1)==197 and [k for k in items0 if items0[k]!=items1[k]]==['fun01-e1-supercritico']
print(json.dumps({'ok':True,'pares':len(mapping['pares']),'classificacao':states,'alteracoes_de_hash':changed,
 'referencias':815,'recursos':138,'recursos_hash_aula_atualizado':changed_resource_hashes,'ativos':len(new['ativos_especificos']),
 'limite':'Correspondência estrutural não transfere cobertura ou mérito científico.'},ensure_ascii=False,indent=2))
