from pathlib import Path
import json,subprocess,tempfile
D=Path('auditoria/termodinamica/evidencias/QA-09/ledger-r28-parcial-r2');data=json.loads((D/'ledger.json').read_text())
def xhash(x): x['objetos'][0]['r28']['sha256']='0'*64
def pos(x): x['objetos'][1]['r28']['inicio_utf16']+=1
def rem(x): x['objetos'].pop()
def pend(x): x['colecoes']['referencias']['estado_padrao']='aprovado'
def contexto(x): x['objetos'][18]['contextos'][0]['sha256_r28']='0'*64
def mapa(x): x['objetos'][0]['par_inventario']['id_r28']='falso'
def juizo(x): x['objetos'][0]['juizo']['juizo_local']='aprovado sem exame'
for f in (xhash,pos,rem,pend,contexto,mapa,juizo):
 x=json.loads(json.dumps(data));f(x)
 with tempfile.NamedTemporaryFile(mode='w',suffix='.json') as out:
  json.dump(x,out);out.flush();p=subprocess.run(['node',str(D/'ledger.mjs'),'--verificar',out.name],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  assert p.returncode!=0,f.__name__
 print(f.__name__+': mutação em cópia rejeitada')
