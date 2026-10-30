#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
import json
Q=Path('auditoria/termodinamica/evidencias/QA-09'); D=Q/'referencias-ashrae-banca-r18-20261030'
def check(p,h):
 b=Path(p).read_bytes();assert sha256(b).hexdigest()==h,p;return b
html=check('modulos/e1-termodinamica.html','7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca').decode().encode('utf-16-le');inv=json.loads(check(Q/'inventario-r18.json','717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc'));s=json.loads(check(D/'identidades.json','25a14c596bfed1c69f17c816417e549f504b917601c63b170a883474e7b6838e'))
assert [x['indice'] for x in s['identidades']]==[117,639,640,641,642,643,644]
for record in s['identidades']:
 i=record['indice'];r=inv['referencias'][i];expect={k:v for k,v in record.items() if k not in ('indice','sha256_elemento')};assert r==expect
 text=html[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le');assert sha256(text.encode()).hexdigest()==record['sha256_elemento'];assert r['valor'] in text and r['tag']=='a' and text.count('<a ')==1 and r['texto'] in text
assert s['base_sha256']=='7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca' and s['inventario_sha256']=='717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc'
print(json.dumps({'ok':True,'ocorrencias':[x['indice'] for x in s['identidades']],'limite':'Inspeção local; não atesta conteúdo remoto, correção de itens ou status em versão posterior.'},ensure_ascii=False))
