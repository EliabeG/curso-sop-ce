# QA-09 — auditoria estrutural do ensaio conjunto r15→r16

Data: 30/10/2026. Auditor automatizado `/root/next_graphics`; autor do ensaio `/root/next_formulas`. **APROVADO o mecanismo e seu resultado de ensaio no alcance estrutural descrito; não é aprovação da aplicação real.** Participei antes da identificação de ressalvas em ciclos e auditei as candidatas das fichas 89/90; o presente parecer não substitui o julgamento científico independente do lote de ciclos, feito por `/root/next_examples`, nem valida a versão efetiva futura.

## Reproduzibilidade e guardas

Identifiquei `ensaio.mjs` SHA-256 `2e91bce9d697189a629797e3371d1afef2a46dc03313c06a71404ba9e67b81ba`, `mapear.py` `4dc74c5694143a9737019c3cdbd21c18eff3e6ffb1bcd51b6b3523063384ab55`, gerador r16 `810d9f61f8c1d36959a4fbcfa997209ea08b50f663259c14f8ae8b4d37e75be2`, mapa fornecido `a3edb9fab577c58e5b3df4831ee8cfb09d8e8b39bf92d1efcd5e0a5f39b2d4d0` e resultado `936ae9c82ae52b6d5c9c63a1c3033cdb1b8cd7448648cafe299bd4e2f3290e67`. Li as guardas de base, pareceres, manifestos, originais, candidatas, offsets e deltas; os pareceres das duas candidaturas são referidos com SHA fixo. As duas fontes r15 estavam na versão esperada no início do ensaio.

Reproduzi o script integral em cópia separada sob `/tmp`, destruída após o teste; não apliquei produto. O mapa gerado ficou byte a byte igual ao mapa de ensaio fornecido e o JSON de resultado foi idêntico. Exercitei três casos de falha: diretório de trabalho fora de `/tmp`, arquivo de destino já existente e formulário com hash alterado; os três foram recusados, com o destino preexistente preservado. A revisão de código confirma as demais guardas declaradas, mas elas não foram individualmente submetidas a todas as alterações adversariais. A gravação do ensaio é sequencial e não transacional: o executor real requer suas próprias guardas e recuperação, não deve ser substituído por este script de teste.

## Reconciliação independente

O mapa possui 11.399 ocorrências antigas e 11.400 novas, com identidade única e correspondência exaustiva sem duplicação; em cada par conferi os hashes registrados contra ambos os inventários. Os 11.021 pares externos têm hash igual; três contextos ancestrais têm hash alterado e de fato contêm pelo menos uma edição. Não há remoção classificada. Nos 375 pares internos conferi arquivo, tipo, tag, seção, âncora, pertença à edição e os hashes, com distribuição:

| Edição | Pares internos | Hashes diferentes |
|---|---:|---:|
| `base-eficiencia-cop` | 164 | 0 |
| `base-limite-carnot` | 120 | 1 |
| `base-brayton-real` | 22 | 2 |
| `formula-politropico` | 44 | 4 |
| `formula-compressao-isotermica` | 25 | 4 |

Os 11 pares de hash diferente representam três textos de Carnot/Brayton e, em cada ficha, seu contêiner, atributos e dois textos de condição e símbolos; li-os contra as candidatas aprovadas. O único novo nó é texto direto de `base-eficiencia-cop`, r16 UTF-16 `300059`, hash `4762d1d2b897111e0af540704428a566f70a46a74d1edb6f98b71885a4525e89`: delimita W>0, apenas duas trocas de calor e o balanço `QH=QL+W`. Esse nó está dentro do bloco novo. São correspondências estruturais por sequência/contexto e não transferência automática de qualquer aceite individual.

Comparei independentemente conteúdo e hash dos **197 artigos excluídos** na aula antes/depois, e a lista do inventário; comparei os campos de todas as **816 referências** e **138 relações de recursos**, com hashes dos recursos que não são os dois documentos alterados. O mecanismo também verificou 98 fichas não alvo, 734/191 MathML, ordem de links e 197 registros oficiais; o validador canônico em cópia retornou sem erros/avisos. Essas comparações não provam integridade semântica dos recursos ou sua apresentação visual.

## Limites e comando

Da raiz, `python3 auditoria/termodinamica/evidencias/QA-09/auditoria-ensaio-conjunto-r16-20261030/verificar.py`, SHA-256 `73d07b04339f013222c82f8ecde399a0d285b1632ddb6a4b7b37a42e88131b57`, refaz os ensaios mencionados; passou. A cópia pode ocupar centenas de MB em `/tmp`. O verificador é independente da construção do mapa, mas utiliza o inventário gerado e o próprio mecanismo de ensaio; não certifica que os inventários capturaram todo o conteúdo ou que a fonte/figura foi validada. Não houve navegador, leitor de tela, estudantes ou revisão humana. A aplicação futura exige controle de versões, evidências históricas e exame da fotografia efetiva por Auditor distinto; QA-09 permanece aberto.
