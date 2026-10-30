import fs from 'node:fs';
import assert from 'node:assert/strict';
import {parseHtml,sha256} from '../../../inventario/validar-inventario.mjs';
const d='auditoria/termodinamica/evidencias/QA-09/candidata-pressao-media-r28/';
const m=JSON.parse(fs.readFileSync(d+'manifesto.json','utf8'));
const h=fs.readFileSync(m.fonte,'utf8');
assert.equal(sha256(h),m.fonte_sha256);assert.equal(sha256(fs.readFileSync(m.inventario)),m.inventario_sha256);assert.equal(sha256(fs.readFileSync(m.parecer)),m.parecer_sha256);
const o=h.slice(m.inicio_utf16,m.fim_utf16);const c=fs.readFileSync(d+'candidata.html','utf8').replace(/\n$/,'');assert.equal(fs.readFileSync(d+'original.html','utf8'),o+'\n');assert.equal(sha256(o),m.original_sha256);assert.equal(sha256(c),m.candidata_sha256);
assert.equal(o.split(m.antes).length,2);assert.equal(o.replace(m.antes,m.depois),c);assert.equal(h.split(o).length,2);const out=h.replace(o,c);const before=parseHtml(h),after=parseHtml(out);assert.equal(before.errors.length,0);assert.equal(after.errors.length,0);
const capture=(s,re)=>[...s.matchAll(re)].map(x=>x[0]);for(const [name,re] of [['article',/<article\b[^>]*>[\s\S]*?<\/article>/g],['math',/<math\b[^>]*>[\s\S]*?<\/math>/g],['href',/\bhref="[^"]*"/g],['id',/\bid="[^"]*"/g],['aria',/\baria-[\w-]+="[^"]*"/g]]){const x=capture(h,re),y=capture(out,re);assert.deepEqual(x,y,name);console.log(name,x.length)}
assert.equal(200/.010,20000);assert.equal(.005*10000+.005*30000,200);console.log(JSON.stringify({ok:true,html_hipotetico_sha256:sha256(out),bloco_candidato_sha256:sha256(c),gravado:false}));
