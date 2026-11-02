# QA-09 — auditoria independente das candidatas de fichas 40 e 67, r9

Data: 30/10/2026. Auditor: agente automatizado `/root/next_examples`, distinto do Corretor das candidatas. **Veredito: APROVADAS como propostas isoladas**, sujeitas à aplicação e auditoria da versão efetiva. A candidata da ficha 40 não altera a base `#base-termoquimica`, cuja explicitação solicitada no parecer da ficha 40 continua pendente; este parecer não encerra a revisão daquela base. QA-09 integral não está aprovado e o próximo ID continua bloqueado.

## Fotografia e identidade

Formulário efetivo r9 SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; inventário r9 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`; análise das candidatas `f7e049ecc4d513a7bb646e16f2cdaba3081018c17d56eae31292af5d0e228e66`; manifesto `dbc90bf734eab940ed7f09790a4fe02ac1efd279d5327086508717d156183a0d`. Li diretamente os cartões originais, o texto e os hashes das propostas, os pareceres anteriores e as bases da aula. Os fragmentos originais são únicos e coincidem com a posição UTF-16 e hashes da fotografia; arquivos isolados possuem uma quebra de linha final que não faz parte dos hashes de fragmento.

O script independente [verificar.mjs](../evidencias/QA-09/candidatas-fichas-40-67-auditoria-r9-20261030/verificar.mjs), SHA-256 `aa2c3f76e87a55aff594ee2197a191fb7dfa1ca0c1d5179c9d95e9861e1c8880`, executou com sucesso uma simulação somente em memória: 100 cartões e seus IDs na mesma ordem; apenas 40 e 67 mudam, 98 permanecem byte a byte iguais; duas expressões MathML em cada cartão-alvo são idênticas; o destino `#base-entropia` existe. O verificador do Corretor também passou. Nenhum HTML foi alterado por esta revisão.

## Ficha 40

A nova condição explicita p termodinâmica constante, fronteira à mesma pressão e único trabalho `Wb=p(V₂−V₁)`, ΔEc/ΔEp desprezíveis. Logo `Q=ΔU+Wb=ΔU+pΔV=Δ(U+pV)=ΔH`. Processo quase estático é exemplo suficiente, não requisito geral único. A frase e `data-busca` concordam; MathML, unidade e inversão entre mesmos estados são preservados.

O contramodelo do Corretor é uma expansão contra p externa constante de 100 kPa de estado inicial (200 kPa, 1 m³) a final (100 kPa, 2 m³), com gás ideal e mesma temperatura nas extremidades: W=100 kJ, ΔU=0, Q=100 kJ e ΔH=0. Ele demonstra que pressão externa constante por si só não estabelece a condição da candidata; não é processo de pressão termodinâmica constante e não refuta a formulação proposta. A [primeira lei do MIT](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html) e a distinção de pressão de fronteira no [MIT, capítulo 3](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_3.htm) sustentam o raciocínio.

**Pendência separada:** o texto da aula em `#base-termoquimica` ainda diz “condições adequadas ao balanço” sem explicitar essa igualdade de pressões/trabalho. O parecer de origem já solicitava verificar a base. Deve-se apresentar correção ou justificativa auditável da base antes de considerar encerrado o achado além do cartão; a aprovação localizada da candidata não cobre essa página.

## Ficha 67

A proposta fixa sistema fechado de massa constante e caminho reversível de referência, com temperatura absoluta T na fronteira de transferência e igualdade à temperatura do sistema ao longo da trajetória reversível. Assim, `δq_rev=T ds` e `q_rev=∫T ds` são específicos por massa de sistema fixo; a área em T–s não é o calor de qualquer trajetória irreversível real. Os símbolos continuam q em kJ/kg, s em kJ/(kg·K), T em K. Essa é uma restrição suficiente para a fórmula ensinada, não uma afirmação de que nunca se pode formular relação análoga para escoamento sob hipóteses próprias. A [expressão reversível do MIT](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node38.html) e a base `#base-entropia` distinguem transferência de entropia e geração.

A conta de controle do contramodelo de volume de controle permanente com 60 kW a 300 K e ṁ=1 kg/s é `Q̇/T=0,2 kW/K=ṁ(s₂−s₁)` para Δs=0,2 kJ/(kg·K), com Sger=0 e acumulação de entropia zero. Isso demonstra a necessidade de tratar escoamentos, não prova por si só a viabilidade de um equipamento específico. O novo link aponta à base pertinente, que existe na fotografia; teste estático de destino não substitui navegador ou leitor de tela.

| Critério | Resultado |
|---|---|
| Identidade, original único, integridade dos demais cartões e MathML | Atendido em simulação e na fotografia declarada. |
| Coerência da candidata 40 e premissas do balanço | Atendido para o texto isolado; base da aula segue pendente de tratamento. |
| Coerência da candidata 67, fronteira e referência de massa | Atendido no modelo de sistema fechado e caminho reversível. |
| Link, texto e busca | Alvo existe e texto visível coincide com `data-busca`; sem teste de navegador real. |
| Versão efetiva pós-aplicação e FOR-01 | Não examinadas; exigem comparação, revalidação de alcance, mapa e novo parecer. |
| QA-09 integral e próximo ID | Não atendidos; continuam bloqueados. |

Não houve teste de estudante, revisão humana ou certificação externa. Simulação não substitui auditoria da versão efetivamente aplicada nem transfere aceites de FOR-01 automaticamente.
