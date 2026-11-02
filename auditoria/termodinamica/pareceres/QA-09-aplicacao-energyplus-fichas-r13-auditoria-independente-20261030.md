# QA-09 — auditoria independente da aplicação do vínculo EnergyPlus e fichas 88/99, r13

Data: 30/10/2026. Auditor automatizado `/root/planning`, distinto de `/root/next_examples` (aplicação), `/root/next_formulas` (candidatas das fichas) e `/root/reference_triage` (candidata do vínculo). **Veredito: APROVADO para os três deltas na versão efetiva e a revalidação localizada descrita.** QA-09 integral permanece em correção e o próximo ID não está liberado.

## Critério, versões e alcance

QA-09 exige inventário e recálculo de conteúdo numérico fora dos 197 artigos, inclusive fichas e explicações, com referências verificáveis. A presente revisão cobre as duas fichas, a troca de um vínculo, preservação dos demais elementos e o efeito localizado em FOR-01 e BAN; não encerra QA-09 ou o núcleo avançado.

Aula r12 SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7` e r13 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; formulário r12 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756` e r13 `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`; inventário r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`, r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b` e mapa r12→r13 `3f198c327e0bbb5d28c116fa5b1d655224e6ad9e24505556397d6c3586169671`. A [entrega do Corretor](../evidencias/QA-09/aplicacao-energyplus-fichas-r13-r1/entrega-r1.md) tem SHA-256 `0e726a68c6f1b08ebd184f6edb96a630fe726102264728cd461a52d8eb97c98b`.

## Reconstrução e modelo

Reconstruí as duas páginas a partir das fotografias anteriores e dos três pares original/candidata aprovados. Cada original e candidata ocorre uma vez em seu contexto e tem o hash esperado; as reconstruções coincidem byte a byte com os arquivos efetivos e as fotografias posteriores. O verificador independente [verificar.mjs](../evidencias/QA-09/auditoria-aplicacao-energyplus-fichas-r13-20261030/verificar.mjs), SHA-256 `4dbf94597f40ed20b31493811445ea8a0bfffdf754aba3898093661c4d6e2971`, passou. Não houve outro delta nas duas páginas.

- **Ficha 88:** a condição adicional de regime permanente complementa, sem substituir, as demais hipóteses: mesmo gás ideal, calores específicos constantes, dois estágios adiabáticos, mesma eficiência isentrópica constante e vazão, resfriamento até T₁ sem queda de pressão e condições de contorno declaradas. Escrevendo `a=(k−1)/k>0`, razões r₁=pi/p₁ e r₂=p₃/pi, com r₁r₂ fixo, o trabalho é proporcional a `r₁ᵃ+r₂ᵃ−2`; pela desigualdade entre média aritmética e geométrica, o mínimo ocorre em r₁=r₂ e `pi=√(p₁p₃)`. Para 1 e 16 bar absolutos, pi=4 bar. A fórmula não é garantia para transientes com armazenamento ou modelos diferentes.
- **Ficha 99:** em regime permanente, q‴V representa a geração térmica total contabilizada e não há outros aportes independentes omitidos; as demais faces são isoladas, sem radiação/outras perdas, com h médio e temperaturas uniformes nos limites da ficha. Assim q‴V=hA(Ts−T∞). Para 1.000 W e hA=20 W/K, ΔT=50 K; um aporte adicional hipotético de 200 W não incluído em q‴ elevaria a saída para 1.200 W e ΔT para 60 K. Se já incluído, somá-lo novamente duplicaria a energia. Valores são testes nominais, não medições nem projeto de componente.

## Referência EnergyPlus

