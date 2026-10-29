import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {validateInventory} from '../../inventario/validar-inventario.mjs';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
export async function testarPdf(){
  const original=JSON.parse(await fs.readFile(root+'auditoria/termodinamica/inventario/inventario-questoes.json','utf8'));
  const pdf='downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf';
  const html='modulos/e1-termodinamica.html';
  const cases=[
    ['PDF com página positiva',pdf+'#page=3',true,null],
    ['PDF com fragmento permitido codificado',pdf+'#page%3D3',true,null],
    ['PDF sem fragmento',pdf,true,null],
    ['PDF com query e página',pdf+'?versao=1#page=3',true,null],
    ['PDF com página zero',pdf+'#page=0',false,'fragmento PDF inválido'],
    ['PDF com página não numérica',pdf+'#page=tres',false,'fragmento PDF inválido'],
    ['PDF com página negativa',pdf+'#page=-3',false,'fragmento PDF inválido'],
    ['PDF com fração',pdf+'#page=3.5',false,'fragmento PDF inválido'],
    ['PDF com inteiro inseguro',pdf+'#page=9007199254740992',false,'fragmento PDF inválido'],
    ['PDF com fragmento arbitrário',pdf+'#secao',false,'fragmento PDF inválido'],
    ['R1-A: PDF com segundo # e sufixo',pdf+'#page=3#extra',false,'fragmento PDF inválido'],
    ['R1-A: PDF com segundo # vazio',pdf+'#page=3#',false,'fragmento PDF inválido'],
    ['PDF com segundo # codificado e sufixo',pdf+'#page=3%23extra',false,'fragmento PDF inválido'],
    ['PDF com segundo # codificado vazio',pdf+'#page=3%23',false,'fragmento PDF inválido'],
    ['Arquivo PDF ausente','downloads/termodinamica/provas/ausente-fon09.pdf#page=3',false,'arquivo inacessível'],
    ['Âncora HTML existente',html+'#fundamentos',true,null],
    ['Âncora HTML ausente',html+'#ausente-fon09',false,'âncora ausente ou duplicada'],
    ['HTML com fragmento completo inexistente',html+'#fundamentos#extra',false,'âncora ausente ou duplicada'],
    ['HTML com fragmento completo codificado inexistente',html+'#fundamentos%23extra',false,'âncora ausente ou duplicada'],
    ['Outro recurso não recebe exceção PDF','assets/termodinamica/fon09-cr68-dados-v1.json#page=3',false,'âncora ausente ou duplicada']
  ];
  const resultados=[];
  for(const[nome,url,esperado,erro]of cases){
    const inv=structuredClone(original);inv.itens.find(x=>x.id==='cr-e1-68').origem.fontes.push({rotulo:'Fixture r2 em memória',url});
    const result=await validateInventory({rootDir:root,inventory:inv});
    resultados.push({nome,referencia:url,esperado_ok:esperado,observado_ok:result.ok,passou:result.ok===esperado&&(!erro||result.erros.some(x=>x.includes(erro))),erros:result.erros});
  }
  return {ok:resultados.every(x=>x.passou),total:resultados.length,resultados,limite:'PDF: sintaxe integral page=N inteiro positivo seguro e arquivo existente; não verifica quantidade real de páginas. Nenhum fixture modifica o produto.'};
}
