# Entrega BAN-01 — rodada 1

**Data:** 27/10/2026, America/Sao_Paulo.  
**Responsável:** agente automatizado Corretor AAA (/root/corretor_aaa).  
**Estado proposto:** entregue para auditoria independente; sem autoaprovação.  
**Escopo liberado:** somente BAN-01, 30 questões iniciais q-e1-01 a q-e1-30.

## Critério aplicado

> Reorganizar as alternativas das 30 questões iniciais e atualizar gabarito, comentário e referências à letra conjuntamente. Aceite: eliminar a sequência ABCDE repetida, manter resposta única correta e verificar cada item após a alteração; não criar outra sequência sistemática como substituta.

## Mudanças

- Permutações individuais das cinco alternativas em todas as 30 questões; rótulos A–E mantidos na ordem de apresentação.
- Atualizados data-gabarito e o gabarito visível de cada item. As 28 listas de comentários organizadas por alternativa acompanharam exatamente a mesma permutação e receberam novas letras. As listas por proposições de Q13/Q18 ficaram intactas.
- Não foram encontrados comentários que referissem uma letra de alternativa por texto literal além dos atributos e gabaritos atualizados. Letras A/B/C/D do diagrama da Q09 são estados físicos, e foram preservadas.
- Sincronizado exclusivamente modulos.e1.questoes em assets/registro.js, pois a digital usa o enunciado, a ordem das alternativas e o gabarito. Nenhum outro módulo ou metadado do registro foi alterado. O gerador ferramentas/registro.py não está na cópia publicada; a transformação e a conferência foram feitas por script local e guardadas como evidência.
- Enunciados, conteúdo das alternativas, soluções, dados, figuras, MathML e justificativas foram preservados. Não houve serialização geral do HTML.

Novo gabarito: **CBECCDEABEDCCEAADDAAECCCEBAECB**. Contagens: A=6, B=4, C=9, D=4, E=7. A permutação foi produzida por Fisher–Yates independente com crypto.randomInt, sem uma regra de rotação entre questões. Foram rejeitadas séries com períodos globais de 1 a 15, blocos completos de cinco repetidos, quatro letras iguais seguidas ou letra com menos de 3/mais de 9 ocorrências. A distribuição não precisa ser perfeitamente uniforme para cumprir BAN-01. Estas verificações afastam os padrões examinados; não constituem prova estatística de aleatoriedade ou validação psicométrica.

## Arquivos de produto e hashes SHA-256

| Arquivo | Antes | Entregue |
|---|---|---|
| modulos/e1-termodinamica.html | 10c3d92ef94136069dc94ee102fc0ff6e30b94cda82a66edf62de7d5346c015f | d375695006edf96cbb709b7e85e7ebb84e94474333505768a3cccec0e94119a4 |
| assets/registro.js | d55c275daf98a485574c40661155b02d25d1636d90ec2cb856d635df0b4f95fc | 234cb179c3a7c81043d9d66ee65116b2f07503999aac6a45c433dccd51545055 |

O HTML mantém 1.109.588 bytes. O verificador confirma identidade exata dos bytes fora dos 30 artigos, preservação do conteúdo de todas as 150 alternativas e associação correta entre 140 justificativas por letra e suas alternativas. Confirma também identidade exata das duas listas por proposições. No registro, todos os bytes fora do mapa de questões E1 permanecem iguais.

## Evidências e reprodução

Em ../evidencias/BAN-01/:

- e1-termodinamica.antes.html e registro.antes.js: cópias integrais anteriores à primeira alteração.
- mapeamento.json e mapeamento.md: cada alternativa antiga → nova, gabaritos e digitais por ID.
- conferencia-cientifica-r1.md: análise de todas as 30 respostas únicas, distratores e cálculos.
- verificar-ban01.mjs: verificador estático executado com sucesso; lê os arquivos reais entregues e os compara com os originais.
- verificacao-r1.json: resultado completo dessa execução, incluindo os 30 IDs e hashes.

Para reproduzir com Node.js: executar `node auditoria/termodinamica/evidencias/BAN-01/verificar-ban01.mjs` a partir do projeto. O script termina sem erro quando todas as asserções passam; também exporta `resultado` para inspeção. A execução desta entrega utilizou o runtime da ferramenta node_repl, pois Node não estava disponível no PATH do terminal.

Verificações concluídas: 30/30 respostas corretas preservadas; 150/150 alternativas preservadas e rotuladas; gabaritos visível/atributo concordantes; 30/30 digitais anteriores reproduzidas antes da mudança e 30/30 novas sincronizadas; 0 colisões entre digitais novas e anteriores; todas as partes externas ao escopo preservadas. A leitura científica item a item está no arquivo específico; a asserção estrutural, sozinha, não prova correção científica.

## Comportamento e limites

A regra existente de curso.js só restaura respostas cuja digital pertence à versão atual. As 30 digitais mudaram; tentativas anteriores não serão associadas à nova posição das alternativas. O histórico dessas tentativas não foi migrado nesta entrega. Isto deve ser considerado ao comparar o progresso antes/depois; o comportamento foi verificado por leitura do código e integridade das digitais, sem alegar ensaio de navegador.

Não foram executados pelo Corretor testes no navegador, uso com alunos ou validação psicométrica. O Auditor deverá examinar a versão e realizar as verificações independentes pertinentes. Esta entrega não avalia os bancos CR/AV, não conclui BAN-07/BAN-08/UX-11 e não certifica o curso como avançado. Nenhum próximo ID foi iniciado.
