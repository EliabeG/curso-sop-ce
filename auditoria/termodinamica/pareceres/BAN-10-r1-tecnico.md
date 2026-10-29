# BAN-10 r1 — subauditoria técnica independente

Data: 27/10/2026. Revisor: agente automatizado de apoio técnico ao Auditor AAA. Versão congelada confirmada pelo Auditor. **Não foi identificado bloqueador no escopo técnico examinado.** Este documento não emite gate geral, não decide sobre mérito científico e não libera próximo ID.

Escopo: regra E1 + marcador explícito, contagem, feedback, identidade/persistência/recarga, filtros/refazer, comportamento padrão dos demais fluxos e integridade. Foram lidos o protocolo, a preparação independente, o plano, os scripts de verificação, o código alterado, a entrega e o manifesto. A evidência detalhada, resultados individuais, digitais e código do adaptador estão em `BAN-10-r1-tecnico.json` neste diretório.

## Versão efetivamente examinada

| Arquivo | SHA-256 |
| --- | --- |
| Manifesto r1 | `1fd879c048b08565e901055281545f44f65a39f21ca87b3901f0e8263077f7f7` |
| HTML | `3839c7ba2e473ee9e5b3cdff80ea64242471b83b961eb117cee5a6918c884ae1` |
| curso.js | `6a450cbfb7049b22e999e3390238fec511c2da24caa3e228871c5a3128121de6` |
| Inventário | `d4a64b53747170f9d1d9cd0446d3f1de22110c73454c9f4fdf9359b005434641` |
| Resumo | `38a90361a7912dfc0839927ea50b044b6e87b0116eec2085b515573b648f3d68` |

Os nove arquivos publicados e suas nove cópias, seis snapshots, 61 evidências e a entrega conferem em tamanho e hash: 77 entradas verificadas, além das cópias. Os hashes HTML/JS permaneceram iguais entre o início da subauditoria e o congelamento. As 13 substituições HTML e quatro substituições JS declaradas reconstroem integralmente os arquivos atuais a partir da base, com ocorrência única de cada trecho anterior.

## Execução e resultados

O kernel Node REPL foi reiniciado antes das importações. Os scripts foram lidos antes de executar; somente verificadores sem gravação de produto foram chamados. Não foram executados os scripts de integração ou atualização de inventário.

- Verificador entregue: **589/589 verificações** satisfeitas, incluindo os **18/18 comportamentos** entregues. O resultado reproduzido coincide integralmente com `verificacao-r1.json`.
- Validação canônica reproduzida: **197 artigos/registros, 29 recursos e 1.166 links locais**, sem erros ou avisos.
- Verificações próprias: **28/28** satisfeitas. Foram executadas as funções reais de `curso.js`, incluindo `idModulo`, `digitalDoBanco`, `textoDaDigital` e `iniciarBanco`, sobre os artigos reais, com DOM e armazenamento controlados. Essas verificações não são contadas como testes de navegador.

## Critérios técnicos e rastreabilidade

| Critério | Resultado observado |
| --- | --- |
| Escopo E1 + marcador exato | O guarda exige `idModulo() === 'e1'` e `crAvaliacao === 'estudo-critico'`. Diferenciais contra JS anterior preservaram o resultado para E2, metadado ausente, E1 sem marcador e marcador diferente. |
| Exclusão efetiva da pontuação | Recarga das 80 respostas CR anteriores: 71 itens pontuáveis e nove marcações documentais. Todas as respostas concordantes produzem 71 acertos; todas as divergentes produzem 71 erros. Nenhum dos nove críticos entra no numerador ou denominador. |
| Feedback crítico | Todos os nove artigos reais foram conferidos com marcas concordantes e divergentes. O feedback compara com a chave oficial, preserva neutralidade e não grava `data-cr-resultado` certo/errado. O roteiro/análise pode ser aberto sem transformar a letra em medida de domínio. |
| Identidade e recarga | As **160 digitais reais CR/AV** são iguais antes/depois, calculadas pelas funções efetivas, incluindo tratamento de MathML. Uma nova marca divergente de CR79 persistiu e foi recarregada sem pontuar. |
| Histórico e falhas de armazenamento | O registro v1 permanece literalmente igual, é anunciado como histórico e não é aplicado ao placar atual. Uma marca nova grava v2. Dados v2 não reconhecidos permanecem ao refazer outro item. Falhas separadas de leitura e gravação mantêm o histórico, exibem aviso e preservam a exclusão local. |
| Filtros/refazer/entre abas | Assunto, banca e busca alteram visibilidade sem alterar agregados. Pendentes trata marcas críticas como respostas documentais; refazer reabre o item. Link direto limpa filtros. O evento `storage` atualiza a marca crítica mantendo os 71 acertos pontuáveis. |
| Preservação Q/AV e fluxo compartilhado | Os 30 Q e 80 AV estão literalmente iguais à base; `iniciarQuestoes` permanece igual. O fluxo AV executado com código anterior/atual produz o mesmo feedback e placar. As alterações JS estão restritas a `iniciarBanco`. |
| Demais preservações declaradas | A reprodução do verificador confirmou os 185 artigos/registros fora das 12 decisões, FUN-01/FUN-02, conteúdo FON-09 e dependências intactas. A identidade do pacote foi conferida separadamente pelo manifesto. |

O banco só crítico, ausência total de respostas, resposta regular e armazenamento negado também constam dos 18 cenários entregues efetivamente reexecutados. A lista dos 28 testes próprios distingue esses resultados da reprodução entregue.

## Limites e encaminhamento

O adaptador usa os artigos reais e executa o código real, mas simula DOM, eventos, armazenamento e lotes de quatro itens. Não verifica layout, CSS, criação física dos lotes, acessibilidade ou comportamento completo de um navegador. O teste E2 verifica o guarda por comparação controlada com o código anterior; não é uma visita ao módulo E2. Nenhum navegador ou armazenamento do usuário foi acessado.

A cobertura estrutural dos 197 registros de triagem no verificador não substitui sua leitura científica. Mérito das 12 decisões, fontes, gabaritos, interpretação física e suficiência pedagógica pertencem ao Auditor principal. Não houve auditoria global BAN-07/BAN-08/FON-01 nem aplicação com alunos.

**Ajustes técnicos obrigatórios identificados: nenhum.** A decisão geral sobre BAN-10 r1 permanece com o Auditor AAA. Foram escritos somente este arquivo e o JSON técnico, sem alteração de produto, controle ou evidências do Corretor.
