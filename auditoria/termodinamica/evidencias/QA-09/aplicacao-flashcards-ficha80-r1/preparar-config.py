#!/usr/bin/env python3
"""Gera configuração de candidatas em destino novo; não altera produto."""
import sys,json,pathlib,hashlib
if len(sys.argv)!=2:raise SystemExit('Uso: preparar-config.py destino-novo.json')
d=pathlib.Path('auditoria/termodinamica/evidencias/QA-09'); target=pathlib.Path(sys.argv[1]);
if target.exists():raise SystemExit('Destino já existe')
F=d/'candidatas-flashcards-resumo-20261030-r2';B=d/'ficha-080-candidata-20261030';mf=json.loads((F/'manifesto.json').read_text());mb=json.loads((B/'manifesto.json').read_text());h=lambda b:hashlib.sha256(b).hexdigest()
expected={'modulos/e1-termodinamica.html':'57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c','formulas/termodinamica.html':'c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0'}
assert h((d/'inventario-r8.json').read_bytes())=='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687'
for doc,sha in expected.items():assert h(pathlib.Path(doc).read_bytes())==sha
ed=[]
for c in mf['candidatas']:
 p,q=F/c['original'],F/c['candidata']; a=p.read_text().removesuffix('\n');b=q.read_text().removesuffix('\n');assert h(a.encode())==c['sha256_original_sem_quebra_final'] and h(b.encode())==c['sha256_candidata_sem_quebra_final']
 ed.append({'id':c['nome'],'documento':mf['documento'],'original':str(p),'candidata':str(q),'original_sha256':h(a.encode()),'candidata_sha256':h(b.encode())})
p,q=B/'original.html',B/'candidata.html';a=p.read_text().removesuffix('\n');b=q.read_text().removesuffix('\n');assert h(a.encode())==mb['fragmento_original_sha256'] and h(b.encode())==mb['fragmento_candidato_sha256'];ed.append({'id':'ficha-080','documento':mb['documento'],'original':str(p),'candidata':str(q),'original_sha256':h(a.encode()),'candidata_sha256':h(b.encode())})
assert len(ed)==8
for e in ed:
 s=pathlib.Path(e['documento']).read_text();a=pathlib.Path(e['original']).read_text().removesuffix('\n');b=pathlib.Path(e['candidata']).read_text().removesuffix('\n');assert s.count(a)==1 and s.count(b)==0,e['id']
target.write_text(json.dumps({'estado':'CONFIGURACAO_SEM_APLICACAO','edicoes':ed},indent=2,ensure_ascii=False)+'\n');print(target)
