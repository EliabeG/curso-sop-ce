# BAN-10 r1 — ambiguidades, chaves oficiais e uso no treino

Entrega congelada do Corretor AAA (agente automatizado), 27/10/2026. Aguardando parecer independente; não constitui aprovação própria.

A triagem individual cobriu os **197 itens**. Doze casos receberam decisão fundamentada, com documentos oficiais, interpretação técnica e suplementos autorais identificados. **CR04, CR09, CR24, CR34, CR35, CR39, CR62, CR79 e CR80** agora são estudos críticos sem pontuação. **CR51, CR55 e CR68** permanecem no treino, com hipóteses e alcance delimitados. O conjunto não foi tratado como automaticamente inválido nem como anulado pelas bancas.

A alteração funciona no produto: os nove críticos ficam fora do numerador e denominador, inclusive após carregar marcações antigas. O banco apresenta **71 itens pontuáveis e nove críticos**; o feedback crítico informa apenas coincidência documental com a letra oficial. Cada crítico oferece roteiro de justificativa e autocorreção sem nota. Marcar uma letra antiga não equivale a realizar esse roteiro novo.

A mudança compartilhada limita-se à função iniciarBanco, condicionada a módulo E1 e marcador explícito. Persistência, filtros e identidades das escolhas foram mantidos. Nos 160 itens CR/AV, enunciados, alternativas, gabaritos e digitais permanecem idênticos; as 30 questões iniciais e registro.js não mudaram. Os **185 artigos/registros fora dos 12 casos** foram preservados. FON-09 conserva integralmente os dois detalhes de CR68 e seu arquivo de dados. FUN-01/FUN-02, CSS, schema e validador não mudaram.

## Decisões e rastreabilidade

- [Leitura das decisões e limites](../evidencias/BAN-10/LEITURA_DECISOES-r1.md) e [registro individual dos 12 casos](../evidencias/BAN-10/decisoes-r1.json): justificativas, hipóteses, roteiro, referências, páginas e hashes. CR39 registra a divergência entre leitura usual do apoio e a exclusão conservadora adotada pelo Corretor.
- [Triagem dos 197 itens](../evidencias/BAN-10/triagem-apoio-r1.json): leitura individual do apoio, com hashes da base; candidatos e retenções revistos pelo Corretor. CR78, AV17 e AV37 têm encaminhamentos específicos sem demonstração de ambiguidade de resposta neste recorte.
- [Conferência visual prioritária](../evidencias/BAN-10/conferencia-visual-coordenador-r1.json), [complementar](../evidencias/BAN-10/conferencia-visual-complementar-coordenador-r1.json) e [CR51/CR80](../evidencias/BAN-10/conferencia-visual-cr51-cr80-coordenador-r1.json): documentos oficiais obtidos pelo coordenador, páginas renderizadas e efetivamente vistas. CR68 herda a conferência FON-09 por identidade. Os contramodelos numéricos de CR79 são autorais, não dados da prova.
- [Delta HTML](../evidencias/BAN-10/delta-html-r1.json), [delta JS](../evidencias/BAN-10/delta-js-r1.json) e [delta do inventário](../evidencias/BAN-10/delta-inventario-r1.json). As 13 substituições HTML e quatro JS reconstroem integralmente a versão entregue a partir dos snapshots anteriores.

## Verificações

- [Integridade e preservação](../evidencias/BAN-10/verificacao-r1.json): **589 verificações**, todas satisfeitas. Reproduzir importando evidencias/BAN-10/verificar-r1.mjs e executando verificar(); a função devolve o resultado sem gravar evidências.
- [Comportamento dinâmico](../evidencias/BAN-10/comportamento-r1.json): **18/18 cenários**, executando a função real em DOM/armazenamento controlados; inclui resposta anterior, recarga lógica, filtros, refazer, armazenamento indisponível e isolamento de outro módulo.
- [Validação canônica](../evidencias/BAN-10/validacao-inventario-r1.json): **197 artigos/registros, 29 recursos e 1.166 links locais**, sem erros ou avisos.
- [Navegador do coordenador](../evidencias/BAN-10/navegador-coordenador-r1.md): teste conjunto de crítico e pontuável, recarga, filtros, teclado e conferência final de singular; leitura E2 preservada. O relatório distingue as versões dos testes. Sem aplicação com alunos, teste móvel ou auditoria integral de acessibilidade.

## Versão congelada

[Manifesto, hashes das evidências e cópias](../evidencias/BAN-10/manifesto-r1.json). Quatro arquivos alterados nesta correção:

| Arquivo | SHA-256 |
|---|---|
| modulos/e1-termodinamica.html | 3839c7ba2e473ee9e5b3cdff80ea64242471b83b961eb117cee5a6918c884ae1 |
| assets/curso.js | 6a450cbfb7049b22e999e3390238fec511c2da24caa3e228871c5a3128121de6 |
| auditoria/termodinamica/inventario/inventario-questoes.json | d4a64b53747170f9d1d9cd0446d3f1de22110c73454c9f4fdf9359b005434641 |
| auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md | 38a90361a7912dfc0839927ea50b044b6e87b0116eec2085b515573b648f3d68 |

O pacote guarda também cinco dependências intactas, e os snapshots anteriores permanecem em antes/. Os apoios técnico, documental e de navegador são atribuídos aos respectivos agentes; não substituem o Auditor. Esta entrega não encerra BAN-07, BAN-08 ou FON-01 globais, nem certifica o curso como avançado. Nenhum controle/checklist ou próximo ID foi alterado/iniciado.
