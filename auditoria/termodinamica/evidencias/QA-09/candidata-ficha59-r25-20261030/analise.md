# QA-09 — candidata isolada para ficha 59 r25

30/10/2026. Corretor `/root/next_formulas`. **Não aplicada; aguarda Auditor independente.** Responde ao parecer `QA-09-fichas-ciclos-latente-r25-auditoria-reference-triage-20261030.md`, SHA `b06fe883ee647a10a12c5e4f01a1a910373db8d933aa40bf8151de24eb96da08`; não encerra QA-09.

## Proposta e modelo

O cartão e `data-busca` passam a definir `Win` como trabalho líquido total recebido, igual às entradas menos as saídas de trabalho na mesma fronteira, ciclo e período, com Win>0. Mantém-se o refrigerador acionado por trabalho sem outra fonte energética de acionamento, o COPR=QL/Win, os símbolos, unidade, título e MathML. QL é explicitado como magnitude do calor retirado da fonte fria. A definição não obriga entrada bruta e líquida a serem diferentes; torna explícita sua diferença quando há saída de trabalho.

Contraste sintético: entradas de trabalho de 100 kJ e saídas de 20 kJ produzem Win=80 kJ. Com QL=300 e QH=380 kJ, primeira lei fecha, COPR=300/80=3,75, enquanto usar apenas entrada bruta daria 3. Com reservatórios a 300 e 350 K, Sger=380/350−300/300=3/35>0 kJ/K. O contraste não é equipamento real nem prova de realização técnica. A [definição DOE/FEMP de COP](https://www.energy.gov/cmei/femp/incorporate-minimum-efficiency-requirements-heating-and-cooling-products-federal) especifica trabalho líquido de entrada e unidades coerentes.

## Identidade e simulação

Formulário r25 SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`; inventário r25 `6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116`. `manifesto.json` SHA `228c16439f800be7b4753b728c42f4a856f88c18b2528b18d8b588c53c82743e` registra recorte, posição UTF-16 e hashes de fragmento sem a quebra terminal dos arquivos. O verificador somente leitura `verificar.mjs` SHA `1006f94eb9ed924bb5707b5ea0ab72d31615be73f6674ef5c3fc2b67294c6b64` reconstrói os dois deltas nas duas ocorrências de cada texto, testa condições, parser, 100 cartões, 99 não alvo, 191 MathML e atributos ID/link/ARIA; passou. Formulário hipotético SHA `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02`. O cálculo não demonstra por si a ciência nem testa navegador ou acessibilidade. Qualquer mudança de base exige reconciliação; eventual aplicação exige nova fotografia, mapa e auditoria distinta da versão efetiva.
