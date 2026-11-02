# QA-09 — auditoria independente da aplicação de pressão, fichas e diagnóstico, r10

Data: 30/10/2026. Auditor automatizado `/root/planning`, distinto do Corretor. **Veredito: APROVADO para os cinco deltas na versão efetiva e os efeitos localizados abaixo.** QA-09 integral permanece em correção; o próximo ID não está liberado.

## Critério e versão

QA-09 exige o inventário e recálculo de todo conteúdo numérico além dos 197 artigos, abrangendo exemplos, oficinas, diagnósticos, fichas, figuras e explicações. Este parecer cobre apenas a aplicação das cinco candidatas e o impacto localizado sobre o inventário, FOR-01 e os bancos; não aprova os demais trechos. As candidatas já tiveram pareceres independentes, que não substituem esta verificação da versão aplicada.

Base r9: aula SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`, formulário `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb` e inventário `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. A versão efetiva é aula `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`, formulário `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`, inventário r10 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c` e mapa r9→r10 `d882301bb56ec469da5bb9b6f0b42f02e908c7dfcbdacaa048d6d0caff552a62`. A [entrega do Corretor](../evidencias/QA-09/aplicacao-pressao-fichas-r10-r1/entrega-r1.md) tem SHA-256 `607af39ff2e5ae59f68cece012bd999149ddad26bf34bb0f5d830dca08559cb8`.

## Reconstrução e conteúdo científico

Reconstruí as duas páginas a partir das fotografias r9 e dos cinco pares original/candidata. Cada original e candidata foi identificado por documento, contexto, unicidade e hash; o resultado coincide byte a byte com as versões efetivas e fotografias posteriores. Nenhum outro delta foi aplicado nessas páginas. O verificador independente [verificar.mjs](../evidencias/QA-09/auditoria-aplicacao-r10-independente-20261030/verificar.mjs), SHA-256 `13d6cd4b5ba62813d1670600ae721b2ec3548929f2baee5bdb964a44bd5d669b`, executou sem erros.

- **Combustão e ficha 40:** para sistema fechado, variações cinética/potencial desprezíveis e Q positivo recebido e W positivo saindo, ΔU=Q−W. Com pressão termodinâmica constante e único trabalho W=p(V₂−V₁), ΔH=ΔU+pΔV=Q. A candidata exige igualdade entre pressão usada no trabalho e p de H, sem presumir que uma pressão interna constante determine sozinha trabalho de fronteira irreversível. A ficha preserva reação inversa entre os mesmos estados, quantidades e referências.
- **Vaporização:** para massa fechada de substância pura de líquido saturado a vapor saturado no mesmo p constante e nas mesmas hipóteses, Q=ΔH=m(hg−hf). No vaporizador estacionário, o texto manteve o balanço incluindo trabalho não associado ao escoamento e o contraexemplo de resistência elétrica; a formulação reduzida Q̇=ṁhfg continua condicionada à ausência desse trabalho e de variações cinética/potencial relevantes.
- **Ficha 67:** para massa fixa em trajetória reversível de referência, δqrev=T ds e qrev=∫T ds por unidade de massa; a temperatura de fronteira na transferência é absoluta e coincide com a temperatura do sistema na trajetória reversível. Não atribui o calor reversível ao processo real irreversível. O novo vínculo `#base-entropia` existe na aula e conduz à seção pertinente, embora existência de destino não prove aprendizagem ou acessibilidade.
- **Diagnóstico 2:** a ligação direta do tubo curvo ao fluido de processo e deformação devido à sua pressão definem o mensurando do manômetro, distinguindo a situação do termômetro a gás com bulbo e tubo Bourdon. Preservam-se instrumento/grandeza como perguntas e a conta −20+150=130 °C. O intervalo de 150 °C tem magnitude 150 K; não se supõe incerteza de medição.

