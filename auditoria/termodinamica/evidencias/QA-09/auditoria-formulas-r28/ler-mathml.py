from pathlib import Path
from xml.etree import ElementTree as E
from html import unescape
import json,re
s=Path('formulas/termodinamica.html').read_text().encode('utf-16-le')
a=json.loads(Path('auditoria/termodinamica/evidencias/QA-09/formulas-r28-fundamentos-gases-r27-20261030/identidades.json').read_text())
def read(x):
 t=x.tag.split('}')[-1];v=[read(z) for z in x];text=(x.text or '').strip()
 if t=='mfrac':return '('+v[0]+')/('+v[1]+')'
 if t=='msup':return '('+v[0]+')^('+v[1]+')'
 if t=='msub':return v[0]+'_'+v[1]
 if t=='msubsup':return v[0]+'_'+v[1]+'^'+v[2]
 if t=='msqrt':return 'sqrt('+''.join(v)+')'
 return text+''.join(v)
for o in a:
 x=s[2*o['inicio_utf16']:2*o['fim_utf16']].decode('utf-16-le');ms=re.findall(r'<math\b[^>]*>.*?</math>',x,re.S)
 print(o['ficha'], '; '.join(read(E.fromstring(unescape(t))) for t in ms))
