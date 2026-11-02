from pathlib import Path
import json,hashlib
p=Path('auditoria/termodinamica/evidencias/QA-09'); inv=json.loads((p/'inventario-r30.json').read_text()); page=Path('modulos/e1-termodinamica.html').read_bytes(); assert hashlib.sha256(page).hexdigest()=='c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4';assert hashlib.sha256((p/'inventario-r30.json').read_bytes()).hexdigest()=='1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4'
s=page.decode().encode('utf-16-le'); prior=[]
for src in ['referencias-gerais-r13-20261030/identidades.json','referencias-propriedades-r12-20261030/identidades.json']:
 prior+=json.loads((p/src).read_text())
for i in [669,670,671,673,674,675,676,677,678,679]:
 x=inv['referencias'][i]; assert x['arquivo']=='modulos/e1-termodinamica.html' and x['secao']=='fontes' and x['ancora']=='fontes'
 frag=s[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le'); sha=hashlib.sha256(frag.encode()).hexdigest(); matches=[y for y in prior if y['valor']==x['valor']]
 assert len(matches)==1 and matches[0]['sha256_elemento']==sha and matches[0]['texto']==x['texto']
 print(f"{i} {x['inicio_utf16']}–{x['fim_utf16']} {sha} {x['valor']}")
print('Dez referências r30 coincidem em URL, texto e SHA com identidades r12/r13. Sem teste de rede.')
