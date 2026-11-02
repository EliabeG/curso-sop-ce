# QA-09 — parecer independente sobre procedência no FUN-01 P3

Data: 30/10/2026. Auditor: agente automatizado `/root/next_formulas`, distinto de `/root/next_graphics` que produziu a entrega. **Veredito localizado: AJUSTES OBRIGATÓRIOS para explicitar ou evitar a alegação de procedimento; o raciocínio de redundância é preservado.** Não aprova QA-09 integral nem libera o próximo ID.

## Escopo e versões

A análise abrange o achado de procedência da solução do artigo `fun01-e1-supercritico` e o contexto explícito do enunciado; também confrontei as contas apresentadas no lote para garantir que a decisão não dependa de confundí-las com a origem dos dados. A aula tem SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`.

- Artigo P3 `fun01-e1-supercritico`: UTF-16 125803–131220, SHA-256 `2fad0e042fb945eb44d0f2abe2c4e64322434195395fa4e5c084f17854f432a7`.
- Artigo da mistura: 119961–125802, SHA-256 `c6a2a5430bdee022dc9db6eb9d0e3c50c33086736b37154dd97d2749f53d4e53`; bloco externo `fun01-dados`: 111432–113604, SHA-256 `f2ad9153af7074ac31be0b322be23bf21a8450b3b98411b54961266c89ff94cc`.
- [Entrega do Corretor](../evidencias/QA-09/fun01-mistura-critico-recursos-r9-20261030/entrega.md), SHA-256 `566161d68c5d2bf22bece0b89711ee2b3090e22ed61dc11fc44ea0df8acdcdf5`; verificador `verificar.py` SHA-256 `9d08d89f3afa2c3d5e21c390312475a695745e2ec396cf9f5816477b88c69bb8`.
- JSON de dados `fun01-dados-v1.json` SHA-256 `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448`; código `fun01-calculos-v1.mjs` SHA-256 `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88`.

Recalculei os três hashes de fragmentos na posição efetiva, li o enunciado e a solução completos e executei o verificador após conferência de que não grava arquivos. Sua execução retornou `ok=true`. O artigo está entre os 197 itens segregados: este parecer não substitui nem anula de forma automática BAN-08 ou FUN-01.

## Interpretação do achado

O enunciado descreve duas colunas **ρ e v=1/ρ produzidas pelo mesmo sensor**, e pede discutir o uso delas em lugar de T e p. Essa notação afirma a relação funcional exata e pode razoavelmente ser lida como uma definição de coluna derivada por inversão. **A conclusão de que não são duas propriedades termodinâmicas independentes está correta**, inclusive sob essa leitura. A solução vai além ao dizer literalmente que “uma é calculada da outra”, expressão que pode ser lida como afirmação factual sobre o procedimento implementado internamente no sensor. O enunciado não descreve o procedimento de processamento, de aquisição nem uma trilha de calibração.

A igualdade exata de duas grandezas não prova, por si só, que uma estimativa instrumental foi computada a partir da outra: um dispositivo com mais de um princípio físico pode produzir estimativas independentes cujos valores nominais coincidam reciprocamente. Por exemplo, ρ=800 kg/m³ e v=0,00125 m³/kg são recíprocos mesmo sem documentação de qual sinal foi calculado de qual. Isso não altera a definição termodinâmica nem torna ρ e v independentes como coordenadas de estado; também não prova que o sensor específico do exercício funcione desse modo.

Há duas leituras defensáveis: (i) a notação do enunciado define expressamente v como inverso calculado de ρ, hipótese que pode ser tornada literal; (ii) ela apenas apresenta a identidade entre as grandezas, hipótese sob a qual a afirmação de procedimento deve ser substituída por “uma pode ser obtida da outra pela identidade”. **Para remover a ambiguidade sem pressupor procedência**, recomendo a segunda redação na solução, mantendo integralmente o enunciado, dados, pontuação e conclusão de redundância. Alternativamente, se a autoria quiser afirmar o processamento, deve definir no enunciado que a coluna v foi efetivamente calculada pela inversão de ρ; isso ampliaria o alcance da edição. Em qualquer caso, não se deve contar as duas colunas como propriedades independentes de estado.

## Contas de apoio verificadas

No modelo ideal hipotético de Raoult/Dalton, pA,sat=150, pB,sat=50 kPa: para zA=0,4, pressões de bolha e orvalho são 90 e 750/11≈68,1818 kPa; para zA=0,8 são 130 e 750/7≈107,1429 kPa. A 80 kPa, equilíbrio dá xA=3/10 e yA=9/16; para zA=2/5, β=8/21 e em 10 mol, nV=80/21 e nL=130/21 mol. Os balanços fecham. Os valores −2/5 e 40/21 para coexistência forçada nos casos I e III são incompatíveis com β∈[0,1], não defeitos dos dados de fase única. Os demais números no lote são fictícios, não medições.

No P3, A atravessa Tc=647,096 K e pc=22,064 MPa; B fica abaixo de Tc e C abaixo de pc; D satisfaz T>Tc e p>pc, e seu título líquido–vapor não é aplicável. Com centros fixos de A, a garantia estrita requer εT<2,904 K e εp<0,036 MPa, simultaneamente. A [publicação IAPWS R2-83(1992)](https://iapws.org/public/documents/CU3rZ/crits.pdf), tabela na terceira página do PDF, confirma os valores centrais usados como referência; seus campos de incerteza não são os erros artificiais do exercício. O link IAPWS específico citado na entrega excedeu o tempo de acesso nesta revisão; não afirmo ter conferido essa URL alternativa. A identidade e o modelo de mistura no recorte foram conferidos de modo algébrico, sem validar com ensaio real.

## Decisão e ajustes

| Critério no alcance examinado | Resultado |
|---|---|
| Identidade do artigo e leitura do enunciado/solução | Atendido na fotografia r9. |
| Redundância termodinâmica de ρ e v | Correta; preservar. |
| Afirmação sobre procedimento de aquisição | Ambígua; **ajuste obrigatório** para explicitar hipótese ou adotar redação que não alegue procedimento. |
| Cálculos de apoio | Conferem no modelo e nas condições delimitadas. |
| Aplicação e aceites anteriores | Pendentes: reexaminar BAN-08/FUN-01 no alcance afetado, com artigo, hashes, inventário, testes e auditoria da versão efetiva. |
| QA-09 integral e próximo ID | Não atendido; não liberado. |

Trata-se de questão autoral, não de alteração de prova ou gabarito oficial. Nenhuma revisão humana, teste em navegador, estudo com alunos ou certificação externa foi realizada. A candidata eventual deve ser submetida a Auditor independente antes da aplicação; preservar históricos e acompanhar o deslocamento do inventário.
