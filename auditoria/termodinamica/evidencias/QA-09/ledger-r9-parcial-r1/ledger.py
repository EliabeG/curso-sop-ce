#!/usr/bin/env python3
"""Ledger esparso QA-09: gera para stdout ou confere JSON sem alterar arquivo."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path('.')
INV = 'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json'
INV_SHA = '023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
CONFIG = 'auditoria/termodinamica/evidencias/QA-09/aplicacao-flashcards-ficha80-r1/config-r2.json'
CONFIG_SHA = '017b14761832e5b371ffc24fa6cccb807f1bb6b2a41b9d160a46d636be1c067a'
EDICOES = 'auditoria/termodinamica/evidencias/QA-09/aplicacao-flashcards-ficha80-r1/edicoes-aplicadas.json'
EDICOES_SHA = '5f75701d8a19898a6068a942d5af2680a9d0a8ea4165f6452ba86a23eba91eaa'
PARECER = 'auditoria/termodinamica/pareceres/QA-09-aplicacao-flashcards-ficha80-auditoria-independente-20261030.md'
PARECER_SHA = 'ad70d72cbe61ea89058406728517008aa379620dcfbb7b05f6cc13cda4e6852a'
DOCUMENTOS = {
    'modulos/e1-termodinamica.html': '2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2',
    'formulas/termodinamica.html': 'cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb',
}
TIPOS = {'cop':'flashcard','valvula':'flashcard','compressor':'flashcard',
         'trocador':'flashcard','pressao-entrada-saida':'flashcard',
         'pressao-1-3':'flashcard','resumo':'texto_direto','ficha-080':'ficha_formula'}

def digest(data):
    return sha256(data).hexdigest()

def ler(path, expected):
    data = (ROOT / path).read_bytes()
    found = digest(data)
    if found != expected:
        raise ValueError(f'{path}: hash divergente: {found}; interrompa e reconcilie')
    return data

def exigir(cond, msg):
    if not cond:
        raise ValueError(msg)

def construir():
    inv = json.loads(ler(INV, INV_SHA))
    cfg = json.loads(ler(CONFIG, CONFIG_SHA))
    changes = json.loads(ler(EDICOES, EDICOES_SHA))
    ler(PARECER, PARECER_SHA)
    docs = {name: ler(name, digest_) for name, digest_ in DOCUMENTOS.items()}
    exigir({x['arquivo']: x['sha256'] for x in inv['documentos']} == DOCUMENTOS,
           'documentos do inventário divergentes')
    occ = inv['ocorrencias']
    exigir(len(occ) == 11397 and len({x['id'] for x in occ}) == len(occ), 'ocorrências divergentes ou IDs repetidos')
    exigir({x['id'] for x in changes} == set(TIPOS) and len(changes) == len(TIPOS), 'conjunto de deltas incompleto')
    by_config = {x['id']: x for x in cfg['edicoes']}
    exigir(set(by_config) == set(TIPOS), 'configuração divergente')
    rows = []
    for change in changes:
        label = change['id']; spec = by_config[label]
        exigir(all(change[k] == spec[k] for k in ('documento','original','candidata','original_sha256','candidata_sha256')),
               f'{label}: configuração e deltas divergentes')
        path = change['documento']; html16 = docs[path].decode('utf-8').encode('utf-16-le')
        start, end = change['inicio_novo'], change['fim_novo']
        piece = html16[start*2:end*2].decode('utf-16-le').encode('utf-8')
        candidate = (ROOT / change['candidata']).read_bytes().removesuffix(b'\n')
        exigir(piece == candidate and digest(piece) == change['candidata_sha256'], f'{label}: fragmento divergente')
        exigir(docs[path].count(candidate) == 1, f'{label}: candidata não é única no documento')
        matches = [(i,o) for i,o in enumerate(occ) if o['arquivo'] == path and o['inicio_utf16'] == start
                   and o['fim_utf16'] == end and o['tipo'] == TIPOS[label]]
        exigir(len(matches) == 1, f'{label}: identidade ambígua ou ausente')
        index, item = matches[0]
        if label == 'resumo':
            exigir(piece.startswith(b'<li>') and piece.endswith(b'</li>'), 'resumo não é li simples')
            inventory_hash = digest(piece[4:-5])
        else:
            inventory_hash = digest(piece)
        exigir(inventory_hash == item['sha256_fragmento'], f'{label}: hash de ocorrência divergente')
        rows.append({'colecao':'ocorrencias','indice_base_zero':index,'id_inventario':item['id'],
                     'id_edicao':label,'arquivo':path,'secao':item.get('secao'),'ancora':item.get('ancora'),
                     'tag':item['tag'],'tipo':item['tipo'],'inicio_utf16':start,'fim_utf16':end,
                     'sha256_ocorrencia':inventory_hash,'sha256_fragmento_html':digest(piece),
                     'estado':'conferido_no_escopo_localizado',
                     'alcance':'A alteração identificada neste bloco foi examinada no parecer; não abrange automaticamente todas as afirmações, filhos, ancestrais, fontes ou dependências.',
                     'parecer':PARECER,'parecer_sha256':PARECER_SHA})
    counts = {k:len(inv[k]) for k in ('ocorrencias','referencias','recursos','ativos_especificos','artigos_excluidos')}
    exigir(counts == {'ocorrencias':11397,'referencias':815,'recursos':138,'ativos_especificos':6,'artigos_excluidos':197},
           'contagens do inventário divergentes')
    return {'versao':'r9-parcial-r1','data':'2026-10-30','estado_global':'QA09_EM_CORRECAO_NAO_APROVADO',
            'fotografia':{'inventario':INV,'inventario_sha256':INV_SHA,'documentos':DOCUMENTOS},
            'fontes':{'configuracao':CONFIG,'configuracao_sha256':CONFIG_SHA,'edicoes':EDICOES,
                      'edicoes_sha256':EDICOES_SHA,'parecer':PARECER,'parecer_sha256':PARECER_SHA},
            'regra_padrao':'Pendente de integração neste ledger, não afirma que faltem revisões históricas. Não herdar aprovação entre nós, coleções, dependências ou versões. Mudanças da fotografia exigem reconciliação e revisão.',
            'colecoes':{k:{'quantidade_fotografia':v,'estado_sem_registro':'pendente',
                             'identidade':('Índice base zero e campos da ocorrência na fotografia r9, incluindo documento, seção, âncora, posição e hash.' if k == 'ocorrencias' else 'Índice base zero e todos os metadados do registro na coleção fixada pela fotografia r9.')}
                        for k,v in counts.items() if k != 'artigos_excluidos'},
            'artigos_ban08':{'quantidade_identificada':197,'tratamento':'Segregados; evidências BAN-08 não são automaticamente cobertura QA-09.'},
            'estados_permitidos':['pendente','conferido_no_escopo_localizado','nao_aplicavel_justificado','achado_aberto'],
            'registros_explicitamente_revisados':rows,
            'limites':['Somente os oito deltas revalidados no parecer r9 estão representados; os demais registros permanecem pendentes de integração.',
                       'O registro de um bloco não aprova automaticamente nós internos nem todo o bloco; o alcance é o definido pelo parecer.',
                       'As contagens se sobrepõem, não são contagem de cálculos nem percentual de progresso.',
                       'Referências, recursos, ativos e registros históricos de outras versões não são automaticamente classificados.',
                       'Não demonstra teste em navegador real, revisão humana, aprendizagem nem aceite integral QA-09.']}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verificar', metavar='ARQUIVO')
    args = parser.parse_args()
    try:
        result = construir()
        if args.verificar:
            saved = json.loads(Path(args.verificar).read_text(encoding='utf-8'))
            exigir(saved == result, 'ledger não corresponde à reprodução atual')
            print(json.dumps({'ok':True,'registros_localizados':len(result['registros_explicitamente_revisados']),
                              'colecoes':{k:v['quantidade_fotografia'] for k,v in result['colecoes'].items()},
                              'qa09':'em correção'}, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, UnicodeError) as error:
        print(f'ERRO: {error}', file=sys.stderr)
        sys.exit(1)
