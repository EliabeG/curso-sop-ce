import fs from 'node:fs';
import vm from 'node:vm';
import {parseHtml, sha256, decodeHtml} from '../../../inventario/validar-inventario.mjs';
const dir='auditoria/termodinamica/evidencias/BAN-07/propostas-r2/';
const source=fs.readFileSync('modulos/e1-termodinamica.html','utf8');
const doc=parseHtml(source);
const specs=[
 {n:'62',digital:'ed91f6ac',hash:'3afa637b59ec0aa48e6885ab0877b0ed1bada0bcebe86c841d221e1559235148',edits:[
 ['válvulas ausentes porque não há diferença de pressão.','admissão aberta somente quando a pressão na câmara supera a pressão da linha de sucção, e descarga fechada.'],
 ['A descrição informa entrada de gás e condições que permitem a abertura da admissão.','Na admissão normal com válvula automática, a pressão da linha de sucção deve superar a pressão na câmara para abrir a admissão; inverter o diferencial não explica a entrada descrita.']]},
 {n:'69',digital:'13da8621',hash:'f1ade775126752789740119acdb33f04190299cc54d46883e4e0354d7c6e6fee',edits:[
 ['Em um trocador com fluidos separados por uma parede metálica, o caminho térmico do fluido quente até o fluido frio envolve, nessa ordem,','Em um trocador com duas correntes de fluidos escoando, separadas por uma parede metálica, o caminho térmico do fluido quente até o fluido frio envolve, nessa ordem,'],
 ['somente mistura das duas correntes.','convecção nos dois lados, sem condução de calor através da parede por ser metálica.'],
 ['As correntes foram especificadas como separadas pela parede.','O metal pode oferecer baixa resistência térmica, mas o calor atravessa a parede por condução. Boa condutividade não elimina esse mecanismo.']]}
];
const js=fs.readFileSync('assets/curso.js','utf8');
const names=['normalizarDigital','textoDaDigital','fnv1a','digitalDoBanco'];
const code=names.map(n=>{const x=js.match(new RegExp('  function '+n+'\\([^]*?\\n  \\}')); if(!x)throw Error(n);return x[0]}).join('\n');
const context={SEPARADOR:'␞',paraArray:x=>Array.from(x)};
vm.createContext(context); vm.runInContext(code+'\nthis.digitalDoBanco=digitalDoBanco;',context);
function item(html,n){
 const parsed=parseHtml(html); if(parsed.errors.length)throw Error(parsed.errors.join(';'));
 const id='av-e1-'+n; const article=parsed.ids.get(id)[0];
 const text=x=>decodeHtml(html.slice(x.openEnd,x.end).replace(/<[^>]*>/g,''));
 const entry=parsed.ids.get(id+'-enunciado')[0];
 const nodeText=t=>({nodeType:3,nodeValue:t});
 const en={nodeType:1,localName:'div',childNodes:[nodeText(text(entry))],querySelectorAll:()=>[]};
 const radios=['A','B','C','D','E'].map(letter=>{const input=parsed.ids.get(id+'-'+letter)[0]; return {value:input.attrs.value,closest:()=>({nodeType:1,localName:'label',childNodes:[nodeText(text(input.parent))]})}});
 return {dataset:{crGabarito:article.attrs['data-cr-gabarito']},querySelector:()=>en,querySelectorAll:()=>radios};
}
const resultados=[];
for(const spec of specs){
 const node=doc.ids.get('av-e1-'+spec.n)[0], original=source.slice(node.start,node.end);
 const candidate=fs.readFileSync(dir+'AV'+spec.n+'-candidata.html','utf8');
 let reversed=candidate; for(const [old,novo] of [...spec.edits].reverse()){if(reversed.split(novo).length!==2)throw Error('Texto candidato ausente/repetido '+spec.n);reversed=reversed.replace(novo,old)}
 if(reversed!==original||sha256(original)!==spec.hash)throw Error('Delta inesperado '+spec.n);
 const before=context.digitalDoBanco(item(original,spec.n)),after=context.digitalDoBanco(item(candidate,spec.n));
 if(before!==spec.digital||before===after)throw Error('Digital divergente '+spec.n);
 resultados.push({item:'AV'+spec.n,artigo_r1:sha256(original),candidato:sha256(candidate),bytes_candidato:Buffer.byteLength(candidate),digital_r1:before,digital_candidato:after});
}
const sources=['modulos/e1-termodinamica.html','auditoria/termodinamica/inventario/inventario-questoes.json','auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md','assets/curso.js','assets/registro.js'];
const expected=['de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80','7d35b07b31c7faa13eb3f98a8c73c3a9bd1c2cf146534464dfdd202e0074e4a7','dba046a5781f6bb82fef14b52af8f3285063c815b130f580edc817e9bd589fb1','a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13','46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c'];
const produto=sources.map((arquivo,i)=>({arquivo,sha256:sha256(fs.readFileSync(arquivo)),esperado:expected[i]}));
if(produto.some(x=>x.sha256!==x.esperado))throw Error('Produto r1 alterado');
console.log(JSON.stringify({resultados,produto},null,2));
