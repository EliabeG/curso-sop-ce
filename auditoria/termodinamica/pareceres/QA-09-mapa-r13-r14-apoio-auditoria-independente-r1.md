# QA-09 — apoio independente ao mapa r13→r14

Data: 30/10/2026. Auditor de apoio: agente automatizado `/root/next_graphics`, distinto do Corretor da aplicação. **APROVADO no alcance estrutural e documental abaixo.** Este agente revisou anteriormente a candidata isentrópica r2; o Auditor principal distinto deve julgar o conteúdo efetivamente aplicado e a revalidação dos aceites. Não encerra QA-09 nem libera outro ID.

## Fotografias e reconstrução

Aula r13 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`, r14 `572b172b29e1aa26873d191ebd827414c99f3122491c6d4c8129a69443f7389c`; formulário r13 `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`, r14 `3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce`. Inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`, r14 `6505b06f3f3ef15bc2904f8a604f6e1f0fa6cf22af822394b2c2a871437b6175`; mapa `a43156dad32d5529850bdd4c40209c68a772fee45cfd8651e3f9b0becaa1ff07`.

`evidencias/QA-09/auditoria-mapa-r13-r14-independente-r1/reconstruir.mjs`, SHA-256 `bef3b5329250adabcc53c9d75099de0abadce8f1da3c0ebeb02f1101774d9b41`, reconstitui as duas páginas em memória a partir das fotos r13 e seis deltas reais, conferindo hashes, unicidade e posições. O resultado e as fotografias posteriores coincidem byte a byte com as páginas efetivas r14. Os 197 artigos e registros individuais mantêm IDs, ordem e conteúdo; somente a chave `fonte` de topo do inventário oficial mudou. Das 100 fichas, 97 são idênticas; mudaram `formula-latente`, `formula-eficiencia` e `formula-cop-refrigerador`. Os 734 MathML da aula e 191 do formulário são idênticos como fragmentos.

O validador canônico retornou `ok=true`, 197 artigos/registros, 29 recursos e 1.263 links locais, sem erros nem avisos. Esses testes são estruturais, não demonstram renderização, aprendizagem ou mérito científico integral.

## Mapa, referências e recursos

`evidencias/QA-09/auditoria-mapa-r13-r14-independente-r1/mapa.py`, SHA-256 `d0572782e99b85cc8c4558b380b65b0bc52f1ee069e283c3a1462f6ca836914b`, confrontou sem gravação documentos, hashes, posições, contextos e ordem. O mapa registra 11.397 pares e dois registros adicionados (r14 tem 11.399 ocorrências): 11.178 pares externos iguais, cinco ancestrais com hash alterado e 214 internos (198 hashes iguais e 16 alterados). Os dois novos textos estão nos deltas `openstax` e `isentropica`. Os pares internos por sequência e contexto não transferem, por si, aceite científico.

As 815 referências r13 mantêm valores e textos; foi adicionada uma referência na seção FUN-02 para `https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node33.html`. O endereço foi aberto em 30/10/2026 e apresenta §4.2 sobre expansão livre e expansão isotérmica reversível; o acesso não substitui confronto científico da lição. Os 138 recursos mantêm caminhos e referências; 105 registros de hash da aula e três do formulário foram atualizados e os demais permanecem iguais. Os seis ativos específicos e os 197 registros de artigos excluídos do inventário estrutural permanecem iguais.

| Critério deste apoio | Resultado |
|---|---|
| Fotografias, seis deltas e inventário oficial | Passou: reconstrução byte a byte; 197 artigos/registros preservados. |
| Fichas e MathML | Passou: 97 fichas não alvo e 734+191 MathML idênticos. |
| Mapa, inclusive 214 pares internos e dois novos | Passou para identidade, ordem e contexto; significado segue sob Auditor principal. |
| 815 referências anteriores, uma nova, 138 recursos e seis ativos | Passou na extensão descrita. |
| Ciência dos textos e QA-09 integral | Não decididos por este apoio; dependem de parecer principal e trabalho restante. |

Qualquer revalidação de pareceres anteriores deve confrontar a versão, o conteúdo e suas dependências; hash idêntico ou correspondência estrutural não transfere aceite automaticamente. Não houve teste em navegador real, leitor de tela, estudante, revisão humana ou certificação externa nesta análise.
