# BAN-02 r1 — verificação técnica independente

Data: 27/10/2026. Autor: apoio do Auditor `/root/auditor_aaa/auditoria_tecnica_ban02`.

**Resultado técnico: não foi identificado bloqueio na estrutura, cobertura atual, rastreabilidade local ou manutenção exercitada. Este documento não aprova BAN-02, não classifica o mérito pedagógico e não libera outro ID.** A leitura semântica dos 190 itens e o parecer geral pertencem ao Auditor responsável.

## Escopo e método

Foram lidos a entrega r1, o guia, o contrato, o validador e o script consolidado antes da execução. A verificação utilizou o HTML e o inventário congelados, sem alterar produto, inventário, controle ou evidências do Corretor. As mutações dos testes ocorreram em diretórios temporários próprios. Os arquivos permanentes escritos por este apoio estão exclusivamente nesta pasta, com prefixo `BAN-02-r1-tecnico`.

O Node REPL importou o módulo real do validador. Um script independente, com extração própria dos artigos do HTML atual e comparação dos metadados, executou também 56 cenários controlados. Sua reprodução em REPL é:

```js
var tecnico = await import('file:///C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/pareceres/BAN-02-r1-tecnico-verificacao.mjs');
nodeRepl.write(tecnico.report);
```

O script exporta os resultados e cria somente fixtures temporárias; não grava resultado sobre arquivos canônicos. A evidência desta execução está em [BAN-02-r1-tecnico-evidencias.json](BAN-02-r1-tecnico-evidencias.json).

## Resultados verificáveis

- O validador real retornou `ok: true`, 190 registros, 190 artigos, sete recursos, 1.022 referências locais, zero erros e zero avisos.
- A comparação independente percorreu os 190 artigos e encontrou 190 IDs únicos, 30 Q, 80 CR e 80 AV. ID, fragmento, arquivo, banco, título e hash de cada artigo conferem.
- Número e formato das opções conferem individualmente: 117 itens de múltipla escolha e 73 itens C/E. A conferência de formato usou os valores reais das respostas no HTML, separadamente da inferência automática do validador.
- Nos 80 CR, atribuição e identificadores coincidem com `cr-meta`; rótulos e destinos das fontes coincidem com `cr-fontes`. Nos 80 AV, atribuição, ligação à questão de origem, identificadores e declaração autoral coincidem com o HTML. Nos 30 Q, o registro limita a atribuição ao banco autoral descrito na página, sem inventar autor nominal ou fonte externa.
- As URLs foram comparadas literalmente após decodificação HTML e normalização dos caminhos locais relativos. Não houve consulta aos PDFs nem confirmação de autenticidade oficial. O estado `nao_realizada` dos CR permanece adequado ao escopo desta entrega.
- Os cinco arquivos publicados do inventário são byte a byte idênticos às cópias em `evidencias/BAN-02/pacote-r1/`.

## Testes independentes

**56 de 56 cenários produziram o resultado esperado.** A evidência contém todos os resultados e mensagens de erro, inclusive para casos em que mais de uma inconsistência foi detectada.

Os positivos exercitaram Q100, CR100 e AV100, três alternativas, item aberto, projeto, cadastro incremental de Q101 e estados `realizada`, `verificado`, `ajustes_obrigatorios` e `pendente` com evidência apropriada quando exigida.

Os negativos exercitaram omissão, registro órfão, duplicação no registro e na fonte, fonte física alterada, artigo alterado mesmo com hash global e snapshot renovados, recurso físico alterado sem mudança no HTML, snapshot alterado, recurso omitido/duplicado, novos Q101/projeto sem registro mesmo com hash global renovado, banco/formato/alternativas divergentes, campo vazio/desconhecido, etapas inconsistentes, classificação pendente, exposição incoerente ou com destino ausente, fonte local inexistente, versão antiga, caminho fora da raiz e estados condicionais sem evidência válida.

Também foram testados oito modos de carregar ou marcar recursos: `srcset`, `poster`, `object[data]`, SVG `image[href]`, SVG `use[xlink:href]`, CSS `style` com `url(...)`, link `download` e link `data-recurso="obrigatorio"`. Para cada modo, o recurso omitido foi rejeitado e o recurso declarado com hash foi aceito. Imagem remota foi rejeitada. O `src` comum foi exercitado em todas as fixtures.

## Reprodução do script entregue

O script consolidado do Corretor foi importado sem alterações. **Os 39 cenários concluíram e o resultado impresso informou 39 sucessos. A importação não terminou limpa:** depois da impressão, seu epílogo `process.exitCode = ...` lançou `process is not defined`, pois esse runtime Node REPL não expõe `process`.

Isso não invalida os resultados já concluídos nem constitui bloqueio do contrato: a reprodução documentada para o script consolidado usa Node CLI convencional; o trecho de importação em REPL do guia refere-se ao módulo `validar-inventario.mjs`, que executou normalmente. Não foi executado Node CLI neste ambiente e não se afirma sucesso dessa via. Se for desejada importação direta do script consolidado também nesse REPL, um guard de disponibilidade de `process` no epílogo seria uma melhoria opcional.

## Hashes auditados

| Arquivo | SHA-256 |
|---|---|
| `inventario-questoes.json` | `740792085cfede3b91131187ebf40ce614b943e296991e05af5d601498ca287f` |
| `inventario.schema.json` | `c71033464d54e71e61d4dcbae56847a88720e5ff937c1e1f7179005ab22d149b` |
| `validar-inventario.mjs` | `ddc8a6831422a868fb5a8b15b2f6653325f6644acf4f5c64dbf35bb0d2369fdd` |
| `LEIA-ME.md` | `cdcd7e965bdc4a998b6e2fa784a53f84f295abcf9ade2d06ce62fff71d072449` |
| `INVENTARIO_QUESTOES.md` | `508d0d2f17d8220d9b69eee8bd60e71c6999bb56ffdd7ff9547dc26174a94c2d` |
| `testar-validador-r1.mjs` entregue | `e7892ba92777fecd4c3b5055ecf351a91452f8f13333c75cdaace6bf245ee527` |
| `modulos/e1-termodinamica.html` | `b4e2d672c6feecb4289ad73bb9c16000ff5156720698f10153ff93fa0b788a8e` |
| `assets/registro.js` | `444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2` |
| `assets/curso.js` | `81728c9fd1e96b738410e6b51cf4ab3ed785fb17753e68a988c1dcf236d8f899` |
| `assets/curso.css` | `b8ded6abc4548f378daab2e299a8a55ba81e8841c41049133a84d93848ee3eaa` |
| Script independente deste apoio | `1dd4452cc8d80bb9f80118c5bdf3c00a61c03ed573533f82e5ec2103aee503aa` |

## Limites para a decisão geral

Esta verificação não comprova solução, gabarito, nível cognitivo, etapas intelectuais, suficiência científica de hipóteses, novidade, independência dos bancos ou aprendizagem. Existência de evidência local não demonstra a suficiência do seu conteúdo.

O guia declara adequadamente que a descoberta se restringe ao módulo principal e aos documentos cadastrados; documentos E1 novos em outro HTML precisam ser cadastrados na mesma entrega. Dependências transitivas e informações trazidas por CSS/scripts externos ao artigo exigem declaração e revisão explícitas. Não foi executada auditoria adversarial genérica do tokenizador HTML nem de todos os recursos possíveis de JSON Schema. O contrato usa um subconjunto implementado e documentado. Não houve teste de navegador, porque o produto permaneceu inalterado.
