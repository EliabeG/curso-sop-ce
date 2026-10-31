#!/usr/bin/env python3
"""Medição de inventário r30, ledger e duplicações grandes; somente leitura."""
from pathlib import Path
from hashlib import sha256
from collections import Counter,defaultdict
import json,urllib.parse
Q=Path('auditoria/termodinamica/evidencias/QA-09');digest=lambda b:sha256(b).hexdigest()
p=Q/'inventario-r30.json';b=p.read_bytes();assert digest(b)=='1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4';j=json.loads(b)
l=Q/'ledger-r30-direto-r2/ledger.json';raw=l.read_bytes();assert digest(raw)=='58d31ac8b26366c543cc439b3b4dc0c7c9428d191949c8ac49d801b4a459dc12';ledger=json.loads(raw);assert len(ledger['objetos'])==78
c=Counter(x['tipo'] for x in j['ocorrencias']);st=Counter(x.get('estado') for x in j['ocorrencias']);ref=Counter();urls=set()
for x in j['referencias']:
 v=x.get('valor','');s=urllib.parse.urlparse(v).scheme
 if s in ('http','https'):ref['externa_http']+=1;urls.add(v)
 elif v.startswith('#'):ref['fragmento_local']+=1
 else:ref['caminho_local_ou_outro']+=1
files=[x for x in Q.rglob('*') if x.is_file() and not x.is_relative_to(Q/'planejamento-escala-r30')];group=defaultdict(list)
for x in files:
 size=x.stat().st_size
 if size>=10000:group[(size,digest(x.read_bytes()))].append(x)
dups=[(k,v) for k,v in group.items() if len(v)>1]
out={'inventario_sha256':digest(b),'ocorrencias':len(j['ocorrencias']),'tipos':dict(c),'estados_inventario':dict(st),'referencias':len(j['referencias']),'referencias_por_forma':dict(ref),'urls_http_distintas_exatas':len(urls),'relacoes_recursos':len(j['recursos']),'ativos_especificos':len(j['ativos_especificos']),'ledger_r30_sha256':digest(raw),'objetos_ledger':len(ledger['objetos']),'diagnosticos_ledger':sum(x['id'].startswith('D') and x['id'][1:].isdigit() for x in ledger['objetos']),'exemplos_ledger':sum(x['id'].startswith('EX-') for x in ledger['objetos']),'fichas_ledger':sum(x['tipo']=='ficha' for x in ledger['objetos']),'pasta_QA09':{'arquivos':len(files),'bytes_aparentes':sum(x.stat().st_size for x in files),'limiar_duplicacao_bytes':10000,'grupos_sha_tamanho_duplicados':len(dups),'bytes_aparentes_duplicados_acima_limiar':sum((len(v)-1)*k[0] for k,v in dups)},'limitacao':'Contagens sobrepostas e fotografia de arquivo no instante; não são porcentagem de cobertura, nem economia automática em Git.'}
print(json.dumps(out,ensure_ascii=False,indent=2))
