#!/usr/bin/env python3
"""Configura quatro candidatas; aceita lista adicional aprovada em JSON, sem editar produto."""
from pathlib import Path
import json,hashlib,sys
if len(sys.argv) not in (2,3):raise SystemExit('Uso: preparar-config.py destino-novo.json [extras.json]')
d=Path('auditoria/termodinamica/evidencias/QA-09'); target=Path(sys.argv[1]);
if target.exists():raise SystemExit('Destino existe')
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert H(Path('modulos/e1-termodinamica.html'))=='2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2'
assert H(Path('formulas/termodinamica.html'))=='cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'
assert H(d/'inventario-r9.json')=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
T=d/'teoria-pressao-entalpia-r9-20261030';F=d/'candidatas-fichas-40-67-r9-20261030';mt=json.loads((T/'manifesto.json').read_text());mf=json.loads((F/'manifesto.json').read_text());ed=[]
def add(id,doc,a,b,ha,hb):
 old=a.read_text().removesuffix('\n');new=b.read_text().removesuffix('\n');h=lambda x:hashlib.sha256(x.encode()).hexdigest();assert h(old)==ha and h(new)==hb and old!=new
 source=Path(doc).read_text();assert source.count(old)==1 and new not in source,id
 ed.append({'id':id,'documento':doc,'original':str(a),'candidata':str(b),'original_sha256':ha,'candidata_sha256':hb})
for x in mt['edicoes']:add(x['id'],x['arquivo'],T/(x['id']+'-original.html'),T/(x['id']+'-candidata.html'),x['original_sha256'],x['candidata_sha256'])
for x in mf['itens']:add('ficha-'+str(x['ficha']),'formulas/termodinamica.html',F/(str(x['ficha'])+'-original.html'),F/(str(x['ficha'])+'-candidata.html'),x['original_sha256'],x['candidata_sha256'])
if len(sys.argv)==3:
 for x in json.loads(Path(sys.argv[2]).read_text()):add(x['id'],x['documento'],Path(x['original']),Path(x['candidata']),x['original_sha256'],x['candidata_sha256'])
assert len({x['id'] for x in ed})==len(ed)
target.write_text(json.dumps({'estado':'CONFIGURACAO_SEM_APLICACAO','edicoes':ed},ensure_ascii=False,indent=2)+'\n');print(target)
