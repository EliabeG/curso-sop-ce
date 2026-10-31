# QA-09 — preparo da aplicação combinada r10 (registro histórico pré-aplicação)

Data: 30/10/2026. Corretor automatizado `/root/next_theory`. Este documento descreve o planejamento anterior à aplicação: a aplicação dependia de liberação da coordenação e revisão independente. A operação efetiva posterior é registrada em `entrega-r1.md`; não reexecutar sobre a versão já aplicada. Base r9: aula SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; formulário `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; inventário `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`.

As quatro candidatas iniciais são dois parágrafos de teoria e as fichas 40/67; a lista opcional [extras-diagnostico02.json](extras-diagnostico02.json) identifica a candidata do diagnóstico 2, que só pode ser incluída após conferência da aprovação específica. A entrada opcional é uma lista de objetos com `id`, `documento`, `original`, `candidata`, `original_sha256` e `candidata_sha256`. Cada nova candidata deve ter sua própria revisão, preservar as condições do script e ser testada numa nova cópia. O mecanismo **rejeita modificações em qualquer dos 197 artigos**: correções em FUN-01 P3 ou outro artigo não podem ser acrescentadas a este lote sem novo procedimento e revalidação próprios.

## Ensaio realizado em cópias descartáveis

Teste 1: as quatro candidatas foram aplicadas em uma cópia isolada do commit local `395beb3`; o original não foi modificado. Aula resultante `ac0f4ce8a7b2c6c99590a1033d241991e1a6bea9ed7ec2d70393fdd4e87d53a6`; formulário `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; 197 artigos/registros, 98 fichas não alvo e 191 MathML preservados; 815 referências, 138 recursos, mapa com 11.397 pares, dos quais 82 internos exigem confronto independente; validador de inventário sem erros e 1.263 links.

Teste 2: a mesma operação em outra cópia, acrescida do diagnóstico 2 como lista opcional; aula resultante `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`, formulário com o mesmo hash do teste 1, 197 artigos e registros, 98 fichas não alvo e 191 MathML preservados; 815 referências, 138 recursos e 11.397 pares, dos quais 89 internos exigem confronto independente; validador sem erros. O mapeamento interno por sequência de tipo/tag/contexto é provisório, não transfere pareceres automaticamente. Nenhum resultado de ensaio afirma que a candidata opcional já tenha sido aprovada. Após qualquer mudança das candidatas ou da base, reexecutar em cópia e inspecionar novas diferenças.

## Preparação e aplicação — somente após liberação

Na raiz do repositório, o preparador verifica as fotografias, hashes e unicidade das candidatas e exige um nome de configuração inexistente. Com a candidata opcional aprovada, por exemplo:

```sh
python3 auditoria/termodinamica/evidencias/QA-09/aplicacao-pressao-fichas-r10-r1/preparar-config.py /tmp/config-r10.json auditoria/termodinamica/evidencias/QA-09/aplicacao-pressao-fichas-r10-r1/extras-diagnostico02.json
node auditoria/termodinamica/evidencias/QA-09/aplicacao-pressao-fichas-r10-r1/aplicar.mjs --apply /tmp/config-r10.json
```

Sem o último argumento do preparador, usa-se apenas as quatro candidatas. O executor exige `--apply`, recusa destinos r10 já existentes, verifica fontes, unicidade e sobreposição, reconstrói páginas, preserva os artigos, exige somente as duas fichas-alvo alteradas, 191 MathML iguais e um único link alterado na ficha 67. Salva fotografias, configurações, registros e inventário oficial anteriores e posteriores, gera `inventario-r10.json`, mapa e validador. `mapear.py` grava e explicita as diferenças de referências/recursos dentro dos blocos alterados; fora deles exige correspondência. `inventariar-r10.mjs` é cópia do gerador r9 com destino novo: não execute em cima de r10 existente.

**Limite operacional:** os arquivos do produto são gravados antes da geração do inventário e do mapa; se uma etapa posterior falhar ou for interrompida, a operação pode ficar parcial. Antes da execução real, garanta o estado da cópia e leia a saída; em caso de falha, não declare aplicação concluída, preserve as fotografias e reconcilie manualmente sem sobrescrever históricos. O executor e os testes são verificações estruturais; não substituem revisão independente, ensaio em navegador, teste de persistência, revalidação de FOR-01 ou avaliação de alunos.

SHA-256: `preparar-config.py` `d55ea2763f99b693fb4b27770caea6b84850fde316be5535ac0100f25bda9f07`; `aplicar.mjs` `012abd6ec0b49912d8fa13a0739fa61895fa5b032ee1409fda4715b0cf46fd41`; `mapear.py` `28dab18403d8303b13baeb79796556aae7582e99eb6ba260038c5560d988623f`; `extras-diagnostico02.json` `f6cf8e3979223cac895b2dc580e30899bb526019d67e1450c30a31f8f4fa2970`; `inventariar-r10.mjs` `2fdfd8a7dcb5f8850aa2649ef103307850615bbacce65474eb0f318e9409c460`.
