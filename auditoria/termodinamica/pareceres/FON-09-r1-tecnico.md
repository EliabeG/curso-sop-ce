# FON-09 r1 — subauditoria técnica independente

Data: 2026-10-27. Escopo: contrato do inventário, preservação, integridade do pacote, execução dos verificadores e sintaxe de referências PDF. Este documento fornece evidências ao Auditor AAA; não emite decisão geral de aceite nem autoriza próximo ID. A evidência detalhada está em `FON-09-r1-tecnico.json`, neste diretório.

## Achado único R1-A — fragmento PDF truncado antes da validação

Em `auditoria/termodinamica/inventario/validar-inventario.mjs:201`, `const [beforeHash, rawFragment] = reference.split('#')` descarta todos os componentes posteriores ao primeiro fragmento. A nova expressão regular PDF valida apenas a parte retida. Assim, os dois valores abaixo são aceitos sem erro, embora não satisfaçam integralmente o contrato declarado `page=N`, com N inteiro positivo seguro:

```text
downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf#page=3#extra
downloads/termodinamica/provas/2024-03-24_petrobras-tecnico-operacao-2023-2_prova.pdf#page=3#
```

Reprodução independente: clonar o inventário atual em memória, acrescentar cada referência isoladamente a `origem.fontes` de CR68 e executar o validador exportado contra a raiz do projeto. Resultado esperado: rejeição. Resultado observado em ambos: `ok: true`, `erros: []`. O caso com `%23extra`, em vez do segundo `#` literal, é rejeitado; a diferença confirma o truncamento como causa comum. Os dois casos constituem um único achado.

A correção deve avaliar o fragmento completo após o primeiro `#` e rejeitar os sufixos inválidos, preservando o contrato para HTML e outros recursos. A existência física da página não é objeto desse achado.

## Integridade e preservação

- Cinco arquivos publicados e suas cinco cópias do pacote coincidem em SHA-256 e tamanho com o manifesto. As 26 evidências e os cinco snapshots anteriores conferem com seus hashes declarados.
- A extração independente dos artigos confirma 196 artigos não afetados idênticos. A comparação dos objetos por ID confirma os 196 registros não afetados idênticos. As 197 linhas individuais anteriores do resumo Markdown permanecem exatamente uma vez.
- Substituir exclusivamente o artigo CR68 atual pelo artigo anterior reconstrói literalmente todo o HTML anterior. A comparação independente do inventário encontrou 11 campos alterados, com listas tratadas como valores completos; o detalhamento está no JSON.
- `registro.js`, `curso.js`, `curso.css`, schema e guia permanecem iguais à base independente previamente conferida. O delta do validador reconstrói integralmente o arquivo atual a partir do prefixo e sufixo preservados e do único trecho declarado.
- O enunciado histórico foi preservado literalmente dentro de `details`; alternativas, gabarito e resolução anteriores permanecem preservados conforme a conferência estrutural reproduzida.
- Funções reais de `assets/curso.js` foram executadas em VM com adaptador DOM, incluindo o tratamento de MathML. A digital de CR68 permanece `f78a5342`. As funções reais de leitura/atualização de respostas recarregaram corretamente C e E em armazenamento simulado. Nenhum armazenamento do usuário foi acessado.

## Execuções reproduzidas e testes próprios

Os scripts foram lidos antes da execução. O verificador e os testes PDF operam por leitura e clones em memória; o contrato anterior cria fixtures em diretório temporário. Foi usado um Node REPL novo, evitando reutilizar o validador anterior em cache. Não houve execução por Node CLI.

| Origem | Execução | Resultado |
| --- | --- | --- |
| Entregue | `verificar-fon09-r1.mjs` | 470/470 verificações satisfeitas |
| Entregue | Validador chamado pelo verificador | 197 registros, 197 artigos, 15 recursos e 1072 links locais; zero erros e avisos |
| Entregue | `testar-pdf-r1.mjs` | 8/8 casos satisfeitos |
| Entregue | `reexecutar-contrato-r1.mjs` | 39/39 casos satisfeitos; importação concluída |
| Independente | 24 casos PDF/HTML/outros recursos | 22 resultados esperados; duas falhas da mesma causa R1-A |

O contrato reexecutado preserva literalmente as fixtures e expectativas do script BAN-02 anterior, até o epílogo adaptado para exportação. Os resultados atuais e os registrados coincidem após normalizar somente o nome aleatório do diretório temporário nas mensagens ENOENT. A comparação bruta difere por esse nome, sem divergência de comportamento. O verificador e os oito testes PDF coincidem com os resultados registrados.

Os casos próprios cobriram página positiva, limite de inteiro seguro, extensão PDF em maiúsculas, query string, fragmento codificado, zero, negativo, fração, notação exponencial, sinal positivo, zero inicial, inteiro inseguro, valor ausente, fragmento arbitrário, parâmetro extra, segundo `#`, espaço final, arquivo ausente, âncoras HTML existentes/ausentes e arquivo JSON com fragmento de página. A lista integral, expectativas e erros observados constam do JSON.

## Documentação e limites

O guia não foi alterado e não explicita a nova regra PDF. O resumo canônico aponta para a entrega, que documenta o limite de sintaxe/existência do arquivo e separa a conferência documental da quantidade real de páginas. Considerados em conjunto, esses documentos não sustentam um segundo achado bloqueador por ausência isolada no guia. Consolidar essa regra no guia seria uma melhoria de manutenção.

Esta subauditoria não reavalia ciência das células, validade das fontes físicas, conteúdo/paginação real dos PDFs ou renderização em navegador. Os 470 checks entregues foram efetivamente reproduzidos; seus checks numéricos não substituem a análise científica independente do Auditor. O teste de digital/respostas executa funções reais com DOM e armazenamento simulados e não constitui teste de navegador.

## Hashes centrais conferidos

| Arquivo | SHA-256 |
| --- | --- |
| HTML publicado | `6ed5c74f03b2ce449f88e79d143c904442c524166a83afce8f12441d391a6625` |
| Dados CR68 | `828b967f1318924742e8b30aca8575549301afcccaad395f9ed5bcee2fc46456` |
| Inventário | `af30160109fa7e9e007e6de74eb1836896194ff90888aec75e0f8a4a86675618` |
| Resumo | `1505e80c437fdd6dbbea40973155446ec859ba2fb363752217346876a8fb43db` |
| Validador atual | `114b1a063cb2a88e505c9ecffd2b22c75f29b709419b24e9e533331fa7283b22` |
| Validador anterior | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |

Nenhum arquivo de produto, controle, inventário ou evidência do Corretor foi modificado nesta subauditoria. Os únicos arquivos permanentes escritos são este parecer e seu JSON técnico.
