# QA-09 — candidata EX-046 r3: alimentação e geração sem dupla contagem

30/10/2026. Corretor `/root/next_examples`. **Nova proposta isolada; não aplicada e pendente de auditor distinto.** A aplicação continua suspensa até decisão da coordenação. QA-09 permanece aberto.

## Histórico e colisão

A primeira proposta r1 foi questionada por `/root/planning`: postulava energia total em regime permanente, sem entrada de energia pela fronteira, ao mesmo tempo que calor saía; geração térmica interna é conversão de energia e não cria energia total. A r1 não deve ser aplicada. Dois agentes trabalharam simultaneamente no mesmo diretório r2; na inspeção, `analise.md` informava hashes de uma proposta enquanto `manifesto.json`, `candidata.html` e `verificar.mjs` tinham outros. A r2 permanece preservada no estado encontrado, sem alegar recuperação dos artefatos anteriormente substituídos, e não constitui pacote coerente nem pode ser usada como candidata aprovada. A r3 foi criada em diretório novo, a partir do fragmento efetivo r20; é outra proposta e requer revisão própria.

## Hipóteses e balanço

A r3 acrescenta um modelo didático suficiente ao EX-046, preservando os dados e contas originais: bloco fechado em regime permanente de energia total; alimentação elétrica fornece 1200 W de trabalho, convertidos integralmente em geração térmica volumétrica uniforme q‴; esta geração e a entrada elétrica representam a mesma energia e não são somadas. Além da entrada elétrica, a única transferência na fronteira é saída de calor por convecção na face exposta, de temperatura uniforme. As outras cinco faces continuam termicamente isoladas; o trabalho elétrico atravessa a fronteira, sem ser uma troca adicional de calor.

`V=3×2×1=6 m³`, `A=3×2=6 m²`, `q‴V=200×6=1200 W`. Para temperatura ambiente 20 °C e coeficiente 20 W/(m²·K), `Q̇out=20×6×(Ts−20)=1200`, portanto Ts=30 °C. No balanço total com Q̇ entrando e Ẇ saindo positivos: `Q̇=−1200 W`, `Ẇ=−1200 W`, logo `dE/dt=Q̇−Ẇ=0`. No balanço térmico, `q‴V−Q̇out=0`; não se acrescenta a entrada elétrica mais uma vez. O valor 1200 W como alimentação é hipótese explicitada neste modelo, não medição.

O contraste do parecer anterior com mais 120 W de trabalho externo, não incluídos na geração original, levaria a 1320 W e Ts=31 °C sob mesmas condições. Esse contraste viola a r3, que fixa alimentação total de 1200 W e exclui outras transferências. Se o trabalho já estiver representado em q‴, somá-lo novamente é dupla contagem. O contraste é hipotético.

## Identidade e verificação

Aula r20 SHA `b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7`; inventário r20 `e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4`. EX-046 original em [460570,461005) UTF-16, SHA `d7fc82a69bdc4bf9a24cebbd6665e2697f1a92dfa3869da604cab37adf6fa8c3`. `candidata.html` SHA `b4d9dafa1f27c766cc44a698709d74f5fbe3ee09cc587c8def6e0709e2f36c55`; `manifesto.json` SHA `a453b56ec947c4d536ab7656543304afcb279acbb52a679cd95950a1dbc221e6`; `verificar.mjs` SHA `0b61175902bb2a3e50322ec201a4051104069cbad2cf06b7f86e43f1b03bfcdb`. Arquivos isolados não têm quebra final acrescentada.

O teste somente leitura `node auditoria/termodinamica/evidencias/QA-09/candidata-ex046-r20-20261030-r3/verificar.mjs` passou: identidade, substituição única, resultado nominal e saldo total, simulação em memória, 197 artigos, 734 MathML e atributos IDs/links/ARIA preservados. HTML hipotético SHA `f7b7a2c23f5e5704bd4d6c456fc431008f9261160a3300128df7a14f13008d24`. A execução não prova física nem apresenta a página em navegador.

Solicita-se Auditor distinto para julgar modelo, fronteira, coerência térmica/energética, ausência de dupla contagem, preservação e hashes r3. Não aplicar até seu parecer e sinal da coordenação. Após eventual aplicação, gerar fotografia e mapa e solicitar auditoria da versão efetiva. Não houve navegador, leitor de tela, alunos, revisão humana ou certificação externa.
