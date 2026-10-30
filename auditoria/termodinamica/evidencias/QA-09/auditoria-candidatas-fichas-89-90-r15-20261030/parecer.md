# QA-09 — parecer independente das candidatas 89 e 90, r15

Data: 30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do Corretor `/root/next_formulas` e do Auditor da ressalva original `/root/next_theory`. **APROVADAS as candidatas isoladas no escopo examinado**, sem aplicação automática; isso não aprova sua aplicação futura, o formulário integral ou QA-09.

## Identidade e preservação

Base `formulas/termodinamica.html` SHA `3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce`; inventário r15 SHA `c8c9c3a3e141eba47a16e9f85c69f97c6e8b8a55aab689c6120ef1a0070c9d9c`; análise da candidata SHA `376d6bd380b91b590a504b93e926f7f399ea4d648460d86e3e0de2f87e1a1f4a`; manifesto SHA `093609d634e7e875aa51e5999494fa3ec2642be5c63c91e8a8c3a58de6a13cdf`. O parecer anterior referido tem SHA `4dbf25c1a899fb3d1f392a5b00ffc7c467aecdc863b1de189db4212c440ce13e`.

Comparei diretamente os HTMLs das duas fichas com a base e entre si. Os quatro pares de substituições ocorrem somente no texto de condição/símbolos e em suas respectivas cópias no atributo `data-busca`. A simulação produz SHA `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`; revertendo os dois recortes, toda a base é recuperada byte a byte. Fórmulas MathML, IDs, títulos, links, demais atributos e texto das fichas permanecem iguais. O verificador do Corretor passou: parser sem erro, 100 cartões, 98 não alvo preservados e 191 MathML, na simulação. Não se construiu nem se aplicou um produto novo no disco.

## Exame físico

As candidatas declaram explicitamente uma entrada e saída, regime permanente internamente reversível, gás ideal de composição fixa, pressões absolutas da entrada e saída na mesma unidade, `p₂>p₁>0`, variações cinética e potencial desprezíveis, e trabalho total não associado ao escoamento somente de eixo. Assim, o trabalho recebido por massa `w_in=∫₁²v dp` é o **total** de eixo, não o trabalho de determinado eixo individual. As condições fazem a diferença apontada pelo parecer original; não exigem adiabaticidade. A 89 mantém `pv^n` constante, n>0 e n≠1; a 90 explicita isotermia.

Na 89, integrando o caminho politrópico ideal obtém-se `n/(n−1) RT₁ [(p₂/p₁)^((n−1)/n)−1]`, sem exigir calores específicos constantes para essa integração. Para R=0,287 kJ/(kg·K), T₁=300 K e p₂/p₁=4: n=2 dá 172,2 kJ/kg; n=0,5 dá 64,575 kJ/kg, ambos positivos. No limite n→1, a expressão tende a `RT ln(p₂/p₁)`; a ficha 90 dá 119,359944 kJ/kg para a mesma condição isotérmica. As pressões absolutas e o argumento da potência/logaritmo são adimensionais; RT possui unidade kJ/kg.

O contraste de dois acionamentos do Corretor soma 89,359944+30=119,359944 kJ/kg: ambas as parcelas são hipotéticas e a equação é do total. Para compressão isotérmica do mesmo gás ideal, Δh=0, q=−119,359944 kJ/kg e Δs=q/T=−R ln 4: balanços são consistentes com reversibilidade interna no modelo. Isso não demonstra um projeto físico construído. A fonte [Purdue ME 200, pp. 68–70](https://www.purdue.edu/freeform/me200/wp-content/uploads/sites/29/2023/03/ME-200-Chapter-6.pdf), reaberta em 30/10/2026, sustenta a integral e as expressões para os modelos expostos; não fornece os números fictícios.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-candidatas-fichas-89-90-r15-20261030/verificar.py` retorna `ok: true`. SHA do script `1270e9b8908857ae612558b8398179a10e4c0c0ba16ce2efcdda0afd2656f65f`. Ele confere hashes, intervalos, substituições, igualdade de MathML, reconstrução integral e valores escolhidos; tolerância absoluta 10⁻¹⁰ kJ/kg nos valores nominais e 10⁻⁴ kJ/kg para as duas aproximações a n=1. A derivação física e a leitura dos cartões são independentes do teste, que não substitui a auditoria da fotografia efetiva após eventual aplicação. Não houve teste em navegador, leitores de tela, estudantes ou revisão humana.
