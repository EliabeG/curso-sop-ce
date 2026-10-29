# Entrega BAN-01 — rodada 2

**Data:** 27/10/2026, America/Sao_Paulo.  
**Responsável:** agente automatizado Corretor AAA (/root/corretor_aaa).  
**Estado:** reapresentada ao Auditor; sem autoaprovação.  
**Parecer respondido:** ../pareceres/BAN-01-r1.md, AJUSTES_OBRIGATORIOS.  
**Único ID em trabalho:** BAN-01. Próximo ID permanece bloqueado até decisão independente e liberação do coordenador.

## Resposta aos ajustes obrigatórios

| Ajuste | Implementação concreta | Evidência |
|---|---|---|
| R1-A — Q10 | Incluído “em regime permanente” antes de “adiabaticamente” no enunciado. A hipótese de acumulação nula está disponível antes da tentativa e coincide com a solução existente. | Comparação literal de enunciado e cálculo de digital ab29d979. |
| R1-B — Q12 | Comando alterado para “Qual é a magnitude aproximada do trabalho específico de entrada (consumido), adotada como positiva?” | Comparação literal, magnitude 0,5 kJ/kg e digital 83f286e2. A opção negativa deixa de competir com a grandeza pedida. |

Estas são duas alterações semânticas autorizadas. Não se afirma identidade byte a byte desses dois enunciados com a versão original. Alternativas, gabaritos, comentários, fórmulas, figuras e as permutações da rodada 1 foram preservados. Nenhuma outra hipótese/enunciado foi reescrito. A análise anterior do Corretor aceitava condições reveladas pela solução; esta rodada resolve a insuficiência observada pelo Auditor trazendo-as ao comando.

## Deltas exatos

**Q10, antes:** Uma válvula de estrangulamento opera adiabaticamente, sem trabalho e com pequenas mudanças de velocidade e altura.

**Q10, depois:** Uma válvula de estrangulamento opera em regime permanente, adiabaticamente, sem trabalho e com pequenas mudanças de velocidade e altura.

**Q12, antes:** Qual trabalho específico aproximado?

**Q12, depois:** Qual é a magnitude aproximada do trabalho específico de entrada (consumido), adotada como positiva?

Digitais r1 → r2: Q10 `1877b147` → `ab29d979`; Q12 `0e39d656` → `83f286e2`. No registro foram substituídas somente essas duas chaves, preservando seus gabaritos E e C. O restante do arquivo é idêntico à rodada 1.

## Arquivos e hashes SHA-256

| Arquivo | Rodada 1 examinada | Rodada 2 entregue |
|---|---|---|
| modulos/e1-termodinamica.html | d375695006edf96cbb709b7e85e7ebb84e94474333505768a3cccec0e94119a4 | a69846fbe1dd1bb8ef3ce3a685ffc2a308d6595a8f95a8637da523e77e231d1d |
| assets/registro.js | 234cb179c3a7c81043d9d66ee65116b2f07503999aac6a45c433dccd51545055 | 444a13658e0b869760296826be30267215293b18c3074f283b2a1ea252e828a2 |

## Verificação e preservação de evidências

As evidências r1 não foram sobrescritas. Foram acrescentadas cópias integrais `e1-termodinamica.r1.html` e `registro.r1.js` antes do primeiro ajuste. Permanecem também as cópias originais anteriores à permutação.

Arquivos novos em ../evidencias/BAN-01/: `mapeamento-r2.json`, `mapeamento-r2.md`, `deltas-semanticos-r2.json`, `conferencia-cientifica-r2.md`, `verificar-ban01-r2.mjs` e `verificacao-r2.json`.

O verificador r2 foi executado com sucesso no runtime node_repl. Mantém a comparação exaustiva dos 30 itens com a base: 150 alternativas, 140 justificativas por letra, duas listas de proposições, gabaritos, 30 digitais e escopo externo. Para Q10 e Q12 ele exige **literalmente os enunciados completos antes e depois**, gravados no próprio script; para os outros 28 exige igualdade integral. Não foi removida a verificação de enunciados.

Além disso, compara integralmente os dois arquivos com as cópias r1 e aceita somente as duas substituições textuais declaradas e as duas novas digitais. Portanto, todos os demais bytes da rodada 1 permanecem preservados. Foram mantidas as 30 permutações já examinadas, a sequência `CBECCDEABEDCCEAADDAAECCCEBAECB`, as contagens e a ausência dos períodos examinados. Não há colisões de digitais.

Reprodução: `node auditoria/termodinamica/evidencias/BAN-01/verificar-ban01-r2.mjs`. Ausência de erro indica que todas as asserções passaram; o script exporta `resultado`, salvo nesta execução em `verificacao-r2.json`. O verificador r1 e seu resultado representam a versão anterior preservada; o verificador r2 examina a entrega atual.

## Limites que permanecem declarados

Esta reapresentação realizou verificação estática e conferência científica das duas condições. Não alega novos testes em navegador, alunos ou validação psicométrica. Os testes funcionais independentes da rodada 1 pertencem ao parecer do Auditor; ele decidirá quais repetir para r2.

A alteração de digitais invalida a associação de tentativas anteriores às questões modificadas pela regra existente do curso. Não houve migração de histórico. Essa limitação permanece explícita e UX-11 segue pendente. BAN-01 não conclui outros IDs nem certifica o curso como avançado.
