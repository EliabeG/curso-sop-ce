#!/usr/bin/env python3
"""Verifica candidatas isoladas, sem editar arquivo de produto ou evidência."""
from pathlib import Path
import hashlib,json
P=Path('auditoria/termodinamica/evidencias/QA-09/candidatas-flashcards-resumo-20261030')
M=json.loads((P/'manifesto.json').read_text());source=Path(M['documento']).read_bytes();inv=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r8.json').read_bytes(); H=lambda b:hashlib.sha256(b).hexdigest()
assert H(source)==M['sha256_documento'] and H(inv)==M['sha256_inventario_r8']
h=source.decode(); raw=h.encode('utf-16-le');data=json.loads(inv);working=h
for e in M['candidatas']:
 original=(P/e['original']).read_text().removesuffix('\n');candidate=(P/e['candidata']).read_text().removesuffix('\n');assert H(original.encode())==e['sha256_original_sem_quebra_final'] and H(candidate.encode())==e['sha256_candidata_sem_quebra_final']
 assert raw[2*e['inicio_utf16']:2*e['fim_utf16']].decode('utf-16-le')==original and h.count(original)==1 and h.count(candidate)==0 and original.count(e['antes'])==1 and original.replace(e['antes'],e['depois'])==candidate
 matching=[x for x in data['ocorrencias'] if x['id']==e['id_r8']]; assert len(matching)==1 and matching[0]['sha256_fragmento']==e['hash_inventario']
 assert working.count(original)==1;working=working.replace(original,candidate,1)
print(json.dumps({'ok':True,'candidatas_verificadas':len(M['candidatas']),'sha256_resultado_hipotetico':H(working.encode()),'estado':'NAO_APLICADO'},ensure_ascii=False))
