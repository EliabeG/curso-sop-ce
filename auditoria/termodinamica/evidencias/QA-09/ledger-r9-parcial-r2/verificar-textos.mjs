// Leitura direta conforme a definição do inventário; não grava arquivos.
import fs from 'node:fs';
import {parseHtml, sha256} from '../../../inventario/validar-inventario.mjs';

const html = fs.readFileSync('modulos/e1-termodinamica.html', 'utf8');
const selection = JSON.parse(fs.readFileSync('auditoria/termodinamica/evidencias/QA-09/ledger-r9-parcial-r2/selecoes.json', 'utf8'));
const doc = parseHtml(html);
if (doc.errors.length) throw Error('Parser encontrou erros');
const textos = selection.registros.filter(x => x.colecao === 'ocorrencias' && x.identidade_r9.tipo === 'texto_direto');
for (const row of textos) {
  const o = row.identidade_r9;
  const matches = doc.nodes.filter(n => n.start === o.inicio_utf16 && n.end === o.fim_utf16 && n.tag === o.tag);
  if (matches.length !== 1) throw Error(`Identidade de nó ausente ou ambígua: ${row.id_local}`);
  const n = matches[0];
  let pos = n.openEnd, parts = [];
  for (const child of n.children) {
    if (child.start > pos) parts.push(html.slice(pos, child.start));
    pos = Math.max(pos, child.end);
  }
  if (n.end > pos) parts.push(html.slice(pos, n.end).replace(new RegExp(`</${n.tag}\\s*>\\s*$`, 'i'), ''));
  const actual = sha256(parts.join(' '));
  if (actual !== o.sha256_fragmento) throw Error(`Hash de texto direto divergente: ${row.id_local}`);
}
console.log(JSON.stringify({ok:true, textos_conferidos:textos.length}));
