import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { parseHtml, isInventoryArticle, sha256 } from '../inventario/validar-inventario.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../..');
const auditDir = path.join(root, 'auditoria/termodinamica');
const reportDir = path.join(auditDir, 'pareceres');
const html = await fs.readFile(path.join(root, 'modulos/e1-termodinamica.html'), 'utf8');
const doc = parseHtml(html);
const articles = doc.nodes.filter(isInventoryArticle);
const current = new Map(articles.map(n => [n.attrs.id, sha256(html.slice(n.start, n.end))]));
const base = JSON.parse(await fs.readFile(path.join(reportDir, 'BAN-07-leitura-base.json'), 'utf8'));
const files = (await fs.readdir(reportDir)).filter(n => /^BAN-07-auditor-bloco-.*\.json$/.test(n)).sort();
const reads = new Map();
const stale = [];
const preliminaryNotes = [];
const issues = [];
const blocks = [];
const laterDecisions = new Map();

for (const r of base.registros) {
  if (current.get(r.id) === r.sha256_artigo) {
    reads.set(r.id, { fonte: 'BAN-07-leitura-base.json', origem: 'preparação anterior; identidade não é aceite científico', sha256_artigo: r.sha256_artigo });
    if (r.pontos_a_verificar?.length) preliminaryNotes.push({ id: r.id, pontos_a_verificar: r.pontos_a_verificar, estado: 'Exige decisão explícita de alcance pelo Auditor principal; o índice não encerra a ressalva.' });
  }
  else stale.push({ id: r.id, motivo: 'Artigo mudou; leitura da versão anterior exige confronto específico.' });
}
const inheritedCurrent = reads.size;
const seenBlocks = new Map();
for (const filename of files) {
  const bytes = await fs.readFile(path.join(reportDir, filename));
  const block = JSON.parse(bytes);
  const rows = (block.registros ?? block.itens ?? []).map(r => ({ ...r, id: r.id ?? r.id_artigo }));
  blocks.push({ arquivo: filename, sha256: sha256(bytes), estado: block.estado, registros: rows.length });
  for (const r of rows) {
    if (!current.has(r.id)) { issues.push({ id: r.id, arquivo: filename, motivo: 'ID não existe no produto atual.' }); continue; }
    if (current.get(r.id) !== r.sha256_artigo) { issues.push({ id: r.id, arquivo: filename, motivo: 'Hash não corresponde ao artigo atual.' }); continue; }
    if (seenBlocks.has(r.id)) issues.push({ id: r.id, arquivo: filename, motivo: 'ID repetido em blocos; conferir intenção e versões.', outro: seenBlocks.get(r.id) });
    seenBlocks.set(r.id, filename);
    if (Array.isArray(r.pontos_decididos)) laterDecisions.set(r.id, { arquivo: filename, veredito_item: r.veredito_item, pontos_decididos: r.pontos_decididos });
    reads.set(r.id, { fonte: filename, origem: r.origem_revisao ?? 'bloco incremental independente', sha256_artigo: r.sha256_artigo, veredito_item: r.veredito_item });
    for (const field of ['ajustes_obrigatorios', 'obrigacoes']) {
      if (r[field] === undefined) continue;
      if (!Array.isArray(r[field])) { issues.push({ id: r.id, arquivo: filename, motivo: `Campo ${field} exige conferência de formato antes de interpretar obrigações.` }); continue; }
      for (const adjustment of r[field]) issues.push({ id: r.id, arquivo: filename, motivo: 'Ajuste obrigatório do Auditor', ajuste: adjustment });
    }
  }
}
for (const note of preliminaryNotes) {
  if (laterDecisions.has(note.id)) {
    note.confronto_posterior = laterDecisions.get(note.id);
    note.estado = 'Confronto posterior do Auditor disponível; consultar pontos decididos e veredito. O índice não substitui o parecer.';
  }
}
// Preserve the historical finding while making the later independent decision visible.
const adjudicationPath = path.join(reportDir, 'BAN-07-auditor-decisoes-av31-41-observacoes-av23-30-r1.json');
try {
  const bytes = await fs.readFile(adjudicationPath);
  const adjudication = JSON.parse(bytes);
  for (const issue of issues) {
    const decision = adjudication.decisoes?.find(d => d.id_artigo === issue.id && d.apontamento === issue.ajuste?.id);
    if (decision) issue.adjudicacao_posterior = {
      arquivo: path.basename(adjudicationPath), sha256: sha256(bytes),
      decisao: decision.decisao, veredito_pontual: decision.veredito_pontual
    };
  }
} catch (error) {
  if (error.code !== 'ENOENT') throw error;
}
const pending = [...current.keys()].filter(id => !reads.has(id));
const result = {
  id: 'BAN-07', responsavel: '/root, coordenador',
  tipo: 'Índice de cobertura e identidade; não é parecer científico nem aprovação automática.',
  html_sha256: sha256(html), artigos: current.size,
  preparacao_anterior_identica_ao_produto: inheritedCurrent,
  novos_registros_por_blocos: seenBlocks.size,
  total_com_leitura_de_versao_atual_disponivel: reads.size,
  pendentes_de_leitura_atual_ou_confronto: pending,
  preparacao_anterior_que_exige_confronto: stale,
  ressalvas_da_preparacao_identica: preliminaryNotes,
  blocos: blocks, alertas: issues,
  leituras: [...reads.entries()].map(([id, info]) => ({ id, ...info })),
  limites: ['A presença de registro não demonstra sozinha o atendimento ao critério.', 'O Auditor deve confrontar a entrega congelada inteira e emitir parecer explícito.']
};
await fs.writeFile(path.join(auditDir, 'evidencias/BAN-07/cobertura-auditoria-atual.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ artigos: result.artigos, identicos_a_preparacao_anterior: inheritedCurrent, ressalvas_preliminares_registradas: preliminaryNotes.length, confrontos_posteriores_disponiveis: preliminaryNotes.filter(n => n.confronto_posterior).length, novos_por_blocos: seenBlocks.size, leitura_atual_disponivel: reads.size, pendentes: pending.length, alertas: issues }, null, 2));
