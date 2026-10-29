/* Busca e treino de evocação. Não altera as respostas ou o progresso do curso. */
(function () {
  'use strict';
  var ferramentas = document.querySelector('.formulario-ferramentas');
  var fichas = Array.from(document.querySelectorAll('.formula-card'));
  var grupos = Array.from(document.querySelectorAll('.formula-grupo'));
  var busca = document.getElementById('formula-busca');
  var assunto = document.getElementById('formula-assunto');
  var modo = document.getElementById('formula-memorizar');
  var treino = false;
  function normalizar(s) { return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase(); }
  function filtrar() {
    var termos = normalizar(busca.value).trim().split(/\s+/).filter(Boolean);
    var n = 0;
    fichas.forEach(function (f) {
      var texto = normalizar(f.dataset.busca);
      f.hidden = !(assunto.value === 'todos' || assunto.value === f.dataset.grupo) || !termos.every(function (t) { return texto.includes(t); });
      if (!f.hidden) n += 1;
    });
    grupos.forEach(function (g) { g.hidden = !Array.from(g.querySelectorAll('.formula-card')).some(function (f) { return !f.hidden; }); });
    document.getElementById('formula-contagem').textContent = n + ' de ' + fichas.length + ' fichas';
    document.getElementById('formula-vazio').hidden = n !== 0;
  }
  function exibir(f, revelar) {
    f.querySelector('.formula-expressao').hidden = !revelar;
    var botao = f.querySelector('.formula-revelar');
    botao.textContent = revelar ? 'Ocultar fórmula' : 'Revelar fórmula';
    botao.setAttribute('aria-expanded', String(revelar));
  }
  modo.addEventListener('click', function () {
    treino = !treino;
    modo.setAttribute('aria-pressed', String(treino));
    modo.textContent = treino ? 'Sair da memorização' : 'Modo memorização';
    document.getElementById('formula-instrucao').hidden = !treino;
    fichas.forEach(function (f) {
      f.querySelector('.formula-revelar').hidden = !treino;
      exibir(f, !treino);
    });
  });
  fichas.forEach(function (f) {
    f.querySelector('.formula-revelar').addEventListener('click', function () {
      exibir(f, f.querySelector('.formula-expressao').hidden);
    });
  });
  busca.addEventListener('input', filtrar);
  assunto.addEventListener('change', filtrar);
  document.getElementById('formula-limpar').addEventListener('click', function () {
    busca.value = ''; assunto.value = 'todos'; filtrar(); busca.focus();
  });
  document.getElementById('formula-imprimir').addEventListener('click', function () { window.print(); });
  document.querySelectorAll('.formulario-indice a').forEach(function (a) {
    a.addEventListener('click', function () { busca.value = ''; assunto.value = 'todos'; filtrar(); });
  });
  // O CSS reserva este espaço desde a primeira pintura com JS. Só habilitar
  // os controles depois de registrar seus eventos mantém a melhoria progressiva.
  ferramentas.hidden = false;
})();
