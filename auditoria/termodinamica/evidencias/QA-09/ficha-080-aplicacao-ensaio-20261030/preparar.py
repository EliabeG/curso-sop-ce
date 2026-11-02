#!/usr/bin/env python3
"""Prepara fotografia experimental em diretório novo; nunca escreve no produto.
Uso: python3 preparar.py DIRETORIO_NOVO. Requer lxml.
"""
import hashlib,json,re,sys
from pathlib import Path
from lxml import html
R=Path(__file__).resolve().parents[5]
if len(sys.argv)!=2:raise SystemExit('Informe diretório novo para a simulação.')
out=Path(sys.argv[1]).resolve();prod=(R/'formulas/termodinamica.html').resolve();historico=(R/'auditoria/termodinamica/evidencias/FOR-01').resolve()
if out==R.resolve() or R.resolve() in out.parents and out!=Path(__file__).resolve().parent/'ensaio':raise SystemExit('Dentro do repositório use somente a pasta ensaio deste pacote.')
if prod in out.parents or historico in out.parents:raise SystemExit('Destino proibido')
H=lambda b:hashlib.sha256(b).hexdigest()
source=prod.read_bytes();approved=(R/'auditoria/termodinamica/evidencias/FOR-01/pacote-r2/formulas/termodinamica.html').read_bytes(); inv=(R/'auditoria/termodinamica/evidencias/QA-09/inventario-r8.json').read_bytes()
assert H(source)=='c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0' and source==approved
assert H(inv)=='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687'
candidate=R/'auditoria/termodinamica/evidencias/QA-09/ficha-080-candidata-20261030'; old=(candidate/'original.html').read_bytes(); new=(candidate/'candidata.html').read_bytes(); assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1]
assert H(old)=='be53d6d4b8ef9305ad4392713fd7ce2c59379393187d06bf0234116ffc431ea5' and H(new)=='9dcaed2872d4754bb8151aae1ada14a4c45a07557e6ed70ec5569b8c4cfc0897' and source.count(old)==1
result=source.replace(old,new,1);assert H(result)=='cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'
pattern=rb'<article\b[^>]*\bclass="formula-card"[^>]*>.*?</article>'
c1=re.findall(pattern,source,re.S);c2=re.findall(pattern,result,re.S);assert len(c1)==len(c2)==100
assert [i+1 for i,(a,b) in enumerate(zip(c1,c2)) if a!=b]==[80]
assert all(c1[i-1]==c2[i-1] for i in (23,46,79,84))
math1=re.findall(rb'<math\b.*?</math>',source,re.S);math2=re.findall(rb'<math\b.*?</math>',result,re.S);assert len(math1)==len(math2)==191 and math1==math2
before,after=html.fromstring(source),html.fromstring(result);assert len(before.xpath('//section[contains(@class,"formula-grupo")]'))==len(after.xpath('//section[contains(@class,"formula-grupo")]'))==11
assert [x.get('id') for x in before.xpath('//*[@id]')]==[x.get('id') for x in after.xpath('//*[@id]')]
for attr in ('href','src','aria-controls','aria-labelledby','aria-describedby'):
 assert [(x.tag,x.get(attr)) for x in before.xpath('//*[@%s]'%attr)]==[(x.tag,x.get(attr)) for x in after.xpath('//*[@%s]'%attr)]
card=after.get_element_by_id('formula-brayton-liquido');phrase='Para η como rendimento motor: Q̇in > 0 e Ẇt > Ẇc.';assert phrase in card.get('data-busca') and phrase in card.xpath('.//p[@class="formula-condicao"]')[0].text_content()
aula_raw=(R/'modulos/e1-termodinamica.html').read_bytes()
assert H(aula_raw)=='57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c'
aula=html.fromstring(aula_raw); aula_ids=set(aula.xpath('//*[@id]/@id'))
cards=after.xpath('//article[contains(concat(" ",normalize-space(@class)," ")," formula-card ")]')
links=[]
for c in cards:
    targets=c.xpath('.//a[contains(concat(" ",normalize-space(@class)," ")," formula-aula ")]/@href')
    assert targets
    links.extend(targets)
assert len(links)==103 and len(set(links))==50
assert all(u.startswith('../modulos/e1-termodinamica.html#') and u.split('#',1)[1] in aula_ids for u in links)
assert source==prod.read_bytes() # nenhum concorrente modificou a base durante a verificação
out.mkdir(parents=True,exist_ok=False)
(out/'formulario.antes.html').write_bytes(source);(out/'formulario.proposto.html').write_bytes(result)
info={'estado':'ENSAIO_EM_COPIA_AGUARDANDO_AUDITORIA','base_sha256':H(source),'formulario_proposto_sha256':H(result),'formulario_FOR01_r2_sha256':H(approved),'inventario_r8_sha256':H(inv),'fichas':100,'fichas_alteradas':[80],'fichas_FOR01_r1_A_preservadas':[23,46,79,84],'mathml_preservados':191,'grupos':11,'vinculos_fichas':103,'destinos_aula_distintos':50,'aula_r8_sha256':H(aula_raw),'ids_vinculos_atributos_preservados':True,'dominio_e_busca_sincronizados':True,'limites':'Ensaio em cópia; não altera produto, não é parecer independente, não executa navegador nem reaprova FOR-01/QA-09 integral. Confere existência dos destinos na aula r8, não sua coerência semântica nem dependências externas.'}
(out/'resultado.json').write_text(json.dumps(info,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(info,ensure_ascii=False,indent=2))
