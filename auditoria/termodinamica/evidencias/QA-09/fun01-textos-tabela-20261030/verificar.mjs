// QA-09 amostra: lê arquivos locais, não grava evidência.
import fs from 'node:fs';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';
const p='modulos/e1-termodinamica.html',h=fs.readFileSync(p,'utf8'), d=JSON.parse(fs.readFileSync('assets/termodinamica/fun01-dados-v1.json','utf8'));
const inv=JSON.parse(fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/inventario-r7.json','utf8'));
if(sha256(h)!=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f')throw Error('fotografia da aula divergente');
const expected={91881:'fad96cafcf88f056ff0a4e69d8fec891c08f407b953c0e692a0f3d69339aa915',92203:'965917bf4caf720957a9b406c4aecac6a7f7717cfe43e6293434c8f217388b5f',96357:'fea165532faadff44f4a29e76bc0daff6f7054b275cf607fedb20c793ed05314',102086:'681bee416847a9eebe2f7e7b8b70e366fe77c1e1699ecc87e256c24670922fe4',105052:'6388e81079087cf2f378761bfca7a28f20fafc5a9760cef081fd56387e3eec11',105534:'34a8181ae2f69e502d28b0d52df65b602fbe7f5490d8432d499781e7ae1b08a7',108659:'d7035a6ada3765be275f56a31c02e851224fa769333e379b3f5e507d91e6e2ca',114112:'83069e3d23f6c8e2a5f1f1d98cdf4df71e23980a0aa6ef3ef192bec67097f6e4',251734:'f658bff16dbeee7fc11fd8d69a8044e7734c99de81c94ca843827d1223a0b899'};
const nodes=parseHtml(h).nodes;
for(const [k, hash] of Object.entries(expected)){
 const pos=Number(k), found=inv.ocorrencias.filter(x=>x.arquivo===p&&x.inicio_utf16===pos&&x.tipo==='texto_direto');
 if(found.length!==1||found[0].sha256_fragmento!==hash)throw Error(`inventário ${k}`);
 const matches=nodes.filter(n=>n.start===pos);if(matches.length!==1)throw Error(`nó ${k}`);
 const n=matches[0];let q=n.openEnd,parts=[];for(const child of n.children){if(child.start>q)parts.push(h.slice(q,child.start));q=Math.max(q,child.end)}if(n.end>q)parts.push(h.slice(q,n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`,'i'),''));
 if(sha256(parts.join(' '))!==hash)throw Error(`hash trecho ${k}`);
}
const node=nodes.filter(n=>n.start===111716&&n.tag==='table');if(node.length!==1||sha256(h.slice(node[0].start,node[0].end))!=='f690a51e46e062591aed6c23d6c01527fe02ca30407caa2118acc964ce42d0dc')throw Error('tabela');
const ref=[{p_MPa:.1,T_C:99.606,vf_m3kg:.00104315,vg_m3kg:1.6939,hf_kJkg:417.50,hg_kJkg:2674.9},{p_MPa:.15,T_C:111.349,vf_m3kg:.00105273,vg_m3kg:1.1593,hf_kJkg:467.13,hg_kJkg:2693.1},{p_MPa:.2,T_C:120.210,vf_m3kg:.00106052,vg_m3kg:.88568,hf_kJkg:504.70,hg_kJkg:2706.2}];
if(JSON.stringify(d.agua_saturacao)!==JSON.stringify(ref))throw Error('JSON não corresponde aos dados esperados da tabela');
const near=(a,b,tol=1e-9)=>{if(Math.abs(a-b)>tol)throw Error(`aritmética ${a} ≠ ${b}`)};
near(.012/4,.003);near(3/(3+2),.6);near(1e-6/1e-3,.001);near(12-3,9);near(12+3,15);near(2*3-6,0);
const r=d.agua_saturacao[0];near(r.vf_m3kg+.2*(r.vg_m3kg-r.vf_m3kg),.33961452);near(r.hf_kJkg+.2*(r.hg_kJkg-r.hf_kJkg),868.98);
near(.25*400+.75*100,175);near(.75*400+.25*100,325);near(80*.25,20);near(160*.125,20);near(80*(1-.25),60);near(160*(1-.125),140);near(1/.004,250);near(d.agua_critico.T_K,647.096);near(d.agua_critico.p_MPa,22.064);
console.log(JSON.stringify({ok:true,textos_diretos:Object.keys(expected).length,tabelas:1,escopo:'ocorrências delimitadas; não é aprovação integral'}));
