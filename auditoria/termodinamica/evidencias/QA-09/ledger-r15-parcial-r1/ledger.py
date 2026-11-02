#!/usr/bin/env python3
"""Fotografia parcial r15; somente leitura, gerador em stdout ou comparador."""
import argparse, hashlib, json, sys
from pathlib import Path

Q = Path('auditoria/termodinamica/evidencias/QA-09')
INV = Q/'inventario-r15.json'
PARECER = Path('auditoria/termodinamica/pareceres/QA-09-aplicacao-wika-r15-auditoria-independente-20261030.md')
ENTREGA = Q/'aplicacao-wika-r15-r1/entrega-r1.md'
FOTOS = {
 'modulos/e1-termodinamica.html':'f6c461f1d6039ea47dc7e97f9ad734bb0ea3fcb902f01ffdbf18d18d88e08d0e',
 'formulas/termodinamica.html':'3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce',
 str(INV):'c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c',
 str(PARECER):'711c80a65248c1bc160f01abb15ab6d0718d8f43af7638bc618542d4fa5af278',
 str(ENTREGA):'92741203699f138eecce7631f405862d7736e6bd623656847c9fd116176583b6'
}
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p):
 b=Path(p).read_bytes()
 if sha(b)!=FOTOS[str(p)]: raise ValueError('SHA divergente: '+str(p))
 return b
def exigir(c,m):
 if not c: raise ValueError(m)
def construir():
 for p in FOTOS: read(p)
 inv=json.loads(read(INV)); collections=['ocorrencias','referencias','recursos','ativos_especificos']
 expected=[11399,816,138,6]
 exigir([len(inv[c]) for c in collections]==expected,'contagens divergentes')
 target='https://www.wika.com/pt-br/111_16_111_26.WIKA'
 matches=[(i,x) for i,x in enumerate(inv['referencias']) if x['valor']==target]
 exigir(len(matches)==1,'referência WIKA não é única')
 i,x=matches[0]; exigir(x['arquivo']=='modulos/e1-termodinamica.html' and x['secao']=='fontes' and x['tag']=='a' and x['texto']=='WIKA — manômetro de tubo Bourdon','identidade WIKA divergente')
 utf16=read(x['arquivo']).decode('utf-8').encode('utf-16-le')
 frag=utf16[x['inicio_utf16']*2:x['fim_utf16']*2].decode('utf-16-le')
 exigir('href="'+target+'"' in frag and x['texto'] in frag,'fragmento WIKA divergente')
 verdict=read(PARECER).decode('utf-8'); exigir('APROVADA ISOLADAMENTE' in verdict and FOTOS['modulos/e1-termodinamica.html'] in verdict,'parecer incompatível')
 return {'versao':'r15-parcial-r1','data':'2026-10-30','estado_global':'QA09_EM_CORRECAO_NAO_APROVADO',
   'fotografia':{p:h for p,h in FOTOS.items() if p not in (str(PARECER),str(ENTREGA))},
   'colecoes':{c:{'total':n,'estado_padrao':'pendente_de_integracao'} for c,n in zip(collections,expected)},
   'registros_explicitamente_revisados':[{'colecao':'referencias','indice_base_zero':i,'identidade_r15':x,
      'fragmento_sha256':sha(frag.encode('utf-8')),'estado':'conferido_no_escopo_localizado',
      'escopo':'Identidade da troca, rótulo e adequação da página WIKA para os modelos 111.16 e 111.26 e seu princípio Bourdon, conforme parecer. Não valida outras afirmações ou acessibilidade futura.',
      'parecer':str(PARECER),'parecer_sha256':FOTOS[str(PARECER)],'autor_parecer':'/root/planning',
      'entrega':str(ENTREGA),'entrega_sha256':FOTOS[str(ENTREGA)]}],
   'limites':['Todos os outros registros permanecem pendentes de integração, independentemente de revisão histórica.',
      'A classificação cobre exclusivamente a referência individual e o alcance do parecer; não se estende a ocorrências, recursos, ativos, pais ou filhos.',
      'Não há transferência automática a partir de r9, mapas ou hash igual; revisões anteriores permanecem no histórico.',
      'As coleções se sobrepõem, não são contagens de cálculos nem um percentual de conclusão.',
      'Os 197 artigos têm tratamento separado; sua preservação estrutural não aprova o restante de QA-09.']}
if __name__=='__main__':
 parser=argparse.ArgumentParser(); parser.add_argument('--verificar',metavar='ARQUIVO'); args=parser.parse_args()
 try:
  data=construir()
  if args.verificar:
   exigir(json.loads(Path(args.verificar).read_text(encoding='utf-8'))==data,'ledger salvo divergente')
   print(json.dumps({'ok':True,'registros_integrados':len(data['registros_explicitamente_revisados']),'padrao':'pendente_de_integracao','qa09':'em correção'},ensure_ascii=False,indent=2))
  else: print(json.dumps(data,ensure_ascii=False,indent=2))
 except (OSError,ValueError,KeyError,UnicodeError) as e:
  print('ERRO: '+str(e),file=sys.stderr); sys.exit(1)
