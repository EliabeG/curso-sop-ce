# Inventário de avaliações de Termodinâmica — BAN-02

Este diretório registra individualmente as avaliações do E1. O inventário não aprova gabaritos, não certifica aprendizagem e não declara o curso avançado. O Auditor emite o aceite do BAN-02 separadamente, depois de examinar a classificação e a evidência.

## Arquivos e execução

- `inventario-questoes.json`: registros preenchidos pelo Corretor.
- `inventario.schema.json`: contrato JSON Schema 2020-12, versão 1.1, com campos obrigatórios, evidências condicionais e rejeição de campos desconhecidos.
- `validar-inventario.mjs`: verificador Node sem dependências npm. Exporta `validateInventory`, `validateSchema`, `parseHtml`, `isInventoryArticle`, `resourceReferences` e `sha256` para reprodução.

Na raiz do projeto, com Node disponível:

```sh
node auditoria/termodinamica/inventario/validar-inventario.mjs
```

Aceita também caminho do inventário e raiz do projeto como argumentos, nessa ordem. No ambiente Node REPL, que independe de Node no PATH:

```js
var modulo = await import('file:///C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/inventario/validar-inventario.mjs');
var resultado = await modulo.validateInventory({rootDir: 'C:/Users/User/Downloads/SOP-CE'});
nodeRepl.write(resultado);
```

`ok: true` significa somente que as verificações automatizadas descritas abaixo passaram. A saída distingue erros, avisos, quantidades e o limite da verificação. O CLI retorna código 1 quando existe erro.

## Cadastro ou atualização de cada item

1. Publique o item completo com ID estável no HTML do E1. Leia enunciado, alternativas, resolução, notas, figura e dados vinculados antes de classificar. Para novos IDs `q-e1-100`, `cr-e1-100` e `av-e1-100`, a descoberta é automática e não limita a quantidade de dígitos.
2. Para resposta aberta ou projeto, use um `article` próprio identificado por `data-inventario="e1"`, `data-banco="aberto"` ou `"projeto"` e `data-formato="resposta_aberta"` ou `"projeto"`. Esses itens têm `numero_alternativas: 0`; múltipla escolha admite duas ou mais alternativas, sem impor cinco. Use o mesmo `id` no artigo, no registro e em `localizacao.fragmento`, sem `#` nesse último campo.
3. Preencha **todos** os campos do esquema. Campos vazios exigidos não são aceitos. `hipoteses.explicitadas`, `hipoteses.implicitas` e `hipoteses.limites` podem conter listas vazias quando cabível: não invente hipóteses para preencher uma cota. Pré-requisitos devem representar conhecimento necessário; se não há conteúdo anterior específico, descreva a base mínima de leitura ou cálculo efetivamente exigida.
4. Registre origem e atribuição honestamente. `identificadores` e `fontes` podem estar vazios quando não existe fonte externa; explique a autoria em `atribuicao`. URLs oficiais não equivalem a conferência oficial. No cadastro atual do BAN-02, questões reais usam `conferencia_oficial: nao_realizada`, autorais usam `nao_aplicavel` e todos os gabaritos usam `nao_auditado_em_BAN02`. Estados posteriores só podem ser registrados depois do trabalho correspondente, com a evidência descrita abaixo.
5. Relacione os códigos C01–C10 e delimite `vinculo_competencias.alcance`. `apoio_fundamental` indica um fundamento necessário; `avaliacao_parcial` mede parte explícita da competência; `avaliacao_integral` só cabe com evidência efetiva da competência completa. A associação temática a C01–C10 não comprova a competência avançada.
6. Classifique o nível pela tarefa realmente exigida e explique a decisão com dados do item. `a_classificar` é aceito pelo esquema apenas como rascunho e bloqueia a validação final. `validacao_empirica: nao_realizada` impede tratar a estimativa como dificuldade medida. Esta classificação não atende sozinha ao BAN-05.
7. Enumere as etapas intelectuais. **Uma etapa é uma decisão, inferência ou transformação de modelo identificável**, e não cada adição, multiplicação ou substituição mecânica. `numero_etapas` deve ser igual ao comprimento da lista; cada etapa deve dizer o que o aluno precisa decidir ou inferir. `formato` descreve apresentação e resposta; `raciocinio.categoria` descreve demanda cognitiva.
8. Registre hipóteses presentes, hipóteses necessárias mas implícitas e limites conhecidos. Uma figura pode ser informativa, redundante ou ilustrativa: explicite o papel observado, sem deduzi-lo do título “com figura”. O hash de todo recurso carregado é obrigatório, independentemente do papel didático.
9. Registre exposição prévia identificada, sua evidência e o limite da busca. `desconhecida` exige lista de relações vazia e não significa “inédita”. `relacao_identificada` exige ao menos uma relação. Use um ID ou `#ancora` do mesmo documento, ou `caminho/desde/raiz.html#ancora`. Relação temática não equivale a repetição de dados nem à reutilização de exemplo. O verificador confere o destino; a pertinência da relação exige leitura.
10. Atualize os hashes somente **depois de reler os conteúdos modificados** e revisar os metadados. Preserve uma cópia integral da fonte em `fonte.snapshot`, distinta do arquivo publicado. Execute o validador e entregue a evidência ao Auditor.

## Estados de revisão e migração do contrato

A versão 1.1 substitui os dois estados fixos da versão 1.0 por enumerações reutilizáveis. A migração exige mudar `schema_version` de `1.0` para `1.1`, revisar a aplicabilidade da conferência oficial item a item e preservar o estado real das verificações. O verificador rejeita a versão antiga em vez de converter dados silenciosamente. Não há mudança automática de um estado pendente para um estado verificado.