Essas conclusões dependem das hipóteses e fronteiras explicitadas; não afirmam que relações simplificadas valham para qualquer dispositivo real. Nenhum resultado de aprendizagem, ensaio de navegador real ou revisão humana foi produzido.

## Estrutura, mapa e impacto

Os 197 artigos e seus 197 registros são iguais e estão na mesma ordem; no inventário oficial só `fonte` mudou. Entre as 100 fichas, apenas `formula-reacao` e `formula-calor-reversivel` mudaram. Todos os 734 elementos MathML da aula e 191 do formulário são idênticos entre r9 e r10. O inventário oficial JSON tem SHA-256 `2362fd386e0b7d1cb31b978a6c513114457e47bfccdda49f8017cba5cea87f88`; Markdown `3076d517ccf106ce414b708b04eaa74771da04256c03cfb45d39d34fd3177cc9`.

O verificador independente [mapa.mjs](../evidencias/QA-09/auditoria-aplicacao-r10-independente-20261030/mapa.mjs), SHA-256 `e244e0092f0b0e6935b90a77e156569233378453965b48e0a5568cb8f3febe09`, conferiu unicidade e campos de todos os 11.397 pares: 11.308 externos com deslocamentos esperados e 89 internos com hashes de ambos os fragmentos reconstituídos. Há cinco hashes diferentes externos de seções ancestrais e dez internos; os demais internos coincidem. Essa associação é estrutural e não transfere mérito científico a outros nós ou versões. Comparei as 815 referências e 138 registros de recursos: a alteração de valor é a remissão da ficha 67 de `#substancias` para `#base-entropia`; os hashes atuais de todos os recursos foram confrontados, e os seis ativos específicos permanecem iguais. Uma [auditoria de apoio independente](QA-09-mapa-r9-r10-apoio-auditoria-independente-r1.md) chegou às mesmas contagens, SHA-256 `46a46cdee594004e7dd88bd6e752656f4be83f743e45fb849d12f7021e2b72fd`.

O validador canônico passou com 197 itens/artigos, 29 recursos e 1.263 links, sem erros. O teste de persistência BAN-08 passou seis cenários com funções reais e DOM/armazenamento simulados. Reexecutei o filtro real de `formulario-e1.js` com dados das 100 fichas e DOM simulado: buscas pelas novas hipóteses localizaram as fichas 40 e 67 e um termo inexistente retornou zero. O teste [testar-filtro.cjs](../evidencias/QA-09/auditoria-aplicacao-r10-independente-20261030/testar-filtro.cjs) tem SHA-256 `4516dd12e2ba96041f05b38dcec31a2b15013a34cedf7a90a796f982095c7f1e`. Node/VM com DOM simulado não é navegador real.

A preservação das outras fichas, MathML, destinos e scripts e a revisão das duas alterações sustentam **revalidação localizada de FOR-01 para o delta examinado**, sem afirmar nova revisão integral das 100 fichas. A preservação dos artigos, registros e código sustenta ponte localizada para BAN-02/07/08 quanto a este delta. As bases de outros pareceres, FUN-01/02 e ledgers anteriores requerem análise individual de alcance e dependências antes de qualquer integração à r10; igualdade de hash ou mapa não transfere aceite automaticamente.

| Critério localizado | Resultado |
|---|---|
| Identidade, reconstrução e aplicação dos cinco deltas | Atendidos na versão efetiva. |
| Hipóteses e contas dos trechos alterados | Atendidos nos modelos e limites declarados. |
| 197 artigos/registros, 98 demais fichas e MathML | Preservados na comparação. |
| Mapa, referências, recursos e efeitos FOR-01/BAN | Conferência localizada com limites acima. |
| Navegador, aprendizagem e QA-09 integral | Não examinados integralmente; QA-09 e próximo ID continuam bloqueados. |

Não houve revisão humana, aplicação com alunos ou certificação externa. A aprovação localizada não classifica o curso inteiro como avançado.
