/** BAN-02: verificações estruturais e de rastreabilidade, sem dependências npm.
 * A aprovação científica/pedagógica cabe ao Auditor; `ok` não é um aceite.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const defaultRoot = path.resolve(here, '../../..');
export const sha256 = value => createHash('sha256').update(value).digest('hex');
const fail = (errors, where, message) => errors.push(`${where}: ${message}`);
const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);

/** Interpreta somente o subconjunto JSON Schema usado pelo schema irmão. */
export function validateSchema(value, schema, root = schema, at = '$', errors = []) {
  if (schema.$ref) {
    const target = schema.$ref.split('/').slice(1).reduce((a, k) => a?.[k], root);
    if (!target) throw new Error(`Referência de schema inexistente: ${schema.$ref}`);
    return validateSchema(value, target, root, at, errors);
  }
  for (const branch of schema.allOf ?? []) validateSchema(value, branch, root, at, errors);
  if (schema.if) {
    const matches = validateSchema(value, schema.if, root, at, []).length === 0;
    const branch = matches ? schema.then : schema.else;
    if (branch) validateSchema(value, branch, root, at, errors);
  }
  if ('const' in schema && value !== schema.const) fail(errors, at, `esperado ${JSON.stringify(schema.const)}`);
  if (schema.enum && !schema.enum.includes(value)) fail(errors, at, `fora dos valores permitidos: ${JSON.stringify(value)}`);
  if (schema.type) {
    const typeOk = schema.type === 'object' ? object(value)
      : schema.type === 'array' ? Array.isArray(value)
      : schema.type === 'integer' ? Number.isSafeInteger(value)
      : typeof value === schema.type;
    if (!typeOk) { fail(errors, at, `tipo esperado: ${schema.type}`); return errors; }
  }
  if (object(value)) {
    for (const key of schema.required ?? []) if (!(key in value)) fail(errors, at, `campo obrigatório ausente: ${key}`);
    for (const key of Object.keys(value)) {
      if (schema.properties?.[key]) validateSchema(value[key], schema.properties[key], root, `${at}.${key}`, errors);
      else if (schema.additionalProperties === false) fail(errors, at, `campo não previsto: ${key}`);
    }
  }
  if (Array.isArray(value)) {
    if (value.length < (schema.minItems ?? 0)) fail(errors, at, `exige ao menos ${schema.minItems} elemento(s)`);
    if (schema.maxItems !== undefined && value.length > schema.maxItems) fail(errors, at, `excede ${schema.maxItems} elementos`);
    if (schema.uniqueItems && new Set(value.map(v => JSON.stringify(v))).size !== value.length) fail(errors, at, 'elementos duplicados');
    value.forEach((v, i) => { if (schema.items) validateSchema(v, schema.items, root, `${at}[${i}]`, errors); });
  }
  if (typeof value === 'string') {
    if (value.length < (schema.minLength ?? 0)) fail(errors, at, 'texto vazio');
    if (schema.pattern && !new RegExp(schema.pattern, 'u').test(value)) fail(errors, at, `não atende ao padrão ${schema.pattern}`);
    if (schema.format === 'date' && (!/^\d{4}-\d{2}-\d{2}$/.test(value) || Number.isNaN(Date.parse(value)) || new Date(value).toISOString().slice(0, 10) !== value)) fail(errors, at, 'data inválida; use AAAA-MM-DD');
  }
  if (typeof value === 'number' && schema.minimum !== undefined && value < schema.minimum) fail(errors, at, `valor mínimo: ${schema.minimum}`);
  return errors;
}

export function decodeHtml(value) {
  const named = { amp: '&', quot: '"', apos: "'", lt: '<', gt: '>', nbsp: ' ' };
  return value.replace(/&(#x[\da-f]+|#\d+|amp|quot|apos|lt|gt|nbsp);/gi, (whole, token) => {
    if (token[0] !== '#') return named[token.toLowerCase()] ?? whole;
    const cp = token[1].toLowerCase() === 'x' ? parseInt(token.slice(2), 16) : Number(token.slice(1));
    return cp <= 0x10ffff && cp >= 0 ? String.fromCodePoint(cp) : whole;
  });
}

