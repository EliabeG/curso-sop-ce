# FON-09 r1 — dados defeituosos associados a CR68

Entrega congelada do Corretor em 27/10/2026 para auditoria independente. Escopo exclusivo FON-09; não encerra FON-01, BAN-10, BAN-08 ou QA-04 gerais. Nenhum controle/checklist foi editado pelo Corretor.

A própria prova oficial p. 3 contém a unidade kg/cm³ e as cinco linhas que o caderno p. 14 e o HTML reproduzem. Foram conferidos os três documentos e o gabarito definitivo, item 85→C. A transcrição histórica ficou recolhida, identificada e advertida como inadequada para cálculos. A afirmação continua visível para julgamento; alternativas, gabarito, resolução e digital de resposta permanecem iguais.

O conjunto editorial corrigido FON-09 v1.0 publica as cinco pressões, temperaturas e volumes de ambas as fases, com fonte/método/precisão. As quatro últimas linhas vêm da NISTIR 5078, tabela 2, p. impressa 12 / PDF 2, com conversões exatas de MPa e cm³/g. A primeira linha veio de consulta direta NIST WebBook a 101,325 kPa; não houve interpolação. A densidade física de referência a 25 °C / 101,325 kPa é 997,04764 kg/m³; 1000 kg/m³ é aproximação incompressível declarada. A correção não se apresenta como errata oficial nem presume intenção tipográfica.

Na primeira linha histórica, 100 °C e 0,00104 m³/kg são compatíveis com arredondamento; o volume do vapor não é. As outras 12 células físicas são incompatíveis com a precisão impressa. O confronto das 15 células está documentado, sem tratar arredondamento legítimo como erro.

## Evidências e validação

- [Origem e confronto integral](../evidencias/FON-09/conferencia-origem-r1.md), [pesquisa das referências físicas](../evidencias/FON-09/apoio-dados-r1.md) e [conferência visual do coordenador](../evidencias/FON-09/conferencia-visual-coordenador-r1.json). Capturas dos três PDFs e respostas HTML primárias estão preservadas.
- [Verificação reproduzível](../evidencias/FON-09/verificacao-r1.json): 470 verificações; somente CR68 mudou no HTML, 196 artigos/registros anteriores intocados e 197 linhas anteriores do resumo preservadas. A digital permaneceu `f78a5342`; `assets/registro.js`, CSS, JavaScript do curso e schema estão intactos.
- [Validação canônica](../evidencias/FON-09/validacao-inventario-r1.json): 197 registros/197 artigos, 15 recursos e 1.072 links locais, zero erros/avisos. O [delta do inventário](../evidencias/FON-09/delta-inventario-r1.json) identifica os 11 campos alterados de metadados gerais/CR68; demanda e classificação preservadas.
- [Contrato existente](../evidencias/FON-09/contrato-existente-r1.json): 39 casos passaram. [Testes PDF](../evidencias/FON-09/teste-pdf-r1.json): 8 casos passaram. Ajuste técnico autorizado: aceitar somente `#page=N` inteiro positivo seguro em arquivos .pdf existentes; âncoras HTML e outros recursos mantêm a verificação. A quantidade real de páginas continua sendo conferência documental, realizada nos três documentos desta entrega. [Delta integral do validador](../evidencias/FON-09/delta-validador-r1.json).
- [Navegador do coordenador](../evidencias/FON-09/navegador-coordenador-r1.md): tabela legível, pressão 101,325 sem quebra, dois blocos recolhíveis funcionais, resolução/gabarito e teclado conferidos; nenhuma alternativa foi marcada. O delta final da nota apenas tornou inequívoca a atribuição dos erros à tabela histórica.

## Arquivos congelados

[Manifesto com cópias, hashes e evidências](../evidencias/FON-09/manifesto-r1.json). Base aprovada preservada em `antes/`; resultado em `pacote-r1/`.

| Arquivo alterado/novo | SHA-256 |
|---|---|
| modulos/e1-termodinamica.html | `6ed5c74f03b2ce449f88e79d143c904442c524166a83afce8f12441d391a6625` |
| assets/termodinamica/fon09-cr68-dados-v1.json | `828b967f1318924742e8b30aca8575549301afcccaad395f9ed5bcee2fc46456` |
| auditoria/termodinamica/inventario/inventario-questoes.json | `af30160109fa7e9e007e6de74eb1836896194ff90888aec75e0f8a4a86675618` |
| auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md | `1505e80c437fdd6dbbea40973155446ec859ba2fb363752217346876a8fb43db` |
| auditoria/termodinamica/inventario/validar-inventario.mjs | `114b1a063cb2a88e505c9ecffd2b22c75f29b709419b24e9e533331fa7283b22` |

Reprodução: importar `verificar-fon09-r1.mjs` e chamar `verificarFon09()`; importar `testar-pdf-r1.mjs` e chamar `testarPdf()`. A cópia `reexecutar-contrato-r1.mjs` mantém os fixtures BAN-02 e exporta `resultadoContrato` em vez da saída CLI, sem mudar expectativas.

Responsáveis: Corretor (confronto, integração, dados, inventário, preservação e ajuste técnico); apoio_fun01 (pesquisa NIST); coordenador (obtenção/renderização de PDFs, conferências visual/numérica e navegador). O Auditor independente ainda emitirá parecer. Não houve teste com estudantes nem reavaliação dos outros itens da prova. Aguardando gate de FON-09 r1.
