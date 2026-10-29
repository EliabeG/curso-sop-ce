import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {validateInventory} from '../../inventario/validar-inventario.mjs';
const hash=bytes=>crypto.createHash('sha256').update(bytes).digest('hex');
export async function verificarR2(rootDir){
 const base='auditoria/termodinamica/evidencias/BAN-02/';
 const read=async f=>JSON.parse(await fs.readFile(path.join(rootDir,f),'utf8'));
 const r1=await read(base+'pacote-r1/inventario-questoes.json');
 const r2=await read('auditoria/termodinamica/inventario/inventario-questoes.json');
 const manifest=await read(base+'manifesto-r1.json');
 const checks=[];
 const check=(nome,ok)=>checks.push({nome,ok});
 const diffs=[];
 function diff(a,b,p){if(JSON.stringify(a)===JSON.stringify(b))return;
 if(a&&b&&typeof a==='object'&&typeof b==='object'&&!Array.isArray(a)&&!Array.isArray(b)){
 for(const k of new Set([...Object.keys(a),...Object.keys(b)]))diff(a[k],b[k],p+'.'+k);
 }else diffs.push({campo:p,antes:a,depois:b});}
 diff(r1.metodo,r2.metodo,'metodo');
 check('Mesmos IDs e ordem',JSON.stringify(r1.itens.map(x=>x.id))===JSON.stringify(r2.itens.map(x=>x.id)));
 for(const item of r1.itens)diff(item,r2.itens.find(x=>x.id===item.id),item.id);
 const allowed=d=>{const id=d.campo.split('.')[0],field=d.campo.slice(id.length+1);
 return id==='metodo'||(/^av-e1-\d+$/.test(id)&&field==='pre_requisitos')||
 (['q-e1-16','cr-e1-45','av-e1-45'].includes(id)&&/^(exposicao_previa\.relacoes|raciocinio\.etapas|hipoteses\.explicitadas|vinculo_competencias\.alcance)/.test(field))||
 (['cr-e1-09','cr-e1-24','cr-e1-79'].includes(id)&&/^(nivel\.|raciocinio\.|competencias$|pre_requisitos$|vinculo_competencias\.)/.test(field))||
 (id==='av-e1-57'&&field==='hipoteses.explicitadas');};
 check('Diferenças restritas aos quatro achados',diffs.every(allowed));
 const byId=id=>r2.itens.find(x=>x.id===id);
 for(const id of ['q-e1-16','cr-e1-45','av-e1-45'])check('R1-A sem unidade J indevida em '+id,!/(?:1000|500)\s*J\b/.test(JSON.stringify(byId(id))));
 check('R1-A CR42 preservada integralmente',JSON.stringify(byId('cr-e1-42'))===JSON.stringify(r1.itens.find(x=>x.id==='cr-e1-42')));
 for(const id of ['cr-e1-09','cr-e1-24','cr-e1-79']){
  const it=byId(id),old=r1.itens.find(x=>x.id===id);
  check('R1-B nível e etapa em '+id,it.nivel.estimado==='iniciante'&&it.raciocinio.numero_etapas===1);
  check('R1-B ressalvas preservadas em '+id,JSON.stringify(it.hipoteses)===JSON.stringify(old.hipoteses)&&JSON.stringify(it.revisao)===JSON.stringify(old.revisao));
 }
 const pre=await read(base+'pre-requisitos-r2.json');
 check('R1-C 80 revisões com antes/depois concordantes',pre.itens.length===80&&pre.itens.every(x=>JSON.stringify(x.depois)===JSON.stringify(byId(x.id).pre_requisitos)&&JSON.stringify(x.antes)===JSON.stringify(r1.itens.find(i=>i.id===x.id).pre_requisitos)));
 check('R1-D hipóteses Brayton e calores constantes',byId('av-e1-57').hipoteses.explicitadas.includes('Ciclo Brayton ideal')&&byId('av-e1-57').hipoteses.explicitadas.includes('Calores específicos constantes'));
 const levelCounts={};for(const it of r2.itens)levelCounts[it.nivel.estimado]=(levelCounts[it.nivel.estimado]||0)+1;
 check('Estatísticas atualizadas',levelCounts.iniciante===171&&levelCounts.intermediario===19&&!levelCounts.avancado);
 const preserved=[];
 for(const f of manifest.arquivos.filter(x=>x.arquivo.startsWith(base))){const actual=hash(await fs.readFile(path.join(rootDir,f.arquivo)));preserved.push({arquivo:f.arquivo,sha256:actual,preservado:actual===f.sha256});}
 check('Toda evidência r1 do manifesto permanece imutável',preserved.every(x=>x.preservado));
 const integrity=await read(base+'verificacao-r1.json');
 const product=[];for(const f of integrity.integridade){const actual=hash(await fs.readFile(path.join(rootDir,f.arquivo)));product.push({arquivo:f.arquivo,sha256:actual,preservado:actual===f.sha256});}
 check('Produto aprovado preservado',product.every(x=>x.preservado));
 const validation=await validateInventory({rootDir});check('Validador canônico sem erros',validation.ok);
 return {id:'BAN-02',rodada:2,natureza:'Verificação do Corretor; não é parecer independente',ok:checks.every(x=>x.ok),checks,contagens:levelCounts,validacao:validation,produto:product,evidencias_r1:preserved,diferencas:diffs,limites:['Comparações estruturais e semânticas dirigidas aos quatro achados. A suficiência pedagógica dos pré-requisitos e classificações continua sujeita à revisão independente.','Sem nova auditoria de gabaritos, fontes oficiais ou aplicação com estudantes.']};
}