| Campo | Valores aceitos | Evidência obrigatória |
|---|---|---|
| `origem.conferencia_oficial` | `nao_realizada`, `nao_aplicavel`, `realizada` | `origem.evidencia_conferencia` quando `realizada` |
| `revisao.gabarito` | `nao_auditado_em_BAN02`, `pendente`, `verificado`, `ajustes_obrigatorios` | `revisao.evidencia_gabarito` quando `verificado` ou `ajustes_obrigatorios` |

`nao_aplicavel` significa que o item não depende de uma conferência com prova/gabarito oficial; não significa que sua solução esteja correta. `pendente` permite registrar a futura revisão do gabarito, enquanto `nao_auditado_em_BAN02` preserva a delimitação da entrega presente. A atribuição dos estados `realizada`, `verificado` e `ajustes_obrigatorios` deve resultar da revisão correspondente, e não da simples presença de um arquivo.

Cada evidência é uma string não vazia com caminho de documento existente relativo à raiz, opcionalmente com `#âncora`, por exemplo `auditoria/termodinamica/pareceres/REVISAO-r1.md#verificações`. URLs remotas, fragmento sem caminho, arquivo inexistente e âncora ausente não servem como evidência local. Âncoras HTML usam o `id` real; Markdown admite títulos ATX (`#` a `######`, com slug em minúsculas, espaços convertidos em hífens e pontuação removida) ou um `id` HTML explícito. Para outros formatos de título Markdown, use o caminho do documento ou uma âncora HTML explícita. A evidência opcional, quando fornecida em qualquer outro estado, também é validada.

Os requisitos condicionais constam tanto do JSON Schema (`allOf`/`if`/`then`) quanto da execução do validador. A existência do documento torna a referência rastreável; seu conteúdo, suficiência e decisão de aceite continuam sujeitos ao Auditor. Esta alteração de contrato não declara FON-01, BAN-08 ou qualquer outro item executado.

## Caminhos, hashes e recursos

Todos os caminhos de `fonte`, `localizacao` e `recursos` são relativos à raiz do projeto, usam `/`, não contêm `..` e permanecem dentro da raiz. Uma fonte local em `origem.fontes[].url` também é relativa à raiz; `href` do HTML segue as regras relativas ao próprio HTML. URLs externas são conferidas apenas sintaticamente: o verificador não consulta a rede nem afirma que o destino oficial foi examinado.

`fonte.sha256` é o SHA-256 dos bytes completos do HTML atual; a cópia indicada em `snapshot` deve ter o mesmo hash. `sha256_artigo` é o SHA-256 dos bytes UTF-8 do trecho exato desde `<article...>` até `</article>`, incluindo abertura, fechamento, espaços e quebras de linha, sem normalização. SVG embutido está coberto por esse hash.

`localizacao.recursos` relaciona `{arquivo, sha256}` de imagens e demais arquivos necessários. O verificador exige os recursos locais carregados por `src`, `srcset`, `poster`, `object[data]`, SVG `image/use[href]` ou `xlink:href`, e CSS `url(...)` no atributo `style`. Um arquivo de dados necessário acessado por link deve ter `data-recurso="obrigatorio"` ou `download` no link e entrar na lista. Recursos embutidos `data:` já pertencem ao hash do artigo. Recursos remotos carregados bloqueiam a verificação: preserve uma versão local e rastreável antes do cadastro. `srcset` contendo data URI exige normalização explícita e também bloqueia, evitando uma leitura ambígua.

Dependências transitivas de um recurso (por exemplo, imagem interna de um SVG externo) devem ser incluídas em `recursos` e explicadas em `hipoteses.limites` ou no método; o verificador compara todos os hashes declarados, mas não descobre dependências transitivas automaticamente. Arquivos adicionais legítimos são permitidos para esse fim. CSS global e scripts externos ao artigo não estão automaticamente nesse conjunto: mudanças que alterem informação, apresentação necessária ou raciocínio exigem revisão do registro e declaração da dependência correspondente. Não basta recalcular hashes para declarar os metadados corretos.

## Cobertura e limites do verificador

O verificador examina o módulo principal e todos os arquivos HTML citados pelos registros. Descobre artigos `q/cr/av-e1-N`, as classes atuais `questao`, `concurso-item`, `avalia-item` e a marca `data-inventario="e1"`; exige exatamente um registro para cada artigo e localização única para cada registro. Projetos novos em outro HTML devem ser cadastrados no inventário na mesma entrega; o verificador não varre todos os HTML do repositório para procurar material E1 fora dos documentos cadastrados. Não há contagem fixa de 190.

Confere estrutura, campos desconhecidos, enumerações, textos obrigatórios, IDs únicos, competências válidas, etapas, alternativas, banco, formato marcado, exposição, arquivos, âncoras, vínculos locais, hashes da fonte, snapshot, artigos e recursos. Identifica itens novos sem registro, registros sem artigo e alterações locais que invalidam a evidência. Os links externos são apenas validados como URLs.

Não comprova correção de solução ou gabarito, completude científica de hipóteses, origem oficial, qualidade de distratores, suficiência da rubrica, nível cognitivo, número pedagógico de etapas ou novidade da avaliação. Esses pontos devem ser examinados pelo Corretor e pelo Auditor. Todo item em aberto deve permanecer explícito nos encaminhamentos e na entrega; execução técnica bem-sucedida não libera a próxima correção.
