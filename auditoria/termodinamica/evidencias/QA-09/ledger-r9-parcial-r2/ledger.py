#!/usr/bin/env python3
"""Constrói para stdout ou confere a r2 sem alterar fontes ou ledgers."""
import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path('.')
DIR = 'auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r2/'
R1 = 'auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r1/'
BASE_SCRIPT_SHA = 'abec471b35be0a7956611f9d5fd3b60135e721042bedb13bea770b73f245e7b1'
BASE_JSON_SHA = '50f529daca4b65876c54bff129b938d0fb0cad7e7194206fcfcc26428e021c59'
BASE_REVIEW = 'auditoria/termodinamica/pareceres/QA-09-ledger-r9-parcial-auditoria-independente-20261030.md'
BASE_REVIEW_SHA = 'fae8248aa29b3561d5fb16d10a42b2fc2bae067340b609d1910f3b64fc48457d'
SELECOES_SHA = '80a5f967663c801ba6b6d25411693d207f338cad9d4f14308891025857f49367'
TEXTOS_SHA = 'c6d53ef85a024a70326d6ac3461f40b8e3b28507de0abc60ea2e1f9e3c10acd7'

def hash_(data): return sha256(data).hexdigest()
def ler(path, expected):
    data = (ROOT / path).read_bytes()
    if hash_(data) != expected: raise ValueError(f'{path}: SHA divergente; interrompa e reconcilie')
    return data
def exigir(cond, message):
    if not cond: raise ValueError(message)

def construir():
    ler(R1+'ledger.py', BASE_SCRIPT_SHA)
    saved_base = json.loads(ler(R1+'ledger.json', BASE_JSON_SHA))
    ler(BASE_REVIEW, BASE_REVIEW_SHA)
    data = json.loads(ler(DIR+'selecoes.json', SELECOES_SHA))
    ler(DIR+'verificar-textos.mjs', TEXTOS_SHA)
    spec = importlib.util.spec_from_file_location('ledger_qa09_r1', R1+'ledger.py')
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    base = mod.construir()
    exigir(base == saved_base, 'ledger r1 não reproduzível')
    inv = json.loads(ler(mod.INV, mod.INV_SHA))
    check = subprocess.run(['node', DIR+'verificar-textos.mjs'], capture_output=True, text=True, check=True)
    result = json.loads(check.stdout)
    exigir(result == {'ok':True,'textos_conferidos':10}, 'conferência de textos diretos divergente')
    identities = set()
    for row in data['registros']:
        col = row['colecao']; index = row['indice_base_zero']; item = row['identidade_r9']
        exigir(col in ('ocorrencias','referencias','recursos','ativos_especificos'), 'coleção desconhecida')
        exigir(isinstance(index,int) and 0 <= index < len(inv[col]) and inv[col][index] == item, 'identidade do inventário divergente')
        key = (col,index); exigir(key not in identities, 'registro duplicado'); identities.add(key)
        ler(row['parecer'],row['parecer_sha256'])
        exigir(row['estado'] in ('conferido_no_escopo_localizado','achado_aberto'), 'estado desconhecido')
        if col == 'ocorrencias' and item['tipo'] != 'texto_direto':
            encoded = Path(item['arquivo']).read_text(encoding='utf-8').encode('utf-16-le')
            piece = encoded[item['inicio_utf16']*2:item['fim_utf16']*2].decode('utf-16-le').encode('utf-8')
            exigir(hash_(piece) == item['sha256_fragmento'], f"{row['id_local']}: hash de fragmento divergente")
        elif col == 'referencias':
            encoded = Path(item['arquivo']).read_text(encoding='utf-8').encode('utf-16-le')
            piece = encoded[item['inicio_utf16']*2:item['fim_utf16']*2].decode('utf-16-le')
            exigir(item['tag'] == 'a' and f'href="{item["valor"]}"' in piece, f"{row['id_local']}: vínculo divergente")
        elif col == 'ativos_especificos':
            ler(item['arquivo'],item['sha256'])
    exigir(len(data['registros']) == 34 and sum(x['estado']=='achado_aberto' for x in data['registros']) == 2,
           'conjunto esperado de seleções divergente')
    return {'versao':'r9-parcial-r2','data':'2026-10-30','estado_global':'QA09_EM_CORRECAO_NAO_APROVADO',
            'fotografia':base['fotografia'],
            'base_r1':{'ledger':R1+'ledger.json','sha256':BASE_JSON_SHA,'parecer':BASE_REVIEW,'parecer_sha256':BASE_REVIEW_SHA},
            'colecoes':base['colecoes'],'regra_padrao':base['regra_padrao'],
            'artigos_ban08':base['artigos_ban08'],'estados_permitidos':base['estados_permitidos'],
            'registros_r1':base['registros_explicitamente_revisados'],
            'registros_adicionais':data['registros'],
            'limites':['Oito registros r1 e 32 novos registram somente o alcance dos pareceres. Dois novos registros são achados abertos; não encerra QA-09.',
                       'Os demais registros permanecem pendentes de integração; isto não apaga revisões históricas.',
                       'Os dois lotes com ajustes obrigatórios não foram aprovados. Nenhuma outra ficha desses lotes foi classificada aqui.',
                       'Não há transferência automática de cobertura para filhos, pais, recursos, fontes ou outras versões.',
                       'Contagens estruturais sobrepostas não são cálculos ou percentual de conclusão.',
                       'Não há teste em navegador, avaliação com estudantes, revisão humana ou certificação externa nesta integração.']}

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verificar',metavar='ARQUIVO');args=parser.parse_args()
    try:
        result=construir()
        if args.verificar:
            saved=json.loads(Path(args.verificar).read_text(encoding='utf-8'))
            exigir(saved == result,'ledger salvo não corresponde à reprodução')
            print(json.dumps({'ok':True,'registros_r1':len(result['registros_r1']),
                              'registros_adicionais':len(result['registros_adicionais']),
                              'achados_abertos':sum(x['estado']=='achado_aberto' for x in result['registros_adicionais']),
                              'qa09':'em correção'},ensure_ascii=False,indent=2))
        else: print(json.dumps(result,ensure_ascii=False,indent=2))
    except (OSError,ValueError,KeyError,UnicodeError,subprocess.CalledProcessError) as error:
        print(f'ERRO: {error}',file=sys.stderr);sys.exit(1)
