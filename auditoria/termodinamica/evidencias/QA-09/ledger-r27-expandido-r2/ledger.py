#!/usr/bin/env python3
"""Consolida escopos explicitamente auditados na r27; só lê e escreve em stdout."""
from pathlib import Path
import json, hashlib, sys
Q=Path('auditoria/termodinamica/evidencias/QA-09')
sha=lambda b:hashlib.sha256(b).hexdigest()
files={
'modulos/e1-termodinamica.html':'9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49',
'formulas/termodinamica.html':'16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02',
str(Q/'inventario-r27.json'):'a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c',
str(Q/'ledger-r27-parcial-r1/ledger.json'):'072186f83f5fe80f8c5460aaf33351d02b25cd2a867f0972adbb68ddc9864d26',
str(Q/'auditoria-ledger-r27-independente-20261030/parecer.md'):'ec6a2adc6ec10155fb627bb94612021dd041c83ff1fd242287367c493c3f9ece',
str(Q/'formulas-r28-fundamentos-gases-r27-20261030/identidades.json'):'c094d3b759f1054931c32e09edb718f105ee73ad8990e15ede8cd11e91c8537a',
str(Q/'formulas-r28-fundamentos-gases-r27-20261030/entrega.md'):'eb9b0d624d967d5e302a02d7c08758068d0149df106181773a8286969752d417',
str(Q/'auditoria-formulas-r28/parecer.md'):'6ecc99c06f9ef2a3c76d75ee3436bfedcfff4732a982c0a7f1db37d93fb04863',
str(Q/'fontes-r28-figuras-r27-20261030/identidades.json'):'db7a58ccca64bdada986ee53c1db6ac6e2ad65b1ef160af67fb18529975efd1c',
str(Q/'fontes-r28-figuras-r27-20261030/entrega.md'):'d7455f7c84dfb1bac5a5d45da8053632fa70034d00479cc8d9c8c3653211cc5e',
str(Q/'auditoria-fontes-r28-figuras-next-formulas-20261030/parecer.md'):'901a53b2e690800c8bdd8882832b8088ee194a6f8544d851bb46754dafee502b',
str(Q/'teoria-r28-entrada-escopo-fun-20261030/entrega.md'):'93334c18eb84ae1dbaaee265642fe43c24315ac0c83171594feb0526d0be1ce7',
str(Q/'auditoria-teoria-r28-entrada-escopo-fun-independente-20261030/parecer.md'):'e9fae35e0a55b5f4ed189c11520141c9372bb05a762f7043672356e527cfd120',
str(Q/'ledger-r27-expandido-r1/ledger.json'):'c91f24e8af862fe452c4d4c4ee9b9a987f548aada987d6501ae06773144ce051',
str(Q/'diagnosticos-r28-3/identidades.json'):'6f66ff4568d1d201d98b82bea686bcb83edc48acdd246657bdf3e0c92a36aad1',
str(Q/'diagnosticos-r28-3/entrega.md'):'a207960549fa1df851e783d62fdcba4ad7a92de6a8742e6b3b56f60a3f645fbc',
str(Q/'auditoria-diagnosticos-r28-3-next-formulas-20261030/parecer.md'):'aabbefd78bd91f52a5fabde46512f08d51a17171caec72dafb022e920ed70931',
str(Q/'diagnosticos-r28-2/identidades.json'):'7e0c1603e26dde8c95a26c0866717e9b4c7f6bd44158628a356627a1e48e4f68',
str(Q/'diagnosticos-r28-2/entrega.md'):'66bdf05a8ec3373253094065aee002b05e039de12f2af93df89c1f4ab71e851b',
str(Q/'auditoria-diagnosticos-r28-2-next-formulas-20261030/parecer.md'):'1f297c78f140f228419db4a2fabdc16a2ef0753e29e0f34198139fa56b79e4eb',
str(Q/'graficos-r28/entrega.md'):'dbdf1ff0259bbdc239d4567835b0b02e8ef4e4b15901d09d7fdc73d58f0c9eaa',
str(Q/'auditoria-graficos-r28-next-theory-20261030/parecer.md'):'e3915e73358c789586846134a199eb8821a42007376f269c88072658f57e4352'}
def load(path):
 b=Path(path).read_bytes(); assert sha(b)==files[path],f'hash divergente: {path}';return b
