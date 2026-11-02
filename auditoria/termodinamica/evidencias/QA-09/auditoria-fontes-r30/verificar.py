#!/usr/bin/env python3
"""Confronta índices, href e fragmentos r30; somente leitura."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';sha=lambda b:sha256(b).hexdigest();p=q/'fontes-r30';assert sha((p/'entrega.md').read_bytes())=='35c2345e35a15174b2c0ea9739348977a58b4e6230a1e6882012364e94dc0be4';assert sha((p/'verificar_identidades.py').read_bytes())=='a9f61832d09c5105bb66317c7fd342ff0551c0b863203e95edf66d6e0211f399'
b=(q/'aplicacao-precisao-r30/resultado/depois-aula.html').read_bytes();assert sha(b)=='c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4';u=b.decode().encode('utf-16-le');invb=(q/'inventario-r30.json').read_bytes();assert sha(invb)=='1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4';inv=json.loads(invb)
urls={128:'https://goldbook.iupac.org/terms/view/C01032/html',129:'https://goldbook.iupac.org/terms/view/C01023',131:'https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/ocw_243_lecture09_2024mar05_v2_transcript.pdf',672:'https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir5078.pdf',680:'https://webbook.nist.gov/cgi/cbook.cgi?ID=C7664417&Mask=887',684:'https://www.grc.nasa.gov/www/BGH/realspec.html',685:'https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html'}
class A(HTMLParser):
 def __init__(self):super().__init__();self.href=[]
 def handle_starttag(self,t,a):
  if t=='a':self.href.append(dict(a).get('href'))
rows=[]
for i,url in urls.items():
 x=inv['referencias'][i];assert x['valor']==url and x['arquivo']=='modulos/e1-termodinamica.html';a,z=x['inicio_utf16'],x['fim_utf16'];frag=u[2*a:2*z].decode('utf-16-le');parser=A();parser.feed(frag);assert url in parser.href;rows.append({'indice':i,'url':url,'inicio_utf16':a,'fim_utf16':z,'sha256_elemento':sha(frag.encode()),'ancora':x['ancora']})
support=['equation-of-state-ideal-gas-2','pub_id=905791','l2Q31eoy_rY'];assert all(not any(needle in x['valor'] for x in inv['referencias']) for needle in support)
report=(q/'tabelas-r30/entrega.md').read_text();assert all(x in report for x in support)
print(json.dumps({'ok':True,'vinculos':rows,'fontes_de_apoio_em_tabelas':3,'nao_vinculadas_na_aula_formulario':True,'sem_escrita_em_produto':True},ensure_ascii=False,indent=2))
