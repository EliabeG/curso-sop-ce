# FUN-01 r1 — auditoria técnica auxiliar

Data: 27/10/2026. Autor: `/root/auditor_aaa/auditoria_tecnica_ban02`, apoio independente do Auditor responsável.

**A infraestrutura, a preservação e a reprodução documental conferem. Há duas divergências documentais de título no inventário. Este relatório não emite o parecer geral de FUN-01 nem libera outro ID.**

## Achado: títulos antigos em dois registros

A comparação dos títulos dos **194 registros** com os `h3` dos respectivos artigos encontrou exatamente estas duas divergências:

| ID | Inventário | Artigo publicado |
|---|---|---|
| `fun01-e1-mistura` | Problema 2 — A mesma temperatura não determina o lote | Problema 2 — Quatro lotes e uma hipótese bifásica |
| `fun01-e1-supercritico` | Problema 3 — Quando a leitura garante condição supercrítica? | Problema 3 — O rótulo “supercrítico” é sustentado pelos dados? |

Os textos antigos também aparecem nas linhas 277–278 do resumo legível, em `novos-registros-r1.json` e nas cópias congeladas da r1. Os outros 192 títulos conferem. IDs, links e hashes dos artigos permanecem corretos; a divergência não conduz a outro problema, mas deixa a descrição documental desatualizada.

O schema define `titulo` como texto não vazio; nem ele nem o guia exigem igualdade literal ao `h3`, e o validador não faz essa comparação. Portanto, o achado é de consistência documental, não uma falha automática de schema. Recomenda-se alinhar os dois títulos no JSON e no resumo vigente e apresentar a revisão correspondente, preservando a evidência histórica r1. Não é necessário modificar o contrato para corrigir os textos.

## Verificações executadas

O código de `verificar-fun01-r1.mjs` e de `fun01-calculos-v1.mjs` foi lido antes da execução. O primeiro apenas lê os arquivos; o segundo recebe dados e calcula em memória. A importação e a chamada `verificarFun01()` concluíram normalmente no Node REPL.

- **239 verificações documentais** passaram, incluindo restauração integral do HTML anterior ao retirar a unidade/menu e reverter somente as seis linhas declaradas da matriz.
- O validador canônico foi chamado diretamente e retornou **194 registros e 194 artigos**, oito recursos, 1.042 referências locais, zero erros e zero avisos.
- As **28 verificações numéricas** executaram efetivamente; são asserções que lançariam erro quando sua condição não fosse satisfeita. O resultado calculado coincide integralmente com `calculo-r1.json`. Isso demonstra reprodutibilidade do código fornecido; a avaliação científica independente pertence ao Auditor principal.
- Os resultados documental e de inventário reexecutados também são integralmente idênticos aos JSON entregues.

Para reproduzir a execução documental:

```js
var modulo = await import('file:///C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/evidencias/FUN-01/verificar-fun01-r1.mjs');
nodeRepl.write(await modulo.verificarFun01());
```

## Preservação e novos registros

Uma extração própria dos artigos, separada do parser do validador, confirmou que os **190 artigos anteriores são byte a byte idênticos**. A comparação dos objetos confirmou os **190 registros anteriores idênticos e na mesma ordem**. O snapshot anterior de inventário coincide integralmente com o pacote BAN-02 r3; o HTML anterior mantém o hash aprovado `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e`.

`registro.js`, `curso.js`, `curso.css`, schema, validador e guia mantêm os hashes da evidência independente BAN-02. As cinco entradas do manifesto FUN-01 conferem em hash e tamanho, e suas cópias congeladas são idênticas aos arquivos vigentes. As 12 cópias de pacotes BAN-02 enumeradas nos manifestos r1/r2/r3 também mantêm os hashes registrados.

Os quatro novos artigos usam IDs próprios, `data-inventario="e1"`, banco `aberto`, formato `resposta_aberta` e zero alternativas. Os quatro registros têm todos os campos do contrato, hash de artigo e do pacote de dados corretos, contagem de etapas coerente e relações de exposição apontando para âncoras existentes. Os vínculos C01–C10 declaram avaliação parcial e a revisão de gabarito permanece `pendente`. O arquivo `novos-registros-r1.json` coincide com os quatro objetos acrescentados ao inventário. Além dos dois títulos, não foi identificada divergência estrutural nesses registros.

## Identificação da versão

| Arquivo | SHA-256 |
|---|---|
| HTML publicado | `cacda8c7742eead77aa1e92021b01c085c1b7340201d5cca0ada8ff743a8b04f` |
| Pacote de dados | `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448` |
| Código de cálculo | `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88` |
| Inventário canônico | `4b18b397b68b9a46aae4db4c526d7bc2e4712df0e65b33359ba414fc6112e4df` |
| Resumo legível | `5242d53447dc9441109586d448793c324596745e2017546a19cb39ff5b854725` |

Resultados por artigo, registro e arquivo, saídas reexecutadas e os dois títulos divergentes estão em [FUN-01-r1-tecnico-evidencias.json](FUN-01-r1-tecnico-evidencias.json).

Esta subauditoria não repete bibliografia, não julga níveis cognitivos ou suficiência científica das rubricas e não executa navegador. Não repete os 56 testes de infraestrutura BAN-02, pois seu código e contrato permanecem idênticos. Nenhum produto, controle ou arquivo do Corretor foi modificado.
