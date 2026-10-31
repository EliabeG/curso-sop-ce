from pathlib import Path
from hashlib import sha256
import json,collections
p=Path('auditoria/termodinamica/evidencias/QA-09');x=json.loads((p/'inventario-r10.json').read_text());y=json.loads((p/'inventario-r11.json').read_text());m=json.loads((p/'mapa-correspondencia-inventario-r10-r11-r1.json').read_text());e=json.loads((p/'aplicacao-fun01-p3-r11-r1/resultado/edicao.json').read_text());digest=lambda v:sha256(v).hexdigest()
assert digest((p/'inventario-r10.json').read_bytes())==m['base_r10']=='3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c';assert digest((p/'inventario-r11.json').read_bytes())==m['base_r11']=='720f2b9ace69ab8f07be685d5205040569cc72814f67d51d44786872469c07d7';assert digest((p/'mapa-correspondencia-inventario-r10-r11-r1.json').read_bytes())=='3c50f64d7f5a318edfc7544c2f2c628ca8789d45efdef8dcb08c88eac027cc3a';assert m['delta']==e
old={a['id']:a for a in x['ocorrencias']};new={a['id']:a for a in y['ocorrencias']};assert len(old)==len(new)==len(m['pares'])==11397
seen=set();seen2=set(); counter=collections.Counter();diffs=[]
def shift(a,key):return a[key]+(e['delta_utf16'] if a['arquivo']==e['documento'] and a[key]>=e['fim_utf16'] else 0)
for r in m['pares']:
 a=old[r['id_r10']];b=new[r['id_r11']];assert a['id'] not in seen and b['id'] not in seen2;seen.add(a['id']);seen2.add(b['id']);assert all(a.get(k)==b.get(k) for k in ('arquivo','secao','ancora','tag','tipo'));assert all(shift(a,k)==b[k] for k in ('inicio_utf16','fim_utf16'));assert r['sha256_r10']==a['sha256_fragmento'] and r['sha256_r11']==b['sha256_fragmento'];same=a['sha256_fragmento']==b['sha256_fragmento'];counter[(r['estado'],same)]+=1
 if not same:diffs.append((a['tipo'],a['tag'],a['secao'],a['inicio_utf16'],a['fim_utf16']))
assert len(seen)==len(seen2)==11397;assert counter=={('PAREADO_EXTERNO',True):11396,('PAREADO_ANCESTRAL_CONFERIR',False):1}; assert diffs==[('secao','section','fun01-estado-equilibrio',88914,157067)]
assert len(x['referencias'])==len(y['referencias'])==815
for a,b in zip(x['referencias'],y['referencias']):
 assert all(a.get(k)==b.get(k) for k in ('arquivo','secao','ancora','tag','atributo','valor','texto'));assert all(shift(a,k)==b[k] for k in ('inicio_utf16','fim_utf16'))
assert len(x['recursos'])==len(y['recursos'])==138
updated=0
for a,b in zip(x['recursos'],y['recursos']):
 assert all(a.get(k)==b.get(k) for k in ('origem','referencia','arquivo','papel','estado'))
 if a['arquivo']==e['documento']:assert (a['sha256'],b['sha256'])==(e['html_antes_sha256'],e['html_depois_sha256']);updated+=1
 else:assert a['sha256']==b['sha256']
assert x['ativos_especificos']==y['ativos_especificos'] and len(x['ativos_especificos'])==6
oldarts=x['artigos_excluidos'];newarts=y['artigos_excluidos'];assert len(oldarts)==len(newarts)==197;diff=[(a,b) for a,b in zip(oldarts,newarts) if a!=b];assert len(diff)==1 and diff[0][0]['id']==diff[0][1]['id']==e['artigo_id'] and diff[0][0]['sha256_fragmento']==e['artigo_antes_sha256'] and diff[0][1]['sha256_fragmento']==e['artigo_depois_sha256']
print(json.dumps({'ok':True,'pares':len(m['pares']),'categoria':{str(k):v for k,v in counter.items()},'ancestral_diferente':diffs,'referencias':815,'recursos':138,'hashes_html_atualizados':updated,'ativos':6,'artigos_excluidos':197,'artigos_alterados':e['artigo_id'],'limite':'Apoio estrutural pelo autor da candidata; auditor distinto decide ciência e aceites.'},ensure_ascii=False,indent=2))
