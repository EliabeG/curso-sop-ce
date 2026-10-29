# QA-09 — revisão independente das candidatas da oficina 8.1, r1

Data: 29/10/2026. Revisor: agente automatizado independente `/root/auditoria_diagnosticos_seis`. **As quatro candidatas isoladas são tecnicamente adequadas aos pontos adjudicados.** Esta decisão é localizada, não aplica as mudanças, não altera produto ou controle e não aprova QA-09 nem libera próximo ID.

## Escopo e método

Confrontei `oficina-8-1-analise-candidatas-r1.md` e o manifesto com a adjudicação `QA-09-oficina-8-1-adjudicacao-independente-r1.md`, os quatro originais e candidatas e a seção efetiva do módulo. Todos os arquivos listados no manifesto conferem com seus hashes. O HTML efetivo tem SHA-256 `49b0df4fe59dfd01913f4d41a5e6869705f4bf4d6ded251060f940cd5d12c91b`, e a seção `#cobertura99-transferencia` tem `332973ea8904d02ceb2e6c54d8713924c517975ce0749f09ee9f1b8ba07d56c2`, iguais às referências das quatro candidatas. Cada original ocorre exatamente uma vez na fonte atual; nenhuma candidata já está aplicada. Cada ocorrência `antes` dos manifestos individuais ocorre uma vez no respectivo fragmento e a aplicação de suas substituições gera exatamente o fragmento candidato. Os hashes de arquivos e de fragmentos, estes sem a quebra de linha final dos arquivos isolados, conferem. Fora dos textos declarados, não há diferença literal em cada bloco.

## Suficiência e contas

- **Estado:** retirar a alegação de valor de temperatura fornecido e afirmar saturação à pressão considerada elimina a atribuição sem dados. Os valores didáticos dão `x = (1380−500)/(2700−500) = 0,40`, 2 kg de vapor e 3 kg de líquido em 5 kg. No diagnóstico seguinte, com a mesma tabela, `x = (2040−500)/2200 = 0,70`, 5,6 kg de vapor e 2,4 kg de líquido em 8 kg. Nenhum valor numérico de temperatura, pressão ou substância real foi inventado; P e T de saturação não fixam sozinhas as frações de fase. O diagnóstico continua dependendo da tabela no exemplo anterior, aceito como suficiente pela adjudicação.
- **Trabalho:** gás como sistema fechado, calor líquido de saída e trabalho de fronteira como único trabalho afastam a interação elétrica adicional que demonstrava subdeterminação. `W_f = 120(0,15−0,40) = −30 kJ`, `W_total = −30 kJ`, `Q = −10 kJ` e `ΔU = Q−W = +20 kJ`; a solução distingue fronteira e total. A convenção é trabalho feito pelo sistema positivo, como ensina a base.
- **Turbina:** permanente, uma entrada e saída, eixo como único trabalho e perda térmica líquida excluem a acumulação e outros termos de trabalho do contramodelo. `−50 − Ẇ = 2(2800−3200) = −800 kW`, logo `Ẇ = 750 kW` produzido; valores de EC/EP são desprezíveis conforme o enunciado. A potência de 800 kW adiabática não se aplica à perda de calor dada.
- **Compressor:** uma entrada e saída, regime permanente, perda líquida e eixo como único trabalho determinam potência de eixo. `−15 − Ẇ = 3(290−250) = 120 kW`, portanto `Ẇ = −135 kW`, isto é, 135 kW recebidos. Isso exclui o contramodelo com parcela elétrica adicional sem alegar sua existência.

Os resultados são iguais aos da adjudicação sob os modelos e dados nominais, sem conferir precisão instrumental. Os dois casos de máquinas térmicas não estão alterados; sua leitura contextual de duas fontes foi julgada suficiente na adjudicação, que distingue esclarecimento recomendável de erro bloqueante.

## Identidade, progresso e dependências

Os blocos são exemplos e casos da oficina, não artigos pontuados de BAN-08; os seletores de banco em `assets/curso.js` abrangem `article.questao` e `.concurso-item, .avalia-item`, não essas classes. A inspeção estática dos deltas não indica alteração dos artigos, respostas pontuadas ou digitais; não comprova persistência real, visualização no navegador, tecnologias externas ou dados salvos de terceiros. A candidata é isolada: não há versão aplicada a auditar neste parecer.

Se o coordenador autorizar aplicação, confrontar novamente a fotografia e os quatro originais com a fonte vigente, preservar antes/depois, verificar os deltas efetivos, artigos, bases e vínculos, atualizar as fotografias e inventários pertinentes e criar mapa rastreável com posições e hashes. Verificar persistência onde pertinente e reexaminar efeitos sobre aceites dependentes. Igualdade de hash ajuda rastreio, mas não transfere provas nem aceite automaticamente; uma aplicação altera o hash do documento. Não foi realizado teste em navegador ou com estudantes. Este parecer não cobre o restante da oficina, todo o universo numérico ou o aceite global de QA-09.

## Hashes SHA-256

Manifesto geral `cd39f6c85a248d6f550e539683cae2260cfee715d6d90123a4a10636b526f819`; análise do Corretor `6e2e6d7b57d061c463381cd4afb55b4bf8a0f70cb1e047c9e7a99e918bcd6c29`; adjudicação `36afd1dd5e12965a66bf2945871c4434771400bbd7a7728ff2eab55d7f3ac4e0`; inventário QA-09 r5 `e21bc074025815cb5708875f938cb8a0de200ebecc66c4a7c8997493c01b0ea4`. `assets/curso.js` `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`; `assets/registro.js` `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`.

| Fragmento | Original | Candidato | Arquivo candidato |
|---|---|---|---|
| Estado | `ab5095512ce0582b481d1e94c74c0c7dbd7a3228c2016c3b17c7fd611823d84b` | `dec11b70113935a4f763cde64bc6b371159284b364e370c6519a6a4f1fc72af2` | `62418797ab11205ff619196e60fcb65b22f4528d0afc912f63a15f5579886642` |
| Trabalho | `bdfc904faec68456481748c2f0d18c46f00b5ab7e421c9e24145e55e1b1bf707` | `8b0baf719dc32ff52efba1a6968b8bef82804e1aad8f26f5949e9258fa50e841` | `24ca90cb4d0e120a0c13f26e3fbbc9afca276c4d1a037f915b6d84fce46c24bc` |
| Turbina | `80a44fade53998980ceb1c75d07a023798b126ea4ca8f30835bfc1de6745b75d` | `ddbee308b1684a4eb8d5884a17a056582016563cc61ba735105eb0d433fe6acd` | `9f662cf7872e5dddb5cad0d7ba3fc10b795db3ffb53002f7f20cd46b32bf8247` |
| Compressor | `9dfddd65f621b05df619ec763ce6fdbffab23fecd60190739feda0871778834a` | `7b45170eba005fecfbd7b39dc6e96656fa8d294f07a93339e2f59a92945e2ae5` | `0b65f6057c08fca38cd06acb9a46907acbdb385c78833b739f828686258b8ced` |
