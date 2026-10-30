from collections import Counter, defaultdict
from pathlib import Path
import json, hashlib

q=Path('auditoria/termodinamica/evidencias/QA-09')
integration=json.loads((q/'inventario-integracao-r30-r1/ledger.json').read_text())
inventory_path=q/'inventario-r30.json'
assert hashlib.sha256(inventory_path.read_bytes()).hexdigest()=='1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4'
inv=json.loads(inventory_path.read_text())
occ=integration['ocorrencias']; orig=inv['ocorrencias']; groups=integration['grupos']
assert len(occ)==len(orig)==11409 and len(groups)==162
assert len({x['id'] for x in orig})==len(orig)
bygroup=defaultdict(Counter)
for idx,(a,b) in enumerate(zip(occ,orig)):
    assert a['indice_inventario']==idx and a['id']==b['id']
    g=groups[a['grupo_id']]
    assert g['grupo_id']==a['grupo_id'] and (g['arquivo'],g['secao'],g['tipo'])==(b['arquivo'],b.get('secao'),b['tipo'])
    assert (a['estado_triagem']=='juizo_local_documentado') == (a['apoio'] is not None)
    assert a['estado_triagem'] in ('juizo_local_documentado','pendente_de_merito_e_classificacao')
    bygroup[a['grupo_id']][a['estado_triagem']]+=1
for g in groups:
    c=bygroup[g['grupo_id']]
    assert g['juizo_local_documentado']==c['juizo_local_documentado'] and g['pendentes']==c['pendente_de_merito_e_classificacao'] and g['total']==sum(c.values())
assert len({(g['arquivo'],g['secao'],g['tipo']) for g in groups})==162
states=Counter(x['estado_triagem'] for x in occ)
assert states=={'juizo_local_documentado':187,'pendente_de_merito_e_classificacao':11222}
types=Counter(orig[x['indice_inventario']]['tipo'] for x in occ if x['apoio'])
assert types=={'ficha_formula':100,'exemplo_ou_diagnostico':78,'figura':4,'equacao_contextualizada':5}
for name,n in [('referencias',816),('recursos',138),('ativos_especificos',6)]:
    a=integration[name]; b=inv[name]; assert len(a)==len(b)==n
    assert all(x['indice_inventario']==i and x['estado_triagem']=='pendente_avaliacao_individual' for i,x in enumerate(a))
    if name=='referencias':
        assert all(x['valor']==y['valor'] and x['atributo']==y['atributo'] for x,y in zip(a,b))
        assert Counter(x['grupo_sintatico'] for x in a)=={'fragmento_local':606,'caminho_local_ou_outro':138,'url_http':72}
    else: assert all(x['arquivo']==y['arquivo'] for x,y in zip(a,b))
assert len(integration['artigos_excluidos'])==len(inv['artigos_excluidos'])==197
for a,b in zip(integration['artigos_excluidos'],inv['artigos_excluidos']):
    assert all(a[k]==v for k,v in b.items()) and a['estado']=='escopo_artigo_segregado_ban08_sem_aceite_novo'
assert len(integration['unidades_com_juizo_sem_ocorrencia_exata'])==9
assert integration['estado_global']=='QA09_EM_CORRECAO_NAO_APROVADO'
print(json.dumps({'ok':True,'ocorrencias':len(occ),'grupos':len(groups),'estados':states,'tipos_juizos':types,'referencias':816,'recursos':138,'ativos':6,'artigos':197},indent=2,ensure_ascii=False))
