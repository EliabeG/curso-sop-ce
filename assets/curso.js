/* ==========================================================================
   Curso SOP-CE 2026 · Engenharia Mecânica — interatividade (versão 2 do estado salvo)
   Sem dependências e sem rede. Carregado no <head> SEM defer (depois de registro.js):
   aplica o tema antes da primeira pintura e registra o restante para DOMContentLoaded.
   Tudo funciona sem este script (gabaritos em <details>) e sem armazenamento local
   (o progresso só deixa de ser salvo, e a página avisa).

   Estado salvo (localStorage, prefixo "sopmec:v2:"):
     tema                      "light" | "dark" (ausente = automático)
     mod:<módulo>              { v, versao, respostas{digital:letra}, erros{digital:n}, simulado?, resumo }
     check:<módulo>:<lista>    [digital do item marcado, ...]
     ultimo                    { modulo, arquivo, secao, secaoTitulo, quando }
   A "digital" de uma questão é o FNV-1a do enunciado, das cinco alternativas e do gabarito
   (mesma função do validador em Python): editar ou reordenar questões nunca aplica a resposta
   antiga a uma questão diferente.
   ========================================================================== */
(function () {
  'use strict';

  var PREFIXO = 'sopmec:v2:';
  var LETRAS = ['A', 'B', 'C', 'D', 'E'];
  var SEPARADOR = '␞';
  var RE_MODULO = /^[a-z0-9-]{1,20}$/;
  var RE_ARQUIVO = /^[a-z0-9-]{1,60}\.html$/;
  var RE_DIGITAL = /^[0-9a-f]{8}$/;
  var RE_LISTA = /^[a-z0-9-]{1,40}$/;
  var RE_SECAO = /^[a-z0-9-]{1,60}$/;
  var ESTREITA = '(max-width: 69.99rem)';
  var ESPERA_CONFIRMAR_MS = 600;
  var LIMITE_ERROS = Number.MAX_SAFE_INTEGER;

  /* ---------- Utilidades ---------- */
  function paraArray(lista) {
    return Array.prototype.slice.call(lista);
  }

  function criar(tag, classe, texto) {
    var el = document.createElement(tag);
    if (classe) el.className = classe;
    if (texto !== undefined) el.textContent = texto;
    return el;
  }

  function seguro(nome, fn) {
    try {
      fn();
    } catch (e) {
      if (window.console && console.error) console.error('[curso] falha em ' + nome + ':', e);
    }
  }

  function inteiroValido(x, max) {
    return typeof x === 'number' && isFinite(x) && Math.floor(x) === x && x >= 0 && (max === undefined || x <= max);
  }

  function incrementarErro(n) {
    n = inteiroValido(n, LIMITE_ERROS) ? n : 0;
    return n < LIMITE_ERROS ? n + 1 : LIMITE_ERROS;
  }

  function normalizarDigital(texto) {
    return String(texto).replace(/[ \t\n\r\f\v ]+/g, ' ').replace(/^ | $/g, '');
  }

  /** Mantém as respostas salvas quando uma fórmula ganha frações/índices em MathML.
      A forma textual original fica só na própria fórmula; o restante do enunciado continua participando da digital. */
  function textoDaDigital(no) {
    if (no.nodeType === 3) return no.nodeValue;
    if (no.nodeType !== 1) return '';
    if (no.localName === 'math' && no.hasAttribute('data-formula-original')) return no.getAttribute('data-formula-original');
    return paraArray(no.childNodes).map(textoDaDigital).join('');
  }

  /** FNV-1a de 32 bits sobre pontos de código (idêntica a validar_curso.fnv1a). */
  function fnv1a(texto) {
    var h = 0x811c9dc5;
    for (var i = 0; i < texto.length; i += 1) {
      var cp = texto.codePointAt(i);
      if (cp > 0xffff) i += 1;
      h ^= cp;
      h = Math.imul(h, 0x01000193) >>> 0;
    }
    return ('0000000' + h.toString(16)).slice(-8);
  }

  function formatarTempo(ms) {
    var s = Math.max(0, Math.floor(ms / 1000));
    var h = Math.floor(s / 3600);
    var m = Math.floor((s % 3600) / 60);
    var seg = s % 60;
    function dois(n) { return (n < 10 ? '0' : '') + n; }
    return dois(h) + ':' + dois(m) + ':' + dois(seg);
  }

  function pluralizar(n, singular, plural) {
    return n + ' ' + (n === 1 ? singular : plural);
  }

  /* ---------- Armazenamento local tolerante a falhas ---------- */
  var armazenamento = (function () {
    var problema = null; // null | 'bloqueado' | 'cheio' | 'erro' | 'leitura' | 'recuperacao'
    var ouvintes = [];
    var conhecidos = Object.create(null);
    var vistos = Object.create(null);
    var pendentes = Object.create(null);
    var recuperacaoPropria = false;
    // Privado: nunca exportado/importado. Enquanto existe, o snapshot é a versão válida.
    var JOURNAL = PREFIXO + '__importacao__';

    function notificar() {
      ouvintes.forEach(function (fn) {
        seguro('aviso de armazenamento', fn);
      });
    }

    function disponivel() {
      try {
        return !!window.localStorage;
      } catch (e) {
        problema = 'bloqueado';
        return false;
      }
    }

    function ehCotaCheia(e) {
      return !!e && (e.name === 'QuotaExceededError' || e.name === 'NS_ERROR_DOM_QUOTA_REACHED' || e.code === 22 || e.code === 1014);
    }

    function falhou(e, leitura) {
      problema = leitura ? 'leitura' : (ehCotaCheia(e) ? 'cheio' : 'erro');
      notificar();
    }

    function objeto(x) { return !!x && typeof x === 'object' && !Array.isArray(x); }
    function parse(texto) { try { return JSON.parse(texto); } catch (e) { return null; } }
    // Patches de campos, incluindo remoções: outra aba pode gravar digitais diferentes.
    function diferenca(antes, depois) {
      if (objeto(depois)) {
        var campos = Object.create(null);
        var origem = objeto(antes) ? antes : {};
        Object.keys(origem).forEach(function (k) {
          if (!Object.prototype.hasOwnProperty.call(depois, k)) campos[k] = { remover: true };
        });
        Object.keys(depois).forEach(function (k) {
          if (JSON.stringify(origem[k]) !== JSON.stringify(depois[k])) campos[k] = diferenca(origem[k], depois[k]);
        });
        return { campos: campos };
      }
      return { valor: depois };
    }
    function aplicar(base, patch) {
      if (!patch.campos) return patch.valor;
      var resultado = objeto(base) ? JSON.parse(JSON.stringify(base)) : {};
      Object.keys(patch.campos).forEach(function (k) {
        if (patch.campos[k].remover) delete resultado[k];
        else Object.defineProperty(resultado, k, { value: aplicar(resultado[k], patch.campos[k]), enumerable: true, configurable: true, writable: true });
      });
      return resultado;
    }
    function compor(antes, depois) {
      if (!antes || !depois.campos) return depois;
      if (!antes.campos) return { valor: aplicar(antes.valor, depois) };
      var campos = Object.create(null);
      Object.keys(antes.campos).forEach(function (k) { campos[k] = antes.campos[k]; });
      Object.keys(depois.campos).forEach(function (k) { campos[k] = compor(campos[k], depois.campos[k]); });
      return { campos: campos };
    }
    function sobrepor(chave, base, conhecido) {
      var p = pendentes[chave];
      if (!p) return base;
      if (!p.patch) return p.valor;
      // Uma ausência lida com sucesso é um estado vazio (inclusive após outra aba
      // apagar). Só uma leitura desconhecida pode recorrer à base da ação local.
      var vazio = { v: 2, respostas: {}, erros: {}, simulado: null };
      var origem = p.reset || (conhecido && base === null) ? vazio : (parse(base) || p.base);
      return JSON.stringify(aplicar(origem, p.patch));
    }

    function chavesDisco() {
      var lista = [];
      for (var i = 0; i < window.localStorage.length; i += 1) {
        var k = window.localStorage.key(i);
        if (k && k.indexOf(PREFIXO) === 0 && k !== JOURNAL) lista.push(k);
      }
      return lista;
    }
    function snapshot() {
      var dados = Object.create(null);
      chavesDisco().forEach(function (k) {
        var v = window.localStorage.getItem(k);
        if (typeof v !== 'string') throw new Error('O progresso mudou durante a leitura.');
        dados[k] = v;
      });
      return dados;
    }
    function restaurar(dados) {
      // Falha em qualquer etapa mantém o journal; leitores continuam usando o snapshot.
      chavesDisco().forEach(function (k) {
        if (!Object.prototype.hasOwnProperty.call(dados, k)) window.localStorage.removeItem(k);
      });
      Object.keys(dados).forEach(function (k) { window.localStorage.setItem(k, dados[k]); });
      window.localStorage.removeItem(JOURNAL); // commit da restauração, sempre por último
    }
    function recuperar(escrever) {
      var texto = window.localStorage.getItem(JOURNAL);
      if (texto === null) return null;
      var j = parse(texto);
      if (!objeto(j) || j.v !== 1 || !inteiroValido(j.inicio, Number.MAX_SAFE_INTEGER) || !objeto(j.originais) || Object.keys(j.originais).some(function (k) {
        return k.indexOf(PREFIXO) !== 0 || k === JOURNAL || typeof j.originais[k] !== 'string';
      })) throw new Error('Cópia de recuperação ilegível; gravação interrompida.');
      // Uma aba lendo não pode desfazer a importação síncrona de outra. A leitura é
      // sempre do snapshot; uma nova escrita recupera somente uma tentativa abandonada.
      if (escrever && (recuperacaoPropria || Date.now() - j.inicio >= 30000)) {
        try {
          restaurar(j.originais);
          recuperacaoPropria = false;
          return null;
        } catch (e) { /* mantém a cópia durável e bloqueia a gravação nova */ }
      }
      if (problema !== 'recuperacao') {
        problema = 'recuperacao';
        notificar();
      }
      return j.originais;
    }
    function lerSeguro(chave, escrever) {
      try {
        var recuperados = recuperar(escrever);
        var valor = recuperados ? (Object.prototype.hasOwnProperty.call(recuperados, PREFIXO + chave) ? recuperados[PREFIXO + chave] : null) : window.localStorage.getItem(PREFIXO + chave);
        conhecidos[chave] = valor;
        return { ok: !recuperados, valor: valor, conhecido: true };
      } catch (e) {
        falhou(e, true);
        var conhecido = Object.prototype.hasOwnProperty.call(conhecidos, chave);
        return { ok: false, valor: conhecido ? conhecidos[chave] : null, conhecido: conhecido };
      }
    }
    function ler(chave) {
      var r = lerSeguro(chave);
      var valor = sobrepor(chave, r.valor, r.conhecido);
      vistos[chave] = valor;
      return valor;
    }
    function mudar(chave, valor, baseMudanca) {
      var anterior = Object.prototype.hasOwnProperty.call(vistos, chave) ? vistos[chave] : ler(chave);
      var r = lerSeguro(chave, true); // falha de leitura nunca autoriza sobrescrever o disco
      if (chave.indexOf('mod:') === 0 && valor !== null && objeto(parse(valor))) {
        var delta = diferenca(baseMudanca || parse(anterior), parse(valor));
        var existente = pendentes[chave];
        pendentes[chave] = { patch: compor(existente && existente.patch, delta), base: baseMudanca || parse(valor), reset: !!(existente && (existente.reset || existente.valor === null)) };
      } else {
        pendentes[chave] = { valor: valor };
      }
      var final = sobrepor(chave, r.valor, r.conhecido);
      vistos[chave] = final;
      if (!r.ok) return false;
      try {
        if (final === null) window.localStorage.removeItem(PREFIXO + chave);
        else window.localStorage.setItem(PREFIXO + chave, final);
        conhecidos[chave] = final;
        delete pendentes[chave];
        if (problema && !Object.keys(pendentes).length) {
          problema = null;
          notificar();
        }
        return true;
      } catch (e) {
        falhou(e, false);
        return false;
      }
    }
    function gravar(chave, valor, baseMudanca) { return mudar(chave, String(valor), baseMudanca); }
    function apagar(chave) { return mudar(chave, null); }

    function substituir(dados) {
      var originais;
      try {
        if (recuperar(true)) throw new Error('Há uma recuperação pendente.');
        originais = snapshot(); // leitura completa antes de qualquer alteração
        window.localStorage.setItem(JOURNAL, JSON.stringify({ v: 1, inicio: Date.now(), originais: originais }));
      } catch (e) {
        falhou(e, !originais);
        return false; // nenhuma chave pública foi alterada
      }
      try {
        Object.keys(dados).forEach(function (k) { window.localStorage.setItem(k, dados[k]); });
        Object.keys(originais).forEach(function (k) {
          if (!Object.prototype.hasOwnProperty.call(dados, k)) window.localStorage.removeItem(k);
        });
        window.localStorage.removeItem(JOURNAL); // commit; até aqui o snapshot segue recuperável
        conhecidos = Object.create(null);
        vistos = Object.create(null);
        pendentes = Object.create(null);
        problema = null;
        notificar();
        return true;
      } catch (e) {
        recuperacaoPropria = true;
        try { restaurar(originais); } catch (rollback) { /* snapshot durável continua sendo a visão válida */ }
        falhou(e, false);
        return false;
      }
    }

    function lerJSON(chave, aoCorromper) {
      var texto = ler(chave);
      if (texto === null) return null;
      try {
        return JSON.parse(texto);
      } catch (e) {
        if (aoCorromper) aoCorromper(texto);
        return null;
      }
    }

    function gravarJSON(chave, objeto, baseMudanca) {
      var texto;
      try {
        texto = JSON.stringify(objeto);
      } catch (e) {
        return false;
      }
      return gravar(chave, texto, baseMudanca);
    }

    function chaves() {
      var lista;
      try {
        var recuperados = recuperar();
        lista = recuperados ? Object.keys(recuperados) : chavesDisco();
      } catch (e) {
        falhou(e, true);
        lista = Object.keys(conhecidos).filter(function (k) { return conhecidos[k] !== null; }).map(function (k) { return PREFIXO + k; });
      }
      Object.keys(pendentes).forEach(function (k) {
        if (lista.indexOf(PREFIXO + k) < 0) lista.push(PREFIXO + k);
      });
      return lista.filter(function (k) { return ler(k.slice(PREFIXO.length)) !== null; });
    }

    function aviso() {
      disponivel();
      if (problema === 'bloqueado') {
        return 'Este navegador não está deixando o curso salvar dados (armazenamento bloqueado). O que você fizer vale só até fechar esta página. Para salvar o progresso, permita que o navegador guarde dados de sites ou use outro navegador atual (Chrome, Edge ou Firefox).';
      }
      if (problema === 'cheio') {
        return 'Não foi possível salvar: o armazenamento do navegador está cheio. As novas ações valem só até fechar esta página. Libere espaço apagando dados de outros sites. O progresso que já estava salvo pode ser exportado no portal do curso.';
      }
      if (problema === 'erro') {
        return 'Não foi possível salvar o progresso neste navegador. O que você fez por último vale só até fechar esta página.';
      }
      if (problema === 'leitura') {
        return 'Não foi possível ler o progresso salvo. Os dados existentes foram preservados; as novas ações valem só até fechar esta página.';
      }
      if (problema === 'recuperacao') {
        return 'A importação não foi concluída. O progresso anterior está preservado na cópia de recuperação e pode ser lido e exportado. Novas ações valem nesta página até ser possível recuperar o armazenamento.';
      }
      return null;
    }

    return {
      disponivel: disponivel,
      ler: ler,
      gravar: gravar,
      apagar: apagar,
      lerJSON: lerJSON,
      gravarJSON: gravarJSON,
      substituir: substituir,
      chaves: chaves,
      aviso: aviso,
      aoMudarAviso: function (fn) { ouvintes.push(fn); }
    };
  })();

  function registrarCorrompido(chave) {
    return function (texto) {
      if (window.console && console.warn) console.warn('[curso] dado salvo ilegível em ' + PREFIXO + chave + '; será substituído. Cópia guardada em ' + PREFIXO + 'corrompido:' + chave);
      if (armazenamento.ler('corrompido:' + chave) === null) armazenamento.gravar('corrompido:' + chave, texto.slice(0, 100000));
    };
  }

  /* ---------- Dados da versão anterior (sopmec:v1:) ---------- */
  // Tema, listas e "continuar" da v1 têm o mesmo sentido na v2 e passam para ela na primeira abertura; a cópia da v1
  // sai depois que a v2 tem o dado (uma lista desmarcada na v2 não "ressuscita"). As respostas da v1 eram presas à
  // posição da questão, sem conversão segura, e ficam onde estão (na v1 só o guia tinha saído, e ele não tem questões).
  var PREFIXO_V1 = 'sopmec:v1:';

  function lerV1(chave) {
    if (!armazenamento.disponivel()) return null;
    try {
      return window.localStorage.getItem(PREFIXO_V1 + chave);
    } catch (e) {
      return null;
    }
  }

  function apagarV1(chave) {
    try {
      window.localStorage.removeItem(PREFIXO_V1 + chave);
    } catch (e) {
      /* fica para a próxima abertura */
    }
  }

  function migrarDaVersao1() {
    var tema = lerV1('tema');
    if (tema !== null && (armazenamento.ler('tema') !== null || tema === 'auto' || !(tema === 'light' || tema === 'dark') || armazenamento.gravar('tema', tema))) {
      apagarV1('tema');
    }
    var ultimo = lerV1('ultimo');
    if (ultimo !== null && (armazenamento.ler('ultimo') !== null || armazenamento.gravar('ultimo', ultimo))) apagarV1('ultimo');
  }

  function migrarListaDaVersao1(l) {
    var bruto = lerV1('check:' + l.nome);
    if (bruto === null) return;
    var ids = null;
    try {
      ids = JSON.parse(bruto);
    } catch (e) {
      ids = null;
    }
    if (Array.isArray(ids) && armazenamento.ler(chaveLista(l.nome)) === null) {
      var digitais = l.caixas.filter(function (c) { return ids.indexOf(c.el.id) >= 0; }).map(function (c) { return c.digital; });
      if (digitais.length && !armazenamento.gravarJSON(chaveLista(l.nome), digitais)) return; // sem espaço: tenta na próxima
    }
    apagarV1('check:' + l.nome);
  }

  /* ---------- Tema (antes da primeira pintura) ---------- */
  var NOME_TEMA = { auto: 'automático', light: 'claro', dark: 'escuro' };

  function temaSalvo() {
    var t = armazenamento.ler('tema');
    return t === 'light' || t === 'dark' ? t : 'auto';
  }

  function aplicarTema(tema) {
    var raiz = document.documentElement;
    if (tema === 'light' || tema === 'dark') raiz.setAttribute('data-theme', tema);
    else raiz.removeAttribute('data-theme');
  }

  seguro('dados da versão 1', migrarDaVersao1);
  var temaAtual = temaSalvo();
  aplicarTema(temaAtual);
  // Antes da primeira pintura: com JS, o CSS mantém o sumário recolhido no celular até o curso.js
  // terminar (classe js-pronto), e o conteúdo não salta quando ele é recolhido de fato.
  document.documentElement.classList.add('js');
  // Um favorito do banco precisa de seus controles primeiro. As seções anteriores conservam content-visibility:
  // auto; forçá-las a visible aqui diagramava toda a teoria e mantinha esse custo em cada troca de tema.
  var entradaE1 = /^(e1|e2)$/.test(idModulo() || '');

  function sistemaEscuro() {
    return !!(window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
  }

  /** O 1º clique sempre muda a aparência: automático → oposto do sistema → igual ao sistema → automático. */
  function proximoTema(atual) {
    var sistema = sistemaEscuro() ? 'dark' : 'light';
    var oposto = sistema === 'dark' ? 'light' : 'dark';
    if (atual === 'auto') return oposto;
    if (atual === oposto) return sistema;
    return 'auto';
  }

  function rotularBotoesTema() {
    paraArray(document.querySelectorAll('[data-acao="tema"]')).forEach(function (b) {
      b.textContent = 'Tema: ' + NOME_TEMA[temaAtual];
      b.setAttribute('title', 'Alternar o tema da página (automático, claro ou escuro)');
    });
  }

  function configurarBotoesTema() {
    var botoes = paraArray(document.querySelectorAll('[data-acao="tema"]'));
    botoes.forEach(function (b) {
      b.hidden = false;
      b.addEventListener('click', function () {
        temaAtual = proximoTema(temaAtual);
        if (temaAtual === 'auto') armazenamento.apagar('tema');
        else armazenamento.gravar('tema', temaAtual);
        aplicarTema(temaAtual);
        rotularBotoesTema();
      });
    });
    rotularBotoesTema();
  }

  function sincronizarTema() {
    temaAtual = temaSalvo();
    aplicarTema(temaAtual);
    rotularBotoesTema();
  }

  /* ---------- Página ---------- */
  function idModulo() {
    var meta = document.querySelector('meta[name="curso:modulo"]');
    var valor = meta ? (meta.getAttribute('content') || '').trim() : '';
    return RE_MODULO.test(valor) ? valor : null;
  }

  function chaveBanco(tipo) {
    return 'sopmec:' + tipo + ':v2:' + (idModulo() || 'e1');
  }

  var MODULO = null;

  /* ---------- Questões: dados e estado ---------- */
  var dadosQuestao = new WeakMap();
  var ctxQuestoes = null;

  function lerEstadoModulo() {
    var vazio = { respostas: {}, erros: {}, simulado: null };
    if (!MODULO) return vazio;
    var bruto = armazenamento.lerJSON('mod:' + MODULO, registrarCorrompido('mod:' + MODULO));
    if (!bruto || typeof bruto !== 'object' || bruto.v !== 2) return vazio;
    var validas = ctxQuestoes ? ctxQuestoes.digitais : {};
    var estado = { respostas: {}, erros: {}, simulado: null };
    if (bruto.respostas && typeof bruto.respostas === 'object') {
      Object.keys(bruto.respostas).forEach(function (d) {
        var l = bruto.respostas[d];
        if (RE_DIGITAL.test(d) && validas[d] && LETRAS.indexOf(l) >= 0) estado.respostas[d] = l;
      });
    }
    if (bruto.erros && typeof bruto.erros === 'object') {
      Object.keys(bruto.erros).forEach(function (d) {
        var n = bruto.erros[d];
        if (RE_DIGITAL.test(d) && validas[d] && inteiroValido(n, LIMITE_ERROS) && n > 0) estado.erros[d] = n;
      });
    }
    var s = bruto.simulado;
    if (s && typeof s === 'object') {
      var sim = { inicio: null, fim: null, corrigido: s.corrigido === true, marcadas: {} };
      if (inteiroValido(s.inicio)) sim.inicio = s.inicio;
      if (inteiroValido(s.fim)) sim.fim = s.fim;
      if (s.marcadas && typeof s.marcadas === 'object') {
        Object.keys(s.marcadas).forEach(function (d) {
          var l = s.marcadas[d];
          if (RE_DIGITAL.test(d) && validas[d] && LETRAS.indexOf(l) >= 0) sim.marcadas[d] = l;
        });
      }
      estado.simulado = sim;
    }
    return estado;
  }

  function resumirEstado(estado) {
    var total = ctxQuestoes ? ctxQuestoes.lista.length : 0;
    var respondidas = 0;
    var acertos = 0;
    var simulado = ctxQuestoes && ctxQuestoes.modo === 'simulado';
    (ctxQuestoes ? ctxQuestoes.lista : []).forEach(function (d) {
      var letra = simulado ? (estado.simulado ? estado.simulado.marcadas[d.digital] : null) : estado.respostas[d.digital];
      if (!letra) return;
      respondidas += 1;
      if (letra === d.gabarito) acertos += 1;
    });
    var r = { total: total, respondidas: respondidas, acertos: acertos, versao: ctxQuestoes ? ctxQuestoes.versao : '' };
    if (simulado) r.corrigido = !!(estado.simulado && estado.simulado.corrigido);
    return r;
  }

  function estadoVazio(estado) {
    return !Object.keys(estado.respostas).length && !Object.keys(estado.erros).length &&
      !(estado.simulado && (estado.simulado.inicio || Object.keys(estado.simulado.marcadas).length));
  }

  /** Lê o estado salvo agora (outra aba pode ter mudado), aplica a mudança e grava (ler → mudar → gravar). */
  function alterarEstado(mudar) {
    var estado = lerEstadoModulo();
    var baseMudanca = {
      respostas: JSON.parse(JSON.stringify(estado.respostas)),
      erros: JSON.parse(JSON.stringify(estado.erros)),
      simulado: estado.simulado ? JSON.parse(JSON.stringify(estado.simulado)) : null
    };
    mudar(estado);
    if (MODULO) {
      if (estadoVazio(estado)) {
        armazenamento.apagar('mod:' + MODULO);
      } else {
        armazenamento.gravarJSON('mod:' + MODULO, {
          v: 2,
          versao: ctxQuestoes ? ctxQuestoes.versao : '',
          respostas: estado.respostas,
          erros: estado.erros,
          simulado: estado.simulado,
          resumo: resumirEstado(estado),
          atualizado: Date.now()
        }, baseMudanca);
      }
    }
    ctxQuestoes.estado = estado;
    return estado;
  }

  function prepararQuestao(q) {
    var gabarito = (q.getAttribute('data-gabarito') || '').trim();
    if (LETRAS.indexOf(gabarito) < 0) return null;
    var lista = q.querySelector('.q-alternativas');
    var enunciado = q.querySelector('.q-enunciado');
    if (!lista || !enunciado) return null;
    var itens = paraArray(lista.children).filter(function (li) {
      return li.tagName === 'LI' && LETRAS.indexOf(li.getAttribute('data-letra')) >= 0;
    });
    if (itens.length !== LETRAS.length) return null;

    var partes = [normalizarDigital(textoDaDigital(enunciado))];
    itens.forEach(function (li) { partes.push(normalizarDigital(textoDaDigital(li))); });
    partes.push(gabarito);
    var digital = fnv1a(partes.join(SEPARADOR));

    lista.classList.add('ativa');
    var botoes = [];
    itens.forEach(function (li) {
      var letra = li.getAttribute('data-letra');
      var botao = criar('button', 'alt');
      botao.type = 'button';
      botao.setAttribute('data-letra', letra);
      botao.setAttribute('aria-pressed', 'false');
      var marcaLetra = criar('span', 'alt-letra', letra);
      marcaLetra.setAttribute('aria-hidden', 'true');
      var leitor = criar('span', 'sr-only', 'Alternativa ' + letra + ': ');
      var texto = criar('span', 'alt-texto');
      while (li.firstChild) texto.appendChild(li.firstChild);
      var selo = criar('span', 'alt-selo');
      botao.appendChild(marcaLetra);
      botao.appendChild(leitor);
      botao.appendChild(texto);
      botao.appendChild(selo);
      li.appendChild(botao);
      botao.addEventListener('click', function () {
        escolher(q, letra);
      });
      botoes.push(botao);
    });

    var cabecalho = q.querySelector('.q-cabecalho');
    var jaErrou = criar('span', 'chip chip-erro', 'Você já errou esta questão');
    jaErrou.hidden = true;
    if (cabecalho) cabecalho.appendChild(jaErrou);

    var feedback = criar('p', 'q-feedback');
    feedback.setAttribute('role', 'status');
    feedback.setAttribute('aria-live', 'polite');
    var acoes = criar('div', 'q-acoes');
    acoes.hidden = true;
    var refazer = criar('button', 'botao', 'Tentar de novo');
    refazer.type = 'button';
    refazer.addEventListener('click', function () {
      tentarDeNovo(q);
    });
    acoes.appendChild(refazer);

    var resolucao = q.querySelector('.q-resolucao');
    if (resolucao) ligarRotuloDaResolucao(resolucao);
    if (resolucao) {
      q.insertBefore(feedback, resolucao);
      q.insertBefore(acoes, resolucao);
    } else {
      q.appendChild(feedback);
      q.appendChild(acoes);
    }

    var d = {
      q: q,
      gabarito: gabarito,
      digital: digital,
      area: (q.getAttribute('data-area') || '').trim(),
      botoes: botoes,
      feedback: feedback,
      acoes: acoes,
      jaErrou: jaErrou,
      resolucao: resolucao
    };
    dadosQuestao.set(q, d);
    return d;
  }

  /** "Ver gabarito e comentário" vira "Ocultar gabarito e comentário" com a resolução aberta, como nos flashcards. */
  function ligarRotuloDaResolucao(resolucao) {
    var resumo = resolucao.querySelector('summary');
    if (!resumo || resumo.children.length) return;
    var fechado = resumo.textContent.trim();
    if (!/^Ver /.test(fechado)) return;
    var aberto = fechado.replace(/^Ver /, 'Ocultar ');
    function atualizar() {
      var texto = resolucao.open ? aberto : fechado;
      if (resumo.textContent !== texto) resumo.textContent = texto;
    }
    resolucao.addEventListener('toggle', atualizar);
    atualizar();
  }

  function limparVisual(d) {
    d.q.removeAttribute('data-respondida');
    d.botoes.forEach(function (b) {
      b.classList.remove('correta', 'errada', 'selecionada');
      b.removeAttribute('aria-disabled');
      b.setAttribute('aria-pressed', 'false');
      b.querySelector('.alt-selo').textContent = '';
    });
    d.feedback.className = 'q-feedback';
    d.feedback.textContent = '';
    d.acoes.hidden = true;
  }

  /** Mostra a correção de uma questão: letra marcada (ou null = em branco) × gabarito. */
  function mostrarCorrecao(d, letra, anunciar, permitirRefazer) {
    var certo = letra === d.gabarito;
    d.q.setAttribute('data-respondida', letra || '-');
    d.botoes.forEach(function (b) {
      var l = b.getAttribute('data-letra');
      var selo = b.querySelector('.alt-selo');
      b.classList.remove('correta', 'errada', 'selecionada');
      b.setAttribute('aria-disabled', 'true');
      b.setAttribute('aria-pressed', l === letra ? 'true' : 'false');
      selo.textContent = '';
      if (l === d.gabarito) {
        b.classList.add('correta');
        selo.textContent = l === letra ? '✓ Sua resposta: certa' : '✓ Resposta certa';
      }
      if (l === letra && !certo) {
        b.classList.add('errada');
        selo.textContent = '✗ Sua resposta: errada';
      }
    });
    var texto;
    if (!letra) texto = 'Sem resposta. Gabarito: ' + d.gabarito + '.';
    else if (certo) texto = 'Você acertou. Gabarito: ' + d.gabarito + '.';
    else texto = 'Você marcou ' + letra + ', mas o gabarito é ' + d.gabarito + '.';
    d.feedback.className = 'q-feedback ' + (certo ? 'ok' : 'erro');
    if (anunciar) {
      // A região viva já existe (vazia) desde a carga: trocar o texto gera o anúncio.
      d.feedback.textContent = texto;
    } else {
      // Ao restaurar respostas salvas, não anunciar dezenas de mensagens de uma vez.
      d.feedback.setAttribute('aria-live', 'off');
      d.feedback.textContent = texto;
      window.setTimeout(function () { d.feedback.setAttribute('aria-live', 'polite'); }, 0);
    }
    d.acoes.hidden = !permitirRefazer;
  }

  function marcarSelecao(d, letra) {
    d.botoes.forEach(function (b) {
      var sel = b.getAttribute('data-letra') === letra;
      b.classList.toggle('selecionada', sel);
      b.setAttribute('aria-pressed', sel ? 'true' : 'false');
      b.querySelector('.alt-selo').textContent = sel ? 'Marcada' : '';
    });
    if (letra) d.q.setAttribute('data-marcada', letra);
    else d.q.removeAttribute('data-marcada');
  }

  function escolher(q, letra) {
    var d = dadosQuestao.get(q);
    if (!d || !ctxQuestoes) return;
    if (ctxQuestoes.modo === 'simulado') {
      var est = ctxQuestoes.estado;
      if (est.simulado && est.simulado.corrigido) return;
      alterarEstado(function (e) {
        if (!e.simulado) e.simulado = { inicio: null, fim: null, corrigido: false, marcadas: {} };
        if (e.simulado.corrigido) return;
        if (!e.simulado.inicio) e.simulado.inicio = Date.now();
        e.simulado.marcadas[d.digital] = letra;
      });
      renderizarQuestoes();
      return;
    }
    if (q.hasAttribute('data-respondida')) return;
    alterarEstado(function (e) {
      e.respostas[d.digital] = letra;
      if (letra !== d.gabarito) e.erros[d.digital] = incrementarErro(e.erros[d.digital]);
    });
    mostrarCorrecao(d, letra, true, true);
    if (d.resolucao) d.resolucao.open = true;
    atualizarMarcasDeErro();
    atualizarPlacar();
  }

  function tentarDeNovo(q) {
    var d = dadosQuestao.get(q);
    if (!d) return;
    alterarEstado(function (e) {
      delete e.respostas[d.digital];
    });
    limparVisual(d);
    if (d.resolucao) d.resolucao.open = false;
    atualizarPlacar();
    if (d.botoes[0]) d.botoes[0].focus();
  }

  function atualizarMarcasDeErro() {
    var erros = ctxQuestoes.estado.erros;
    ctxQuestoes.lista.forEach(function (d) {
      var errou = !!erros[d.digital];
      if (d.jaErrou.hidden === errou) d.jaErrou.hidden = !errou;
      if (d.q.classList.contains('ja-errou') !== errou) d.q.classList.toggle('ja-errou', errou);
    });
  }

  /** Redesenha todas as questões a partir do estado (carga, outra aba, voltar do histórico). */
  function renderizarQuestoes() {
    if (!ctxQuestoes) return;
    var estado = ctxQuestoes.estado;
    var simulado = ctxQuestoes.modo === 'simulado';
    var corrigido = simulado && estado.simulado && estado.simulado.corrigido;
    if (ctxQuestoes.secao) ctxQuestoes.secao.classList.toggle('corrigido', !!corrigido);
    ctxQuestoes.lista.forEach(function (d) {
      if (simulado) {
        var marcada = estado.simulado ? estado.simulado.marcadas[d.digital] || null : null;
        limparVisual(d);
        if (corrigido) mostrarCorrecao(d, marcada, false, false);
        else marcarSelecao(d, marcada);
      } else {
        var letra = estado.respostas[d.digital];
        var atual = d.q.getAttribute('data-respondida');
        if (letra && atual !== letra) mostrarCorrecao(d, letra, false, true);
        if (!letra && atual) {
          limparVisual(d);
          if (d.resolucao) d.resolucao.open = false;
        }
      }
    });
    if (!simulado) atualizarMarcasDeErro();
    atualizarPlacar();
  }

  /* ---------- Confirmação sem prazo, protegida contra duplo clique ---------- */
  var contadorConfirmacao = 0;

  function montarConfirmacao(pergunta, textoConfirmar, aoConfirmar, aoCancelar) {
    contadorConfirmacao += 1;
    var id = 'confirmar-' + contadorConfirmacao;
    var caixa = criar('div', 'confirmar');
    caixa.setAttribute('role', 'group');
    caixa.setAttribute('aria-labelledby', id);
    caixa.hidden = true;
    var texto = criar('p', 'confirmar-texto', pergunta);
    texto.id = id;
    var cancelar = criar('button', 'botao', 'Cancelar');
    cancelar.type = 'button';
    var confirmar = criar('button', 'botao botao-perigo', textoConfirmar);
    confirmar.type = 'button';
    var armadoEm = 0;
    cancelar.addEventListener('click', function () {
      caixa.hidden = true;
      if (aoCancelar) aoCancelar();
    });
    confirmar.addEventListener('click', function () {
      if (Date.now() - armadoEm < ESPERA_CONFIRMAR_MS) return; // duplo clique ou tecla segurada
      caixa.hidden = true;
      aoConfirmar();
    });
    caixa.appendChild(texto);
    caixa.appendChild(cancelar);
    caixa.appendChild(confirmar);
    return {
      caixa: caixa,
      abrir: function (novaPergunta) {
        if (novaPergunta) texto.textContent = novaPergunta;
        armadoEm = Date.now();
        caixa.hidden = false;
        cancelar.focus();
      },
      fechar: function () { caixa.hidden = true; }
    };
  }

  /* ---------- Placar (modo estudo e modo simulado) ---------- */
  // O placar é montado antes da primeira pintura da seção de questões (anteciparComponentes), com os números do
  // portal: quem abre o módulo direto em #questoes (pelo "Continuar") não vê as questões saltarem para baixo quando
  // ele aparece. O iniciar() depois só o liga ao estado completo. Os botões conferem ctxQuestoes na hora do clique.
  var placarAntecipado = null;

  function criarPlacar(caixa, modo) {
    while (caixa.firstChild) caixa.removeChild(caixa.firstChild);
    var p = { caixa: caixa, modo: modo };
    p.texto = criar('p', 'placar-texto');
    p.texto.setAttribute('aria-live', 'polite');
    p.texto.setAttribute('tabindex', '-1');
    p.barra = criar('div', 'placar-barra');
    p.barra.setAttribute('aria-hidden', 'true');
    p.preenchimento = criar('span');
    p.barra.appendChild(p.preenchimento);
    p.acoes = criar('div', 'placar-acoes');
    p.aviso = criar('p', 'placar-aviso');
    p.aviso.setAttribute('role', 'status');
    p.aviso.hidden = true;

    p.proxima = criar('button', 'botao', modo === 'simulado' ? 'Ir para a próxima sem marcar' : 'Ir para a próxima não respondida');
    p.proxima.type = 'button';
    p.proxima.addEventListener('click', function () {
      if (!ctxQuestoes) return;
      var alvo = ctxQuestoes.lista.filter(function (d) {
        if (ctxQuestoes.modo === 'simulado') return !d.q.hasAttribute('data-marcada');
        return !d.q.hasAttribute('data-respondida') && !d.q.hidden && getComputedStyle(d.q).display !== 'none';
      })[0];
      if (!alvo) return;
      alvo.q.scrollIntoView({ block: 'start' });
      if (alvo.botoes[0]) alvo.botoes[0].focus({ preventScroll: true });
    });
    p.acoes.appendChild(p.proxima);

    if (modo === 'simulado') {
      p.finalizar = criar('button', 'botao botao-primario', 'Finalizar e corrigir');
      p.finalizar.type = 'button';
      p.recomecar = criar('button', 'botao', 'Recomeçar simulado');
      p.recomecar.type = 'button';
      p.confirmacao = montarConfirmacao('', 'Finalizar', function () { if (ctxQuestoes) finalizarSimulado(); }, function () { p.finalizar.focus(); });
      p.confRecomecar = montarConfirmacao('Apagar as marcações e o resultado deste simulado e começar de novo?', 'Sim, recomeçar', function () {
        if (!ctxQuestoes) return;
        alterarEstado(function (e) { e.simulado = null; });
        renderizarQuestoes();
        p.texto.focus();
      }, function () { p.recomecar.focus(); });
      p.finalizar.addEventListener('click', function () {
        if (!ctxQuestoes) return;
        var r = resumirEstado(ctxQuestoes.estado);
        var faltam = r.total - r.respondidas;
        if (faltam > 0) p.confirmacao.abrir('Ainda há ' + pluralizar(faltam, 'questão sem marcar', 'questões sem marcar') + '. Finalizar e corrigir mesmo assim?');
        else finalizarSimulado();
      });
      p.recomecar.addEventListener('click', function () { p.confRecomecar.abrir(); });
      p.acoes.appendChild(p.finalizar);
      p.acoes.appendChild(p.recomecar);
      p.acoes.appendChild(p.confirmacao.caixa);
      p.acoes.appendChild(p.confRecomecar.caixa);
      p.resultado = criar('div', 'sim-resultado');
      p.resultado.setAttribute('tabindex', '-1');
      p.resultado.hidden = true;
    } else {
      p.soErros = criar('button', 'botao', 'Só as que errei');
      p.soErros.type = 'button';
      p.soErros.setAttribute('aria-pressed', 'false');
      p.soErros.addEventListener('click', function () {
        if (!ctxQuestoes) return;
        var ativo = !ctxQuestoes.secao.classList.contains('filtro-erros');
        ctxQuestoes.secao.classList.toggle('filtro-erros', ativo);
        atualizarPlacar();
      });
      p.refazerTodas = criar('button', 'botao', 'Refazer todas');
      p.refazerTodas.type = 'button';
      p.confirmacao = montarConfirmacao('Apagar todas as suas respostas deste módulo? O registro das questões que você já errou é mantido.', 'Sim, apagar', function () {
        if (!ctxQuestoes) return;
        alterarEstado(function (e) { e.respostas = {}; });
        ctxQuestoes.lista.forEach(function (d) {
          limparVisual(d);
          if (d.resolucao) d.resolucao.open = false;
        });
        p.refazerTodas.hidden = false;
        atualizarPlacar('Respostas apagadas. ');
        p.texto.focus();
      }, function () {
        p.refazerTodas.hidden = false;
        p.refazerTodas.focus();
      });
      p.refazerTodas.addEventListener('click', function () {
        p.refazerTodas.hidden = true;
        p.confirmacao.abrir();
      });
      p.acoes.appendChild(p.soErros);
      p.acoes.appendChild(p.refazerTodas);
      p.acoes.appendChild(p.confirmacao.caixa);
    }

    caixa.appendChild(p.texto);
    caixa.appendChild(p.barra);
    caixa.appendChild(p.acoes);
    caixa.appendChild(p.aviso);
    if (p.resultado) caixa.appendChild(p.resultado);
    return p;
  }

  function montarPlacar() {
    var caixa = ctxQuestoes.secao ? ctxQuestoes.secao.querySelector('[data-placar]') : document.querySelector('[data-placar]');
    if (!caixa) return;
    var antecipado = placarAntecipado && placarAntecipado.caixa === caixa && placarAntecipado.modo === ctxQuestoes.modo;
    var p = antecipado ? placarAntecipado : criarPlacar(caixa, ctxQuestoes.modo);
    placarAntecipado = null;
    ctxQuestoes.placar = p;
    caixa.hidden = false;
    armazenamento.aoMudarAviso(atualizarAvisoPlacar);
    atualizarAvisoPlacar();
  }

  /** Placar provisório (antes do iniciar): mesmos textos, com os números que o portal calcula do registro. */
  function preencherPlacarProvisorio(p, secao) {
    var mid = idModulo();
    var reg = window.CURSO_REGISTRO;
    var m = mid && reg && reg.modulos ? reg.modulos[mid] : null;
    if (!m || !m.questoes || typeof m.questoes !== 'object') return;
    var digitais = Object.keys(m.questoes);
    var r = progressoDoModulo(mid) || { total: digitais.length, respondidas: 0, acertos: 0 };
    var estado = armazenamento.lerJSON('mod:' + mid);
    if (!estado || typeof estado !== 'object' || estado.v !== 2) estado = null;
    var sim = p.modo === 'simulado' && estado && estado.simulado && typeof estado.simulado === 'object' ? estado.simulado : null;
    var dur = secao ? parseInt(secao.getAttribute('data-duracao-min') || '', 10) : NaN;
    p.texto.textContent = textoDoPlacar(p.modo, r, sim, inteiroValido(dur) && dur > 0 && dur <= 600 ? dur : 0);
    p.preenchimento.style.width = (r.total ? (r.respondidas / r.total) * 100 : 0) + '%';
    if (p.modo === 'simulado') {
      p.finalizar.hidden = !!(sim && sim.corrigido);
      p.recomecar.hidden = !sim;
    } else {
      var erros = estado && estado.erros && typeof estado.erros === 'object' ? digitais.filter(function (d) { return !!estado.erros[d]; }).length : 0;
      p.soErros.textContent = rotuloSoErros(erros, false);
    }
  }

  function anteciparPlacar() {
    if (placarAntecipado) return;
    var caixa = document.querySelector('[data-placar]');
    if (!caixa) return;
    var secao = caixa.closest('section');
    var modo = secao && secao.getAttribute('data-modo') === 'simulado' ? 'simulado' : 'estudo';
    var p = criarPlacar(caixa, modo);
    placarAntecipado = p;
    preencherPlacarProvisorio(p, secao);
    caixa.hidden = false;
  }

  function atualizarAvisoPlacar() {
    if (!ctxQuestoes || !ctxQuestoes.placar) return;
    var msg = MODULO ? armazenamento.aviso() : 'Esta página não tem identificação de módulo; as respostas não são salvas.';
    ctxQuestoes.placar.aviso.textContent = msg || '';
    ctxQuestoes.placar.aviso.hidden = !msg;
  }

  function textoTempoSimulado(sim, duracaoMin) {
    if (!sim || !sim.inicio) return '';
    var fim = sim.corrigido && sim.fim ? sim.fim : Date.now();
    var tempo = ' · Tempo: ' + formatarTempo(fim - sim.inicio);
    if (duracaoMin) tempo += ' de ' + formatarTempo(duracaoMin * 60000) + (fim - sim.inicio > duracaoMin * 60000 ? ' (tempo esgotado)' : '');
    return tempo;
  }

  function textoDoPlacar(modo, r, sim, duracaoMin, prefixo) {
    if (modo === 'simulado') {
      var corpo = sim && sim.corrigido ? 'Simulado corrigido: ' + r.acertos + ' de ' + r.total + ' acertos' : 'Marcadas: ' + r.respondidas + ' de ' + r.total;
      return (prefixo || '') + corpo + textoTempoSimulado(sim, duracaoMin);
    }
    var pct = r.respondidas ? Math.round((r.acertos * 100) / r.respondidas) : 0;
    return (prefixo || '') + 'Respondidas: ' + r.respondidas + ' de ' + r.total +
      ' · Acertos: ' + r.acertos + (r.respondidas ? ' (' + pct + '% das respondidas)' : '');
  }

  function rotuloSoErros(nErros, filtrando) {
    return filtrando ? 'Mostrar todas as questões' : 'Só as que errei (' + nErros + ')';
  }

  function atualizarPlacar(prefixo) {
    if (!ctxQuestoes || !ctxQuestoes.placar) return;
    var p = ctxQuestoes.placar;
    var estado = ctxQuestoes.estado;
    var r = resumirEstado(estado);
    if (ctxQuestoes.modo === 'simulado') {
      var sim = estado.simulado;
      var corrigido = !!(sim && sim.corrigido);
      p.texto.textContent = textoDoPlacar('simulado', r, sim, ctxQuestoes.duracaoMin, prefixo);
      p.preenchimento.style.width = (r.total ? (r.respondidas / r.total) * 100 : 0) + '%';
      p.proxima.disabled = corrigido || r.respondidas >= r.total;
      p.finalizar.hidden = corrigido;
      p.finalizar.disabled = r.respondidas === 0;
      p.recomecar.hidden = !sim;
      desenharResultado(corrigido, r);
      gerenciarRelogio(sim && sim.inicio && !corrigido);
      return;
    }
    p.texto.textContent = textoDoPlacar('estudo', r, null, 0, prefixo);
    p.preenchimento.style.width = (r.total ? (r.respondidas / r.total) * 100 : 0) + '%';
    p.proxima.disabled = r.respondidas >= r.total;
    var nErros = ctxQuestoes.lista.filter(function (d) { return !!estado.erros[d.digital]; }).length;
    var filtrando = ctxQuestoes.secao.classList.contains('filtro-erros');
    if (filtrando && nErros === 0) {
      ctxQuestoes.secao.classList.remove('filtro-erros');
      filtrando = false;
    }
    p.soErros.textContent = rotuloSoErros(nErros, filtrando);
    p.soErros.setAttribute('aria-pressed', filtrando ? 'true' : 'false');
    p.soErros.disabled = !filtrando && nErros === 0;
    p.refazerTodas.disabled = r.respondidas === 0;
  }

  var relogio = null;

  function gerenciarRelogio(ligado) {
    if (ligado && !relogio) {
      relogio = window.setInterval(function () { seguro('relógio do simulado', function () { atualizarPlacar(); }); }, 1000);
    } else if (!ligado && relogio) {
      window.clearInterval(relogio);
      relogio = null;
    }
  }

  function finalizarSimulado() {
    alterarEstado(function (e) {
      if (!e.simulado) e.simulado = { inicio: Date.now(), fim: null, corrigido: false, marcadas: {} };
      e.simulado.corrigido = true;
      e.simulado.fim = Date.now();
      ctxQuestoes.lista.forEach(function (d) {
        var l = e.simulado.marcadas[d.digital];
        if (l && l !== d.gabarito) e.erros[d.digital] = incrementarErro(e.erros[d.digital]);
      });
    });
    renderizarQuestoes();
    var p = ctxQuestoes.placar;
    if (p && p.resultado && !p.resultado.hidden) p.resultado.focus();
  }

  function desenharResultado(corrigido, r) {
    var p = ctxQuestoes.placar;
    if (!p.resultado) return;
    while (p.resultado.firstChild) p.resultado.removeChild(p.resultado.firstChild);
    if (!corrigido) {
      p.resultado.hidden = true;
      return;
    }
    var estado = ctxQuestoes.estado;
    var titulo = criar('p', 'sim-resultado-titulo', 'Resultado: ' + r.acertos + ' de ' + r.total + ' questões (' + (r.total ? Math.round((r.acertos * 100) / r.total) : 0) + '%)');
    p.resultado.appendChild(titulo);
    var areas = {};
    var ordem = [];
    ctxQuestoes.lista.forEach(function (d) {
      var a = d.area || 'Geral';
      if (!areas[a]) {
        areas[a] = { questoes: 0, acertos: 0 };
        ordem.push(a);
      }
      areas[a].questoes += 1;
      if (estado.simulado && estado.simulado.marcadas[d.digital] === d.gabarito) areas[a].acertos += 1;
    });
    var envoltorio = criar('div', 'tabela tabela-grade');
    var tabela = criar('table');
    var legenda = criar('caption', '', 'Acertos por bloco');
    tabela.appendChild(legenda);
    var cab = criar('thead');
    var linhaCab = criar('tr');
    ['Bloco', 'Acertos', 'Questões', '%'].forEach(function (t) {
      var th = criar('th', '', t);
      th.setAttribute('scope', 'col');
      linhaCab.appendChild(th);
    });
    cab.appendChild(linhaCab);
    tabela.appendChild(cab);
    var corpo = criar('tbody');
    ordem.forEach(function (a) {
      var tr = criar('tr');
      var th = criar('th', '', a);
      th.setAttribute('scope', 'row');
      tr.appendChild(th);
      tr.appendChild(criar('td', 'num', String(areas[a].acertos)));
      tr.appendChild(criar('td', 'num', String(areas[a].questoes)));
      tr.appendChild(criar('td', 'num', Math.round((areas[a].acertos * 100) / areas[a].questoes) + '%'));
      corpo.appendChild(tr);
    });
    tabela.appendChild(corpo);
    envoltorio.appendChild(tabela);
    p.resultado.appendChild(envoltorio);
    p.resultado.appendChild(criar('p', 'nota', 'As questões erradas ficam registradas para revisão, e cada uma mostra agora o gabarito e o comentário.'));
    p.resultado.hidden = false;
  }

  // Bancos complementares: itens de origem e versões autorais no estilo Avalia.
  // IDs e chaves próprios mantêm separados os placares de cada banco.
  var reveladoresBanco = Object.create(null);
  function iniciarBancoConcursos() {
    iniciarBanco('questoes-reais', 'cr', chaveBanco('concursos'));
    iniciarBanco('treino-avalia', 'av', chaveBanco('avalia'));
  }

  function digitalDoBanco(item) {
    var enunciado = item.querySelector('.cr-enunciado');
    var partes = [normalizarDigital(textoDaDigital(enunciado))];
    paraArray(enunciado.querySelectorAll('img')).forEach(function (img) {
      partes.push(img.getAttribute('src') || '', img.getAttribute('alt') || '');
    });
    paraArray(item.querySelectorAll('input[type="radio"]')).forEach(function (radio) {
      partes.push(radio.value, normalizarDigital(textoDaDigital(radio.closest('label'))));
    });
    partes.push(item.dataset.crGabarito);
    return fnv1a(partes.join(SEPARADOR));
  }

  function iniciarBanco(secao, prefixo, chave) {
    var banco = document.getElementById(secao);
    if (!banco) return;
    var itens = Array.from(banco.querySelectorAll('.concurso-item, .avalia-item'));
    // A seção tem 80 artigos. Grupos pequenos usam a mesma contenção dos blocos da aula, conservando os
    // artigos, IDs e ordem; entrar no banco não exige diagramar os 80 enunciados e alternativas no mesmo quadro.
    // A impressão já desfaz a contenção de .bloco-aula, e sem JS os artigos mantêm sua estrutura original.
    if (!banco.querySelector('.cr-lote')) {
      var lote = null;
      itens.forEach(function (item, i) {
        if (i % 4 === 0) {
          lote = criar('div', 'bloco-aula cr-lote');
          item.parentNode.insertBefore(lote, item);
        }
        lote.appendChild(item);
      });
    }
    var lotes = Array.from(banco.querySelectorAll('.cr-lote'));
    var assunto = banco.querySelector('#' + prefixo + '-assunto');
    var banca = banco.querySelector('#' + prefixo + '-banca');
    var busca = banco.querySelector('#' + prefixo + '-busca');
    var pendentes = banco.querySelector('#' + prefixo + '-pendentes');
    var placar = banco.querySelector('#' + prefixo + '-placar');
    var aviso = banco.querySelector('#' + prefixo + '-armazenamento');
    var respostas = Object.create(null);
    var digitais = Object.create(null);
    var pendencias = Object.create(null);
    var legado = false;
    var gravacao = true;
    itens.forEach(function (item) { digitais[item.id] = digitalDoBanco(item); });
    function normalizarBusca(t) {
      return t.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    }
    function informarArmazenamento() {
      aviso.textContent = gravacao
        ? 'As últimas respostas deste banco ficam salvas neste navegador, separadas do placar das questões autorais.'
        : 'O navegador não permitiu ler ou salvar este banco. As tentativas novas ficam nesta página e podem se perder ao sair ou recarregar. Os dados anteriores não foram substituídos.';
      if (legado) aviso.textContent += ' Há tentativas antigas sem identificação do conteúdo. Elas foram preservadas no armazenamento anterior, mas você precisa responder novamente para contar no placar atual.';
    }
    function lerRespostas() {
      var bruto = window.localStorage.getItem(chave);
      var dados = bruto === null ? { v: 2, respostas: {} } : JSON.parse(bruto);
      var limpos = Object.create(null);
      if (!dados || dados.v !== 2 || !dados.respostas || typeof dados.respostas !== 'object' || Array.isArray(dados.respostas)) throw new Error('Formato de respostas do banco não reconhecido.');
      Object.keys(dados.respostas).forEach(function (digital) {
        var valor = dados.respostas[digital];
        if (/^[a-f0-9]{8}$/.test(digital) && /^[A-E]$/.test(valor)) limpos[digital] = valor;
      });
      return limpos;
    }
    function aplicarPendencias(dados) {
      Object.keys(pendencias).forEach(function (digital) {
        if (pendencias[digital] === null) delete dados[digital];
        else dados[digital] = pendencias[digital];
      });
      return dados;
    }
    function atualizarRespostas(dados) {
      var atuais = Object.create(null);
      itens.forEach(function (item) {
        var valor = dados[digitais[item.id]];
        if (item.querySelector('input[value="' + valor + '"]')) atuais[item.id] = valor;
      });
      respostas = atuais;
    }
    try {
      atualizarRespostas(lerRespostas());
      var anterior = window.localStorage.getItem(chave.replace(':v2:', ':v1:'));
      legado = anterior !== null && anterior !== '{}';
    } catch (e) { gravacao = false; }
    function salvar(id, valor) {
      if (valor) respostas[id] = valor;
      else delete respostas[id];
      pendencias[digitais[id]] = valor || null;
      try {
        // Relê antes de gravar, preservando outras abas e todas as ações locais ainda não salvas.
        // Falha de leitura nunca autoriza substituir o conteúdo do disco por um objeto vazio.
        var atuais = aplicarPendencias(lerRespostas());
        window.localStorage.setItem(chave, JSON.stringify({ v: 2, respostas: atuais }));
        pendencias = Object.create(null);
        atualizarRespostas(atuais);
        itens.forEach(function (item) { mostrarResposta(item, false); });
        gravacao = true;
      } catch (e) { gravacao = false; }
      informarArmazenamento();
    }
    function mostrarResposta(item, abrir) {
      var valor = respostas[item.id];
      var campo = item.querySelector('fieldset');
      var feedback = item.querySelector('.cr-feedback');
      campo.disabled = !!valor;
      item.querySelector('[data-cr-acao="corrigir"]').disabled = !!valor;
      item.querySelector('[data-cr-acao="refazer"]').disabled = !valor;
      item.querySelectorAll('input[type="radio"]').forEach(function (radio) { radio.checked = radio.value === valor; });
      if (!valor) {
        item.removeAttribute('data-cr-resultado');
        feedback.textContent = '';
        return;
      }
      var correta = valor === item.dataset.crGabarito;
      item.dataset.crResultado = correta ? 'certo' : 'errado';
      feedback.textContent = (correta ? 'Resposta correta.' : 'Resposta incorreta.') + ' Sua marcação: ' + valor + '. Gabarito: ' + item.dataset.crGabarito + '. Veja o raciocínio na resolução.';
      if (abrir) item.querySelector('.cr-resolucao').open = true;
    }
    function filtrar() {
      var termo = normalizarBusca(busca.value.trim());
      var visiveis = 0;
      var respondidas = 0;
      var certas = 0;
      itens.forEach(function (item) {
        var valor = respostas[item.id];
        if (valor) { respondidas += 1; if (valor === item.dataset.crGabarito) certas += 1; }
        item.hidden = (assunto.value && item.dataset.crAssunto !== assunto.value)
          || (banca.value && item.dataset.crBanca !== banca.value)
          || (pendentes.checked && !!valor)
          || (termo && item.dataset.crBusca.indexOf(termo) < 0);
        if (!item.hidden) visiveis += 1;
      });
      // Um lote vazio não pode conservar sua altura intrínseca ou lembrada entre resultados do filtro.
      lotes.forEach(function (lote) {
        lote.hidden = !lote.querySelector('.concurso-item:not([hidden]), .avalia-item:not([hidden])');
      });
      placar.textContent = visiveis + ' de ' + itens.length + ' questões exibidas · ' + pluralizar(respondidas, 'respondida', 'respondidas') + ' no banco · ' + pluralizar(certas, 'correta', 'corretas') + ' · ' + pluralizar(respondidas - certas, 'incorreta', 'incorretas') + '.';
      banco.querySelector('#' + prefixo + '-vazio').hidden = visiveis > 0;
    }
    itens.forEach(function (item) {
      // Não pesquisa dentro das soluções: o filtro não revela respostas por correspondência.
      item.dataset.crBusca = normalizarBusca(item.querySelector('.cr-meta').textContent + ' ' + item.querySelector('h3').textContent + ' ' + item.querySelector('.cr-assunto').textContent + ' ' + item.querySelector('.cr-enunciado').textContent + ' ' + item.querySelector('.cr-alternativas').textContent);
      mostrarResposta(item, false);
      item.querySelector('.cr-acoes').hidden = false;
      item.querySelector('[data-cr-acao="corrigir"]').addEventListener('click', function () {
        var marcado = item.querySelector('input:checked');
        if (!marcado) {
          item.querySelector('.cr-feedback').textContent = 'Selecione uma resposta antes de conferir.';
          item.querySelector('input').focus();
          return;
        }
        salvar(item.id, marcado.value);
        mostrarResposta(item, true);
        filtrar();
        if (item.hidden) pendentes.focus();
      });
      item.querySelector('[data-cr-acao="refazer"]').addEventListener('click', function () {
        salvar(item.id, null);
        mostrarResposta(item, false);
        item.querySelector('.cr-resolucao').open = false;
        filtrar();
        item.querySelector('input').focus();
      });
    });
    [assunto, banca, pendentes].forEach(function (campo) { campo.addEventListener('change', filtrar); });
    busca.addEventListener('input', filtrar);
    reveladoresBanco[secao] = function (alvo) {
      var item = alvo.closest('.concurso-item, .avalia-item');
      if (!item || !banco.contains(item) || !item.hidden) return;
      assunto.value = '';
      banca.value = '';
      busca.value = '';
      pendentes.checked = false;
      filtrar();
      placar.textContent += ' Filtros limpos para abrir a questão indicada pelo link.';
    };
    window.addEventListener('beforeprint', function () {
      banco.querySelectorAll('.cr-figura img').forEach(function (img) { img.loading = 'eager'; });
    });
    window.addEventListener('storage', function (evento) {
      if (evento.key !== chave && evento.key !== null) return;
      try {
        atualizarRespostas(aplicarPendencias(lerRespostas()));
        if (!Object.keys(pendencias).length) gravacao = true;
        informarArmazenamento();
      }
      catch (e) { gravacao = false; informarArmazenamento(); return; }
      itens.forEach(function (item) { mostrarResposta(item, false); });
      filtrar();
    });
    informarArmazenamento();
    filtrar();
    banco.querySelector('.cr-controles').hidden = false;
  }

  function iniciarQuestoes() {
    var questoes = paraArray(document.querySelectorAll('article.questao'));
    if (!questoes.length) return;
    var secao = questoes[0].closest('section') || document.body;
    var modo = secao.getAttribute('data-modo') === 'simulado' ? 'simulado' : 'estudo';
    ctxQuestoes = { lista: [], digitais: {}, versao: '', modo: modo, secao: secao, estado: null, placar: null, duracaoMin: 0 };
    if (modo === 'simulado') {
      secao.classList.add('modo-simulado');
      var dur = parseInt(secao.getAttribute('data-duracao-min') || '', 10);
      if (inteiroValido(dur) && dur > 0 && dur <= 600) ctxQuestoes.duracaoMin = dur;
    }
    questoes.forEach(function (q) {
      var d = prepararQuestao(q);
      if (!d) return;
      if (ctxQuestoes.digitais[d.digital]) {
        if (window.console && console.error) console.error('[curso] questões com conteúdo idêntico: ' + q.id);
        return;
      }
      ctxQuestoes.lista.push(d);
      ctxQuestoes.digitais[d.digital] = true;
    });
    ctxQuestoes.versao = fnv1a(ctxQuestoes.lista.map(function (d) { return d.digital; }).join(','));
    ctxQuestoes.estado = lerEstadoModulo();
    montarPlacar();
    renderizarQuestoes();
  }

  function sincronizarQuestoes() {
    if (!ctxQuestoes) return;
    ctxQuestoes.estado = lerEstadoModulo();
    renderizarQuestoes();
  }

  /* ---------- Flashcards ---------- */
  // Grades de flashcards que já têm a barra de ações (montada antes da primeira pintura ou no iniciar).
  var gradesComBarra = [];

  function iniciarFlashcards() {
    paraArray(document.querySelectorAll('.flashcards')).forEach(function (grade) {
      if (grade.querySelector(':scope > details.flashcard')) prepararFlashcards(grade);
    });
  }

  function prepararFlashcards(grade) {
    if (gradesComBarra.indexOf(grade) >= 0) return;
    gradesComBarra.push(grade);
    function cartoes() { return paraArray(grade.querySelectorAll(':scope > details.flashcard')); }
    (function () {
      var barra = criar('div', 'flash-acoes');
      var status = criar('p', 'flash-status');
      status.setAttribute('role', 'status');
      status.setAttribute('aria-live', 'polite');
      function anunciar(t) { status.textContent = t; }
      var abrir = criar('button', 'botao', 'Mostrar todas as respostas');
      abrir.type = 'button';
      abrir.addEventListener('click', function () {
        var lista = cartoes();
        lista.forEach(function (c) { c.open = true; });
        anunciar('Respostas dos ' + lista.length + ' cartões à mostra.');
      });
      var fechar = criar('button', 'botao', 'Ocultar todas');
      fechar.type = 'button';
      fechar.addEventListener('click', function () {
        cartoes().forEach(function (c) { c.open = false; });
        anunciar('Respostas ocultadas.');
      });
      var embaralhar = criar('button', 'botao', 'Embaralhar');
      embaralhar.type = 'button';
      embaralhar.addEventListener('click', function () {
        var antes = paraArray(grade.querySelectorAll(':scope > details.flashcard'));
        var ordem = antes.slice();
        for (var tentativa = 0; tentativa < 10; tentativa += 1) {
          for (var i = ordem.length - 1; i > 0; i -= 1) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = ordem[i];
            ordem[i] = ordem[j];
            ordem[j] = tmp;
          }
          var mudou = ordem.some(function (c, k) { return c !== antes[k]; });
          if (mudou || ordem.length < 2) break;
        }
        var lote = document.createDocumentFragment();
        ordem.forEach(function (c) {
          c.open = false;
          lote.appendChild(c);
        });
        grade.appendChild(lote);
        anunciar('Cartões embaralhados e respostas ocultadas.');
      });
      barra.appendChild(abrir);
      barra.appendChild(fechar);
      barra.appendChild(embaralhar);
      grade.parentNode.insertBefore(barra, grade);
      grade.parentNode.insertBefore(status, grade);
    })();
  }

  /* ---------- Listas de verificação (por módulo e por item) ---------- */
  var listas = [];

  function chaveLista(nome) {
    return 'check:' + (MODULO || 'pagina') + ':' + nome;
  }

  function lerMarcados(nome) {
    var salvo = armazenamento.lerJSON(chaveLista(nome), registrarCorrompido(chaveLista(nome)));
    var marcados = {};
    if (Array.isArray(salvo)) {
      salvo.forEach(function (d) {
        if (typeof d === 'string' && RE_DIGITAL.test(d)) marcados[d] = true;
      });
    }
    return marcados;
  }

  function desenharLista(l) {
    var marcados = lerMarcados(l.nome);
    l.caixas.forEach(function (c) { c.el.checked = !!marcados[c.digital]; });
  }

  function atualizarNotasListas() {
    var aviso = armazenamento.aviso();
    listas.forEach(function (l) {
      if (!l.nota) return;
      l.nota.textContent = aviso ? l.textoBase + ' ' + aviso : l.textoBase + ' As marcações ficam salvas neste navegador.';
      l.nota.classList.toggle('aviso', !!aviso);
    });
  }

  function iniciarChecklists() {
    paraArray(document.querySelectorAll('[data-checklist]')).forEach(function (el) {
      var nome = el.getAttribute('data-checklist');
      if (!RE_LISTA.test(nome)) return;
      var caixas = paraArray(el.querySelectorAll('input[type="checkbox"]')).map(function (c) {
        var rotulo = c.closest('label');
        return { el: c, digital: fnv1a(normalizarDigital(rotulo ? textoDaDigital(rotulo) : c.id)) };
      });
      var nota = document.querySelector('[data-nota-checklist="' + nome + '"]');
      var l = { nome: nome, caixas: caixas, nota: nota, textoBase: nota ? nota.textContent.trim() : '' };
      seguro('lista da versão 1', function () { migrarListaDaVersao1(l); });
      caixas.forEach(function (c) {
        c.el.addEventListener('change', function () {
          var marcados = lerMarcados(nome); // ler → mudar → gravar
          if (c.el.checked) marcados[c.digital] = true;
          else delete marcados[c.digital];
          var ids = Object.keys(marcados);
          if (ids.length) armazenamento.gravarJSON(chaveLista(nome), ids);
          else armazenamento.apagar(chaveLista(nome));
        });
      });
      listas.push(l);
      desenharLista(l);
    });
    if (listas.length) {
      armazenamento.aoMudarAviso(atualizarNotasListas);
      atualizarNotasListas();
    }
  }

  /* ---------- Sumário: recolhível, seção ativa e atalho no celular ---------- */
  var secaoAtual = null;

  /** Abre o sumário no computador e o recolhe no celular; depois, só age ao cruzar o limite de largura. */
  function ajustarSumarioALargura() {
    var caixa = document.querySelector('.sumario-caixa');
    if (!caixa || !window.matchMedia) return;
    var estreita = window.matchMedia(ESTREITA);
    function aplicar(consulta) {
      caixa.open = !consulta.matches;
    }
    aplicar(estreita);
    // Só age ao cruzar o limite (girar o tablet, redimensionar); entre cruzamentos, vale a escolha do aluno.
    if (estreita.addEventListener) estreita.addEventListener('change', aplicar);
    else if (estreita.addListener) estreita.addListener(aplicar);
  }

  function iniciarSumario() {
    var links = paraArray(document.querySelectorAll('.sumario a[href^="#"]'));
    if (!links.length || !('IntersectionObserver' in window)) return;
    var alvos = [];
    var linkDe = new Map();
    links.forEach(function (a) {
      var id;
      try {
        id = decodeURIComponent(a.getAttribute('href').slice(1));
      } catch (e) {
        return;
      }
      var alvo = document.getElementById(id);
      if (alvo) {
        alvos.push(alvo);
        linkDe.set(alvo, a);
      }
    });
    if (!alvos.length) return;
    var visiveis = new Set();
    function marcar(atual) {
      links.forEach(function (a) { a.removeAttribute('aria-current'); });
      linkDe.get(atual).setAttribute('aria-current', 'true');
      if (secaoAtual !== atual) {
        secaoAtual = atual;
        seguro('visita', registrarVisita);
      }
    }
    function noFimDaPagina() {
      var doc = document.documentElement;
      return window.innerHeight + window.scrollY >= doc.scrollHeight - 4;
    }
    function marcarAtual() {
      // No fim da página, a última seção pode ser curta demais para entrar na faixa observada.
      if (noFimDaPagina()) {
        marcar(alvos[alvos.length - 1]);
        return;
      }
      var atual = null;
      visiveis.forEach(function (el) {
        if (!atual || el.getBoundingClientRect().top < atual.getBoundingClientRect().top) atual = el;
      });
      if (atual) marcar(atual);
    }
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) visiveis.add(e.target);
        else visiveis.delete(e.target);
      });
      marcarAtual();
    }, { rootMargin: '-12% 0px -70% 0px' });
    alvos.forEach(function (alvo) { observador.observe(alvo); });
    var pendente = false;
    window.addEventListener('scroll', function () {
      if (pendente) return;
      pendente = true;
      window.requestAnimationFrame(function () {
        pendente = false;
        if (noFimDaPagina()) marcarAtual();
      });
    }, { passive: true });
  }

  /* ---------- Saltos para âncoras (seções com content-visibility) ---------- */
  // Seções fora da tela têm altura provisória (content-visibility: auto). Num salto para uma âncora (sumário, link com
  // #, "Continuar" do portal), as do caminho ganham o tamanho real depois do salto e o alvo sai do lugar: o Chrome
  // segura pela ancoragem de rolagem, o Firefox não (parava centenas de pixels antes). Depois do salto, o alvo é
  // conferido por alguns quadros e reposicionado até assentar, a menos que a pessoa comece a rolar.
  var saltoAtual = 0;
  var entradaInterrompida = false;
  var ancoraInicialAssentada = '';
  var eventosEntrada = ['wheel', 'touchstart', 'keydown', 'mousedown'];
  function interromperEntrada() { entradaInterrompida = true; }

  function estabilizarVizinhoBanco(banco) {
    var anterior = banco.previousElementSibling;
    if (!anterior || anterior.tagName !== 'SECTION') return;
    var blocos = anterior.querySelectorAll('.cr-lote, article.questao');
    // O auto também pré-renderiza vizinhos acima da tela. No Edge, as duas questões anteriores à última
    // cresciam depois da pintura e moviam o banco em 449 px. Mede o pequeno trecho final antes do salto.
    var vizinhos = Array.prototype.slice.call(blocos, Math.max(0, blocos.length - (anterior.id === 'questoes' ? 3 : 2)));
    var caixas = [anterior].concat(vizinhos);
    var anteriores = caixas.map(function (el) {
      var salvo = { el: el, visibilidade: el.style.contentVisibility, contencao: el.style.contain };
      // Só a seção vizinha e seus últimos blocos ganham tamanho real. Os outros filhos continuam em auto.
      // Conserva a contenção de layout/pintura do auto durante a medida, inclusive as margens dos artigos.
      el.style.contain = 'layout style paint';
      el.style.contentVisibility = 'visible';
      return salvo;
    });
    var alturas = caixas.map(function (el) {
      var estilo = getComputedStyle(el);
      return Math.max(0, el.getBoundingClientRect().height - (parseFloat(estilo.paddingTop) || 0)
        - (parseFloat(estilo.paddingBottom) || 0) - (parseFloat(estilo.borderTopWidth) || 0)
        - (parseFloat(estilo.borderBottomWidth) || 0));
    });
    anteriores.forEach(function (salvo, i) {
      salvo.el.style.containIntrinsicBlockSize = 'auto ' + alturas[i] + 'px';
      salvo.el.style.contentVisibility = salvo.visibilidade;
      salvo.el.style.contain = salvo.contencao;
    });
    // A reserva vale para esta largura. Redimensionar devolve as estimativas do CSS; a renderização nativa
    // aprende os tamanhos da nova largura quando o aluno navega para as caixas novamente.
    function limpar() {
      caixas.forEach(function (el) { el.style.containIntrinsicBlockSize = ''; });
      window.removeEventListener('resize', limpar);
    }
    window.addEventListener('resize', limpar, { passive: true });
  }

  function assentarAncora(id) {
    var alvo = id ? document.getElementById(id) : null;
    if (!alvo || !window.requestAnimationFrame) return;
    var banco = alvo.closest('.banco-concursos');
    if (banco && reveladoresBanco[banco.id]) reveladoresBanco[banco.id](alvo);
    var meu = saltoAtual += 1;
    var mexeu = false;
    var eventos = ['wheel', 'touchstart', 'keydown', 'mousedown'];
    function parar() { mexeu = true; }
    eventos.forEach(function (t) { window.addEventListener(t, parar, { passive: true }); });
    function encerrar() { eventos.forEach(function (t) { window.removeEventListener(t, parar); }); }
    var quadros = 0;
    function conferir() {
      if (mexeu || meu !== saltoAtual) return encerrar();
      quadros += 1;
      var folga = parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop) || 0;
      var topo = alvo.getBoundingClientRect().top;
      var noFim = window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2;
      if (Math.abs(topo - folga) > 2 && !(noFim && topo > folga)) alvo.scrollIntoView({ block: 'start' });
      if (quadros < 20) window.requestAnimationFrame(conferir);
      else encerrar();
    }
    // Resolve o primeiro salto ainda na tarefa que publicou os controles. As conferências seguintes corrigem
    // alturas que o navegador aprende ao tornar o alvo visível, antes da pintura de cada quadro.
    conferir();
  }

  function idDaAncora(hash) {
    try {
      return decodeURIComponent(String(hash || '').replace(/^#/, ''));
    } catch (e) {
      return '';
    }
  }

  function iniciarAncoras() {
    document.addEventListener('click', function (ev) {
      var a = ev.target && ev.target.closest ? ev.target.closest('a[href^="#"]') : null;
      if (!a || ev.defaultPrevented || a.getAttribute('href').length < 2) return;
      var id = idDaAncora(a.getAttribute('href'));
      window.requestAnimationFrame(function () { if (!ev.defaultPrevented) assentarAncora(id); });
    });
    window.addEventListener('hashchange', function () { assentarAncora(idDaAncora(window.location.hash)); });
    var inicial = idDaAncora(window.location.hash);
    if (inicial && inicial !== ancoraInicialAssentada && !entradaInterrompida) assentarAncora(inicial);
    eventosEntrada.forEach(function (t) { window.removeEventListener(t, interromperEntrada); });
  }

  function iniciarAtalhoSumario() {
    var nav = document.getElementById('sumario');
    var caixa = nav ? nav.querySelector('.sumario-caixa') : null;
    if (!nav || !caixa || !window.matchMedia) return;
    var botao = criar('a', 'ir-sumario', 'Sumário');
    botao.href = '#sumario';
    botao.hidden = true;
    botao.addEventListener('click', function (ev) {
      ev.preventDefault();
      caixa.open = true;
      nav.scrollIntoView({ block: 'start' });
      var resumo = caixa.querySelector('summary');
      if (resumo) resumo.focus({ preventScroll: true });
    });
    document.body.appendChild(botao);
    var estreita = window.matchMedia(ESTREITA);
    var pendente = false;
    function atualizar() {
      pendente = false;
      botao.hidden = !(estreita.matches && nav.getBoundingClientRect().bottom < 0);
    }
    window.addEventListener('scroll', function () {
      if (!pendente) {
        pendente = true;
        window.requestAnimationFrame(atualizar);
      }
    }, { passive: true });
    if (estreita.addEventListener) estreita.addEventListener('change', atualizar);
    else if (estreita.addListener) estreita.addListener(atualizar);
    window.requestAnimationFrame(atualizar);
  }

  /* ---------- Tabelas: rolagem acessível das grades e cartões no celular ---------- */
  // Mesmo limite do CSS em que as tabelas viram cartões.
  var TABELAS_EM_CARTOES = '(max-width: 39.99rem)';
  var contadorTabelas = 0;

  /**
   * Cada tabela é medida quando é diagramada (ResizeObserver), sem forçar a diagramação da página inteira: num
   * módulo longo, ler a largura de todas as tabelas no início custava centenas de milissegundos no celular. As
   * que rolam para os lados ganham foco por teclado, rótulo e o aviso visível; as que viram cartões ganham os
   * papéis ARIA de tabela.
   */
  function ajustarTabelas(tabelas) {
    // Lê todas as medidas antes de escrever qualquer coisa: um só cálculo de layout, em vez de um por tabela.
    var rolam = tabelas.map(function (t) { return t.scrollWidth > t.clientWidth + 1; });
    var emCartoes = !!(window.matchMedia && window.matchMedia(TABELAS_EM_CARTOES).matches);
    tabelas.forEach(function (t, i) {
      var rola = rolam[i];
      if (emCartoes && !t.classList.contains('tabela-grade')) manterSemanticaDaTabela(t.querySelector('table'));
      var dica = t.previousElementSibling && t.previousElementSibling.classList.contains('tabela-dica') ? t.previousElementSibling : null;
      t.classList.toggle('rola', rola);
      if (rola) {
        t.setAttribute('tabindex', '0');
        t.setAttribute('role', 'region');
        if (!t.hasAttribute('aria-label') || t.hasAttribute('data-rotulo-auto')) {
          var legenda = t.querySelector('caption');
          t.setAttribute('aria-label', (legenda ? legenda.textContent.trim() : 'Tabela') + ' (role para os lados para ver todas as colunas)');
          t.setAttribute('data-rotulo-auto', '');
        }
        if (!dica) {
          dica = criar('p', 'tabela-dica', 'Deslize a tabela para os lados para ver todas as colunas →');
          dica.setAttribute('aria-hidden', 'true');
          t.parentNode.insertBefore(dica, t);
        }
      } else {
        t.removeAttribute('tabindex');
        t.removeAttribute('role');
        if (t.hasAttribute('data-rotulo-auto')) {
          t.removeAttribute('aria-label');
          t.removeAttribute('data-rotulo-auto');
        }
        if (dica) dica.parentNode.removeChild(dica);
      }
    });
  }

  /**
   * Em cartões (display: block no CSS), alguns navegadores deixam de anunciar a tabela como tabela. Papéis ARIA
   * explícitos (os mesmos da semântica nativa) mantêm a navegação por células nos leitores de tela.
   */
  function manterSemanticaDaTabela(tabela) {
    if (!tabela || tabela.getAttribute('role') === 'table') return;
    contadorTabelas += 1;
    tabela.setAttribute('role', 'table');
    var legenda = tabela.querySelector('caption');
    if (legenda) {
      if (!legenda.id) legenda.id = 'tabela-legenda-' + contadorTabelas;
      tabela.setAttribute('aria-labelledby', legenda.id);
    }
    paraArray(tabela.querySelectorAll('thead, tbody, tfoot')).forEach(function (g) { g.setAttribute('role', 'rowgroup'); });
    paraArray(tabela.querySelectorAll('tr')).forEach(function (tr) { tr.setAttribute('role', 'row'); });
    paraArray(tabela.querySelectorAll('th')).forEach(function (th) {
      th.setAttribute('role', th.getAttribute('scope') === 'row' ? 'rowheader' : 'columnheader');
    });
    paraArray(tabela.querySelectorAll('td')).forEach(function (td) { td.setAttribute('role', 'cell'); });
  }

  function iniciarTabelas() {
    var tabelas = paraArray(document.querySelectorAll('.tabela'));
    if (!tabelas.length) return;
    // A semântica não depende de a tabela já ter sido diagramada pelo ResizeObserver.
    // Isso inclui tabelas recolhidas em details e em seções fora da tela.
    tabelas.forEach(function (t) {
      if (!t.classList.contains('tabela-grade')) manterSemanticaDaTabela(t.querySelector('table'));
    });
    if (window.ResizeObserver) {
      var observador = new window.ResizeObserver(function (entradas) {
        seguro('tabelas', function () { ajustarTabelas(entradas.map(function (e) { return e.target; })); });
      });
      tabelas.forEach(function (t) { observador.observe(t); });
      return;
    }
    ajustarTabelas(tabelas);
    var espera = null;
    window.addEventListener('resize', function () {
      if (espera) window.clearTimeout(espera);
      espera = window.setTimeout(function () {
        seguro('tabelas', function () { ajustarTabelas(paraArray(document.querySelectorAll('.tabela'))); });
      }, 150);
    });
  }

  /* ---------- Links para módulos do registro (a seta dos links externos é só CSS) ---------- */
  function atualizarRefsModulos() {
    var reg = window.CURSO_REGISTRO;
    if (!reg || typeof reg !== 'object' || !reg.modulos) return;
    var prefixo = document.body.classList.contains('pg-modulo') ? '' : 'modulos/';
    paraArray(document.querySelectorAll('a[data-ref-modulo]')).forEach(function (a) {
      var id = a.getAttribute('data-ref-modulo');
      var m = RE_MODULO.test(id) ? reg.modulos[id] : null;
      if (!m || typeof m.arquivo !== 'string' || !RE_ARQUIVO.test(m.arquivo)) return;
      if (m.publicado === true) {
        a.setAttribute('href', prefixo + m.arquivo);
      } else if (!a.querySelector('.ref-status')) {
        a.appendChild(criar('span', 'ref-status', ' (em produção)'));
      }
    });
  }

  /* ---------- Continuar de onde parou e progresso no portal ---------- */
  function registrarVisita() {
    if (!MODULO) return;
    var arquivo = (window.location.pathname.split('/').pop() || '');
    try {
      arquivo = decodeURIComponent(arquivo);
    } catch (e) {
      return;
    }
    if (!RE_ARQUIVO.test(arquivo)) return;
    var registro = { modulo: MODULO, arquivo: arquivo, quando: Date.now() };
    if (secaoAtual && RE_SECAO.test(secaoAtual.id)) {
      registro.secao = secaoAtual.id;
      var titulo = secaoAtual.querySelector('h2');
      if (titulo) registro.secaoTitulo = titulo.textContent.trim().slice(0, 120);
    }
    armazenamento.gravarJSON('ultimo', registro);
  }

  function mostrarContinuar() {
    var caixa = document.querySelector('[data-continuar]');
    if (!caixa) return;
    var link = caixa.querySelector('a');
    var detalhe = caixa.querySelector('[data-continuar-detalhe]');
    var ultimo = armazenamento.lerJSON('ultimo');
    caixa.hidden = true;
    if (!ultimo || typeof ultimo !== 'object' || typeof ultimo.arquivo !== 'string' || !RE_ARQUIVO.test(ultimo.arquivo)) return;
    var origem = document.querySelector('.lista-modulos a[href="modulos/' + ultimo.arquivo + '"]');
    if (!origem || !link) return;
    var destino = 'modulos/' + ultimo.arquivo;
    if (typeof ultimo.secao === 'string' && RE_SECAO.test(ultimo.secao)) destino += '#' + ultimo.secao;
    link.setAttribute('href', destino);
    link.textContent = origem.textContent.trim();
    if (detalhe) {
      detalhe.textContent = typeof ultimo.secaoTitulo === 'string' && ultimo.secao ? 'Última seção vista: ' + ultimo.secaoTitulo.slice(0, 120) : '';
    }
    caixa.hidden = false;
  }

  /**
   * Progresso de cada módulo no portal, calculado a partir das respostas salvas e da lista ATUAL de questões
   * do módulo (digital → gabarito, gerada em assets/registro.js). Respostas de questões que mudaram ou saíram
   * não contam, e portal e módulo mostram sempre os mesmos números, mesmo depois de uma atualização.
   */
  function progressoDoModulo(modulo) {
    var reg = window.CURSO_REGISTRO;
    var m = reg && reg.modulos && reg.modulos[modulo];
    if (!m || !m.questoes || typeof m.questoes !== 'object') return null;
    var estado = armazenamento.lerJSON('mod:' + modulo);
    if (!estado || typeof estado !== 'object' || estado.v !== 2) return null;
    var simulado = !!(estado.simulado && typeof estado.simulado === 'object' && m.tipo === 'simulado');
    var respostas = simulado ? estado.simulado.marcadas : estado.respostas;
    if (!respostas || typeof respostas !== 'object') return null;
    var total = 0;
    var respondidas = 0;
    var acertos = 0;
    Object.keys(m.questoes).forEach(function (d) {
      total += 1;
      var l = respostas[d];
      if (RE_DIGITAL.test(d) && LETRAS.indexOf(l) >= 0) {
        respondidas += 1;
        if (l === m.questoes[d]) acertos += 1;
      }
    });
    return { total: total, respondidas: respondidas, acertos: acertos, simulado: simulado, corrigido: simulado && estado.simulado.corrigido === true };
  }

  function mostrarProgressoPortal() {
    paraArray(document.querySelectorAll('.lista-modulos [data-modulo][data-total-questoes]')).forEach(function (item) {
      var modulo = item.getAttribute('data-modulo');
      var alvo = item.querySelector('[data-progresso]');
      if (!alvo) return;
      alvo.hidden = true;
      if (!RE_MODULO.test(modulo)) return;
      var r = progressoDoModulo(modulo);
      if (!r || !r.total || !r.respondidas) return;
      var texto = alvo.querySelector('[data-progresso-texto]');
      var barra = alvo.querySelector('[data-progresso-barra]');
      if (texto) {
        var questoes = r.respondidas + ' de ' + r.total + (r.total === 1 ? ' questão' : ' questões');
        if (r.simulado && !r.corrigido) texto.textContent = questoes + ' marcadas · simulado em andamento';
        else texto.textContent = questoes + ' · ' + pluralizar(r.acertos, 'acerto', 'acertos');
      }
      if (barra) barra.style.width = (r.respondidas / r.total) * 100 + '%';
      alvo.hidden = false;
    });
  }

  /* ---------- Painel "Seu progresso" (portal): exportar, importar, apagar ---------- */
  function coletarProgresso() {
    var dados = {};
    armazenamento.chaves().forEach(function (k) {
      var v = armazenamento.ler(k.slice(PREFIXO.length));
      if (typeof v === 'string') dados[k] = v;
    });
    return { curso: 'sopmec', v: 2, exportado: new Date().toISOString(), dados: dados };
  }

  function objetoImportavel(x) { return !!x && typeof x === 'object' && !Array.isArray(x); }
  function camposPermitidos(x, nomes) {
    return objetoImportavel(x) && Object.keys(x).every(function (k) { return nomes.indexOf(k) >= 0; });
  }
  function mapaImportavel(x, erros) {
    return objetoImportavel(x) && Object.keys(x).every(function (d) {
      return RE_DIGITAL.test(d) && (erros ? inteiroValido(x[d], LIMITE_ERROS) : LETRAS.indexOf(x[d]) >= 0);
    });
  }
  function chavePublicaValida(chave) {
    var partes = chave.split(':');
    if (chave === 'tema' || chave === 'ultimo') return true;
    return (partes[0] === 'mod' && partes.length === 2 && RE_MODULO.test(partes[1])) ||
      (partes[0] === 'check' && partes.length === 3 && RE_MODULO.test(partes[1]) && RE_LISTA.test(partes[2]));
  }
  function itemImportavel(chave, texto) {
    if (chave.indexOf('corrompido:') === 0) {
      // Cópia opaca de diagnóstico: aceita somente destino público conhecido; nunca é consumida como progresso.
      return chavePublicaValida(chave.slice('corrompido:'.length)) && texto.length <= 100000;
    }
    if (!chavePublicaValida(chave)) return false;
    if (chave === 'tema') return texto === 'light' || texto === 'dark';
    var x;
    try { x = JSON.parse(texto); } catch (e) { return false; }
    if (chave.indexOf('check:') === 0) return Array.isArray(x) && x.every(function (d) { return typeof d === 'string' && RE_DIGITAL.test(d); }) && new Set(x).size === x.length;
    if (chave === 'ultimo') {
      return camposPermitidos(x, ['modulo', 'arquivo', 'quando', 'secao', 'secaoTitulo']) &&
        typeof x.modulo === 'string' && RE_MODULO.test(x.modulo) && typeof x.arquivo === 'string' && RE_ARQUIVO.test(x.arquivo) &&
        inteiroValido(x.quando, Number.MAX_SAFE_INTEGER) &&
        (x.secao === undefined || (typeof x.secao === 'string' && RE_SECAO.test(x.secao))) &&
        (x.secaoTitulo === undefined || (typeof x.secaoTitulo === 'string' && x.secaoTitulo.length <= 120 && typeof x.secao === 'string'));
    }
    if (!camposPermitidos(x, ['v', 'versao', 'respostas', 'erros', 'simulado', 'resumo', 'atualizado']) || x.v !== 2 || !mapaImportavel(x.respostas, false) ||
      (x.erros !== undefined && !mapaImportavel(x.erros, true)) ||
      (x.versao !== undefined && (typeof x.versao !== 'string' || !RE_DIGITAL.test(x.versao))) ||
      (x.atualizado !== undefined && !inteiroValido(x.atualizado, Number.MAX_SAFE_INTEGER))) return false;
    var s = x.simulado;
    if (s !== undefined && s !== null && (!camposPermitidos(s, ['inicio', 'fim', 'corrigido', 'marcadas']) ||
      !mapaImportavel(s.marcadas, false) || typeof s.corrigido !== 'boolean' ||
      !(s.inicio === null || inteiroValido(s.inicio, Number.MAX_SAFE_INTEGER)) ||
      !(s.fim === null || inteiroValido(s.fim, Number.MAX_SAFE_INTEGER)) ||
      (s.fim !== null && (s.inicio === null || s.fim < s.inicio)) ||
      (s.corrigido && s.fim === null) || (!s.corrigido && s.fim !== null))) return false;
    var r = x.resumo;
    return r === undefined || (camposPermitidos(r, ['total', 'respondidas', 'acertos', 'versao', 'corrigido']) &&
      inteiroValido(r.total, Number.MAX_SAFE_INTEGER) && inteiroValido(r.respondidas, r.total) && inteiroValido(r.acertos, r.respondidas) &&
      typeof r.versao === 'string' && RE_DIGITAL.test(r.versao) && (r.corrigido === undefined || typeof r.corrigido === 'boolean'));
  }

  function validarImportacao(texto) {
    if (typeof texto !== 'string' || !texto.trim()) return { erro: 'Cole o conteúdo do arquivo exportado ou escolha o arquivo.' };
    if (texto.length > 2000000) return { erro: 'O arquivo é grande demais para ser um progresso do curso.' };
    var obj;
    try {
      obj = JSON.parse(texto);
    } catch (e) {
      return { erro: 'O conteúdo não é um arquivo de progresso válido (JSON ilegível).' };
    }
    if (!objetoImportavel(obj) || obj.curso !== 'sopmec' || obj.v !== 2 || !objetoImportavel(obj.dados)) {
      return { erro: 'Este arquivo não é um progresso exportado por este curso.' };
    }
    var dados = {};
    var chaves = Object.keys(obj.dados);
    for (var i = 0; i < chaves.length; i += 1) {
      var k = chaves[i];
      var v = obj.dados[k];
      if (k.indexOf(PREFIXO) !== 0 || typeof v !== 'string' || v.length > 200000 || k.length > 200 || !itemImportavel(k.slice(PREFIXO.length), v)) {
        return { erro: 'O arquivo tem um item inválido (' + k.slice(0, 60) + ').' };
      }
      dados[k] = v;
    }
    return { dados: dados, total: chaves.length };
  }

  function iniciarPainelProgresso() {
    var painel = document.querySelector('[data-painel-progresso]');
    if (!painel) return;
    var status = criar('p', 'painel-status');
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    var acoes = criar('div', 'painel-acoes');
    var exportar = criar('button', 'botao', 'Exportar progresso');
    exportar.type = 'button';
    var importar = criar('button', 'botao', 'Importar progresso');
    importar.type = 'button';
    var apagar = criar('button', 'botao', 'Apagar todo o progresso');
    apagar.type = 'button';
    acoes.appendChild(exportar);
    acoes.appendChild(importar);
    acoes.appendChild(apagar);

    var areaExport = criar('div', 'painel-bloco');
    areaExport.hidden = true;
    var rotuloExp = criar('label', '', 'Progresso exportado (guarde este texto ou baixe o arquivo):');
    rotuloExp.setAttribute('for', 'progresso-exportado');
    var textoExp = criar('textarea', 'painel-texto');
    textoExp.id = 'progresso-exportado';
    textoExp.readOnly = true;
    textoExp.rows = 5;
    var copiar = criar('button', 'botao', 'Copiar');
    copiar.type = 'button';
    var baixar = criar('a', 'botao', 'Baixar arquivo');
    areaExport.appendChild(rotuloExp);
    areaExport.appendChild(textoExp);
    var linhaExp = criar('div', 'painel-acoes');
    linhaExp.appendChild(copiar);
    linhaExp.appendChild(baixar);
    areaExport.appendChild(linhaExp);

    var areaImport = criar('div', 'painel-bloco');
    areaImport.hidden = true;
    var rotuloArq = criar('label', '', 'Escolha o arquivo exportado…');
    rotuloArq.setAttribute('for', 'progresso-arquivo');
    var arquivo = criar('input');
    arquivo.type = 'file';
    arquivo.id = 'progresso-arquivo';
    arquivo.accept = '.json,application/json';
    var rotuloImp = criar('label', '', '…ou cole aqui o texto exportado:');
    rotuloImp.setAttribute('for', 'progresso-importar');
    var textoImp = criar('textarea', 'painel-texto');
    textoImp.id = 'progresso-importar';
    textoImp.rows = 5;
    var aplicarImp = criar('button', 'botao botao-primario', 'Importar');
    aplicarImp.type = 'button';
    areaImport.appendChild(rotuloArq);
    areaImport.appendChild(arquivo);
    areaImport.appendChild(rotuloImp);
    areaImport.appendChild(textoImp);
    var linhaImp = criar('div', 'painel-acoes');
    linhaImp.appendChild(aplicarImp);
    areaImport.appendChild(linhaImp);

    var pendente = null;
    var confImportar = montarConfirmacao('Isso substitui todo o progresso salvo neste navegador pelo do arquivo. Continuar?', 'Sim, importar', function () {
      if (!pendente) return;
      var ok = armazenamento.substituir(pendente.dados);
      status.textContent = ok ? 'Progresso importado: ' + pluralizar(pendente.total, 'item', 'itens') + '.' : 'Não foi possível importar. O progresso anterior foi preservado. ' + (armazenamento.aviso() || 'Erro ao gravar.');
      pendente = null;
      sincronizarTudo();
      importar.focus();
    }, function () { aplicarImp.focus(); });
    var confApagar = montarConfirmacao('Apagar todo o progresso deste curso neste navegador (respostas, erros registrados, listas, tema e "continuar")? Não dá para desfazer; se quiser, exporte antes.', 'Sim, apagar tudo', function () {
      var n = armazenamento.chaves().length;
      var ok = armazenamento.substituir({});
      status.textContent = ok ? (n ? 'Progresso apagado.' : 'Não havia progresso salvo.') : 'Não foi possível apagar o progresso. O progresso anterior foi preservado e continua disponível para exportar. ' + (armazenamento.aviso() || 'Erro ao gravar.');
      sincronizarTudo();
      apagar.focus();
    }, function () { apagar.focus(); });

    exportar.addEventListener('click', function () {
      var dados = coletarProgresso();
      var texto = JSON.stringify(dados);
      textoExp.value = texto;
      areaImport.hidden = true;
      areaExport.hidden = false;
      var n = Object.keys(dados.dados).length;
      status.textContent = n ? 'Progresso pronto para exportar: ' + pluralizar(n, 'item', 'itens') + '.' : 'Ainda não há progresso salvo para exportar.';
      if (armazenamento.aviso()) status.textContent = 'Cópia do progresso disponível nesta página, incluindo ações ainda não salvas. ' + armazenamento.aviso();
      try {
        var blob = new Blob([texto], { type: 'application/json' });
        if (baixar.href && baixar.href.indexOf('blob:') === 0) URL.revokeObjectURL(baixar.href);
        baixar.href = URL.createObjectURL(blob);
        baixar.setAttribute('download', 'progresso-curso-sop-' + new Date().toISOString().slice(0, 10) + '.json');
      } catch (e) {
        baixar.hidden = true;
      }
      textoExp.focus();
      textoExp.select();
    });
    copiar.addEventListener('click', function () {
      function selecionar() {
        textoExp.focus();
        textoExp.select();
        status.textContent = 'Texto selecionado: use Ctrl+C para copiar.';
      }
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(textoExp.value).then(function () {
            status.textContent = 'Progresso copiado.';
          }, selecionar);
        } else {
          selecionar();
        }
      } catch (e) {
        selecionar();
      }
    });
    importar.addEventListener('click', function () {
      areaExport.hidden = true;
      areaImport.hidden = false;
      status.textContent = '';
      textoImp.focus();
    });
    arquivo.addEventListener('change', function () {
      var f = arquivo.files && arquivo.files[0];
      if (!f) return;
      if (f.size > 2000000) {
        status.textContent = 'O arquivo é grande demais para ser um progresso do curso.';
        return;
      }
      var leitor = new FileReader();
      leitor.onload = function () {
        textoImp.value = String(leitor.result || '');
        status.textContent = 'Arquivo lido. Confira e clique em Importar.';
      };
      leitor.onerror = function () { status.textContent = 'Não foi possível ler o arquivo escolhido.'; };
      leitor.readAsText(f);
    });
    aplicarImp.addEventListener('click', function () {
      var r = validarImportacao(textoImp.value);
      if (r.erro) {
        status.textContent = r.erro;
        textoImp.focus();
        return;
      }
      pendente = r;
      confImportar.abrir();
    });
    apagar.addEventListener('click', function () { confApagar.abrir(); });

    painel.appendChild(acoes);
    painel.appendChild(confApagar.caixa);
    painel.appendChild(areaExport);
    painel.appendChild(areaImport);
    painel.appendChild(confImportar.caixa);
    painel.appendChild(status);
    var aviso = armazenamento.aviso();
    if (aviso) {
      status.textContent = aviso;
      [importar, apagar].forEach(function (b) { b.disabled = true; });
    }
    painel.hidden = false;

  }

  /* ---------- Impressão: abre gabaritos e flashcards ---------- */
  function iniciarImpressao() {
    var abertosPelaImpressao = [];
    window.addEventListener('beforeprint', function () {
      abertosPelaImpressao = paraArray(document.querySelectorAll('details:not([open])'));
      abertosPelaImpressao.forEach(function (d) { d.open = true; });
    });
    window.addEventListener('afterprint', function () {
      abertosPelaImpressao.forEach(function (d) { d.open = false; });
      abertosPelaImpressao = [];
    });
  }

  /* ---------- Sincronização entre abas e ao voltar pelo histórico ---------- */
  function sincronizarTudo() {
    seguro('tema', sincronizarTema);
    seguro('questões', sincronizarQuestoes);
    seguro('listas', function () { listas.forEach(desenharLista); atualizarNotasListas(); });
    seguro('continuar', mostrarContinuar);
    seguro('progresso', mostrarProgressoPortal);
  }

  function iniciarSincronizacao() {
    window.addEventListener('storage', function (ev) {
      if (ev.key !== null && (typeof ev.key !== 'string' || ev.key.indexOf(PREFIXO) !== 0)) return;
      sincronizarTudo();
    });
    window.addEventListener('pageshow', function (ev) {
      if (ev.persisted) sincronizarTudo();
    });
  }

  /* ---------- Inicialização ---------- */
  /** Uma etapa por tarefa: a inicialização não vira uma tarefa longa (bloqueio de toque e rolagem no celular). */
  function emEtapas(etapas, aoFim, aposPintura) {
    var agendar = window.scheduler && typeof window.scheduler.postTask === 'function'
      ? function (fn) { window.scheduler.postTask(fn, { priority: 'user-visible' }); }
      : function (fn) { window.setTimeout(fn, 0); };
    var i = 0;
    function proxima() {
      if (i >= etapas.length) {
        aoFim();
        return;
      }
      var etapa = etapas[i];
      i += 1;
      seguro(etapa[0], etapa[1]);
      agendar(proxima);
    }
    var comecou = false;
    function comecar() {
      if (comecou) return;
      comecou = true;
      agendar(proxima);
    }
    if (aposPintura && window.requestAnimationFrame) {
      // Dois RAFs ainda podiam chegar antes do FCP no Edge. As atividades fora da tela aguardam a pintura
      // entregue; o conteúdo e seus controles prioritários já foram publicados pela primeira fase.
      var observadorPintura = null;
      var pinturaObservavel = false;
      var limiteEsperaPintura = Date.now() + 2000;
      function pintou() {
        if (observadorPintura) observadorPintura.disconnect();
        comecar();
      }
      try {
        if (!window.PerformanceObserver || !window.performance || !performance.getEntriesByType
          || !PerformanceObserver.supportedEntryTypes || PerformanceObserver.supportedEntryTypes.indexOf('paint') < 0) throw new Error('pintura indisponível');
        pinturaObservavel = true;
        if (performance.getEntriesByType('paint').some(function (e) { return e.name === 'first-contentful-paint'; })) pintou();
        else {
          observadorPintura = new PerformanceObserver(function (lista) {
            if (lista.getEntries().some(function (e) { return e.name === 'first-contentful-paint'; })) pintou();
          });
          observadorPintura.observe({ type: 'paint', buffered: true });
        }
      } catch (e) {
        window.requestAnimationFrame(function () { window.requestAnimationFrame(pintou); });
      }
      function conferirPintura() {
        if (comecou) return;
        // Uma aba visível lenta ainda pode não ter pintado em 250 ms. Alguns navegadores anunciam paint,
        // mas não entregam FCP nesta navegação: o limite garante que os controles sempre sejam iniciados.
        if (!pinturaObservavel || document.hidden || Date.now() >= limiteEsperaPintura || performance.getEntriesByType('paint').some(function (e) { return e.name === 'first-contentful-paint'; })) pintou();
        else window.setTimeout(conferirPintura, 100);
      }
      window.setTimeout(conferirPintura, 250);
    } else comecar();
  }

  /**
   * Enquanto a página carrega, monta o placar e a barra dos flashcards assim que a caixa deles é lida — antes da
   * primeira pintura que os mostra (requestAnimationFrame roda antes de cada pintura). Assim nada salta quando a
   * página abre direto numa seção (#questoes, #flashcards).
   */
  var iniciado = false;
  var observadorEntrada = null;
  var vizinhoPreparado = null;
  var bancoRealPreparado = null;
  var preparandoEntrada = false;
  var entradaAguardando = false;
  function anteciparVizinhoInicial() {
    if (iniciado) return;
    var alvo = document.getElementById(idDaAncora(window.location.hash));
    var banco = alvo && alvo.closest('.banco-concursos');
    // A próxima seção garante que o parser terminou as 30 autorais e os 80 artigos deste banco.
    // Os lotes já contêm o banco antes da rolagem nativa do fragmento no fim do parser. O predecessor é
    // preparado em outra tarefa; converter controles, questões e diagramar o vizinho juntos bloqueava 70 ms.
    if (!banco || banco.id !== 'questoes-reais' || !document.getElementById('treino-avalia')) return;
    observadorEntrada.disconnect();
    preparandoEntrada = true;
    seguro('banco de entrada antecipado', function () {
      iniciarBanco('questoes-reais', 'cr', chaveBanco('concursos'));
      bancoRealPreparado = banco;
    });
    emEtapas([
      ['questões e vizinho anteriores ao banco', function () {
        MODULO = idModulo();
        iniciarQuestoes();
        estabilizarVizinhoBanco(banco);
        vizinhoPreparado = banco;
        if (!entradaInterrompida) {
          ancoraInicialAssentada = idDaAncora(window.location.hash);
          assentarAncora(ancoraInicialAssentada);
        }
      }]
    ], function () {
      preparandoEntrada = false;
      if (entradaAguardando) iniciar();
    }, false);
  }
  function anteciparComponentes() {
    if (iniciado || document.readyState !== 'loading') return;
    var alvo = entradaE1 ? document.getElementById(idDaAncora(window.location.hash)) : null;
    if (!entradaE1 || (alvo && (alvo.id === 'questoes' || alvo.closest('article.questao')))) seguro('placar antecipado', anteciparPlacar);
    if (!entradaE1 || (alvo && (alvo.id === 'flashcards' || alvo.closest('.flashcards')))) seguro('flashcards antecipados', function () {
      paraArray(document.querySelectorAll('.flashcards')).forEach(prepararFlashcards);
    });
    window.requestAnimationFrame(anteciparComponentes);
  }

  function iniciar() {
    if (preparandoEntrada) { entradaAguardando = true; return; }
    iniciado = true;
    if (observadorEntrada) observadorEntrada.disconnect();
    MODULO = idModulo();
    // Fase 1: tudo o que muda a primeira tela (tema, questões e placar, flashcards, sumário, portal e avisos).
    seguro('tema', configurarBotoesTema);
    seguro('registro', atualizarRefsModulos);
    var alvoInicial = document.getElementById(idDaAncora(window.location.hash));
    var bancoInicial = alvoInicial && alvoInicial.closest('.banco-concursos');
    var bancoAntecipado = bancoInicial ? bancoInicial.id : '';
    var questoesAntecipadas = !entradaE1 || bancoAntecipado === 'questoes-reais' || !!(alvoInicial && (alvoInicial.id === 'questoes' || alvoInicial.closest('article.questao')));
    var flashcardsAntecipados = !entradaE1 || !!(alvoInicial && (alvoInicial.id === 'flashcards' || alvoInicial.closest('.flashcards')));
    // O banco e seu vizinho anterior ficam prontos antes do salto. As demais atividades entram em tarefas
    // posteriores; só os últimos blocos vizinhos precisam de medida para manter a âncora na primeira pintura.
    if (questoesAntecipadas && !ctxQuestoes) seguro('questões', iniciarQuestoes);
    if (bancoAntecipado && !bancoRealPreparado) seguro('questões reais', function () { iniciarBanco('questoes-reais', 'cr', chaveBanco('concursos')); });
    if (bancoAntecipado === 'treino-avalia') seguro('treino Avalia', function () { iniciarBanco('treino-avalia', 'av', chaveBanco('avalia')); });
    if (bancoInicial && vizinhoPreparado !== bancoInicial) seguro('vizinho do banco', function () { estabilizarVizinhoBanco(bancoInicial); });
    if (flashcardsAntecipados) seguro('flashcards', iniciarFlashcards);
    seguro('sumário recolhível', ajustarSumarioALargura);
    seguro('sumário', iniciarSumario);
    seguro('âncoras', iniciarAncoras);
    seguro('continuar', mostrarContinuar);
    seguro('progresso', mostrarProgressoPortal);
    seguro('painel de progresso', iniciarPainelProgresso);
    document.documentElement.classList.add('js-pronto');
    // Fase 2: o resto, uma etapa por tarefa; js-completo marca o fim (é o que os testes esperam).
    emEtapas([
      ['questões reais', function () { if (!bancoAntecipado && !bancoRealPreparado) iniciarBanco('questoes-reais', 'cr', chaveBanco('concursos')); }],
      ['treino Avalia', function () { if (bancoAntecipado !== 'treino-avalia') iniciarBanco('treino-avalia', 'av', chaveBanco('avalia')); }],
      ['questões', function () { if (!questoesAntecipadas && !ctxQuestoes) iniciarQuestoes(); }],
      ['flashcards', function () { if (!flashcardsAntecipados) iniciarFlashcards(); }],
      ['listas', iniciarChecklists],
      ['atalho do sumário', iniciarAtalhoSumario],
      ['tabelas', iniciarTabelas],
      ['visita', registrarVisita],
      ['sincronização', iniciarSincronizacao]
    ], function () { document.documentElement.classList.add('js-completo'); }, entradaE1);
  }

  seguro('impressão', iniciarImpressao);
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', iniciar);
    if (window.location.hash.length > 1) eventosEntrada.forEach(function (t) { window.addEventListener(t, interromperEntrada, { passive: true }); });
    if (entradaE1 && window.location.hash.length > 1 && window.MutationObserver) {
      observadorEntrada = new MutationObserver(anteciparVizinhoInicial);
      observadorEntrada.observe(document, { childList: true, subtree: true });
    }
    if (window.requestAnimationFrame) window.requestAnimationFrame(anteciparComponentes);
  } else {
    iniciar();
  }
})();
