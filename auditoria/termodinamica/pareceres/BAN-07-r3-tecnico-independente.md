# BAN-07 r3 — parecer técnico independente

Data: 29/10/2026. Revisora: agente automatizado `/root/auditoria_av61_70`, independente do Corretor. **Resultado: AJUSTE R2-A ATENDIDO no escopo técnico e de BAN-02 afetado.** Este parecer de apoio não aprova BAN-07 global, não certifica o curso e não libera outro ID; a decisão da versão completa cabe ao Auditor principal e ao coordenador.

## Versão e integridade

Li [entrega BAN-07-r3](../entregas/BAN-07-r3.md), SHA-256 `cd4ffc56d53f8c0a0ba429e1162c88ec10faead9bed82600a875076b5cdd95c1`, e manifesto `auditoria/termodinamica/evidencias/BAN-07/manifesto-r3.json`, SHA-256 `04c677c6bd5472e65c2ba381549461df3412d6a43313721ca4caf2c071526b3b`. Conferi independentemente **15 entradas**: inventário atual, dez arquivos declarados preservados, três evidências de r3 e parecer r2. Todos existem e seus SHA-256 coincidem com o manifesto. Isso cobre essas entradas, não todos os arquivos não enumerados.

O inventário r2 de backup tem SHA-256 `71ac07e042aa65675fc3d4b69d8d0ae11cb66df967d45e66b1a88f4f1350e074`; o inventário aplicado r3 `486c53c5aa6c432831599c4eca170e4620d089b4eb15b480dbfb2cbfaf54c9ce`. O HTML e snapshot mantêm `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; `assets/curso.js` mantém `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` e `assets/registro.js` mantém `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`. Markdown, complementos, manifesto e entrega r2 também coincidem com suas referências de r2.

## Comparação e revalidação localizada de BAN-02

Comparei os JSONs r2/r3 recursivamente e encontrei **somente dois caminhos alterados**, ambos no único registro `cr-e1-06`:

1. `raciocinio.etapas[0]`: de “Relacionar dilatação constante com transformação afim entre escalas” para “Reconhecer a relação afim entre as escalas quando ambas são lineares na altura da coluna, conforme hipótese editorial do curso”.
2. `vinculo_competencias.alcance`: usa a mesma nova descrição, mantendo o vínculo parcial C08 e a ressalva de que não avalia integralmente a competência avançada.

A nova redação identifica a condição efetivamente necessária e sua origem editorial, sem a atribuir ao original. Categoria `reconhecimento`, uma etapa, nível estimado `iniciante` e competência C08 permanecem coerentes com essa tarefa delimitada; o julgamento é local, não valida empiricamente o nível nem a competência inteira. Os demais 196 registros e todos os outros campos permanecem iguais. Em teste próprio, reverter em memória as duas ocorrências do texto novo restaura **byte a byte** o backup r2 completo; nenhum arquivo foi regravado. A linha única do Markdown CR06 permanece coerente com competência, nível, uma etapa e justificativa, que identifica o suplemento do curso. Assim a pendência apontada por [BAN-07-r2](BAN-07-r2.md), SHA-256 `06ee05437bf9b834ba6936b269c44b30da9f265fc51b73b24ee1beaa5b65cd2f`, está resolvida na versão r3.

Executei diretamente `validateInventory` em leitura no produto atual, sem escrever resultados: **197 registros, 197 artigos, 29 recursos, 1.261 links locais, zero erros e avisos**. O validador verifica estrutura e rastreio, não substitui a comparação semântica nem certifica ciência ou aprendizagem. A identidade de HTML e JS sustenta a aplicabilidade dos testes de digitais e progresso r2 no mesmo alcance, e não prova navegador real, todos os históricos ou novos cenários. As evidências anteriores são atribuídas aos seus autores; não alego novo teste de navegador ou persistência nesta r3.

## Falha inicial e restauração

A entrega e `aplicacao-r3/verificacao-r3.json`, SHA-256 `f990f55066e42a10e1bf75867de271055ebb37255351ec933d7a5fcd4065387b`, relatam que a primeira execução falhou ao registrar a verificação após substituir o inventário, que o retorno restaurou r2, e que a segunda execução, após correção do registrador, foi bem-sucedida. Li `aplicar-r3.mjs`, SHA-256 `eb71c10a6965b2cef2129af18dc4f5596dc552ae792eb29242aa711f9aa8aa44`: na versão atual, a exceção depois da substituição entra no `catch` e copia o backup para o inventário. O backup efetivo coincide com o hash r2 e o estado atual é comprovadamente r3, com apenas as duas substituições acima.

Esses elementos sustentam a consistência do estado final e a capacidade prevista pelo código atual; **não são uma gravação independente do erro original ou do instante da restauração**. Não reexecutei o aplicador nem provo por observação própria o fluxo da primeira tentativa. O relato permanece atribuído ao Corretor; a verificação final não oculta o incidente e não transforma a narrativa em teste executado por esta revisora.

## Critérios e decisão

| Critério | Resultado localizado |
|---|---|
| Integridade de manifesto, versão e backup | 15 entradas coincidem; HTML, Markdown, JS e evidências de r2 preservados nos hashes declarados. |
| Delta e preservação | Exatamente dois campos de CR06; reversão em memória restaura integralmente os bytes r2. |
| R2-A e coerência BAN-02 | Atendidos para raciocínio, alcance, hipóteses, nível e resumo de CR06, no escopo afetado. |
| Validador canônico | 197/197, 29 recursos, 1.261 links, sem falhas ou avisos; limite estrutural declarado. |
| Falha e rollback | Incidente registrado pelo Corretor; código atual e backup sustentam o mecanismo e o estado final, sem observação independente da primeira tentativa. |
| Digitais/persistência | R2 é reutilizável no alcance de identidade de HTML e código; nenhum novo teste em navegador ou armazenamento pessoal. |

**Recomendação:** considerar R2-A atendido e levar esta evidência ao Auditor principal para integrar os demais critérios e decidir BAN-07 r3. Não se aprova BAN-08, DID-07, acessibilidade, aprendizagem ou próximo ID por este parecer. Produto e controle não foram alterados nesta revisão.
