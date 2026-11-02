from pathlib import Path
import json, hashlib, re, collections
root=Path.cwd(); p=root/'auditoria/termodinamica/evidencias/QA-09'; result=p/'aplicacao-wika-r15-r1/resultado'
def read(path): return path.read_bytes()
def sha(data): return hashlib.sha256(data).hexdigest()
def doc(name): return json.loads(read(p/name))
a=read(result/'antes-aula.html'); b=read(result/'depois-aula.html'); f=read(result/'antes-formulario.html')
assert sha(a)=='572b172b29e1aa26873d191ebd827414c99f3122491c6d4c8129a69443f7389c'
assert sha(b)=='f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e'
assert b==read(root/'modulos/e1-termodinamica.html')
assert sha(f)=='3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce'
assert f==read(result/'depois-formulario.html')==read(root/'formulas/termodinamica.html')
old=b'https://www.wika.com/en-us/111_16_111_26.WIKA'; new=b'https://www.wika.com/pt-br/111_16_111_26.WIKA'
assert a.count(old)==1 and a.count(new)==0 and a.replace(old,new)==b
arts=lambda s: re.findall(rb'<article\b[^>]*>.*?</article\s*>',s,re.I|re.S)
assert len(arts(a))==197 and arts(a)==arts(b)
assert len(re.findall(rb'<math\b',a,re.I))==734 and len(re.findall(rb'<math\b',b,re.I))==734
x=doc('inventario-r14.json'); y=doc('inventario-r15.json'); m=doc('mapa-correspondencia-inventario-r14-r15-r1.json')
assert sha(read(p/'inventario-r15.json'))=='c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c'
assert sha(read(p/'mapa-correspondencia-inventario-r14-r15-r1.json'))=='1a264971f918313d3a495f9af18f7f712c18b6bceeca5e1494dfdad2e9fb2533'
assert x['artigos_excluidos']==y['artigos_excluidos'] and len(x['artigos_excluidos'])==197
io=json.loads(read(result/'inventario-oficial-antes.json')); inew=json.loads(read(root/'auditoria/termodinamica/inventario/inventario-questoes.json')); assert io['itens']==inew['itens'] and len(io['itens'])==197
assert io['fonte']['sha256']==sha(a) and inew['fonte']['sha256']==sha(b)
assert x['ativos_especificos']==y['ativos_especificos'] and len(x['ativos_especificos'])==6
assert len(x['ocorrencias'])==len(y['ocorrencias'])==len(m['pares'])==11399
ix={z['id']:z for z in x['ocorrencias']}; iy={z['id']:z for z in y['ocorrencias']}
assert len(ix)==len(iy)==11399
seenx=set(); seeny=set()
for z in m['pares']:
 u,v=ix[z['id_r14']],iy[z['id_r15']]; seenx.add(u['id']); seeny.add(v['id'])
 assert z['sha256_r14']==u['sha256_fragmento'] and z['sha256_r15']==v['sha256_fragmento']
 if z['estado']=='PAREADO_EXTERNO': assert u==v
 else: assert z['estado'] in ('PAREADO_INTERNO_CONFERIR','PAREADO_CONTEXTO_ANCESTRAL_CONFERIR')
assert len(seenx)==len(seeny)==11399
assert collections.Counter(z['estado'] for z in m['pares'])=={'PAREADO_EXTERNO':11397,'PAREADO_CONTEXTO_ANCESTRAL_CONFERIR':1,'PAREADO_INTERNO_CONFERIR':1}
assert len(x['referencias'])==len(y['referencias'])==816
refdiff=[(u,v) for u,v in zip(x['referencias'],y['referencias']) if u!=v]; assert len(refdiff)==1
u,v=refdiff[0]; assert u['valor']==old.decode() and v['valor']==new.decode(); assert {**u,'valor':v['valor']}==v
assert len(x['recursos'])==len(y['recursos'])==138
for u,v in zip(x['recursos'],y['recursos']):
 assert {**u,'sha256':v['sha256']}==v
 if u['arquivo']=='modulos/e1-termodinamica.html': assert u['sha256']==sha(a) and v['sha256']==sha(b)
 else: assert u==v
print('OK: troca única, 197 artigos, 734 MathML, formulário, mapa bijetivo com 11.399 pares, 816 referências, 138 recursos e seis ativos')
