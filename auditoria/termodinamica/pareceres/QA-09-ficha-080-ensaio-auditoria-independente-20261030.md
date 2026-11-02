# QA-09 — auditoria independente do ensaio em cópia da ficha 80

Data: 30/10/2026. Revisor automatizado independente `/root/qa_examples`. **Veredito: APROVADO para o ensaio em cópia, no alcance indicado**. O formulário de produção não foi alterado por este parecer. A decisão não aprova a aplicação futura, não reaprova FOR-01 integral, não encerra QA-09 e não libera o próximo ID.

## Critério, versão e reconstrução

O ajuste da ficha 80 deve explicitar Q̇in>0 e Ẇt>Ẇc quando a razão é usada como rendimento de motor, e manter a expressão e seus vínculos. A candidata isolada recebeu revisão prévia; aqui o objeto é a **fotografia simulada** produzida por `auditoria/termodinamica/evidencias/QA-09/ficha-080-aplicacao-ensaio-20261030/` e sua repercussão identificável no alcance de FOR-01.

O formulário atual e cópia FOR-01 r2 são byte a byte idênticos, SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`. O inventário r8 é `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`, e a aula r8 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`. O original e a candidata isolados têm respectivamente hashes de fragmento sem quebra final `be53d6d4b8ef9305ad4392713fd7ce2c59379393187d06bf0234116ffc431ea5` e `9dcaed2872d4754bb8151aae1ada14a4c45a07557e6ed70ec5569b8c4cfc0897`.

De modo independente comparei a fotografia anterior do ensaio com a fonte efetiva, substituí a ocorrência única original pela candidata e obtive byte a byte a fotografia proposta `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`. Inspecionei o script `preparar.py` antes de executá-lo em diretório novo em `/tmp`; ele não escreve no produto e impede regravar o destino. A execução reproduziu tanto a fotografia proposta como o JSON de resultado fornecido, byte a byte.

## Conferências independentes e limites de FOR-01

- O exame bruto das 100 fichas na sequência encontrou alteração apenas na ficha 80; as 99 restantes são idênticas, inclusive as fichas 23, 46, 79 e 84 tratadas em FOR-01 r2. Os 191 elementos MathML são idênticos byte a byte; o texto acrescentado é o mesmo em condição visível e `data-busca`.
- Comparei estrutura com parser HTML antes/depois: 11 grupos, 431 IDs, 121 `href`, 3 `src`, 100 `aria-controls`, 111 `aria-labelledby` e 191 `aria-describedby` mantêm valores e ordem. São atributos selecionados, não ensaio completo de acessibilidade ou interação.
- Verifiquei que os 103 vínculos das fichas têm 50 destinos distintos presentes na aula r8. A ficha 80 aponta a `base-brayton-real`, título “Brayton real: trabalho líquido, perdas e regeneração”; a base apresenta trabalho de turbina menos trabalho de compressor, outros consumos desprezados e rendimento como trabalho líquido por calor de entrada. Existência de todos os destinos não comprova sua coerência pedagógica integral.
- A expressão existente é Ẇlíq=Ẇt−Ẇc e η=Ẇlíq/Q̇in. Para 1.000, 400 e 1.200 kW, Ẇlíq=600 kW e η=0,50. A condição proposta exclui denominador zero e trabalho líquido não positivo para interpretação como motor. São restrições necessárias no modelo e não provam viabilidade de estados ou segunda lei.
- Os arquivos `assets/formulario-e1.js`, `assets/formulario-e1.css` e `assets/curso.css` coincidem com o pacote FOR-01 r2. `assets/curso.js`, `assets/registro.js` e a aula atual diferem das versões históricas: os hashes ou igualdade das fichas não provam ausência de impacto de todas as alterações intermediárias. Os aceites históricos são válidos nas versões e alcances documentados, e o impacto de dependências deve ser resolvido quando a versão efetiva for auditada.

## Evidência e decisão

Entrega do Corretor SHA-256 `3d3a4dc48a643f7d78dfc3978e9179a0bf6ac2b6ccb69011f22288ca98ab79bf`; `preparar.py` `468813907fcd3b2f34da34cf2b93e8368038ab64d385385dadf33d3d32ccdbc0`; resultado `ensaio/resultado.json` `8f4789bc109bf3a99cda625c386c7c1a39384fdb7e9631badd1e22465d734e7c`.

| Critério localizado | Resultado |
|---|---|
| Reconstrução e reprodução da simulação | Atendido para a base e os fragmentos identificados, sem modificar produção. |
| Cálculo e domínio da ficha 80 | Atendido no modelo indicado, com as reservas acima. |
| Integridade estática dos cartões, MathML, links e atributos selecionados | Atendido na comparação e na aula r8; existência de vínculo não valida todos os destinos semanticamente. |
| Impacto anterior de FOR-01 | As fichas são preservadas à exceção da 80; diferenças das dependências e aceites intermediários não foram integralmente revalidados. |
| Aplicação efetiva, testes de navegador e revalidação do novo hash | Não realizados nesta rodada e exigem exame próprio após aplicação. |
| QA-09 integral e liberação do próximo ID | Não atendidos; permanecem pendentes. |

Antes de aplicação, conferir novamente arquivo efetivo, contexto e hashes para evitar base desatualizada. Após aplicação, obter novo inventário e mapa de correspondência, verificar o escopo de FOR-01 e demais dependências relevantes, e solicitar auditoria independente da versão realmente usada. Sem ensaio em navegador ou leitor de tela, revisão humana, teste com estudantes ou certificação externa.
