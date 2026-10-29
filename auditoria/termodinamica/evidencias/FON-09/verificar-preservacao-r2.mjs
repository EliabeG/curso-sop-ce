import fs from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const root=fileURLToPath(new URL('../../../../',import.meta.url));
const dir='auditoria/termodinamica/evidencias/FON-09/';
const sha=x=>createHash('sha256').update(x).digest('hex');
export async function verificarPreservacao(){
  const checks=[];const check=(nome,ok)=>{checks.push({nome,ok});if(!ok)throw new Error(nome);};
  const manifestBytes=await fs.readFile(root+dir+'manifesto-r1.json');
  check('manifesto r1 imutável',sha(manifestBytes)==='d054c3eb9a8337c59959eed9e78c2028b9e2c68f36293e3ed8076a3c01fd2b4d');
  const m=JSON.parse(manifestBytes);
  for(const f of m.arquivos){
    check('pacote r1 '+f.arquivo,sha(await fs.readFile(root+f.copia))===f.sha256);
    if(!f.arquivo.endsWith('/validar-inventario.mjs'))check('produto científico preservado '+f.arquivo,sha(await fs.readFile(root+f.arquivo))===f.sha256);
  }
  for(const e of m.evidencias)check('evidência r1 '+e.arquivo,sha(await fs.readFile(root+e.arquivo))===e.sha256);
  for(const b of m.base)check('snapshot anterior '+b.arquivo,sha(await fs.readFile(root+b.copia))===b.sha256);
  const file='auditoria/termodinamica/inventario/validar-inventario.mjs';
  const old=await fs.readFile(root+dir+'pacote-r1/'+file,'utf8'),now=await fs.readFile(root+file,'utf8');
  const antes="      const [beforeHash, rawFragment] = reference.split('#');";
  const depois="      const hashIndex = reference.indexOf('#');\n      const beforeHash = hashIndex === -1 ? reference : reference.slice(0, hashIndex);\n      const rawFragment = hashIndex === -1 ? undefined : reference.slice(hashIndex + 1);";
  check('delta exclusivo no corte do fragmento',old.split(antes).length===2&&old.replace(antes,depois)===now);
  check('guia sem alteração',sha(await fs.readFile(root+'auditoria/termodinamica/inventario/LEIA-ME.md'))==='cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449');
  return {ok:true,verificacoes:checks.length,checks,delta:{arquivo:file,antes,depois,sha256_antes:sha(old),sha256_depois:sha(now)},limite:'Ciência herdada do exame r1 por identidade dos quatro arquivos; nenhuma reconsulta física ou teste de navegador reexecutado.'};
}
