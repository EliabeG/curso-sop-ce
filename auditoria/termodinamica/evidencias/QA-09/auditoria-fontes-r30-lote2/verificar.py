from pathlib import Path
from html.parser import HTMLParser
import hashlib, json

Q = Path('auditoria/termodinamica/evidencias/QA-09')
sha = lambda b: hashlib.sha256(b).hexdigest()
snap = (Q / 'aplicacao-precisao-r30/resultado/depois-aula.html').read_bytes()
assert sha(snap) == 'c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4'
inv_file = Q / 'inventario-r30.json'
assert sha(inv_file.read_bytes()) == '1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4'
refs = json.loads(inv_file.read_text())['referencias']
ids = [669,670,671,673,674,675,676,677,678,679]
historical = [json.loads((Q / name / 'identidades.json').read_text()) for name in ('referencias-gerais-r13-20261030','referencias-propriedades-r12-20261030')]
class Anchor(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True); self.targets=[]
    def handle_starttag(self, tag, attrs):
        if tag == 'a': self.targets.append(dict(attrs).get('href'))
raw=snap.decode().encode('utf-16-le')
output=[]
for index in ids:
    item=refs[index]
    assert item['arquivo']=='modulos/e1-termodinamica.html' and item['secao']=='fontes' and item['ancora']=='fontes'
    part=raw[item['inicio_utf16']*2:item['fim_utf16']*2].decode('utf-16-le')
    parser=Anchor(); parser.feed(part)
    assert parser.targets == [item['valor']]
    hits=[(i,x) for i, old in enumerate(historical) for x in old if x['valor']==item['valor']]
    assert len(hits)==1
    source, old=hits[0]
    h=sha(part.encode())
    assert h==old['sha256_elemento'] and item['texto']==old['texto']
    output.append({'r30':index,'historico':'r13' if source==0 else 'r12','indice_historico':old['indice'],'sha256':h,'url':item['valor']})
print(json.dumps({'ok':True,'referencias':output,'rede':'nao testada neste script'},indent=2,ensure_ascii=False))
