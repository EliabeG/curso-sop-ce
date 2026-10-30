from pathlib import Path
import json,hashlib,re,collections
from html.parser import HTMLParser
p=Path('auditoria/termodinamica/evidencias/QA-09'); a=p/'aplicacao-precisao-r30'; rs=a/'resultado'; fixture=Path('/tmp/curso-r30-ensaio-pre-aplicacao')
h=lambda b:hashlib.sha256(b).hexdigest()
manifest=json.loads((p/'candidata-refrigeracao-precisao-r30-next-examples/manifesto.json').read_text())
assert h((p/'candidata-refrigeracao-precisao-r30-next-examples/manifesto.json').read_bytes())=='586ef6cee0ddab40bfc8ab180af39a2f14a1f4d5af0b7a539f38cc062a1bb0c2'
class A(HTMLParser):
 def __init__(self): super().__init__();self.attrs=[]
 def handle_starttag(self,t,attrs): self.attrs += [(t,k,v) for k,v in attrs if k in ('id','href','src') or k.startswith('aria-')]
def attrs(s):
 x=A();x.feed(s);return x.attrs
def maths(s):return re.findall(r'<math\b.*?</math>',s,re.S|re.I)
for edit,base in zip(manifest['edicoes'],['aula','formulario']):
 old=(rs/f'antes-{base}.html').read_text(); new=(rs/f'depois-{base}.html').read_text();current=Path(edit['documento']).read_text()
 assert h(old.encode())==edit['sha_base'] and h(new.encode())==edit['sha_hipotetico']
 assert old.count(edit['antes'])==edit['quantidade'] and old.replace(edit['antes'],edit['depois'])==new==current
 assert maths(old)==maths(new) and attrs(old)==attrs(new)
 assert len(re.findall(r'<article\b',old))==len(re.findall(r'<article\b',new))
 assert (fixture/edit['documento']).read_text()==new
 print(base, 'substituições:', edit['quantidade'], 'MathML:',len(maths(new)))
i29=json.loads((p/'inventario-r29.json').read_text());i30=json.loads((p/'inventario-r30.json').read_text()); m=json.loads((p/'mapa-correspondencia-inventario-r29-r30-r1.json').read_text())
assert h((p/'inventario-r29.json').read_bytes())==m['base_r29'] and h((p/'inventario-r30.json').read_bytes())==m['base_r30']
assert h((p/'mapa-correspondencia-inventario-r29-r30-r1.json').read_bytes())=='7aca7066c5b3da141549566be2b6539643ebadcd44acc2473bccdcce4a986d17'
old={x['id']:x for x in i29['ocorrencias']}; new={x['id']:x for x in i30['ocorrencias']}; pairs=m['pares']
assert len(old)==len(new)==len(pairs)==11409
assert len(set(x['id_r29'] for x in pairs))==len(set(x['id_r30'] for x in pairs))==len(pairs)
counts=collections.Counter()
for x in pairs:
 o=old[x['id_r29']];n=new[x['id_r30']]; assert x['sha256_r29']==o['sha256_fragmento'] and x['sha256_r30']==n['sha256_fragmento']
 assert all(o[k]==n[k] for k in ('arquivo','secao','ancora','tag','tipo'))
 if x['estado']=='PAREADO_EXTERNO':assert o['sha256_fragmento']==n['sha256_fragmento']
 else:assert x['estado']=='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR'
 counts[x['estado']]+=1
assert counts=={'PAREADO_EXTERNO':11403,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':6}
# Reconstrói os seis trechos dos ancestrais a partir dos limites UTF-16.
for x in pairs:
 if x['estado']!='PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':continue
 o=old[x['id_r29']];n=new[x['id_r30']]; e=next(e for e in manifest['edicoes'] if e['documento']==o['arquivo']); base='aula' if o['arquivo'].startswith('modulos/') else 'formulario'
 def trecho(version,entry):
  raw=(rs/f'{version}-{base}.html').read_text().encode('utf-16-le')
  return raw[2*entry['inicio_utf16']:2*entry['fim_utf16']].decode('utf-16-le')
 before=trecho('antes',o);after=trecho('depois',n)
 assert e['antes'] in before and before.replace(e['antes'],e['depois'])==after

ignored={'inicio_utf16','fim_utf16','linha'}
strip=lambda x:{k:v for k,v in x.items() if k not in ignored}
assert len(i29['referencias'])==len(i30['referencias'])==816
assert [strip(x) for x in i29['referencias']]==[strip(x) for x in i30['referencias']]
assert len(i29['recursos'])==len(i30['recursos'])==138
for x,y in zip(i29['recursos'],i30['recursos']):
 assert {k:v for k,v in x.items() if k!='sha256'}=={k:v for k,v in y.items() if k!='sha256'}
 if x['sha256']!=y['sha256']:assert x['arquivo'] in [e['documento'] for e in manifest['edicoes']]
pre=json.loads((rs/'inventario-oficial-antes.json').read_text());post=json.loads(Path('auditoria/termodinamica/inventario/inventario-questoes.json').read_text())
assert all(pre[k]==post[k] for k in pre if k!='fonte')
assert Path('auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md').read_text().startswith((rs/'inventario-oficial-antes.md').read_text())
seven=['modulos/e1-termodinamica.html','formulas/termodinamica.html','auditoria/termodinamica/inventario/inventario-questoes.json','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md',str(p/'inventario-r30.json'),str(p/'mapa-correspondencia-inventario-r29-r30-r1.json'),str(rs/'edicoes-aplicadas.json')]
for f in seven: assert Path(f).read_bytes()==(fixture/f).read_bytes(),f
x=json.loads((a/'ensaio.json').read_text()); y=json.loads((rs/'verificacoes.json').read_text()); assert x.pop('modo')=='--fixture' and y.pop('modo')=='--apply' and x==y
assert x['validacao']['ok'] and not x['validacao']['erros'] and not x['validacao']['avisos']
print('mapa:',dict(counts),'referências:',len(i30['referencias']),'recursos:',len(i30['recursos']))
print('Sete saídas do ensaio são iguais às efetivas; inventário oficial preserva itens; teste OK.')
