# QA-09 — dados FUN-01 de mistura e ponto crítico na fotografia r9

Data: 30/10/2026. Corretor: agente automatizado `/root/next_graphics`. Estado: **aguardando auditoria independente; um possível achado de procedência está aberto.** Este lote recalcula dados numéricos do JSON e saídas do código FUN-01 que são vinculados fora dos artigos, confrontando os problemas que os usam. Não modifica produto, não encerra QA-09 e não aprova BAN-08 nem FUN-01 integralmente.

## Fotografia, vínculos e escopo

Aula `modulos/e1-termodinamica.html` SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. JSON `assets/termodinamica/fun01-dados-v1.json` SHA-256 `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448`; código `assets/termodinamica/fun01-calculos-v1.mjs` SHA-256 `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88`. Os links fora dos artigos estão em `fun01-dados`, UTF-16 113050 e 113328. O bloco `fun01-dados` em 111432–113604 tem SHA-256 `f2ad9153af7074ac31be0b322be23bf21a8450b3b98411b54961266c89ff94cc`.

Os confrontos da mistura e do ponto crítico usam os artigos `fun01-e1-mistura` (119961–125802, SHA-256 `c6a2a5430bdee022dc9db6eb9d0e3c50c33086736b37154dd97d2749f53d4e53`) e `fun01-e1-supercritico` (125803–131220, SHA-256 `2fad0e042fb945eb44d0f2abe2c4e64322434195395fa4e5c084f17854f432a7`). Ambos estão entre os 197 artigos segregados; não são novas ocorrências fora desse conjunto. A aplicação externa dos ativos não é automaticamente aceita só por sua revisão anterior. O recorte das três linhas NIST da água já foi examinado separadamente em `fun01-textos-tabela-20261030` e não é refeito aqui; os dados de equilíbrio e problema de saturação deste JSON continuam fora deste lote.

## Mistura fictícia A/B a 350 K

Modelo declarado: solução líquida e vapor ideais, Raoult e Dalton, componentes não reativos, sem efeitos relevantes de gravidade ou capilaridade; pressões absolutas fictícias pA_sat=150 e pB_sat=50 kPa. Não são dados de mistura real. O cálculo em pontos de orvalho e bolha parte de composição global z na fase única: `p_b=z pA_sat+(1−z)pB_sat`; `p_d=[z/pA_sat+(1−z)/pB_sat]⁻¹`.

| Lote | zA | p (kPa) | p_b (kPa) | p_d (kPa) | Classificação para o modelo |
|---|---:|---:|---:|---:|---|
| I | 0,40 | 100 | 90 | 68,181818… | líquido, acima da bolha |
| II | 0,40 | 80 | 90 | 68,181818… | duas fases, entre os limites |
| III | 0,80 | 80 | 130 | 107,142857… | vapor, abaixo do orvalho |
| IV | não informado | 80 | não determinado | não determinado | não se conclui coexistência sem composição ou observação |

Se coexistência for imposta a 80 kPa, `x_A=(80−50)/(150−50)=0,30` e `y_A=x_A 150/80=0,5625`. No II, `β=(0,40−0,30)/(0,5625−0,30)=8/21≈0,380952381`; nV=80/21≈3,80952381 mol e nL=130/21≈6,19047619 mol. Fechamentos: nV+nL=10 mol e nL xA+nV yA=4 mol de A. III forçado a duas fases dá β=40/21>1. Em I, sob a pressão de 100 kPa, xA=0,50, yA=0,75 e β=−0,4. Esses valores inválidos refutam apenas a suposição de coexistência nos lotes I e III, não os dados de fase única. Para IV, zA=0,35 e 0,50 levam, se coexistência for imposta, a β=4/21 e 16/21, respectivamente: T,p fixam as composições de fase nesse modelo mas não a quantidade relativa sem composição global. A fração β é molar; título em massa requer massas molares médias das fases. Igualdades são exatas para o modelo e dados; decimais são aproximações, não erro instrumental.

## Ponto crítico de água e erros limitados

Valores da base IAPWS: Tc=647,096 K e pc=22,064 MPa. As leituras e erros são hipotéticos, absolutos e determinísticos, não intervalos de confiança. A caixa de A é T=[645,655] K e p=[22,00,22,20] MPa; cruza ambos os limiares, logo o rótulo supercrítico não é garantido. B tem Tmax=641 K<Tc; C tem pmax=20,1 MPa<pc; ambos são certamente fora da região T>Tc e p>pc. D tem T=700 K e p=25 MPa exatos no problema: satisfaz ambas as desigualdades, mas título líquido–vapor x=0,20 não é um metadado aplicável nesse estado.

Em A, somente reduzir εT para 1 K deixa pressão atravessando pc; somente reduzir εp para 0,01 MPa deixa temperatura atravessando Tc; ambas as melhorias garantem as duas desigualdades na caixa. Com centros mantidos, os limites são **εT<2,904 K e εp<0,036 MPa**; a igualdade toca o limiar e não garante condição estrita. O código classifica as quatro caixas e dá esses mesmos limites. Os valores críticos não são uma tabela completa para obter h, v ou s.

## Achado possível: dependência não comprova procedência

Na solução do artigo supercrítico, a frase “A identidade v=1/ρ torna essas duas colunas redundantes; uma é calculada da outra” segue a proposta de usar duas colunas produzidas pelo mesmo sensor. A identidade afirma dependência exata e sustenta a conclusão de redundância do par; **não informa por si só o procedimento de obtenção**. Contramodelo: um dispositivo hipotético pode obter duas estimativas por princípios de medição distintos, e seus valores nominais publicados podem coincidir reciprocamente (por exemplo ρ=800 kg/m³, v=0,00125 m³/kg), sem que uma tenha sido calculada da outra. Portanto, a segunda oração sobre origem parece mais forte que as premissas. É necessário exame independente do contexto e da interpretação antes de alterar o artigo. A frase semelhante na apresentação externa foi corrigida anteriormente, mas isso não comprova que esta ocorrência tenha sido resolvida. Se o Auditor confirmar e houver alteração, reavaliar a identidade e o alcance BAN-08/FUN-01 dos 197 artigos; preservar histórico e não alterar gabaritos oficiais. Não há candidata nem alteração aplicada neste lote.

## Reprodução e fontes

Execute da raiz `python3 auditoria/termodinamica/evidencias/QA-09/fun01-mistura-critico-recursos-r9-20261030/verificar.py` (SHA-256 `9d08d89f3afa2c3d5e21c390312475a695745e2ec396cf9f5816477b88c69bb8`). É somente leitura; identifica as versões e fragmentos, recalcula com frações exatas e passou. A função `calcularFun01` foi executada por importação Node com o JSON efetivo: 28 verificações internas passaram, e as saídas de mistura e supercrítico coincidem com os valores acima; isso não substitui auditoria independente.

[IAPWS, Guideline G5-01(2020), §4.1](https://www.iapws.org/relguide/fundam.pdf) fornece Tc e pc da água. [OpenStax Chemistry 2e, §11.4](https://openstax.org/books/chemistry-2e/pages/11-4-colligative-properties) explica frações molares e pressão de vapor no modelo de Raoult. Ambas foram consultadas em 30/10/2026; nenhuma é fonte dos números artificiais de A/B ou dos erros da instrumentação.

Não houve execução em navegador, leitor de tela, piloto com alunos, revisão humana ou certificação externa. Auditor distinto deve conferir os cálculos, a classificação do achado e os vínculos na fotografia; QA-09 e próximo ID permanecem bloqueados.
