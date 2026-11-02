# QA-09 — auditoria independente das fichas 64–69 e 73–78, r9

Data: 30/10/2026. Revisor: agente automatizado `/root/next_theory`, distinto do Corretor `/root/next_formulas`. **Veredito: AJUSTES OBRIGATÓRIOS** para o lote, em razão da ficha 67. QA-09 integral permanece em correção; o próximo ID não está liberado.

## Critério, fotografia e alcance

QA-09 exige inventariar e recalcular todo o conteúdo numérico fora dos 197 artigos, incluindo fichas, exemplos, oficinas, diagnósticos, projetos, figuras e explicações, com referência verificável e resultado conferido por ocorrência. Este parecer verifica somente as 12 fichas mencionadas, seus modelos e cálculos de teste; não encerra o ID. A regra curricular comum diz respeito à conclusão de conteúdo novo e não transforma esta conferência localizada em evidência de aprendizagem.

Examinei diretamente o formulário `formulas/termodinamica.html`, SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`, e `inventario-r9.json`, SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. A entrega do Corretor [entrega.md](../evidencias/QA-09/fichas-entropia-r9-20261030/entrega.md) tem SHA-256 `06dfab2cb4ac60efce188821052392fe20cc457aa9c2f68e44c3a3937126ec10`. O arquivo de identidades do Corretor contém IDs, deslocamentos e hashes dos 12 blocos. O teste independente [verificar.py](../evidencias/QA-09/auditoria-fichas-entropia-r9-20261030/verificar.py), SHA-256 `61cc145242ee11eb2a7b966656624f2986f65a516587485f025d8b989ab16aa6`, reconstruiu os hashes das 12 fichas, conferiu seu inventário e fez parsing XML dos 20 MathML; executei-o e também o script read-only do Corretor, ambos com sucesso. Inspeção direta da estrutura complementou esses testes; não foi feito ensaio visual de navegador.

## Achado obrigatório — ficha 67

`formula-calor-reversivel` apresenta `δqrev = T ds` e `qrev = ∫T ds` por unidade de massa, com condição “trajetória reversível de referência”, sem dizer que a aplicação da ficha é a um **sistema de massa fixa** (ou explicitar outra hipótese equivalente de parcela material). A entrega assume sistema fechado, mas essa hipótese não está no cartão. Em volume de controle geral há entropia carregada pelas correntes e, eventualmente, acumulação; não se obtém automaticamente `δQ/T = dS` para o conteúdo do volume apenas por o processo ser reversível. A hipótese de trajetória reversível não identifica sozinha o que é a massa de referência nem todos os fluxos.

O link “Retomar na aula” da ficha 67 conduz a `#substancias`, seção que começa com reconhecimento de fases, ao passo que o tratamento de entropia por calor e geração está em `#base-entropia` e a relação de referência em `#base-gibbs`. O vínculo existe, mas não conduz ao desenvolvimento pertinente de modo identificável. Corrigir ou justificar com localização específica, preservando caminhos e o comportamento do formulário.

**Solicitação ao Corretor:** preparar candidata que defina o sistema de massa fixa, as unidades por massa e a temperatura da transferência na trajetória reversível; ajustar o contexto e o vínculo de retomada, inclusive o texto de busca se afetado. Conferir que as fórmulas, os demais cartões, os vínculos e o MathML permanecem coerentes; após aplicação, atualizar fotografia/mapa, revalidar o alcance de FOR-01 e solicitar auditoria da versão efetiva. Esta solicitação não implica que a relação seja incorreta no domínio fechado, tampouco afirma que toda relação análoga em escoamento esteja errada.

## Outros resultados e limites

