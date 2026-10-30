# QA-09 — aplicação de precisão em refrigeração r29 → r30

**Estado: aguardando auditoria independente.** A candidata `candidata-refrigeracao-precisao-r30-next-examples`, manifesto SHA-256 `586ef6cee0ddab40bfc8ab180af39a2f14a1f4d5af0b7a539f38cc062a1bb0c2`, foi aprovada pelo parecer `auditoria-candidata-precisao-r30-next-theory/parecer.md`, SHA `4d7c7c6aac549c70e39ec646a2391929bec1099a3ad908a97296ae9c68675d6e`. As três substituições, restritas à base de refrigeração e às versões visível e de busca da ficha 84, distinguem igualdade exata para saldo nulo e igualdade aproximada para saldo desprezível. Dados e equações permanecem iguais. A candidata opcional EX028 não foi aplicada.

## Sequência e ensaio

Criou-se a cópia mínima `/tmp/curso-r30-ensaio-pre-aplicacao` da fotografia r29. O executor, com modos e diretórios reais distintos fixados por guarda, foi executado **primeiro** na cópia com `--fixture`, terminando com código zero. Seu registro `ensaio.json` foi copiado para o pacote antes de se executar `--apply` no diretório real; o executor exige o ensaio, os hashes de base, a candidata, o parecer, destinos ainda inexistentes, preservação dos artigos, fichas, MathML e atributos selecionados. Depois da aplicação, sete saídas (páginas, inventários oficiais, fotografia QA, mapa e edições) foram comparadas byte a byte à cópia; todas idênticas. Os resultados JSON têm igual conteúdo exceto o campo de modo. A cópia é temporária; a evidência pequena permanece no pacote. O executor escreve vários arquivos e não é transacional.

Na r29 anterior houve execução real antes do ensaio por engano de diretório. O incidente e o ensaio retrospectivo estão descritos em `aplicacao-refrigeracao-r29/entrega-r29.md`, SHA `7655fcafc54b9bde876402699ff1ef54ec2801458fd15eb019b65c31b1f9b73a`. A auditoria daquela aplicação está em `auditoria-aplicacao-r29-next-theory-20261030/parecer.md`, SHA `8812b87f269417c335d5082a936251a239a9411fd2beb468bf1d6b109e80da4b`. Esta r30 foi ensaiada antes da aplicação.

## Identidades SHA-256

| Arquivo | SHA-256 |
|---|---|
| aula r29 | `f932d341a543f05b9f7b31b037cb28f21f8d4e9933536656475f99fd3d3ba7d5` |
| formulário r29 | `b839310edfa655e1da907757119beaeacdabd7d088211ac189c38c3dbeb38932` |
| aula r30 | `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4` |
| formulário r30 | `949c44fc5b96703929770b2881383d449af890616d34b9ab10b998ca96c75749` |
| inventário oficial JSON | `205c74f161b5ba4de3a4f7f6c9ab694e0238d28d68df125a232846c5dffa8228` |
| inventário oficial Markdown | `f0015ed3535b9ad8997b8c92e4322cad98a599dd972186c1a6cb8b65614e9e40` |
| `inventario-r30.json` | `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4` |
| `mapa-correspondencia-inventario-r29-r30-r1.json` | `7aca7066c5b3da141549566be2b6539643ebadcd44acc2473bccdcce4a986d17` |
| `ensaio.json` | `7a56802e18dc990cc934985c8f70266190bad5d2e28ba2870139375481cd71ce` |
| `resultado/verificacoes.json` | `a7ac61faa97d591f55a3b61e567e4f38d29e6484972e1ba4ebc93bd03750c4e2` |
| `resultado/edicoes-aplicadas.json` | `caadf0f18b598626f601625edc719bb05c0309faddbd5a4ff1b7930ae642975b` |
| `aplicar.mjs` | `ce4215c1c4e7110fd56ebc90e426357a21f5cfc632ac108207fe311805b37eeb` |
| `mapear.py` | `8b027a5adec65d5cc780e23741a61dd8bdb9f0463341720b0b3ab1c60b7c39bd` |
| `montar-fixture.py` | `a1a0e60100918dafafbac6db33035d74a9f2f66635c5b928f7836a8cc9f5bc87` |
| `verificar.mjs` | `3b01b11222067992f28872cd754e612eeb11e7abdc0899fd1efd2087fe5707cd` |
| `inventariar-r30.mjs` | `0718adaa5067db57d0c9be8addba18d3aec0dbf2fd49ef85507b49b191aa038a` |

## Verificações e limites

O executor preservou 197 artigos e registros, 99 fichas não alvo, 734/191 elementos MathML e atributos de identidade, links e ARIA selecionados; conserva snapshots r29 e r30 em `resultado/`. O mapa contém 11.409 pares, 11.403 externos e seis contextos ancestrais para conferência, 816 referências e 138 recursos; nenhuma referência nova ou modificada. A classificação estrutural não transfere automaticamente aceite científico. O validador oficial retornou `ok`, 197 itens/artigos, 29 recursos e 1.263 links locais, sem erros nem avisos.

Para repetir a verificação somente leitura da versão efetiva, na raiz execute `node auditoria/termodinamica/evidencias/QA-09/aplicacao-precisao-r30/verificar.mjs`. Ela reconstrói as páginas a partir dos snapshots e manifesto, verifica preservação, hashes da fotografia e mapa e chama o validador oficial. Auditoria científica independente da aplicação e QA-09 integral permanecem pendentes; não se certifica aprendizagem ou nível global do curso.
