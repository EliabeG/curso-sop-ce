from pathlib import Path
import json,subprocess,tempfile
D=Path('auditoria/termodinamica/evidencias/QA-09/inventario-integracao-r30-r1');data=json.loads((D/'ledger.json').read_text())
def id_ocorrencia(x): x['ocorrencias'][0]['id']='falso'
def omissao(x): x['ocorrencias'].pop()
def grupo(x): x['ocorrencias'][0]['grupo_id']=999999
def promocao(x): x['ocorrencias'][0]['estado_triagem']='juizo_local_documentado'
def apoio(x): x['ocorrencias'][next(i for i,v in enumerate(x['ocorrencias']) if v['apoio'])]['apoio']['objeto']='falso'
def referencia(x): x['referencias'][0]['estado_triagem']='aprovado'
def recurso(x): x['recursos'][0]['sha256_recurso']='0'*64
def ativo(x): x['ativos_especificos'][0]['estado_triagem']='aprovado'
def artigo(x): x['artigos_excluidos'].pop()
for f in (id_ocorrencia,omissao,grupo,promocao,apoio,referencia,recurso,ativo,artigo):
 x=json.loads(json.dumps(data));f(x)
 with tempfile.NamedTemporaryFile(mode='w',suffix='.json') as out:
  json.dump(x,out);out.flush();p=subprocess.run(['node',str(D/'gerar.mjs'),'--verificar',out.name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  assert p.returncode!=0,f.__name__
 print(f.__name__+': mutação em cópia rejeitada')