| Fichas | Verificação independente no escopo examinado |
|---|---|
| 64–66 | Balanço de sistema fechado e soma de subsistemas coerentes com os sinais. Testes: 0,2−30/300=0,1 kJ/K; −0,1+0,3=0,2 kJ/K. As temperaturas devem ser absolutas e os contatos distinguidos. |
| 68–69 | Derivações de gás ideal e razão adimensional conferem; para cp=1,005, cv=0,718 e R=0,287, com T₂/T₁=p₂/p₁=2, ambas as expressões dão 0,718 ln 2 = 0,4976796756… kJ/(kg·K). Composição fixa e calor específico constante são condições das fichas. |
| 73–74 | Equação de entropia estacionária e Gouy–Stodola em ambiente de referência T₀ constante conferem: 1 kg/s×(0,5−0,4)=0,1 kW/K; T₀=300 K dá 30 kW de exergia destruída. Correntes, fronteira e sinais devem ser os escolhidos no balanço. |
| 75–76 | Para propriedades de equilíbrio de substância simples compressível de composição fixa, as identidades `du=Tds−pdv` e `dh=Tds+vdp` e o limite isentrópico conferem. Testes artificiais dão du=10, dh=50 e Δh≈1 kJ/kg. As hipóteses de equipamento não decorrem automaticamente da identidade de propriedade. |
| 77 | Com T,p fixas e transferência interna dn do mesmo componente f→g, `dG=(μg−μf)dn`; a igualdade de potenciais é condição necessária para equilíbrio entre fases presentes com troca permitida, não prova independente de estabilidade global. O teste 1 J/mol×0,001 mol=0,001 J confere. |
| 78 | ∫₃₀₀⁴⁰⁰ (0,8+0,001T)/T dT = 0,8 ln(4/3)+0,1 = 0,3301456579… kJ/(kg·K) quando a razão de pressão é 1. A aproximação 0,33015 é consistente com cinco casas decimais. |

Esses resultados são para os valores fictícios do teste, exatos no modelo salvo os logaritmos; não são medições nem dados de tabela. Não foram encontradas outras discrepâncias científicas nas 11 fichas restantes **no recorte dos modelos e exemplos acima**. Esse recorte não garante cobertura das suas demais dependências e não permite aprovar QA-09 inteiro.

## Fontes e limites de acesso

Confrontei [MIT, balanço de entropia e volume de controle, pp. 9–10](https://www.ocw.mit.edu/courses/2-611-marine-power-and-propulsion-fall-2006/4c32b0845d40ee00555da443f8a0f58b_06second_law.pdf), [MIT, processo reversível e entropia](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node48.html), [NASA, exergia destruída, equação 8](https://ntrs.nasa.gov/api/citations/20205003644/downloads/NASA_TP_20205003644_interactive.pdf), [MIT, identidade de Gibbs](https://web.mit.edu/course/16/16.unified/www/SPRING/thermodynamics/notes/node38.html) e [MIT, equilíbrio entre fases, p. 1](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/b312114e4e885b69b5746dcad660cc4f_lec_18.pdf). As páginas foram acessadas em 30/10/2026. A URL OSTI da entrega retornou erro/tempo excedido nesta auditoria; não a considerei verificada. A fonte NASA acima dá suporte independente à relação de exergia destruída.

| Critério | Resultado |
|---|---|
| Identidade e cálculos das 12 fichas | Atendido para a fotografia r9, com as limitações de testes artificiais e parsing estático. |
| Domínio e referência de retomada da ficha 67 | **Não atendido:** massa de referência/sistema e vínculo de aula precisam ser explicitados ou tecnicamente justificados. |
| Demais 11 fichas e fontes examinadas | Sem divergência no recorte; URL OSTI não foi acessível e foi usado apoio NASA alternativo. |
| Critério integral QA-09 | Não atendido: triagem, recálculo e reconciliação restantes continuam abertos. |
| Próximo ID | **Não liberado.** |

Nenhuma revisão humana, aplicação com alunos ou certificação externa foi realizada. A eventual alteração exige nova fotografia e exame independente do que for efetivamente aplicado.