/** Tokenizador conservador: mantém offsets exatos, ignora comentários e scripts. */
export function parseHtml(html) {
  const nodes = [], roots = [], stack = [], errors = [];
  const voids = new Set('area base br col embed hr img input link meta param source track wbr'.split(' '));
  const tags = /<!--[\s\S]*?-->|<![^>]*>|<\/?[a-zA-Z][^>"']*(?:(?:"[^"]*"|'[^']*')[^>"']*)*>/g;
  let match;
  while ((match = tags.exec(html))) {
    const raw = match[0];
    if (raw.startsWith('<!')) continue;
    const parsed = /^<(\/)?([\w:-]+)/.exec(raw);
    const tag = parsed[2].toLowerCase();
    if (parsed[1]) {
      const at = stack.findLastIndex(n => n.tag === tag);
      if (at >= 0) {
        const node = stack[at];
        node.end = tags.lastIndex;
        if (tag === 'article' && stack.slice(at + 1).some(n => n.tag === 'article')) errors.push('article aninhado sem fechamento explícito');
        stack.splice(at);
      }
      continue;
    }
    const attrs = {};
    const attributeText = raw.slice(parsed[0].length, raw.length - 1);
    for (const a of attributeText.matchAll(/([^\s=/'">]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?/g)) attrs[a[1].toLowerCase()] = decodeHtml(a[2] ?? a[3] ?? a[4] ?? '');
    const parent = stack.at(-1) ?? null;
    const node = { tag, attrs, start: match.index, openEnd: tags.lastIndex, end: tags.lastIndex, parent, children: [] };
    (parent ? parent.children : roots).push(node); nodes.push(node);
    if (voids.has(tag) || /\/\s*>$/.test(raw)) continue;
    if (['script', 'style', 'textarea', 'title'].includes(tag)) {
      const closing = new RegExp(`</${tag}\\s*>`, 'ig'); closing.lastIndex = tags.lastIndex;
      const end = closing.exec(html);
      if (end) { node.end = closing.lastIndex; tags.lastIndex = closing.lastIndex; }
      continue;
    }
    stack.push(node);
  }
  for (const node of stack) if (node.tag === 'article') errors.push(`article não fechado: ${node.attrs.id ?? '(sem ID)'}`);
  const ids = new Map();
  for (const node of nodes) if (node.attrs.id) ids.set(node.attrs.id, [...(ids.get(node.attrs.id) ?? []), node]);
  return { html, nodes, roots, ids, errors };
}

/** Âncoras de títulos ATX Markdown, inclusive duplicatas; ignora blocos cercados. */
function markdownHeadingAnchors(markdown) {
  const counts = new Map(), anchors = [];
  let fence = null;
  for (const line of markdown.split(/\r?\n/)) {
    const delimiter = /^\s{0,3}(`{3,}|~{3,})/.exec(line);
    if (delimiter) {
      if (!fence) fence = { char: delimiter[1][0], length: delimiter[1].length };
      else if (delimiter[1][0] === fence.char && delimiter[1].length >= fence.length) fence = null;
      continue;
    }
    if (fence) continue;
    const heading = /^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$/.exec(line);
    if (!heading) continue;
    const label = decodeHtml(heading[1].replace(/<[^>]*>/g, '').replace(/!?\[([^\]]+)\]\([^)]*\)/g, '$1'));
    const slug = label.toLowerCase().replace(/[^\p{L}\p{N}\p{M}_\-\s]/gu, '').replace(/\s/g, '-');
    const seen = counts.get(slug) ?? 0; counts.set(slug, seen + 1);
    anchors.push(seen ? `${slug}-${seen}` : slug);
  }
  return anchors;
}

const classes = node => new Set((node.attrs.class ?? '').split(/\s+/));
export function isInventoryArticle(node) {
  if (node.tag !== 'article') return false;
  return /^(?:q|cr|av)-e1-\d+$/.test(node.attrs.id ?? '') || node.attrs['data-inventario'] === 'e1'
    || ['questao', 'concurso-item', 'avalia-item'].some(c => classes(node).has(c));
}
const inside = (node, article) => node.start >= article.start && node.end <= article.end;
const descendants = (document, article) => document.nodes.filter(n => inside(n, article));
const external = value => /^(?:https?:)?\/\//i.test(value);
const nonLocal = value => /^[a-z][a-z\d+.-]*:/i.test(value);
const relative = (root, filename) => path.relative(root, filename).split(path.sep).join('/');

function resolveInside(root, filename) {
  const resolved = path.resolve(root, filename);
  const rel = path.relative(root, resolved);
  if (path.isAbsolute(rel) || rel === '..' || rel.startsWith(`..${path.sep}`)) throw new Error(`caminho fora da raiz: ${filename}`);
  return resolved;
}

/** Referências carregadas, mais downloads/dados obrigatórios marcados no artigo. */
export function resourceReferences(document, article) {
  const refs = [];
  for (const node of descendants(document, article)) {
    for (const attr of ['src', 'poster']) if (node.attrs[attr]) refs.push(node.attrs[attr]);
    if (node.tag === 'object' && node.attrs.data) refs.push(node.attrs.data);
    if (['image', 'use'].includes(node.tag)) for (const attr of ['href', 'xlink:href']) if (node.attrs[attr]) refs.push(node.attrs[attr]);
    if (node.tag === 'a' && ('download' in node.attrs || node.attrs['data-recurso'] === 'obrigatorio') && node.attrs.href) refs.push(node.attrs.href);
    if (node.attrs.srcset) {
      // Dados embutidos já estão no hash do artigo. URLs locais não contêm vírgula literal.
      if (/data:/i.test(node.attrs.srcset)) throw new Error('srcset com data URI exige normalização antes do rastreamento');
      for (const candidate of node.attrs.srcset.split(',')) refs.push(candidate.trim().split(/\s+/)[0]);
    }
    for (const m of (node.attrs.style ?? '').matchAll(/url\(\s*["']?([^"')]+)["']?\s*\)/gi)) refs.push(m[1]);
  }
  return [...new Set(refs.filter(Boolean))];
}

/** Executa o contrato + vínculo completo fonte/registro. Sem escrever no curso. */
export async function validateInventory({ rootDir = defaultRoot, inventoryPath = 'auditoria/termodinamica/inventario/inventario-questoes.json', inventory } = {}) {
  const root = path.resolve(rootDir), errors = [], warnings = [];
  const result = { ok: false, curso: 'E1', itens_registrados: 0, artigos_encontrados: 0, recursos_verificados: 0, links_locais_verificados: 0, erros: errors, avisos: warnings, alcance: 'Estrutura, cobertura e integridade documental. Não certifica mérito científico, nível avançado, gabaritos ou aprendizagem.' };
  const documents = new Map(), resources = new Set();
  const bytes = async (filename, where) => {
    try { return await fs.readFile(resolveInside(root, filename)); }
    catch (error) { fail(errors, where, `arquivo inacessível: ${filename} (${error.message})`); return null; }
  };
  const document = async filename => {
    if (documents.has(filename)) return documents.get(filename);
    const buffer = await bytes(filename, filename);
    if (!buffer) { documents.set(filename, null); return null; }
    const parsed = parseHtml(buffer.toString('utf8')); parsed.buffer = buffer;
    if (/\.md$/i.test(filename)) for (const id of markdownHeadingAnchors(parsed.html)) {
      parsed.ids.set(id, [...(parsed.ids.get(id) ?? []), { tag: 'markdown-heading', attrs: { id } }]);
    }
    documents.set(filename, parsed);
    parsed.errors.forEach(e => fail(errors, filename, e));
    return parsed;
  };
  const target = async (reference, fromFile, where, rootRelative = false) => {
    if (external(reference)) {
      try { const parsed = new URL(reference.startsWith('//') ? `https:${reference}` : reference); if (!parsed.hostname) throw new Error('host ausente'); }
      catch { fail(errors, where, `URL externa inválida: ${reference}`); }
      return null;
    }
    if (nonLocal(reference)) {
      if (!/^(?:mailto:|tel:|data:)/i.test(reference)) fail(errors, where, `protocolo não permitido: ${reference}`);
      return null;
    }
    try {
      const hashIndex = reference.indexOf('#');
      const beforeHash = hashIndex === -1 ? reference : reference.slice(0, hashIndex);
      const rawFragment = hashIndex === -1 ? undefined : reference.slice(hashIndex + 1);
      const urlPath = decodeURIComponent(beforeHash.split('?')[0]);
      const fragment = rawFragment === undefined ? undefined : decodeURIComponent(rawFragment);
      const filename = urlPath ? relative(root, resolveInside(root, rootRelative ? urlPath : path.join(path.dirname(fromFile), urlPath))) : fromFile;
      if (fragment !== undefined && fragment !== '') {
        if (/\.pdf$/i.test(filename)) {
          // PDF usa parâmetro de abertura, não ID HTML. A existência da página exige conferência documental.
          if (!/^page=[1-9]\d*$/.test(fragment) || !Number.isSafeInteger(Number(fragment.slice(5)))) {
            fail(errors, where, `fragmento PDF inválido (esperado page=N inteiro positivo): ${filename}#${fragment}`);
          }
          if (!(await bytes(filename, where))) return null;
        } else {
          const doc = await document(filename);
          if (doc && (doc.ids.get(fragment)?.length ?? 0) !== 1) fail(errors, where, `âncora ausente ou duplicada: ${filename}#${fragment}`);
        }
      } else if (!(await bytes(filename, where))) return null;
      result.links_locais_verificados++; return filename;
    } catch (error) { fail(errors, where, `referência local inválida: ${reference} (${error.message})`); return null; }
  };
  let data;
  try {
    data = inventory ?? JSON.parse((await fs.readFile(resolveInside(root, inventoryPath), 'utf8')).replace(/^\uFEFF/, ''));
    const schema = JSON.parse(await fs.readFile(path.join(here, 'inventario.schema.json'), 'utf8'));
    validateSchema(data, schema, schema, '$', errors);
  } catch (error) { fail(errors, '$', error.message); return result; }
  if (errors.length) return result;
  result.itens_registrados = data.itens.length;
  const source = await document(data.fonte.arquivo);
  if (source && sha256(source.buffer) !== data.fonte.sha256) fail(errors, '$.fonte.sha256', 'fonte atual modificada; revisão dos registros necessária');
  const snapshot = await bytes(data.fonte.snapshot, '$.fonte.snapshot');
  if (snapshot && sha256(snapshot) !== data.fonte.sha256) fail(errors, '$.fonte.snapshot', 'snapshot difere do hash registrado da fonte');
  if (data.fonte.snapshot === data.fonte.arquivo) fail(errors, '$.fonte.snapshot', 'snapshot deve ser uma cópia preservada distinta da fonte');
  const byId = new Map();
  for (const item of data.itens) {
    if (byId.has(item.id)) fail(errors, item.id, 'ID duplicado no inventário');
    byId.set(item.id, item);
    await document(item.localizacao.arquivo);
  }
  // O módulo principal e todos os documentos cadastrados são percorridos por inteiro.
  const sourceDocs = new Set([data.fonte.arquivo, ...data.itens.map(i => i.localizacao.arquivo)]);
  const found = new Map();
  for (const filename of sourceDocs) {
    const doc = documents.get(filename); if (!doc) continue;
    for (const article of doc.nodes.filter(isInventoryArticle)) {
      const id = article.attrs.id;
      result.artigos_encontrados++;
      if (!id) { fail(errors, filename, 'artigo de avaliação sem ID'); continue; }
      if (found.has(id)) fail(errors, id, 'ID de avaliação duplicado entre fontes');
      found.set(id, { filename, article });
      const item = byId.get(id);
      if (!item) fail(errors, id, 'artigo da fonte sem registro no inventário');
      else if (item.localizacao.arquivo !== filename || item.localizacao.fragmento !== id) fail(errors, id, 'registro não aponta para sua fonte exata');
    }
  }
  for (const item of data.itens) {
    const loc = item.localizacao, doc = documents.get(loc.arquivo);
    if (loc.fragmento !== item.id) fail(errors, item.id, 'fragmento deve coincidir com o ID');
    const matches = doc?.ids.get(loc.fragmento) ?? [];
    if (matches.length !== 1 || matches[0].tag !== 'article') { fail(errors, item.id, 'localização precisa identificar um único article existente'); continue; }
    const article = matches[0], nodes = descendants(doc, article);
    if (!isInventoryArticle(article)) fail(errors, item.id, 'artigo extra sem identificação de avaliação; use data-inventario="e1"');
    if (sha256(doc.html.slice(article.start, article.end)) !== loc.sha256_artigo) fail(errors, item.id, 'hash do artigo desatualizado; reler enunciado, alternativas, comentários, notas e recursos');
    const prefixBank = /^(q|cr|av)-e1-\d+$/.exec(item.id);
    const expectedBank = prefixBank ? { q: 'inicial', cr: 'real', av: 'avalia' }[prefixBank[1]] : article.attrs['data-banco'];
    if (expectedBank !== item.banco) fail(errors, item.id, 'banco diverge do prefixo ou data-banco do artigo');
    const count = nodes.filter(n => n.tag === 'input' && n.attrs.type === 'radio').length
      || nodes.filter(n => n.tag === 'li' && n.parent?.tag === 'ol' && classes(n.parent).has('q-alternativas')).length;
    if (count !== item.formato.numero_alternativas) fail(errors, item.id, `alternativas no HTML=${count}, registro=${item.formato.numero_alternativas}`);
    const kind = item.formato.tipo;
    if (kind === 'multipla_escolha' && count < 2) fail(errors, item.id, 'múltipla escolha exige pelo menos duas alternativas');
    if (kind === 'certo_errado' && count !== 2) fail(errors, item.id, 'certo/errado exige duas alternativas');
    if (['resposta_aberta', 'projeto'].includes(kind) && count !== 0) fail(errors, item.id, 'resposta aberta/projeto exige zero alternativas');
    if (article.attrs['data-formato'] && article.attrs['data-formato'] !== kind) fail(errors, item.id, 'formato diverge do data-formato do artigo');
    if (item.banco === 'aberto' && kind !== 'resposta_aberta') fail(errors, item.id, 'banco aberto exige resposta_aberta');
    if (item.banco === 'projeto' && kind !== 'projeto') fail(errors, item.id, 'banco projeto exige formato projeto');
    if (item.raciocinio.numero_etapas !== item.raciocinio.etapas.length) fail(errors, item.id, 'numero_etapas difere do tamanho de etapas');
    if (item.nivel.estimado === 'a_classificar') fail(errors, item.id, 'item ainda não classificado; registro incompleto para BAN-02');
    const exposure = item.exposicao_previa;
    if ((exposure.estado === 'relacao_identificada') !== (exposure.relacoes.length > 0)) fail(errors, item.id, 'estado de exposição e relações são incompatíveis');
    for (const relation of exposure.relacoes) {
      const ref = relation.id_ou_ancora;
      if (external(ref) || nonLocal(ref)) { fail(errors, item.id, 'relação interna exige ID/âncora local existente'); continue; }
      await target(ref.startsWith('#') || ref.includes('#') ? ref : `#${ref}`, loc.arquivo, `${item.id}.exposicao_previa`, !ref.startsWith('#') && ref.includes('#'));
    }
    for (const node of nodes) if (node.attrs.href && node.tag === 'a') await target(node.attrs.href, loc.arquivo, `${item.id}.link`);
    for (const origin of item.origem.fontes) await target(origin.url, loc.arquivo, `${item.id}.origem`, !origin.url.startsWith('#'));
    for (const [field, evidence] of [
      ['origem.evidencia_conferencia', item.origem.evidencia_conferencia],
      ['revisao.evidencia_gabarito', item.revisao.evidencia_gabarito]
    ]) {
      if (evidence === undefined) continue;
      if (!evidence.trim() || evidence.startsWith('#') || external(evidence) || nonLocal(evidence)) {
        fail(errors, `${item.id}.${field}`, 'evidência exige caminho local não vazio, relativo à raiz, opcionalmente com #âncora');
        continue;
      }
      await target(evidence, loc.arquivo, `${item.id}.${field}`, true);
    }
    const declared = new Map();
    for (const resource of loc.recursos) {
      if (declared.has(resource.arquivo)) fail(errors, item.id, `recurso duplicado: ${resource.arquivo}`);
      declared.set(resource.arquivo, resource);
      const buffer = await bytes(resource.arquivo, item.id);
      if (buffer && sha256(buffer) !== resource.sha256) fail(errors, item.id, `recurso alterado: ${resource.arquivo}`);
      if (buffer) resources.add(resource.arquivo);
    }
    let refs = [];
    try { refs = resourceReferences(doc, article); } catch (error) { fail(errors, item.id, error.message); }
    for (const ref of refs) {
      if (ref.startsWith('#')) { await target(ref, loc.arquivo, `${item.id}.recurso_embutido`); continue; }
      if (ref.startsWith('data:')) continue;
      if (external(ref)) { fail(errors, item.id, `recurso remoto sem snapshot rastreável: ${ref}`); continue; }
      const filename = await target(ref, loc.arquivo, `${item.id}.recurso`);
      if (filename && !declared.has(filename)) fail(errors, item.id, `recurso usado sem hash no registro: ${filename}`);
    }
    // Hashes extras são permitidos para dependências transitivas ou material referenciado.
    // Cada dependência adicional deve ser explicada no campo hipoteses.limites/metodo.
  }
  result.recursos_verificados = resources.size;
  result.ok = errors.length === 0;
  return result;
}

if (typeof process !== 'undefined' && process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url) {
  const result = await validateInventory({ inventoryPath: process.argv[2] ?? undefined, rootDir: process.argv[3] ?? undefined });
  console.log(JSON.stringify(result, null, 2));
  process.exitCode = result.ok ? 0 : 1;
}
