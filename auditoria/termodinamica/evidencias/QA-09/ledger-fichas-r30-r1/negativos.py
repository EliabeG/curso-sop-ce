from pathlib import Path
import json,subprocess,tempfile
D=Path('auditoria/termodinamica/evidencias/QA-09/ledger-fichas-r30-r1');data=json.loads((D/'ledger.json').read_text())
def hash_ficha(x):x['fichas'][42]['versoes'][3]['sha256']='0'*64
def posicao(x):x['fichas'][83]['versoes'][3]['inicio_utf16']+=1
def omissao(x):x['fichas'].pop()
def fonte(x):x['fichas'][83]['parecer_original']['sha256']='0'*64
def contexto(x):x['fichas'][0]['contextos'][0]['sha256_r30']='0'*64
def mapa(x):x['fichas'][42]['versoes'][2]['ocorrencia_id']='falso'
def estado(x):x['colecoes']['referencias']['estado_padrao']='aprovado'
def juizo(x):x['fichas'][0]['juizo']['juizo_local']='aprovado sem exame'
for f in (hash_ficha,posicao,omissao,fonte,contexto,mapa,estado,juizo):
 x=json.loads(json.dumps(data));f(x)
 with tempfile.NamedTemporaryFile(mode='w',suffix='.json') as out:
  json.dump(x,out);out.flush();p=subprocess.run(['node',str(D/'ledger.mjs'),'--verificar',out.name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  assert p.returncode!=0,f.__name__
 print(f.__name__+': mutação em cópia rejeitada')
