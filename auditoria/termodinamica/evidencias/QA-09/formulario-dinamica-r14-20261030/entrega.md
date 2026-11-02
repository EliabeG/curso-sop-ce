# QA-09 — contagem e controles do formulário, fotografia r14

Data: 30/10/2026. Corretor: agente automatizado `/root/next_graphics`. **Aguardando Auditor independente**. Lote de apresentação e resultados numéricos da contagem, externo aos 197 artigos da aula. Não é parecer de QA-09 nem aceitação das fichas ou de outros IDs. Não modifica o produto.

## Versão e objeto

`formulas/termodinamica.html`: SHA-256 `3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce`; inventário r14 `6505b06f3f3ef15bc2904f8a604f6e1f0fa6cf22af822394b2c2a871437b6175`. O arquivo carrega `../assets/formulario-e1.js` em UTF-16 630 (hash da string do caminho `b0fb9d121b56a236ec0852b70097e4aefb09a5442d1f0d1eab1a956ed564a3ab`), além de `registro.js` e `curso.js`. O código `assets/formulario-e1.js` tem SHA-256 `90102be814345ef26326011df263dc75e98ceaf983f6be2f4f57ab43848a2a79`. Contém filtro, contagem, revelação e solicitação de impressão; no código examinado não há cálculo de propriedades termodinâmicas. O texto inicial `100 de 100 fichas` começa em UTF-16 3034, SHA-256 da string `9d6c9d919d4f693f194629b68258e5448cf4951b79e540a0a1d01efbba5ea257`.

São **100 cartões** com IDs distintos e dados de busca, distribuídos em **11 grupos**, coincidentes com a descrição inicial da página e com o inventário r14. Quantidade por grupo: medidas 11, gases 9, fases 5, calorimetria 4, primeira lei 11, escoamento 17, segunda lei 6, entropia 15, ciclos 8, compressores 4 e transferência 10; a soma é 100. Isto é uma contagem exata de elementos, não verificação científica das 100 fichas.

## Ensaios localizados

O programa real de produção foi executado em VM JavaScript com objetos que simulam apenas as chamadas de DOM utilizadas, alimentados com `id`, `data-grupo` e `data-busca` extraídos do HTML real. O extrator também confere se cada cartão está no grupo declarado e contém uma expressão inicialmente visível e um botão de revelar inicialmente oculto e com `aria-expanded=false`. Verificações específicas:

* `  CARNOT  ` gera 7 cartões e `7 de 100 fichas`; ao selecionar `segunda-lei`, permanecem 6 e o placar muda para `6 de 100 fichas`.
* `ENTRÓPIA` encontra 17 fichas por normalização de caixa e acento. Uma busca sem resultado gera zero, oculta grupos e mostra aviso; limpar restaura 100 e solicita foco no campo.
* Entrar em memorização oculta expressões e mostra botões; revelar um cartão altera seu estado e `aria-expanded`; sair restaura expressões e oculta botões. O link de índice testado limpa o filtro; o botão de impressão solicita `window.print` uma vez.

O arquivo da aula r14 (`572b172b29e1aa26873d191ebd827414c99f3122491c6d4c8129a69443f7389c`) carrega `registro.js` e `curso.js`; a seção chamada laboratório apresenta roteiro e exercícios na marcação, não um script especializado incluído por esse nome. Os ativos de cálculo FUN-01 e FUN-02 são baixáveis e têm lotes específicos anteriores; isto não cobre automaticamente todas as suas funções ou resultados.

## Reprodução e limites

Na raiz execute `python3 auditoria/termodinamica/evidencias/QA-09/formulario-dinamica-r14-20261030/verificar.py`. Resultado observado: `ok: true`, 100 cartões, 11 grupos. O programa é somente leitura; valida os SHA do HTML e do script, extrai os atributos reais e passa os dados ao ensaio. SHA-256 `verificar.py`: `2dadbf9c048b5b7ad12dbd72eeee6d2abb2055416fdc95d822575a188e3722ec`; `verificar-vm.cjs`: `1aa8c9f6f9753a6ad213e8404a8a8208bd9c14654d0000512a2a62450c31a816`.

O DOM simulado não prova construção do DOM real, funcionamento de CSS, foco real, impressão, acessibilidade, leitor de tela nem integração em navegador. Não foram executados os scripts compartilhados na simulação, nem todas as combinações de busca e grupos ou interações; os testes não comprovam que o índice de busca espelha integralmente o texto apresentado de cada ficha. O arquivo `assets/curso.js` e a saída dinâmica de pontuação/temporizador permanecem fora deste lote. A leitura de navegador requerida no plano e a revisão independente continuam pendentes. Não há fonte física externa aplicável à contagem de elementos; isto não valida seus conteúdos científicos.