for p in files: load(p)
base=json.loads(load(str(Q/'ledger-r27-parcial-r1/ledger.json')))
assert len(base['registros_explicitamente_revisados'])==18
review=load(str(Q/'auditoria-ledger-r27-independente-20261030/parecer.md')).decode();assert 'APROVAD' in review.upper()
lesson=load('modulos/e1-termodinamica.html').decode().encode('utf-16-le');form=load('formulas/termodinamica.html').decode().encode('utf-16-le')
rows=[]
def add(id,kind,doc,start,end,digest,delivery,review,scope,extra=None):
 raw=(form if doc.startswith('formulas/') else lesson)[2*start:2*end].decode('utf-16-le').encode()
 assert sha(raw)==digest,(id,'recorte divergente')
 item={'id':id,'tipo':kind,'arquivo':doc,'inicio_utf16':start,'fim_utf16':end,'sha256_fragmento':digest,'estado':'conferido_no_escopo_localizado','escopo':scope,'entrega':{'arquivo':str(Q/delivery),'sha256':files[str(Q/delivery)]},'parecer_independente':{'arquivo':str(Q/review),'sha256':files[str(Q/review)]}}
 if extra:item.update(extra)
 rows.append(item)
forms=json.loads(load(str(Q/'formulas-r28-fundamentos-gases-r27-20261030/identidades.json')));assert len(forms)==22 and [x['ficha'] for x in forms]==list(range(1,23))
for x in forms:
 add(x['id'],'ficha','formulas/termodinamica.html',x['inicio_utf16'],x['fim_utf16'],x['sha256'],'formulas-r28-fundamentos-gases-r27-20261030/entrega.md','auditoria-formulas-r28/parecer.md','Ficha e expressões conforme modelos e ressalvas de domínio do parecer; não valida acessibilidade ou as outras fichas.',{'numero_ficha':x['ficha'],'mathml':x['mathml']})
figs=json.loads(load(str(Q/'fontes-r28-figuras-r27-20261030/identidades.json')))['figuras'];assert len(figs)==4
for i,x in enumerate(figs,1):
 add('figura-r27-'+str(i),'figura_svg','modulos/e1-termodinamica.html',x['inicio_utf16'],x['fim_utf16'],x['sha256'],'fontes-r28-figuras-r27-20261030/entrega.md','auditoria-fontes-r28-figuras-next-formulas-20261030/parecer.md','Geometria e conteúdo no modelo e contexto indicados; SVG reconstruído, não verificação de acessibilidade ou renderização real.',{'rotulos_aria':x['rotulos_aria']})
for id,a,b,h in [('fun01-objetivos',89932,91254,'999acac3f3f2c9eac594e4468c8f265e2a981f7244cf2671b3d7a67eedd60678'),('fun01-entrada',91255,92956,'e07c1062616fb496db85a84ca9c223174d5cfdd00458f36ea02e9a0f063629f3'),('fun01-parecer',114996,116657,'f5a41941645486e3672e6bd7c6fea5be46b61b4b51ade8bfaf7f26c37fcc4bdd'),('fun01-problemas',116658,117167,'5c64656f2708769997300502847f3a533a22864bc8c95a3300a25fdec69dcbbf'),('fun02-objetivos',236884,238201,'1ddee9e8484a7c44ab3619e6f97f503b5fe50fa42484a1697328f08dec202870'),('fun02-problemas',257431,258209,'85d9a6d965187feb06acc76469ef416593e2c8c5c92948a662113815e68bf9db')]:
 add(id,'bloco_teoria','modulos/e1-termodinamica.html',a,b,h,'teoria-r28-entrada-escopo-fun-20261030/entrega.md','auditoria-teoria-r28-entrada-escopo-fun-independente-20261030/parecer.md','Apenas trecho e alegações específicas; pontos de rubricas não validam artigos integrais nem certificam aprendizagem.')
for id,a,b,h,key,asset in [('av-e1-06',990447,994499,'89dc4205deb6e31424ecf39c1abc0a270339b7200d33d281f528f7c28762e87d','922604ee21ac','922604ee21ac25fec713806a3102c7b775b9cd16ba2c77054cb45d976226b17e'),('av-e1-30',1076355,1080938,'b15d6dd6aa44531627bb9a953e5d572a383804b557bb38df3869b581420c3b01','de4ee7b16ed4','de4ee7b16ed42d37537a23bbcf6cf7aee66cb447e11bb950b3c783e3a859aa1b'),('av-e1-37',1103560,1107932,'b741f7c26e317df09eaf7984e2065f881464ffc7367202fa2968b4ce30efe928','222735fab01e','222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb')]:
 p='assets/questoes-reais-e1/figura-'+key+'.png';assert sha(Path(p).read_bytes())==asset
 scope='Gráfico e resultado no recorte e modelo do parecer, sem prova de proveniência oficial ou acessibilidade.'
 if id=='av-e1-06':scope+=' Há melhoria editorial de clareza recomendada; não foi demonstrado erro do resultado ou figura.'
 add(id,'artigo_grafico','modulos/e1-termodinamica.html',a,b,h,'graficos-r28/entrega.md','auditoria-graficos-r28-next-theory-20261030/parecer.md',scope,{'ativo':{'arquivo':p,'sha256':asset}})
