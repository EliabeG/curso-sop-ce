import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseHtml, sha256 } from '../inventario/validar-inventario.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const audit = 'auditoria/termodinamica';
const read = name => fs.readFile(path.join(root, name));
const currentBytes = await read('modulos/e1-termodinamica.html');
const current = currentBytes.toString('utf8');
const currentDoc = parseHtml(current);
const inventory = JSON.parse(await read(`${audit}/inventario/inventario-questoes.json`));
const control = JSON.parse(await read(`${audit}/CONTROLE_AAA.json`));
const groups = [
  { id: 'FUN-01', rodada: 2, section: 'fun01-estado-equilibrio', prefix: 'fun01-', reports: ['FUN-01-r1.md', 'FUN-01-r2.md'] },
  { id: 'FUN-02', rodada: 1, section: 'fun02-diferenciais-caminhos', prefix: 'fun02-', reports: ['FUN-02-r1.md'] }
];
const extract = (html, doc, id) => {
  const nodes = doc.nodes.filter(n => n.attrs.id === id);
  if (nodes.length !== 1) throw new Error(`ID ausente ou duplicado: ${id}`);
  return html.slice(nodes[0].start, nodes[0].end);
};
const result = {
  id: 'BAN-07', data: '2026-10-28', responsavel: '/root, coordenador',
  tipo: 'Conferência de identidade e índice de alcance; não é parecer científico independente.',
  html_atual_sha256: sha256(currentBytes), grupos: [],
  limites: ['A decisão de herdar ciência e rubricas pertence ao Auditor principal.', 'Não se reivindica nova resolução dos problemas nem novo exame de fontes externas.', 'O HTML inteiro mudou desde os aceites; a identidade é demonstrada por unidade, artigo e recurso.']
};
for (const group of groups) {
  const accepted = control.itens.find(r => r.id === group.id);
  if (accepted.estado !== 'aprovado' || accepted.rodada !== group.rodada) throw new Error(`Estado inesperado: ${group.id}`);
  const packageDir = `${audit}/evidencias/${group.id}/pacote-r${group.rodada}`;
  const oldBytes = await read(`${packageDir}/modulos/e1-termodinamica.html`);
  if (sha256(oldBytes) !== accepted.hashes_aprovados['modulos/e1-termodinamica.html']) throw new Error(`Pacote histórico divergente: ${group.id}`);
  const old = oldBytes.toString('utf8');
  const oldDoc = parseHtml(old);
  const units = [group.section, ...inventory.itens.filter(r => r.id.startsWith(group.prefix)).map(r => r.id)];
  const components = units.map(id => {
    const before = extract(old, oldDoc, id), now = extract(current, currentDoc, id);
    return { id, tipo: id === group.section ? 'unidade_completa' : 'problema_com_solucao_e_rubrica', sha256_aprovado: sha256(before), sha256_atual: sha256(now), identico: before === now };
  });
  const resources = [];
  for (const [file, approvedHash] of Object.entries(accepted.hashes_aprovados).filter(([f]) => f.startsWith('assets/termodinamica/'))) {
    const [now, before] = await Promise.all([read(file), read(`${packageDir}/${file}`)]);
    resources.push({ arquivo: file, sha256_aprovado: approvedHash, sha256_copia: sha256(before), sha256_atual: sha256(now), identico: now.equals(before) && sha256(now) === approvedHash });
  }
  const reports = [];
  for (const file of group.reports) reports.push({ arquivo: `${audit}/pareceres/${file}`, sha256: sha256(await read(`${audit}/pareceres/${file}`)) });
  result.grupos.push({ ...group, html_historico_sha256: sha256(oldBytes), componentes: components, recursos: resources, pareceres: reports });
}
result.conferencias = result.grupos.reduce((n, g) => n + g.componentes.length + g.recursos.length, 0);
result.divergencias = result.grupos.flatMap(g => [...g.componentes, ...g.recursos].filter(c => !c.identico).map(c => ({ grupo: g.id, ...c })));
await fs.writeFile(path.join(root, `${audit}/evidencias/BAN-07/heranca-abertos-coordenador-r1.json`), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ conferencias: result.conferencias, problemas: 7, unidades: 2, recursos: 5, divergencias: result.divergencias }, null, 2));
if (result.divergencias.length) process.exitCode = 1;
