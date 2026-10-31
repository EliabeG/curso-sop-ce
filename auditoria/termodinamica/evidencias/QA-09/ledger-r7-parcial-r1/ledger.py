#!/usr/bin/env python3
"""QA-09: fotografia esparsa. Padrão: gera para stdout. --verificar ARQUIVO compara o ledger salvo sem sobrescrever históricos."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import argparse,json,sys

BASE=Path('.')
INV='auditoria/termodinamica/evidencias/QA-09/inventario-r7.json'
HTML='modulos/e1-termodinamica.html'
INV_SHA='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
HTML_SHA='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
MAP='auditoria/termodinamica/pareceres/QA-09-mapa-independente-r1.json'
MAP_SHA='892b63067b87316009a89a8553e8288a9bc51c2c66929b33a4fd19d927d2ede9'
REV1='auditoria/termodinamica/pareceres/QA-09-aplicacao-exemplos-011-013-auditoria-independente-r1.md'
REV1_SHA='30971b46f9ffe605dd355d2b5b244ef9ef6e806a4d9292759985db167ca62471'
REV2='auditoria/termodinamica/pareceres/QA-09-exemplos-021-030-auditoria-independente-r1.md'
REV2_SHA='e9ebf7ffcb7a3a6325e6aac93efabac08b3ede3b96c736d23e3426182c43ac74'

def read_sha(path,expected):
 data=(BASE/path).read_bytes(); actual=sha256(data).hexdigest()
 if actual!=expected: raise ValueError(f'{path}: SHA-256 esperado {expected}, encontrado {actual}; pare e reconcilie')
 return data

def build():
 raw=read_sha(INV,INV_SHA); inv=json.loads(raw); html=read_sha(HTML,HTML_SHA); mapa=json.loads(read_sha(MAP,MAP_SHA));read_sha(REV1,REV1_SHA);read_sha(REV2,REV2_SHA)
 assert inv['estado']=='PENDENTE_DE_TRIAGEM_E_RECALCULO'
 occurrences=inv['ocorrencias']; ids=[o['id'] for o in occurrences]; assert len(ids)==len(set(ids))
 for entry in inv['documentos']:
  read_sha(entry['arquivo'],entry['sha256'])
 selected=[('EX-011','8ec6ce4013a1be49c569b5e3b8ab5e80b899cb9d250396be6023b1eecfa2d3c9',REV1,REV1_SHA),('EX-013','7438f121e00f4c757b695c3de6f881d295128696b48bad8f5d387b0e6547dfea',REV1,REV1_SHA)]
 for item in mapa['exemplos'][20:30]: selected.append((item['id_mapa'],item['sha256_fragmento_html'],REV2,REV2_SHA))
 source=html.decode('utf-8').encode('utf-16-le');rows=[]
 for label,digest,review,review_sha in selected:
  found=[(i,o) for i,o in enumerate(occurrences) if o.get('arquivo')==HTML and o.get('secao') in ('energia','segunda-lei','ciclos') and o.get('tipo')=='exemplo_ou_diagnostico' and o.get('sha256_fragmento')==digest]
  if len(found)!=1: raise ValueError(f'{label}: identidade não única, {len(found)} ocorrências')
  i,o=found[0]; piece=source[2*o['inicio_utf16']:2*o['fim_utf16']].decode('utf-16-le').encode('utf-8')
  if sha256(piece).hexdigest()!=digest: raise ValueError(f'{label}: fragmento divergente')
  rows.append({'colecao':'ocorrencias','indice_base_zero':i,'id_inventario':o['id'],'id_historico':label,'arquivo':o['arquivo'],'secao':o['secao'],'ancora':o['ancora'],'inicio_utf16':o['inicio_utf16'],'fim_utf16':o['fim_utf16'],'sha256_fragmento':digest,'estado':'conferido_no_escopo_localizado','alcance':'Cálculos e modelos do bloco conforme parecer; não abrange nós ancestrais, filhos, figuras, referências ou recursos automaticamente.','parecer':review,'parecer_sha256':review_sha})
 counts={k:len(inv[k]) for k in ('ocorrencias','referencias','recursos','ativos_especificos','artigos_excluidos')}
 return {'versao':'r7-parcial-r1','data':'2026-10-30','estado_global':'QA09_EM_CORRECAO_NAO_APROVADO','fotografia':{'inventario':INV,'inventario_sha256':INV_SHA,'documentos':inv['documentos']},'regra_padrao':'Cada elemento em cada coleção está pendente de integração neste ledger, exceto para a identidade, escopo e versão do registro explícito correspondente; ausência de registro não afirma que nenhuma revisão histórica exista. Não herdar aprovação por nó ancestral ou filho, hash igual, outra coleção, outra versão ou alegada semelhança. Qualquer mudança de fonte, inventário ou parecer encerra validade desta fotografia e exige reconciliação e revisão de impacto.','colecoes':{k:{'quantidade_fotografia':v,'estado_sem_registro':'pendente','identidade':'índice base zero na coleção do inventário fixado por SHA-256; para ocorrências conferir também id, arquivo, seção, âncora, posição e hash do fragmento; para referências e recursos confrontar todos os metadados do registro','regras':'Não agregar contagens de coleções sobrepostas nem interpretá-las como número de cálculos.'} for k,v in counts.items() if k!='artigos_excluidos'},'artigos_ban08':{'quantidade_identificada':counts['artigos_excluidos'],'tratamento':'Identificadores segregados do inventário QA-09 e sujeitos às evidências próprias de BAN-08; não são cobertura de QA-09 nem autorizam transferência automática de aceites.'},'estados_permitidos':['pendente','conferido_no_escopo_localizado','nao_aplicavel_justificado','achado_aberto'],'registros_explicitamente_revisados':rows,'limites':['Estas linhas não encerram QA-09; registram apenas o escopo localizado dos pareceres vinculados.','Referências, recursos e ativos têm coleções separadas e permanecem pendentes aqui; não implica que sejam atividades adicionais.','Os registros do inventário se sobrepõem e não contam contas distintas.','Este arquivo não comprova testes em navegador, revisão humana, eficácia ou aprendizagem.']}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--verificar',metavar='ARQUIVO');args=parser.parse_args()
 try:
  result=build()
  if args.verificar:
   saved=json.loads(Path(args.verificar).read_text(encoding='utf-8'))
   if saved!=result: raise ValueError('ledger salvo difere da reprodução a partir da fotografia e dos pareceres')
   print(json.dumps({'ok':True,'registros_auditados':len(result['registros_explicitamente_revisados']),'colecoes':{k:v['quantidade_fotografia'] for k,v in result['colecoes'].items()},'qa09':'em correção'},ensure_ascii=False,indent=2))
  else: print(json.dumps(result,ensure_ascii=False,indent=2))
 except (OSError,ValueError,KeyError,AssertionError) as error:
  print(f'ERRO: {error}',file=sys.stderr);sys.exit(1)
