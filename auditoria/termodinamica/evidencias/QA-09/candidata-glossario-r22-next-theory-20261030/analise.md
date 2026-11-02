# QA-09 — candidata isolada do glossário, r22

30/10/2026. Corretor `/root/next_theory`. **Não aplicada; aguarda auditor independente.** Responde ao [parecer de resumo e glossário](../../../pareceres/QA-09-teoria-resumo-glossario-r22-auditoria-next-formulas-20261030.md).

No verbete COP, a candidata restringe a definição a refrigerador/bomba de calor acionados por trabalho, sem outro acionamento energético relevante; divide calor útil pelo trabalho líquido total recebido positivo na mesma fronteira e período. Esse é um modelo determinado, sem negar que outros tipos de máquina térmica admitam indicadores próprios. O verbete de Z passa a chamar-se “Fator de compressibilidade”, indicador adimensional do desvio da relação p–V–T de gás ideal, distinto da compressibilidade isotérmica. Z=1 num estado não prova comportamento ideal de todas as demais propriedades.

Em um gás ideal, Z=1 e κT=1/p: a 100 e 200 kPa, κT=0,01 e 0,005 kPa⁻¹, respectivamente. [NIST REFPROP](https://www.nist.gov/system/files/documents/srd/REFPROP8_manua3.htm) distingue fator de compressibilidade e compressibilidade isotérmica.

Fotografia r22 SHA `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f`; inventário SHA `6e68d5a9e5cfec73aa2a5ce24121ede1c3a155ca2a5783cf6f17ca95eee8061b`. Seção `glossario` UTF-16 1285927–1288715; original SHA `9348a83d7a739d23a454f8a3ca8810f4891f09fd762dd69b3fa1aa5895a5cf01`; candidata SHA `40e448e1d3c7d1294f9332b1ff780f1f5fd7566da772210c06e4e8f1c93e429c`. Arquivos isolados possuem quebra final excluída dos hashes; manifesto registra duas substituições literais.

`node auditoria/termodinamica/evidencias/QA-09/candidata-glossario-r22-next-theory-20261030/verificar.mjs` passou: simulação em memória preserva 197 artigos, todos os 734 MathML e atributos inspecionados de IDs, links e ARIA; SHA do HTML hipotético `958daf07cf7c908a8e1ead2ceba64806df2c978d97836fdc5692c1dbe269d7fe`. O teste não substitui revisão científica independente nem experiência de navegador. Qualquer aplicação exige reconciliação, fotografia e auditoria efetiva.
