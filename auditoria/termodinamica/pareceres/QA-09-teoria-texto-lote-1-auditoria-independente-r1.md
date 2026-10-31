# QA-09 — auditoria independente do lote textual 1 e candidata percentual, r1

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_diagnosticos`. **Veredito: AJUSTES OBRIGATÓRIOS no lote da versão efetiva**, pois o trecho de razão e percentual não delimita o sinal do valor inicial. **A candidata isolada revisada é adequada para esse ponto**, mas ainda não foi aplicada nem auditada como produto. QA-09 continua em correção; o próximo ID não é liberado.

## Critério, versões e abrangência

QA-09 exige identificar e recalcular todas as ocorrências numéricas externas aos 197 artigos, com referência verificável, inclusive textos e figuras. Este parecer cobre 20 trechos de texto direto selecionados, suas contas e os limites descritos na entrega; não abrange os outros registros do inventário, a totalidade dos nós que os contêm, figuras, conteúdo dinâmico, revisão de acessibilidade ou aprendizado. A regra comum de entrega curricular não está concluída por este lote de verificação.

Base `modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; entrega `auditoria/termodinamica/evidencias/QA-09/teoria-texto-lote-1-r1/entrega-r1.md` SHA-256 `474cc8f8fd2e9e5831906f14d339d8c572c031519b4c4d8a781bf6aefb427e0e`; script `verificar-r1.py` SHA-256 `209a92711c6e198d43bce42d56b51426773a4bbc5e28887cd4e14ec42f7df1ca`. Candidata em `auditoria/termodinamica/evidencias/QA-09/candidata-razao-percentual-20261030/`: `analise.md` SHA-256 `f31f23019a227d74ca0d4febed96daee96143491a5c39149cb82686c1e17da2d`, `candidata.html` (com quebra final) `e42865b2309e4e00fbbca0caf8ebfe9967f2f1a8a24d0be45b11902a3a9e45c9`, `manifesto.json` `47c5012592e75e97bb31c9886d232ee976c8ef5314baf4ceb8fd0a68587b78da`.

Localizei os vinte nós no HTML e reli os trechos e contexto. Reproduzi seus hashes de texto direto a partir dos intervalos e filhos com o parser do projeto, todos iguais aos de r7; essa operação usa o mesmo parser do inventário e não é prova de cobertura independente do DOM. O verificador do Corretor executou com `ok=true`. Fiz as contas em separado e confrontei os vínculos metrológicos; o link anterior NIST com consulta malformada foi substituído na entrega pela [lista CODATA 2018](https://physics.nist.gov/cuu/pdf/all_2018.pdf), p. 6, onde R=8,314462618… J/(mol·K). O BIPM, apêndice do kelvin, p. 2, relaciona Celsius e kelvin; BIPM define a atmosfera padrão 101.325 Pa; NIST registra a caloria termoquímica como 4,184 J. Essas fontes dão suporte às definições, não aos demais dados fictícios.

## Conferência numérica dos 19 demais trechos

- **Fundamentos 31291, 35359, 35746, 36216, 36410, 36561, 39501, 42129:** 10 °C = 283,15 K; variação de 10 °C = 10 K; 200/0,010 = 20.000 Pa; 55−80 = −25 kJ; 2 kJ/s × 60 s = 120 kJ; litro e centímetro cúbico têm fatores 10⁻³ e 10⁻⁶ m³; ln(2)=0,693147… arredonda a 0,693; os pontos da escala dão b=2 e X(30)=70. As condições da entrega para pressão, potência e escalas se aplicam. O argumento de logaritmo precisa ser positivo e adimensional.
- **Substâncias 77466, 77974, 79064, 79927, 81742, 81928:** mol = 6,02214076×10²³ entidades; 8,314462618… J/(mol·K) corresponde a 0,082057… atm·L/(mol·K), ambos arredondamentos conferem; 350/280=1,25 e V₂=V₁/3 leva a p₂=3p₁ sob as condições de gás ideal descritas; 120/150=0,8; 70%=0,70; 50% da pressão de saturação implica metade da quantidade de vapor no mesmo T e V no modelo ideal. Não equivale à fração de massa do ar que é água.
- **Energia 194365, 200027, 225352:** 1 kcal=1.000 cal e 4.184 J=4,184 kJ na definição termoquímica; inverter o mesmo processo de −50 kJ fornece +50 kJ; 2 kg/s a 20 °C e 1 kg/s a 80 °C resultam em 40 °C no modelo de mesmo líquido, cₚ constante, misturador estacionário adiabático sem trabalho e sem mudanças relevantes de fase, pressão e energia cinética/potencial.
- **Segunda lei 342330 e aplicações 412780:** 100−20=80 kJ é conta condicional sobre a disponibilidade de referência e as mesmas restrições, não afirma que energia foi destruída. 600 m³/h / 200 m³ = 3 h⁻¹ é taxa de renovação, não garantia de remoção de todos os contaminantes.

Nenhuma divergência adicional foi identificada nas afirmações aritméticas selecionadas acima sob os modelos referidos. Valores nominais fornecidos na aula; em `ln(2)` e R, a tolerância de arredondamento da última casa publicada é ±0,0005. A inspeção não esgota todas as afirmações dos mesmos parágrafos ou suas dependências.

## Ajuste obrigatório e candidata

No nó 36056, o HTML atual diz que X₂/X₁=1,4 representa aumento de 40%, sem exigir X₁ positivo. Com X₁=−10 e X₂=−14, a razão é 1,4 mas a variação numérica é −4, portanto não houve aumento. X₁=0 também torna a razão indefinida. O trecho atual precisa delimitar o domínio para a interpretação de aumento e redução.

Verifiquei a candidata isolada: o fragmento original ocorre uma vez no HTML atual, a candidata não ocorre; seus SHA-256 **sem quebra final** são respectivamente `8a084ef1539e7b1a4b427ad5da7865c67876ca80a4dafef72cf1e991ecba2b8c` e `96b658b0b27f4e4d9f14a146a926906219078f252461bfaaf5d3bb639f891739`. A candidata declara X₁>0 para o exemplo e X₁>0, X₂<X₁ para a fórmula de redução. Para X₁=100, X₂=140 há aumento de 40%; para X₁=100, X₂=70 a redução é 30%. A alteração resolve o contramodelo no alcance proposto e a codificação HTML `&gt;`/`&lt;` representa os sinais pretendidos. Sua adequação **não comprova aplicação**: exigir substituição única, conferência do delta e da versão efetiva, atualização e reconciliação do inventário por posição, contexto e hashes, análise dos aceites afetados, validação estrutural e novo parecer independente.

| Critério | Resultado |
|---|---|
| Identidade dos 20 trechos da fotografia | Atendido no método e limites declarados. |
| Recalcular e confrontar valores selecionados | 19 sem divergência identificada no alcance descrito; o nó 36056 requer delimitação. |
| Fontes das constantes e unidades utilizadas | Conferidas no alcance descrito; dados do exercício permanecem didáticos. |
| Candidata percentual isolada | Adequada para revisão e possível aplicação; não aplicada ou aprovada na versão efetiva. |
| Critério integral QA-09 e próximo ID | Não atendido; permanecem bloqueados. |

Sem teste em navegador real, revisão humana, aplicação com alunos ou certificação externa. Qualquer nova edição exige reconstruir a identidade e avaliar alcance, sem transferência automática de aceites.
