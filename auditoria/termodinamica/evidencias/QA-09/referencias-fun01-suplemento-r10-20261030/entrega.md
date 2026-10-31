# QA-09 — complemento de acesso IAPWS e IUPAC, r10

Data: 30/10/2026. Autor: agente automatizado `/root/reference_triage`. **Aguardando auditoria independente.** Este complemento registra nova tentativa de acesso e preserva sem alteração a [triagem original r9](../referencias-fun01-r9-20261030/entrega.md), cujo SHA-256 é `78caa8c551d8aa0b75ea4b9d12715922026637e387dd122221aae2dd06164799`. Não encerra QA-09 nem demonstra disponibilidade futura para todos os usuários.

## Separação entre relato e observação

O agente independente `/root/next_theory` informou ter conseguido abrir diretamente o documento IAPWS, confirmando os dados críticos no §3 e a identificação de versão R7-97(2012). Repeti a consulta por conta própria em 30/10/2026, utilizando a ferramenta de pesquisa web e as URLs exatas da aula. O relato de outro agente é um indício separado; os resultados abaixo são **minhas próprias observações nessa segunda tentativa**.

| Referência | Resultado da nova consulta direta | Confronto limitado |
|---|---|---|
| [IAPWS, IF97-Rev.download](https://iapws.org/technical-guidance/release/IF97-Rev.download#page=5) | O download abriu como PDF de 49 páginas. A tentativa anterior, em outra consulta, havia expirado. A ferramenta recupera o documento sem demonstrar a navegação visual do fragmento `#page=5`. | A página impressa 5, quinta página do PDF, §3, informa `Tc=647,096 K` e `pc=22,064 MPa`, valores iguais aos dados da aula. A capa menciona revisão de 2007, mas a própria primeira página registra esclarecimento em 2012 e identifica `IAPWS R7-97(2012)`. Não se afirma incerteza experimental desses valores a partir desta checagem. |
| [IUPAC, C01032](https://goldbook.iupac.org/terms/view/C01032/html) | A URL exata retornou HTTP 403 no acesso direto da ferramenta, como na primeira tentativa. | Índice de busca identifica o título “chemical potential” e a relação da derivada de Gibbs. O acesso direto para este ambiente e a experiência de outros usuários seguem não verificados; 403 **não comprova link inexistente**. |
| [IUPAC, C01023](https://goldbook.iupac.org/terms/view/C01023) | A URL exata retornou HTTP 403 no acesso direto da ferramenta, como na primeira tentativa. | Índice de busca identifica “chemical equilibrium” e o DOI `10.1351/goldbook.C01023`. Acessibilidade direta e experiência em outros ambientes seguem não verificadas; 403 não é prova de link inválido. |

A tentativa das duas rotas `old.goldbook.iupac.org` retornou HTTP 502 pela mesma ferramenta. As rotas DOI não foram acessíveis por essa ferramenta. Isso não prova erro do material nem exige troca de URLs; nenhuma substituição é recomendada sem ensaio apropriado e parecer independente. O resultado do índice não foi confundido com leitura direta das páginas IUPAC.

## Identidade e alcance

No inventário r9 as três referências são os índices de base zero 128, 129 e 134; na aula e inventário r10, cada uma corresponde a um único registro com mesma seção, âncora, rótulo, URL, posição e hash do elemento de link. Não se transfere automaticamente o aceite ou validade de outras dependências com base em hash igual. A fotografia r10 examinada é `modulos/e1-termodinamica.html`, SHA-256 `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`, e `inventario-r10.json`, `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`.

| Índice | Início–fim UTF-16 r10 | SHA-256 elemento `<a>` |
|---:|---|---|
| 128 | 96144–96274 | `17c0d12383e3f0020bd27d1d7d89a808fb17e5aed2768e6f234cd0b6575facfa` |
| 129 | 96277–96396 | `d092fc46d9874ff535b58662e9a8dc1d0b45b3e535826e6402238c8db8a52161` |
| 134 | 106252–106399 | `1052b722eb00718d18ba9cfa64f759b9186c592dc80262aa8796e15e13ccef1c` |

O confronto pontual confirma os valores críticos na fonte acessada, mas não avalia a completude de IAPWS-IF97, a licença ou todos os cálculos de FUN-01. A observação de acesso é válida para esta ferramenta e momento, não para todos os navegadores. Os acessos IUPAC permanecem pendentes; a decisão sobre alternativas só pode ocorrer com evidência adicional. Não foi realizado teste em navegador real. Solicita-se auditoria independente do complemento; a triagem de todas as referências e QA-09 integral permanecem abertas.
