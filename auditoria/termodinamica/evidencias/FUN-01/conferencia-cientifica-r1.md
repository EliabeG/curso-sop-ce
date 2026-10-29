# FUN-01 r1 — fontes, modelos e conferência científica do Corretor

Data: 27/10/2026. Responsável: Corretor; preparação da bancada e relações auxiliares por apoio_fun01. Conferência auxiliar de dados e números por coordenador. Este documento não é o parecer independente.

| Conteúdo publicado | Fonte / versão | Uso e limite |
|---|---|---|
| Estado e equilíbrio | [MIT, Unified Engineering, §1.2](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node10.html) | Conceitos; explicações e casos escritos para o E1. |
| Postulado de estado | [Purdue ME200, Spring 2023, p.15](https://www.purdue.edu/freeform/me200/wp-content/uploads/sites/29/2023/01/ME-200-Chapter-1.pdf) | Sistema simples compressível, composição fixa, duas propriedades independentes; não uma regra para dois números quaisquer. |
| Pureza, qualidade, mistura zeotrópica | [ASHRAE Fundamentals 2025, cap.2, §1.2](https://handbook.ashrae.org/Handbooks/F25/IP/f25_ch02/f25_ch02_ip.aspx) | Relação p/T em pura bifásica versus misturas; não atribui a esta fonte números fictícios. |
| Contagem de fases | [MIT 2.43, aula9, Spring2024](https://ocw.mit.edu/courses/2-43-advanced-thermodynamics-spring-2024/ocw_243_lecture09_2024mar05_v2_transcript.pdf) | Derivação de F, explicitamente exclui quantidades de fases e reações/restrições não contadas. |
| Definições químicas | [IUPAC Gold Book, C01032](https://goldbook.iupac.org/terms/view/C01032/html) e [C01023](https://goldbook.iupac.org/terms/view/C01023), edição2025 | μ parcial molar e condição de reação; coordenador consultou as entradas. Consulta web pelo Corretor retornou403, portanto não alegada como leitura independente dessas páginas por ele. |
| Raoult ideal | [University of Washington, CHEM452 Winter2023, §5.1,eq5.1](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/ideal_solutions_and_colligative_properties.html) | Relação p_i=x_i Psat_i; soma/normalização/conservação derivam as expressões usadas. Não se copiam os exercícios da fonte. |
| Água saturada | [NISTIR5078,1998,Table2,pp11–12](https://www.nist.gov/document/nistir5078-tab2pdf) | Três linhas em0,10/0,15/0,20MPa; volumes de cm³/g para m³/kg por fator0,001. Sem interpolação nem incerteza certificada inventada. |
| Referência crítica água | [IAPWS R7-97(2012),§3,p5](https://iapws.org/technical-guidance/release/IF97-Rev.download) | Tc647,096K e pc22,064MPa. Não implementa IF97 nem fornece propriedades fora das linhas NIST. |
| Mistura gasosa ideal / μ | [MIT3.020 Spring2021,aula13](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf) | Pressões parciais e potencial com log adimensional; caso multicâmara próprio. |
| F/G e diferencial material | [Cambridge,Tong,§4.4](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S4.html#S4.SS4) | Critério F em T,V fixos, G em T,p fixos; base molar declarada. Dedução gravitacional mostrada no próprio texto. |
| Hidrostática | [OpenStax/Rice,UniversityPhysics1,§14.1](https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure) | dp/dz=-ρg; gravidade é compatível com equilíbrio e pressão não uniforme. |

## Decisões conferidas

- Duas propriedades devem ser independentes; identidade vρ=1 não fornece coordenada extra. Contagem local por Jacobiano não promete unicidade global.
- Pura LV: p/T dependentes; GibbsF=1 fixa propriedades das fases, não seu título. Mistura binária ideal: T,p podem fixar composições coexistentes, mas sem z não fixam fração das fases nem provam que o lote esteja bifásico.
- Raoult/Dalton e parâmetros fictícios: lotes I/III são monofásicos, e β forçada fora de[0,1] rejeita a hipótese de coexistência. β molar não vira título mássico sem massas molares.
- Água supercrítica exige p>pc e T>Tc simultaneamente. Margens são estritas e determinísticas; qualidade não se define nessa região.
- Equilíbrio mecânico permite hidrostática e suporte de membrana. μ intrínseco varia com altura; μ+Mgz permanece constante nas hipóteses ensinadas.
- Mistura sob membrana fixa: só A iguala μ entre regiões; B não atravessa. F, não G com pressão global fixa presumida, rege T/volumes constantes. Estabilidade é demonstrada apenas na coordenada permitida.
- Reação A⇌2B: condição é2μB−μA=0, nãoμA=μB. Ausência de mudança por bloqueio não demonstra reação em equilíbrio.

## Reprodução e alcance

[calculo-r1.json](calculo-r1.json) registra28 verificações de domínios, conservação e equações de estado pelo módulo publicado; [calculos-coordenador-r1.json](calculos-coordenador-r1.json) registra a conferência independente do coordenador. Os dois caminhos coincidem dentro da precisão declarada. Exemplos, valores finais e unidades foram comparados com as soluções.

Os problemas1 e3 receberam estimativa intermediária;2 e4 avançada dentro de modelos delimitados. Há decisões que exigem mais que substituição, mas não se certificam o curso, competências completas ou dificuldade empírica. O material novo não usa CR09/24/68/79 como prova de domínio. As190 questões e seus registros não foram corrigidos nem reavaliados cientificamente neste item.