diags=json.loads(load(str(Q/'diagnosticos-r28-2/identidades.json')))['diagnosticos']; assert [x['numero'] for x in diags]==list(range(6,11))+list(range(21,26))
for x in diags:
 for link in x['links']:
  assert lesson.decode('utf-16-le').count('id="'+link+'"')==1,link
 add('D'+str(x['numero']).zfill(2),'diagnostico','modulos/e1-termodinamica.html',x['inicio_utf16'],x['fim_utf16'],x['sha256'],'diagnosticos-r28-2/entrega.md','auditoria-diagnosticos-r28-2-next-formulas-20261030/parecer.md','Diagnóstico e resultado no modelo com condições das bases indicadas no parecer; não aprova bases inteiras nem os demais diagnósticos.',{'links':x['links']})
r1=json.loads(load(str(Q/'ledger-r27-expandido-r1/ledger.json'))); assert rows==r1['registros_adicionais_por_recorte']
diags=json.loads(load(str(Q/'diagnosticos-r28-3/identidades.json')))['diagnosticos']; assert [x['numero'] for x in diags]==list(range(1,6))
for x in diags:
 for link in x['links']:
  assert lesson.decode('utf-16-le').count('id="'+link+'"')==1,link
 scope='Diagnóstico e resultado no modelo com condições das bases indicadas no parecer; não aprova bases inteiras nem os demais diagnósticos.'
 if x['numero']==5: scope+=' Modelo de mistura ideal e fator de intensificação desprezado vem da base, não do enunciado isolado.'
 add('D'+str(x['numero']).zfill(2),'diagnostico','modulos/e1-termodinamica.html',x['inicio_utf16'],x['fim_utf16'],x['sha256'],'diagnosticos-r28-3/entrega.md','auditoria-diagnosticos-r28-3-next-formulas-20261030/parecer.md',scope,{'links':x['links']})
assert len(rows)==50 and len({(x['arquivo'],x['inicio_utf16'],x['fim_utf16']) for x in rows})==50
out={'versao':'r27-expandido-r2','data':'2026-10-30','estado_global':'QA09_EM_CORRECAO_NAO_APROVADO','base_parcial':{'arquivo':str(Q/'ledger-r27-parcial-r1/ledger.json'),'sha256':files[str(Q/'ledger-r27-parcial-r1/ledger.json')],'parecer_independente':str(Q/'auditoria-ledger-r27-independente-20261030/parecer.md'),'parecer_sha256':files[str(Q/'auditoria-ledger-r27-independente-20261030/parecer.md')]},'fotografia':base['fotografia'],'colecoes':base['colecoes'],'registros_explicitamente_revisados':base['registros_explicitamente_revisados'],'registros_adicionais_por_recorte':rows,'revisao_r1_preservada':{'arquivo':str(Q/'ledger-r27-expandido-r1/ledger.json'),'sha256':files[str(Q/'ledger-r27-expandido-r1/ledger.json')]},'diagnosticos_lote_adicional':'D01-D10 e D21-D25 conferidos no escopo; outros permanecem pendentes','limites':['Consolidação r27 expandida pendente de parecer independente.','Recortes adicionais não promovem automaticamente registros de ocorrência, filhos, pais, fórmulas, fontes ou ativos.','Conjuntos sobrepostos não são percentual de conclusão; os demais registros permanecem pendentes.','Escopo gráfico não decide autoria oficial nem acessibilidade; QA-09 permanece aberto.']}
if len(sys.argv)==1:print(json.dumps(out,ensure_ascii=False,indent=2))
elif len(sys.argv)==3 and sys.argv[1]=='--verificar':
 assert json.loads(Path(sys.argv[2]).read_text())==out; print(json.dumps({'ok':True,'base':18,'adicionais':len(rows),'diagnosticos_adicionais':15}))
else:raise SystemExit('uso: ledger.py [--verificar ARQUIVO]')
