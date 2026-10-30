import fs from 'node:fs';
import crypto from 'node:crypto';
const root='auditoria/termodinamica/evidencias/QA-09/';
const html=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const inv=JSON.parse(fs.readFileSync(root+'inventario-r18.json','utf8'));
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
if(sha(html)!=='7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca') throw Error('base mudou');
const ids=[117,639,640,641,642,643,644].map(i=>{const x=inv.referencias[i];const fragmento=html.slice(x.inicio_utf16,x.fim_utf16);if(!fragmento.startsWith('<a ')||!fragmento.endsWith('</a>')||!fragmento.includes(x.valor)) throw Error(`identidade ${i}`);return {indice:i,...x,sha256_elemento:sha(fragmento)};});
const out=JSON.stringify({base_sha256:sha(html),inventario_sha256:sha(fs.readFileSync(root+'inventario-r18.json')),identidades:ids},null,2)+'\n';
const file=root+'referencias-ashrae-banca-r18-20261030/identidades.json';
if(process.argv.includes('--criar')){if(fs.existsSync(file))throw Error('já existe');fs.writeFileSync(file,out);}else{if(fs.readFileSync(file,'utf8')!==out)throw Error('manifesto diverge');console.log('ok: 7 identidades exatas');}
