# QA-09 — interatividade e módulos numéricos E1, fotografia git 093eef7 (r27)

30/10/2026. Corretor automatizado `/root/next_graphics`. **Aguardando Auditor independente.** O nome `r28` identifica este lote de evidência, não uma fotografia r28. A fotografia r27 foi preservada em `aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html` e coincide com `git show 093eef7:modulos/e1-termodinamica.html`, SHA-256 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`. Comparei também com esse commit os hashes dos seis arquivos listados no verificador. A árvore efetiva avançou depois para outra fotografia; este lote não a revalida.

## Inventário e alcance

O HTML r27 carrega `assets/registro.js` e `assets/curso.js`. A inspeção estática encontra 581 entradas radio, duas de busca e duas checkboxes, 321 botões, quatro selects e 261 details; não encontra canvas, vídeo, iframe ou entradas number/range. Esses valores descrevem tags estáticas, não recursos testados nem número de questões aprovadas. O JavaScript compartilhado contém, entre outros, interações de questões/placar, simulado, flashcards e persistência. Não identifiquei nesse recorte uma calculadora numérica embutida: os módulos FUN-01 e FUN-02 são arquivos **baixáveis** com dados JSON próprios, destinados a execução em Node.js. Isso não demonstra comportamento completo em navegador ou ausência de quaisquer caminhos dinâmicos não detectados pela inspeção estática.

`inventariar.py` SHA `82f2ff6ed418a8efffb6988b4c84200597e1867b03f143502658542c9f968b06`, saída `inventario.json` SHA `e4a89d00b1a812da0efa31bf9b366d2f42fe82c5eec66a926dae6a3e62cfe9d5`, registra contagens, scripts e downloads em leitura. Avaliações históricas já abordaram FUN-01/FUN-02 e seus dados: este lote acrescenta execução da interface dos módulos com o pacote nominal e um teste de fronteira alterado, não reivindica que suas contas sejam inéditas.

## Execução dos pacotes nominais

`node auditoria/termodinamica/evidencias/QA-09/dinamicos-r28/verificar.mjs`, SHA `df0eef93dc9f7f236def4b10ccba26913d0abc280c878d9664978dba646c9282`, passou. Ele importa as versões do repositório com os dados associados, verifica suas identidades contra r27 e faz conferências independentes selecionadas:

- FUN-01: v=0,45 m³/kg, x≈0,507494, h≈1.621,949 kJ/kg; intervalos da previsão e sensor não se sobrepõem sob tolerâncias declaradas. Lotes de mistura são líquido, coexistência, vapor e global indeterminado; no lote II β=8/21. Uma melhoria isolada das incertezas não garante supercriticidade no caso estudado; a conjunta garante. Os 28 testes internos do módulo passam para os dados originais.
- FUN-02: cinco percursos aceitos e um rejeitado pela janela, todos com ΔU≈1.870,65 J; ciclo por diferença entre I e II tem W≈Q≈765,352 J. Compressão com expoente 3/2 dá W=−4.988,4 J, Q=−1.247,1 J e ΔS≈−2,8814 J/K no modelo. No teste de integrabilidade, κ=0,2, o ciclo amplo é aproximadamente nulo e o ciclo esquerdo é −20 ln 2 J/mol. Os 49 testes internos passam com dados originais. Ambos os módulos rejeitam ID incompatível no teste.

Os dados são os modelos definidos pelo pacote, não propriedades físicas universais; ensaios não verificam cada caminho, unidade ou condição possível e não certificam a aprendizagem. Os módulos não são carregados automaticamente por tags de script da aula.

## Lacuna de fronteira em dados modificados — não é defeito nominal comprovado

O código FUN-01 declara que seu módulo é um modelo didático de pacote, não biblioteca geral de propriedades. Ainda assim, para testar limites do reuso, clonei o JSON **somente em memória**, mantendo o ID e a versão, e alterei apenas a pressão do lote IV de 80 para 50 kPa, igual a p_B^sat, mantendo p_A^sat=150 kPa. O código calcula x_A=y_A=0 e, sem verificar denominador y_A−x_A, devolve `Infinity` em ambos `beta_para_z_035` e `beta_para_z_050`; `JSON.stringify` converte esses valores para `null`. Neste limite de componente puro B, os z_A=0,35 e 0,50 não são admissíveis como mistura líquido–vapor na pressão imposta; não existe β finito que satisfaça aqueles balanços. O programa, porém, não emite diagnóstico específico da degenerescência ou incompatibilidade dos z forçados.

Isso **não ocorre no JSON nominal**, no qual p=80 e y_A−x_A=0,2625, nem prova que o pacote prometa suportar entrada arbitrária. Trata-se de limite de generalização e lacuna de teste/guarda caso o programa venha a ser reutilizado com variantes: uma solução possível seria recusar denominador nulo e indicar incompatibilidade, ou explicitar que o cálculo é restrito ao arquivo original. Solicita-se Auditor independente para julgar se o contrato atual exige ação; nenhuma alteração foi aplicada.

## Limites adicionais

Os testes são em Node, não verificam clique, teclado, pontuação, restauro, visualização, persistência real, acessibilidade ou compatibilidade em navegador. Existem verificações históricas de componentes do banco, mas não as reexecutei nem as promovo como prova da interface r27. Não houve alunos, leitor de tela, revisão humana ou certificação externa; QA-09 continua aberto.
