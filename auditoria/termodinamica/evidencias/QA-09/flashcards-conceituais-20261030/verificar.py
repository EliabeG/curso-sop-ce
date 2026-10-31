from pathlib import Path
import hashlib,json
p=Path('modulos/e1-termodinamica.html'); inv=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r8.json'); h=hashlib.sha256
assert h(p.read_bytes()).hexdigest()=='57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c'
assert h(inv.read_bytes()).hexdigest()=='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687'
source=p.read_text().encode('utf-16-le'); j=json.loads(inv.read_text()); positions=[1258382,1258554,1258726,1258891,1259055,1260863,1261026,1261181,1261323,1261480,1261653,1269356]
for n in positions:
 row=[x for x in j['ocorrencias'] if x['arquivo']==str(p) and x['tipo']=='flashcard' and x['inicio_utf16']==n];assert len(row)==1
 x=row[0];data=source[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le').encode();assert h(data).hexdigest()==x['sha256_fragmento']
print(json.dumps({'fotografia_valida':True,'cartoes_conferidos':len(positions),'posicoes':positions,'limite':'Identidade estrutural; não julga mérito nem conclui QA-09.'},ensure_ascii=False))
