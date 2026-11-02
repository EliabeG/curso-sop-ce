import json,hashlib
from pathlib import Path
p=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r30.json');raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()=='1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4'
d=json.loads(raw);expected={128:'https://goldbook.iupac.org/terms/view/C01032/html',129:'https://goldbook.iupac.org/terms/view/C01023',131:'https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/ocw_243_lecture09_2024mar05_v2_transcript.pdf',672:'https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir5078.pdf',680:'https://webbook.nist.gov/cgi/cbook.cgi?ID=C7664417&Mask=887',684:'https://www.grc.nasa.gov/www/BGH/realspec.html',685:'https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html'}
for index,url in expected.items():
 x=d['referencias'][index];assert x['valor']==url
 b=Path(x['arquivo']).read_bytes(); assert hashlib.sha256(b).hexdigest()=='c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4'
 u=b.decode().encode('utf-16-le'); frag=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert url.replace('&','&amp;') in frag or url in frag
 print(index,x['secao'],x['ancora'],hashlib.sha256(frag.encode()).hexdigest(),url)
for needle in ['equation-of-state-ideal-gas-2','pub_id=905791','l2Q31eoy_rY']:
 assert not any(needle in x['valor'] for x in d['referencias'])
print('Identidades dos sete vínculos e três fontes de apoio externas conferidas.')