O único `href` alterado na aula aponta agora à [Engineering Reference — EnergyPlus 24.1, Carbon Dioxide Predictor-Corrector](https://bigladdersoftware.com/epx/docs/24-1/engineering-reference/carbon-dioxide-predictor-corrector.html). Abri o destino em 30/10/2026: a página identifica a versão 24.1 e contém balanço transiente de CO₂ com geração, armazenamento e escoamentos, compatível como referência para o tema. O URL antigo do PDF respondeu HTTP 404 na ferramenta de acesso; não se infere indisponibilidade em todos os ambientes. A numeração “seção 2.5” preservada no texto é compatível com o conteúdo indexado do PDF antigo, mas **o PDF não foi obtido em leitura direta** e o HTML consultado não exibe essa numeração. A referência apoia o modelo e não valida automaticamente dados ou decisões de ventilação de uma edificação. O endereço semelhante existente em outro módulo está fora do escopo desta aplicação.

## Preservação, mapa e comportamento

Os 197 artigos e seus 197 registros são idênticos e na mesma ordem; somente `fonte` do inventário oficial atualizou o SHA e fotografia da aula. O JSON do inventário tem SHA-256 `272d7a8fb277b45b60c9253475abe33de2accd061a3e9fe158b9207011bc874e`; o Markdown `0f9e94ea3714ea868b50c76086093ba7b5b3ceb53d387cd24fd4eacbc97ff2e9` preserva o conteúdo anterior e acrescenta seção histórica. Das 100 fichas, apenas `formula-intermediaria` e `formula-geracao` mudaram; as outras 98 são idênticas. Preservaram-se 734 MathML da aula, 191 do formulário e 103 vínculos das fichas para destinos existentes na aula.

O verificador independente [mapa.mjs](../evidencias/QA-09/auditoria-aplicacao-energyplus-fichas-r13-20261030/mapa.mjs), SHA-256 `c53e7b8ea4a9fcaf3d8f3fe6f8375b3bfa0f8d36812bddf96accafc5b5214420`, examinou 11.397 pares únicos: 11.320 externos com deslocamentos esperados e 77 internos cujos hashes foram reconstituídos nas duas fotografias. Seis hashes internos mudaram e três externos, de ancestrais; isso não transfere automaticamente aceites. Dos 815 registros de referências, somente o URL EnergyPlus mudou; os metadados e texto remanescem. Os 138 recursos mantêm suas referências e os hashes atuais foram verificados; os seis ativos específicos não mudaram. O [parecer de apoio independente](QA-09-mapa-r12-r13-apoio-auditoria-independente-r1.md), SHA-256 `ef6e1dd5a8c580979a8607b45807fcdd3f1fb54d761e3b4d8943c965d3b3610b`, descreve a mesma correspondência e a atualização de hashes dos documentos nos registros de recursos.

O validador canônico passou com 197 artigos/itens, 29 recursos e 1.263 links locais, sem erros ou avisos. O teste independente [testar-filtro.cjs](../evidencias/QA-09/auditoria-aplicacao-energyplus-fichas-r13-20261030/testar-filtro.cjs), SHA-256 `08f3821921b43c0697972a67134fbb26c51f2684536103339e10252223e56443`, usa o código real do formulário em Node/VM com DOM simulado e localizou as duas fichas por suas novas hipóteses; termo inexistente retornou zero. Não é teste de navegador real.

A preservação das 98 fichas, MathML, destinos e código, somada ao exame das duas alterações, sustenta **revalidação localizada de FOR-01 para este delta**, não nova auditoria integral de todas as fichas. A preservação dos 197 artigos/registros sustenta ponte localizada para BAN-02/07/08 quanto a esta troca. Os demais pareceres, fontes e ledgers exigem revisão de identidade e dependências para integração em r13.

| Critério localizado | Resultado |
|---|---|
| Reconstrução e identidade dos três deltas | Atendidas na versão efetiva. |
| Modelos e condições das fichas | Atendidos no alcance e nas hipóteses declaradas. |
| Novo vínculo e limites da fonte | Conteúdo e versão verificados; numeração do PDF antigo apoiada em índice, sem leitura direta. |
| Outros artigos, fichas, MathML, mapa e recursos | Preservados ou reconciliados no alcance comparado. |
| QA-09 integral e próximo ID | Não atendidos; permanecem bloqueados. |

Não houve revisão humana, ensaio em navegador real, teste com alunos ou certificação externa. Esta aprovação localizada não classifica o curso inteiro como avançado.
