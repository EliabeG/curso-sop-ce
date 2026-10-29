import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {validateInventory} from '../../inventario/validar-inventario.mjs';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
export async function testarPdf(){
  const original=JSON.parse(await fs.readFile(root+'auditoria/termodinamica/inventario/inventario-questoes.json','utf8'));
  const pdf='downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf';
  const cases=[
    ['PDF com página positiva',pdf+'#page=3',true,null],
    ['PDF com página zero',pdf+'#page=0',false,'fragmento PDF inválido'],
    ['PDF com página não numérica',pdf+'#page=tres',false,'fragmento PDF inválido'],
    ['PDF com fragmento arbitrário',pdf+'#secao',false,'fragmento PDF inválido'],
    ['Arquivo PDF ausente','downloads/termodinamica/provas/ausente-fon09.pdf#page=3',false,'arquivo inacessível'],
    ['Âncora HTML existente','modulos/e1-termodinamica.html#fundamentos',true,null],
    ['Âncora HTML ausente','modulos/e1-termodinamica.html#ausente-fon09',false,'âncora ausente ou duplicada'],
    ['Outro recurso não recebe exceção PDF','assets/termodinamica/fon09-cr68-dados-v1.json#page=3',false,'âncora ausente ou duplicada']
  ];
  const resultados=[];
  for(const[nome,url,esperado,erro]of cases){
    const inv=structuredClone(original);inv.itens.find(x=>x.id==='cr-e1-68').origem.fontes.push({rotulo:'Fixture em memória',url});
    const result=await validateInventory({rootDir:root,inventory:inv});
    resultados.push({nome,esperado_ok:esperado,observado_ok:result.ok,passou:result.ok===esperado&&(!erro||result.erros.some(x=>x.includes(erro))),erros:result.erros});
  }
  return {ok:resultados.every(x=>x.passou),total:resultados.length,resultados,limite:'PDF: sintaxe page=N inteiro positivo e arquivo existente; quantidade de páginas conferida documentalmente nos três PDFs, não por este validador. Nenhum fixture modifica o produto.'};
}
