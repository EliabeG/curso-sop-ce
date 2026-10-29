# QA-09 — adendo: fotografia das bases EX-006–010 e adjudicação de EX-008

Data: 29/10/2026. Apoio independente automatizado. Objeto: `QA-09-exemplos-06-10-apoio-independente-r1.md`, SHA-256 `dc88dac4fdef3b70594b7adc1072bd606424d4056a6ee8b18e65debe410ff161`. Sem alteração do produto ou controle e sem aprovação global QA-09.

## Comparação das bases por hash

A fotografia anterior efetivamente lida está preservada em `auditoria/termodinamica/evidencias/QA-09/aplicacao-diagnosticos-seis-r1/antes/e1-termodinamica.html`, SHA-256 `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`. A fotografia posterior é `modulos/e1-termodinamica.html`, SHA-256 `49b0df4fe59dfd01913f4d41a5e6869705f4bf4d6ded251060f940cd5d12c91b`, idêntica à cópia `auditoria/termodinamica/evidencias/QA-09/aplicacao-diagnosticos-seis-r1/e1-termodinamica-depois.html` pelo mesmo hash. Inventário posterior `auditoria/termodinamica/evidencias/QA-09/inventario-r5.json`: SHA-256 `e21bc074025815cb5708875f938cb8a0de200ebecc66c4a7c8997493c01b0ea4`.

Extraí de cada HTML o `div.bloco-aula` ancestral imediato do título com o ID indicado, incluindo marcação, texto e conteúdo descendente; comparei os bytes UTF-8 integralmente. **Todos os cinco blocos são idênticos entre as duas fotografias**, sem depender apenas do hash dos exemplos:

| Âncora da base | SHA-256 do bloco em ambas as versões |
|---|---|
| `#base-gas-modelo` | `eac52ff635952b4f0fac43b907bcdb76401d66c9e1eb4cc9cb04a92da1ce2333` |
| `#base-umidade` | `8abffd37dfbfa4a223b0d49d2cec00e31b827fed0191f855d61823f4e05fa464` |
| `#base-equilibrio-fases` | `9dcee90f44c7cad186eeb40d4c890635ea943a985709b97fa5f68dfe2125d633` |
| `#base-calor-variavel` | `26e3fb8bf391caa4840a092edc386f55979fded03d0fa6771af94120c800b2de` |
| `#base-turbina-potencia` | `a9a8a163cb667a472acb0475a598541bf38353f6278153f4f590f4e58ae2588e` |

O último bloco inclui tanto a tabela anterior de balanços estacionários quanto o exemplo de turbina; comparação cobre o contexto que sustenta regime permanente. Os cinco fragmentos EX-006–010 já tinham sido reextraídos na fotografia posterior, com hashes preservados no parecer de origem. Assim, a pendência específica de confirmação das bases para esses cinco exemplos está resolvida; não se infere igualdade do documento inteiro nem das demais aulas.

## EX-008 — decisão sobre dG e transferência

O texto anterior trata de fases de **substância pura**, T e p impostas e transferência de pequena quantidade `dn`, e apresenta a relação diferencial `dG=(μv−μl)dn`. O exemplo hipotético aplica a expressão com `μl=5`, `μv=7 kJ/mol` e `dn=0,02 mol`, chegando a `+0,04 kJ=40 J`, e conclui corretamente que a direção líquido→vapor não é favorecida no estado descrito. As unidades coincidem; não se trata de valor tabelado da água. [MIT, equilíbrio de fases de uma substância pura](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/b312114e4e885b69b5746dcad660cc4f_lec_18.pdf) trata o potencial de cada fase como função de T e p e descreve o sinal e a condição de coexistência.

A notação `dG` é uma avaliação diferencial/local; por si só ela não autoriza uma variação finita exata em modelos gerais de mistura em que potenciais mudem com composição. Contudo, o caso aqui está inserido no modelo da aula de fases puras a T e p fixas, que não introduz dependência de composição, e descreve transferência pequena. Nesse recorte, os potenciais de cada fase pura permanecem funções do mesmo T e p; tratando fases como reservatórios homogêneos que subsistem e desprezando efeitos interfaciais, a diferença constante também pode ser integrada no trecho: `(7−5)×0,02=0,04 kJ`. A hipótese de persistência das fases é necessária para essa extensão finita e não deve ser transportada para uma mistura genérica. Potenciais diferentes descrevem tendência fora do equilíbrio de fases; não se afirma coexistência em equilíbrio com potenciais distintos.

**Decisão: não é necessário ajuste do exemplo no contexto didático atual.** O uso numérico como diferencial/local já corresponde à notação e à explicação da aula; mencionar “estimativa local” ou explicitar persistência das fases seria melhoria opcional caso se queira ensinar variações finitas, não condição para resolver a questão atual. Nenhuma incerteza experimental ou tolerância de primeira ordem foi fornecida, e 0,02 mol por si só não é prova universal de que efeitos de composição sejam desprezíveis. Mantém-se a ressalva de alcance do parecer original como limitação, não como defeito confirmado.

Fonte externa consultada em 29/10/2026 sem captura ou hash local. Este adendo não é teste de navegador, não revalida outros exemplos e não aprova QA-09.
