# BAN-07 r1 — entrega congelada para auditoria

Data: 28/10/2026. Corretor: agente automatizado `/root/corretor_aaa`. Escopo exclusivo: enunciados e alternativas dos197itens de E1. A entrega não é aprovação independente e não libera outro ID.

O [diagnóstico integrado antes da edição](../evidencias/BAN-07/diagnostico-197-integrado-r1.json) registra197IDs únicos e731juízos individuais de opções:117múltipla escolha×5 e73C/E×2, além de sete problemas abertos com solução/rubrica e família de respostas admissíveis. Os três diagnósticos originais permanecem preservados e identificados por hash. O [plano](../evidencias/BAN-07/PLANO_DIAGNOSTICO-r1.md) foi confirmado pelo coordenador antes da edição.

Foram corrigidos25artigos autorais: Q02/09/13/15/16/18/19/24/26/28 e AV08/10/17/18/33/35/37/38/45/48/50/57/58/64/73. Quatro comandos explicitam condições antes da tentativa; os demais ajustes relacionam alternativas a erros concretos e sincronizam comentários. Nenhuma chave foi trocada. Os80CR, sete abertos e demais85artigos autorais permanecem idênticos, totalizando172artigos preservados. Os nove estudos críticos continuam fora da nota com documento, chave e análise técnica distinguidos.

O [diagnóstico após a correção](../evidencias/BAN-07/diagnostico-pos-correcao-197-r1.json) associa cada registro ao artigo examinado. A [releitura científica dos25](../evidencias/BAN-07/corretor/verificacao-cientifica-25-r1.json) registra125opções,16casos numéricos e nove conceituais. Os distratores novos têm operações ou confusões identificáveis; equivalências após arredondamento foram confrontadas. AV10B/E repetem800kg/m³ com classificações distintas, e somenteB fornece o par pedido. Q09 distingue trabalho produzido e consumido pelo sinal físico, apesar da mesma magnitude.

O [mapa dos197itens](../evidencias/BAN-07/mapa-identidades-r1.json) confirma20novasdigitais(oitoQ e12AV) e cinco mudanças somente de comentários(Q13/18,AV17/18/64). Nenhuma letra antiga foi migrada. Q E1 conserva respostas/erros/marcações de versões anteriores e conta somente digitais atuais; AV mantém seu mapa de histórico. Avisos aparecem quando pertinentes. JSON ilegível E1 não é sobrescrito: tentativas novas ficam na página com aviso. O comportamento dos demais módulos e o registro fora de E1 foram preservados.

## Verificações executadas e atribuição

- Corretor: [264verificações estruturais](../evidencias/BAN-07/corretor/verificacao-produto-r1.json), sem falhas;58substituições reproduzem integralmente oHTML;734elementosMathML preservados; apenas cinco arquivos e25registros de inventário alterados.
- Corretor: [15casos de persistência](../evidencias/BAN-07/corretor/testes-persistencia-r1.json), sem falhas, executando funções reais e a camada real de armazenamento em Node/VM com DOM/localStorage controlados. Não é teste de navegador.
- Validador canônico: [197registros,29recursos e1261links locais](../evidencias/BAN-07/corretor/validacao-inventario-r1.json), sem erro ou aviso. Isso verifica estrutura/rastreabilidade, não certifica ciência ou aprendizagem.
- Coordenador, apoio separado: [376verificações de preservação](../evidencias/BAN-07/conferencia-coordenador-r1.json), [59verificações de reconstrução](../evidencias/BAN-07/reconstrucao-coordenador-r1.json) e [15testes de funções Q](../evidencias/BAN-07/persistencia-q-coordenador-r1.json), sem falhas.
- Coordenador, navegador CUA: [nove verificações antes/depois](../evidencias/BAN-07/navegador-coordenador-r1.json). Q24/AV08 revisadas exigiram nova tentativa; Q23 preservou sua resposta; avisos apareceram; novas respostas persistiram após recarga. Há captura de Q24. Esse apoio não foi apresentado como execução do Auditor e o DOM não prova sozinho todos os bytes do histórico.

## Versão e arquivos

| Arquivo alterado | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `7d35b07b31c7faa13eb3f98a8c73c3a9bd1c2cf146534464dfdd202e0074e4a7` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `dba046a5781f6bb82fef14b52af8f3285063c815b130f580edc817e9bd589fb1` |
| `assets/curso.js` | `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` |
| `assets/registro.js` | `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c` |

O [delta completo dos cinco arquivos](../evidencias/BAN-07/corretor/delta-produto-r1.patch), o [manifesto](../evidencias/BAN-07/manifesto-r1.json) e nove cópias finais em `evidencias/BAN-07/pacote-r1` identificam a versão. O HTML anterior, as fontes e os pacotes aceitos usados por herança permanecem identificados por hash. Hash diferente não foi tratado como identidade integral.

Não houve piloto com estudantes, revisão humana, certificação externa, auditoria integral de acessibilidade ou fechamento de BAN-08/QA globais. A plausibilidade dos erros é teórica. Inventário usa `verificado` para a conferência do Corretor dos25registros atingidos, explicitamente sujeita ao parecer independente.

Entrega para o Auditor independente designado pelo coordenador. O próximo ID permanece bloqueado até parecer explícito `APROVADO` sobre esta versão e liberação pelo coordenador.
