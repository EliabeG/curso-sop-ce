# QA-09 — quatro referências gerais, r19

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto de `/root/reference_triage`, autor do lote histórico. **Identidade, acesso observado e pertinência temática confirmados para estes quatro vínculos**, sem aprovar todo o conteúdo remoto, os demais vínculos ou QA-09. A aula e o inventário r19 têm SHA `9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65` e `ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f`.

Comparei os elementos com o lote r13 `referencias-gerais-r13-20261030/entrega.md`, SHA `6f81d89b3a712bdbb23ed5c91759ca41ff6d30e97876df0cefd1a2368f0cf706`, e identidades `58fd0bc7b7db347b85f54998d3f05d32858d298b2c4ffb8b5facdc1e963e5b84`. Depois reabri as fontes, sem presumir aceite pela identidade. Os offsets são UTF-16 r19 e cada hash cobre o elemento `<a>` completo.

| Índice r13 | Posição r19 | SHA-256 do elemento |
|---:|---|---|
| 668 | 1300744–1300934 | `23df24f80bce0e0569557601cb3a0f7b08db7026d9b4f70d10525e06e6fe5b21` |
| 669 | 1300943–1301124 | `3f46423ef2785aeed356bacf6cc83176939e1e9e0f94b02b58f532ac416c7069` |
| 670 | 1301133–1301297 | `d0a1b4360bab8e6a280bee6c54832540488344bdecdbe0bdfa3ee613fcb6ef41` |
| 672 | 1301661–1301810 | `02ed5681a4cef01118a3422c9185550da98e61c42b1b421a9c101e0992d0b759` |

* [MIT OCW, Thermal Energy, índice de notas](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/pages/lecture-notes/) abriu e lista segunda lei, ciclos a gás e a vapor e transferência de calor, em curso de 2002. É índice de material didático; a verificação do índice não é exame integral dos PDFs nem certificação de nível avançado.
* [MIT, primeira lei aplicada a ciclos](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node21.html) abriu e apresenta a análise de ciclos ar-padrão como idealização, incluindo ar como gás perfeito com capacidades constantes e processos internamente reversíveis. A fonte não garante as hipóteses ou resultados de uma instalação real.
* [DOE-HDBK-1012/1-92](https://www.energy.gov/ehss/articles/doe-hdbk-10121-92) abriu, identifica manual de propriedades e balanços e aponta ao PDF de 138 páginas, cuja capa indica junho de 1992. A página o classifica como **Archive**: usar como referência didática contextual, não presumir norma vigente nem aplicar números do manual a qualquer caso do curso.
* [BIPM, Brochura SI](https://www.bipm.org/en/publications/si-brochure) abriu; a versão inglesa examinada é 9ª edição, versão 4.01, junho de 2026, DOI `10.59161/AUEZ1291`. Na p. 19 do PDF (p. impressa 129), a relação é `t/°C=T/K−273,15` e intervalos em °C e K têm mesmo valor numérico; o grau Celsius tem nome especial no SI. É uma página dinâmica, por isso a versão e trecho consultados são identificados aqui.

O verificador `auditoria/termodinamica/evidencias/QA-09/auditoria-fontes-gerais-r19-20261030/verificar.py`, SHA `205a4ae3db75a69c6d1c539cd6fb8a1cbe3ca10c8729aa6cea3be92d520aa418`, passou e verifica em leitura local os quatro vínculos, posições e hashes r13/r19. Não testa rede nem estabelece mérito científico integral. As observações de acesso são da ferramenta de pesquisa em 30/10/2026 e podem variar; não houve navegador do curso, leitor de tela, estudantes ou revisão humana. Outros registros seguem pendentes de integração individual.
