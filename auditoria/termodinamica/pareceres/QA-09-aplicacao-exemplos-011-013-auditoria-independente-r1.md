# QA-09 — auditoria independente da aplicação EX-011 e EX-013, r1

Data: 30/10/2026. Revisor: agente automatizado independente `/root/auditor`, com apoio automatizado independente em estrutura e mapa. **Veredito localizado: APROVADO para a aplicação examinada, sem ajustes obrigatórios identificados nesse alcance.** QA-09 permanece em correção e o próximo ID não está liberado.

## Critério e alcance

QA-09 exige inventariar e recalcular todo o conteúdo numérico além dos itens BAN-08, incluindo exemplos, oficinas, diagnósticos, fichas, projetos, figuras e explicações; cada ocorrência deve ter referência verificável e resultado conferido. Esta revisão não representa a conclusão desse trabalho. Examina somente os dois exemplos aplicados, as fotografias, a correspondência r6→r7 e o impacto localizado sobre BAN-02/07/08. A regra curricular comum da seção 3.2 diz respeito à conclusão de itens curriculares; esta correção localizada de enunciados existentes não encerra tal item nem substitui seus requisitos de ensino, exercício, rubrica e matriz.

## Identidade e alterações

Examinei a base `ee5da2588b799cc62bf85c5146ab8bb4982d2352` e a versão efetiva em `modulos/e1-termodinamica.html`. Os dois originais ocorrem uma vez na base e as candidatas uma vez no resultado, nos contextos dos respectivos títulos. Uma reconstrução independente, substituindo os dois fragmentos originais pelas candidatas, reproduz o arquivo efetivo **byte a byte** e sua fotografia posterior. Assim não há outras modificações no HTML neste delta. Os SHA-256 dos fragmentos, sem a quebra final dos arquivos isolados, conferem com os manifestos anteriores:

| Exemplo | Original | Candidata |
|---|---|---|
| EX-011 | `b0259df0ccfb9755fe447a080f0b4f4ae5b79a797ca924a7ad4611e8781c8c27` | `8ec6ce4013a1be49c569b5e3b8ab5e80b899cb9d250396be6023b1eecfa2d3c9` |
| EX-013 | `d8fc4f1313b7ac9a73c7b256aabf31ab2df4ba8026f6fd9fae89ccfd9bee1cac` | `7438f121e00f4c757b695c3de6f881d295128696b48bad8f5d387b0e6547dfea` |

## Recálculo independente

Na convenção explicitada na aula, calor recebido é positivo e trabalho saindo é positivo; a base despreza variações cinética e potencial.

- **EX-011:** sem massa cruzando a fronteira, a perda líquida fornece `Q = −40 kJ`. A entrada por eixo é o único trabalho, `W = −250 kJ`. Assim, `ΔU = Q − W = −40 − (−250) = +210 kJ`. A rigidez elimina trabalho de fronteira, mas não trabalho de eixo; a exclusividade esclarece que não existe trabalho elétrico adicional.
- **EX-013, compressão:** para pressão constante de 200 kPa e `ΔV = −0,020 m³`, `W_b = pΔV = −4 kPa·m³ = −4 kJ`. Este é o único trabalho; com `Q = −7 kJ` líquido, `ΔU = −7 − (−4) = −3 kJ`.
- **EX-013, aquecimento:** no segundo caso, preservado, `ΔT = 35/[1 × 0,70] = 50 K`, para o modelo de gás ideal e calor específico constante ou representativo na faixa, tanque rígido e ausência de outros trabalhos. É variação de temperatura, não temperatura final absoluta.

Os resultados são exatos para os dados nominais e hipóteses do modelo; não foi informada precisão instrumental. Não há alternativas nem gabarito pontuável nesses dois blocos.

## Estrutura, mapa e alcance dos aceites

Os 197 artigos da base e do resultado são idênticos e na mesma ordem. Os 197 registros individuais do inventário oficial permanecem iguais; apenas a chave `fonte` foi atualizada para apontar à fotografia e ao hash atuais. O Markdown do inventário recebeu seção histórica. O validador `node auditoria/termodinamica/inventario/validar-inventario.mjs` retornou `ok=true`: 197 itens e artigos, 29 recursos, 1.263 links locais, nenhum erro ou aviso. Trata-se de verificação estrutural/documental, não de correção científica integral ou aprendizagem.

Os arquivos `assets/curso.js`, `assets/registro.js` e `formulas/termodinamica.html` permanecem iguais à base. O teste de persistência BAN-08, após inspeção para garantir que não grava evidência, passou nos cenários de histórico, contagem, alerta, gravação/releitura, refazer e falhas. Usa DOM e armazenamento simulados, com foco em AV42/45/52; não é teste em navegador real. A preservação dos artigos, registros e scripts sustenta uma ponte localizada sem impacto identificado nos aceites BAN-02/07/08, não uma nova aprovação integral nem transferência automática de aceite para o novo hash.

Na comparação independente das fotografias r6 e r7, os 11.396 pares foram conferidos por ordem, unicidade de IDs, documento, tipo, tag, seção, âncora, posições UTF-16 e hashes. Há 5.484 IDs deslocados, 11.391 hashes iguais e cinco diferentes: a seção ancestral, as duas divs e seus parágrafos. Os hashes dos cinco trechos foram recalculados. As listas de 197 artigos excluídos permanecem iguais; as contagens de referências (815) e recursos (138) permanecem iguais, mas essas listas não são abrangidas pelo mapa. Hash igual não demonstra preservação de todas as dependências nem transfere prova; a triagem e o recálculo do inventário continuam pendentes.

| Critério da aplicação localizada | Resultado |
|---|---|
| Identidade das candidatas e aplicação na versão efetiva | Atendido: reconstrução byte a byte. |
| Hipóteses, unidades e resultados dos dois exemplos | Atendido no modelo e com os limites acima. |
| Preservação dos artigos, inventário e recursos afetados | Atendido no alcance descrito; verificação estrutural sem erros. |
| Fotografias e mapa | Atendido para os pares estruturais, com limitações acima. |
| Efeito sobre BAN-02/07/08 e persistência | Sem impacto localizado identificado; teste com ambiente simulado. |
| Critério integral de QA-09 e liberação do próximo ID | Não atendido nesta entrega parcial; continuam bloqueados. |

Não houve teste com estudantes, revisão humana, ensaio em navegador real ou certificação externa. A conclusão localizada não demonstra aprendizagem nem que o curso inteiro seja avançado.

## SHA-256 da versão examinada

- HTML anterior: `dd47dc9dbc5c22f6f74a4fa67bd28b495cff775ff8ca04cec2c76c405dfefd1a`; HTML atual e fotografia: `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`.
- Inventário QA-09 r6: `a38b60799c23cf88fb0085e7c9bd82b4f22f58a4c7f89b6b418f8b3f5ae5d1aa`; r7: `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; mapa r6→r7: `21fc816ecb3e5191463a089a3a23ab76b4b9aa42431b14f8e48f35f7f7200c26`.
- Inventário oficial JSON: `c240148429da2f2a295e6a97bce2f466a255fdc5f5fef1858aaed2fc2a687e89`; Markdown: `939b865b200f20061b56cd5f4e0163948d8b8d48fbf9fd30c68322a392ea2e4b`.
- Entrega do Corretor: `88655a0040adbe9665c550248d1e286bebf2c19ad0ac0a81fcbc0b8578c927c0`.
- `assets/curso.js`: `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`; `assets/registro.js`: `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`; ficha: `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`.
