# QA-09 — auditoria independente da aplicação conjunta dos diagnósticos 6 e 9

Data: 29/10/2026. Responsável: apoio auditor independente `/root/auditoria_av61_70`. Escopo: aplicação, inventários, mapa r3→r4 e revalidação localizada BAN-02, BAN-07 e BAN-08. Sem aprovação global QA-09 ou alteração de produto e controle.

## Decisão e mérito das alterações

A aplicação efetiva reproduz exatamente as duas candidatas individualmente aprovadas: cada original e cada candidata ocorre uma vez no respectivo HTML, os arquivos isolados correspondem aos fragmentos e a aplicação sucessiva das duas substituições ao HTML anterior reproduz byte a byte o documento atual. Nenhum outro trecho HTML mudou. Soluções, âncoras e links foram preservados.

No diagnóstico 6, a exclusividade das transferências pela fronteira elimina a possibilidade de trabalho adicional; sob as condições declaradas, ΔU = −30 − (−180) = 150 kJ e U₂ = 650 kJ. No diagnóstico 9, a máquina é cíclica e troca calor somente com as duas fontes especificadas; η máximo de Carnot é 2/3 e a rejeição mínima é 300 kJ, logo rejeitar 100 kJ não é possível. Equivalente: ΔS das fontes = −900/900 + 100/300 = −2/3 kJ/K por ciclo. Esses são cálculos para os valores nominais das candidatas revisadas, sem arredondamento.

## Preservação e testes

A comparação independente do HTML identifica 190 artigos Q/CR/AV na fonte principal idênticos e na mesma ordem. Os 197 registros do inventário oficial são idênticos aos do backup: apenas `fonte.sha256` e `fonte.snapshot` mudaram, para o HTML e a fotografia atuais. O validador oficial, executado sem gravar evidências, verificou os hashes dos 197 artigos nas fontes correspondentes, 29 recursos e 1.263 links locais: sucesso, sem erros ou avisos. A comparação do Markdown com o backup mostra apenas nova seção histórica da aplicação; o link de entrega existe. O validador não verifica genericamente todos os links do Markdown.

Os hashes de `assets/curso.js`, `assets/registro.js` e da ficha de fórmulas permanecem os da versão anterior. Os diagnósticos são blocos explicativos, não artigos pontuados. Com os artigos e código preservados, as entradas das digitais e os dados pontuados não mudaram por este delta. Reexecutei o teste de persistência de BAN-08, após inspeção: passou nos cenários de histórico, gravação, recarga, placar, refazer e falhas, com funções reais e DOM e armazenamento simulados. O teste concentra-se em AV42/45/52 e não equivale a navegador real nem comprova dados de usuários. `verificar-aplicacao-r1.mjs` escreve em evidência histórica e não foi reexecutado; seu resultado OK e `validacao-levantamento-r3.json` são atribuídos ao Corretor e não substituem este parecer.

## Inventário QA-09 e mapa

O levantamento r4 contém 11.396 ocorrências e conserva a mesma lista de 197 artigos excluídos do r3; fragmentos dos outros 26 diagnósticos coincidem. A validação de duas leituras sintáticas do Corretor informa `OK_ESTRUTURAL`; não demonstra a completude visual ou o mérito das ocorrências.

Confrontei todos os 11.396 pares do mapa com ambas as listas, na ordem, checando documento, tipo, tag, seção, âncora, IDs, posições e hashes. Não houve erro, IDs duplicados ou colisão de documento/tipo/tag/seção/âncora/início em qualquer versão. As regiões de substituição r3 vão de 521981 a 522051 e de 523453 a 523519, com acréscimos respectivos de 62 e 124 unidades UTF-16; os deslocamentos conferem. Dos pares, 11.391 têm hash igual, cinco diferem e 1.016 IDs mudaram. Os cinco são a seção ancestral de preparação, os blocos dos diagnósticos 6 e 9 e seus parágrafos; todos os cinco intervalos r4 são reproduzidos com as substituições autorizadas aplicadas aos intervalos r3. Uma cópia temporária do gerador, apenas com importação absoluta e saída redirecionada, executou com sucesso e reproduziu o mapa byte a byte sem regravar o original.

O mapa usa ordem e posições das fotografias, não IDs duráveis. A igualdade de hash pode referir-se a texto direto que exclui filhos e não garante preservação de contexto ou dependências; provas herdadas exigem conciliação de escopo, fontes e figuras. Hashes diferentes não recebem herança automática; os dois diagnósticos corrigidos foram reavaliados acima. O mapa não cobre as listas separadas de referências/recursos nem prova revisão ou completude do universo QA-09.

## Revalidação localizada dos aceites

BAN-02: os 197 registros individuais, seus artigos e recursos registrados permanecem íntegros; apenas a referência à fotografia integral e o resumo histórico foram atualizados. Não foi identificado efeito do delta nos atributos ou vínculos dos itens inventariados. O validador estrutural acima não substitui reclassificação pedagógica integral.

BAN-07 e BAN-08: os artigos, registros, recursos e scripts abrangidos foram preservados; a alteração aperfeiçoa hipóteses de dois exemplos fora dos artigos, sem mudar as questões ou contradizer seus cálculos. Não se identificou impacto dos dois deltas nos resultados anteriormente validados para os 197 itens. Esta é ponte localizada das evidências históricas às versões atuais, não nova revisão integral de todos os itens nem autorização para aprovar QA-09. As evidências antigas continuam associadas às versões que identificam.

## SHA-256

- HTML anterior `0de7342b99b9ebef8c1526f0b8eefb3544f000a4546d7b500558550d178285eb`; atual e fotografia `7541e7c4c8314922992e99e8b62b40342c2d938e6edeac67ef9f74b69f86c17c`.
- Inventário JSON anterior `6276476a66629d50406c08eb23fb185a5828a48c0a175d54bba8227679ecd396`, atual `6910b7b3ec783040859302bc21ebbd463a8faf447ddfce36bf745b5a261d0d55`; Markdown anterior `d9b944f1d02d9d21aa74e3d66389479be210f194ec61633e929199d565e7e493`, atual `e4b2a2db2aae0d574fc0fe2f44801a27edbd99a57cb75d2e2648da7c1e4a9be2`.
- Manifesto da aplicação `cea7c448fc24095f82d450b36143871bb1f1907eb21707f2d59a0c614688f5e1`; verificação do Corretor `4793e0f63692ba6dc84e0997f21b47785c0e8c70d110314044c72e225040c8c2`; parecer das candidatas `d53f9666384928ba27edb7f23f35c24e96c2b2e2a2e81f4fc80a63e8850a22bf`.
- Levantamento r3 `3074ab8fdf511d68dce73ec97bacca9dd9d5b0bbc3fe07a7d4ce329669b8b446`, r4 `44d19642bcf39109edf620e7304580b7a8a686e7c42cfa7101fa3d118a79d054`; validação estrutural do Corretor `fb38286b9540d4c28d796098177314a1b34f9c978fce237506866fd601941871`.
- Mapa `84c926657b89ee9ae65c89652442b96536dabe93e65e486d6de275dd4718ae0c`; gerador `dda9e3a6bff5566c0589faab3f262469bd7bddd4621f7a11a9e58dc15319acf9`.
- `assets/curso.js` `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13`; `assets/registro.js` `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c`; ficha `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`.
