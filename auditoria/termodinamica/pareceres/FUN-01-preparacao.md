# FUN-01 — preparação da auditoria independente

Data: 27/10/2026. Revisor: agente automatizado `/root/auditor_aaa`. Estado: preparação; nenhum parecer sobre a implementação ainda em elaboração. O controle indica FUN-01, rodada 1, em correção. Este documento não libera outro ID.

## Escopo de aceite

Aplicam-se FUN-01 e a regra comum da seção 3.2 de `AUDITORIA_TERMODINAMICA_NIVEL_AVANCADO.md`: desenvolver estado, equilíbrio térmico, mecânico, químico e de fases, postulado de estado para sistemas simples compressíveis, composição e independência de propriedades. O aluno deve classificar dados suficientes, redundantes ou incompatíveis, incluindo saturação, misturas e região supercrítica.

A revisão examinará o encadeamento entre objetivo, pré-requisitos, teoria/hipóteses, exemplo que explicita decisões, prática independente inédita, solução/rubrica, fontes/versionamento dos dados e vínculo C01–C10. Não bastam títulos, fórmulas ou uma troca de números. Não há exigência artificial de número fixo de exercícios: a cobertura efetiva das decisões previstas determina a suficiência.

## Referências conferidas e limites científicos

- [MIT 16.Unified, §1.2.3–1.2.4](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node11.html): definição de estado e condições de equilíbrio. Nesta versão, `node10.html` é a introdução geral; a discussão de estado/equilíbrio está em `node11.html`. Uma observação de temperatura uniforme, por si só, não comprova todos os equilíbrios. O exame respeitará as restrições físicas explicitadas, sem exigir pressões iguais onde forças de suporte, gravidade ou interface exijam outro balanço.
- [Purdue ME 200, Spring 2023, capítulo 1, páginas 14–15](https://www.purdue.edu/freeform/me200/wp-content/uploads/sites/29/2023/01/ME-200-Chapter-1.pdf): propriedades independentes e postulado para substância simples compressível. Contar duas leituras não comprova independência nem consistência com o modelo.
- [ASHRAE Handbook 2025, capítulo 2, §1.2](https://handbook.ashrae.org/Handbooks/F25/IP/f25_ch02/f25_ch02_ip.aspx): dependência de pressão e temperatura na saturação pura; necessidade de outra propriedade, como título ou volume específico; diferença entre substância pura e mistura zeotrópica. A regra da saturação pura não pode ser generalizada automaticamente a toda mistura.
- [MIT 2.43, Spring 2024, aula 09, slides 09.15–09.18 e 09.25](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/mit2_43_s24_lec09.pdf): estado intensivo versus quantidade total, condições de equilíbrio entre fases, regra das fases sem reações e propriedades de mistura líquido–vapor. A variância das propriedades das fases não determina sozinha suas quantidades relativas. A igualdade dos potenciais químicos pertinentes não implica igualdade de composição de fases diferentes. Não se exige aqui derivar Clapeyron ou concluir PROP-08.
- [NISTIR 5078, tabela 2](https://www.nist.gov/document/nistir5078-tab2pdf): referência independente para conferir dados de saturação efetivamente utilizados. Atenção às unidades da tabela: pressão em MPa, entalpia em kJ/kg e volume em cm³/g. Os valores específicos da entrega serão conferidos após o congelamento.
- [IAPWS R7-97(2012), §3, página 5](https://iapws.org/technical-guidance/release/IF97-Rev.download): constantes críticas da água, 647,096 K e 22,064 MPa; a estrutura e o domínio do modelo estão no §2. Não tratar título como propriedade definida de um fluido supercrítico, nem substituir a verificação de ambos os limites críticos pela de apenas um deles.

## Verificações a aplicar à entrega concreta

1. Conferir se as hipóteses distinguem equilíbrio de simples ausência de mudança observada, identificam os modos de interação relevantes e justificam quando o postulado reduz a caracterização a duas propriedades independentes. Verificar a diferença entre estado específico/intensivo e valores extensivos que ainda requerem a quantidade de matéria.
2. Resolver os casos propostos sem seguir previamente a solução. Separar dados redundantes, dados insuficientes por composição ou fração de fase desconhecida e dados incompatíveis com as condições declaradas. Dados incompatíveis com uma hipótese de duas fases não significam necessariamente impossibilidade de outro estado físico.
3. Verificar toda aplicação à saturação: condição de coexistência, propriedade adicional independente, fração admissível e conservação na combinação das fases. Distinguir fração mássica de vapor de fração volumétrica e de composição química, quando utilizadas.
4. Conferir composição conhecida versus livre, fases presentes e eventual restrição de reação; não aplicar a regra das fases irrestrita a um sistema com restrições adicionais sem explicação. A prática deve exigir alguma decisão real sobre suficiência dos dados, e não apenas recitar a contagem.
5. Examinar a região supercrítica, a adequação do modelo e a validade dos pares escolhidos. Independência depende da relação entre propriedades no domínio considerado: dois nomes de propriedades não garantem dois graus de liberdade.
6. Comparar exemplo, exercício e rubrica: o exercício deve exigir decisões independentes e a rubrica deve valorizar hipóteses, justificativa da classificação e diagnóstico/correção dos dados. Conferir cálculos, unidades, referências e tolerâncias efetivamente necessárias.
7. Conferir hashes, escopo E1, preservação dos itens e comportamentos antes aprovados, manutenção do inventário para novos itens e alterações reais. Inspeção estática, cálculo e evidência de navegador serão identificados separadamente. Não alegar aplicação com alunos.

## Dependências e próximo passo

Não há impedimento prévio para uma unidade própria de estado/equilíbrio, com seus dados e exercícios rastreáveis, sem usar os problemas pendentes de CR09/CR24/CR68/CR79 como evidência de domínio. BAN-10/FON-09 e GOV-02 continuam abertos; este preflight não os conclui. Aguardar pacote congelado, examinar integralmente o conteúdo afetado e emitir `FUN-01-r1.md` com critérios, evidências, hashes e decisão explícita.
