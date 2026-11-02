# QA-09 — ensaio conjunto r15→r16 de três blocos e duas fichas

30/10/2026. `/root/next_formulas`. **Somente ensaio em cópia; não aplicado ao produto.** Este mecanismo testa as três candidatas de teoria COP, Carnot e Brayton e as fichas 89/90, cujos pareceres isolados são favoráveis. Não substitui auditoria do ensaio, sinal da coordenação, executor de produto protegido, ou auditoria da eventual versão efetiva.

## Guardas e reprodução

Em uma cópia separada da árvore sob `/tmp`, partindo da raiz da cópia, executar `node auditoria/termodinamica/evidencias/QA-09/aplicacao-conjunta-r16-r1/ensaio.mjs`. O script recusa localização fora de `/tmp`, argumentos adicionais e destinos já existentes. Confere os hashes da aula e do formulário r15, inventário estrutural, inventário oficial e nota, manifestos das duas candidaturas, pareceres independentes de r15 e das candidatas, gerador e mapeador. Confere ainda originais, candidatas, offsets, ocorrências únicas e reconstrução de cada delta; grava snapshots e executa a alteração somente na cópia. Atualiza a fonte do inventário oficial e uma nota **provisória** na cópia, gera inventário/mapa e executa o validador canônico. O script não deve ser usado como executor real; uma aplicação exige guardar hash deste ensaio e do novo parecer que o revisar, entre outras guardas, e empregar registro histórico efetivo.

## Resultado reproduzido

Aula hipotética SHA `55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23`; formulário hipotético SHA `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`. Inventário hipotético `2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd`; [mapa de ensaio](mapa-ensaio.json) SHA `a3edb9fab577c58e5b3df4831ee8cfb09d8e8b39bf92d1efcd5e0a5f39b2d4d0`; [resultado](resultado-ensaio.json) SHA `936ae9c82ae52b6d5c9c63a1c3033cdb1b8cd7448648cafe299bd4e2f3290e67`.

Os 197 artigos da aula e os 197 registros oficiais, 98 fichas não alvo e os 734/191 blocos MathML da aula/formulário foram preservados. Links por tag/destino permanecem iguais. O mapa registra 11.021 pares externos idênticos, três contextos ancestrais alterados, 375 pares internos que exigem conferência e um nó adicionado ou reestruturado; as 816 referências e 138 relações de recursos mantêm valores. Tais classificações são estruturais, não transferem aceite automaticamente. Validador local passou: 197 artigos/itens, 1.263 links locais, 29 recursos, sem erros nem avisos. Não há teste visual, navegador, leitor de tela ou validação científica na aplicação.

## Integridade e limite

Hashes: `ensaio.mjs` `2e91bce9d697189a629797e3371d1afef2a46dc03313c06a71404ba9e67b81ba`; `mapear.py` `4dc74c5694143a9737019c3cdbd21c18eff3e6ffb1bcd51b6b3523063384ab55`; `inventariar-r16.mjs` `810d9f61f8c1d36959a4fbcfa997209ea08b50f663259c14f8ae8b4d37e75be2`. A operação de ensaio faz gravações sequenciais na cópia e não é transacional. Uma falha em execução real hipotética exigiria preservar snapshots e reconciliar, não prosseguir cegamente. QA-09 permanece aberto.
