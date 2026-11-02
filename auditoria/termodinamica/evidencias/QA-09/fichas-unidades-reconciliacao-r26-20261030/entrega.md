# QA-09 — reconciliação de unidades, modelos e balanços r26

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente.** Fichas 03, 04, 10–12, 19, 25, 30, 42, 57 e 60 já foram examinadas na r17 e a 60 foi corrigida na r18; esta rodada revisa fotos, fórmulas e contextos na r26. Não é lote histórico inédito, não transfere aceite global e não altera produto.

## Identidade, contextos e testes

Formulário r26 SHA `16329b7369c4ba927f5f7da30551f86934aad1f6a6e55627443dea5cb9fe0c02`, aula r26 `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2`, inventário r26 `d73d6b239822b288329a75fc1f976419ccae7047d1bc74ba161102a529038241`. Formulários r17 `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d` e r18 `463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895`: dez cartões r26 iguais aos r17, ficha 60 mudou na r18, e os 11 são idênticos aos r18. Parecer r17 SHA `645641fefb6a5a8d401ac0fbd3a93d55672f190bf300be495347e4ca627dc57c`; parecer da aplicação r18 `dc7cfd2a55c3e8b8abd8a75814f7a637cc4492cc2ef8a9bd8ec370ddb36b817b`.

`identidades.json` SHA `d63ae331bc179e27d652abda75138f01b0b4b1c60537974ee718f13adead460c` fixa os cartões; `contextos.json` SHA `ca9e5ca20d6285bcce14a1cade0114389b9fc29b05557a51d7ff648deff83628` fixa 11 destinos distintos: nove contêineres coincidem com r17; `base-primeira-lei` e seção `energia` mudaram. Reli os trechos pertinentes: a primeira lei r26 distingue energia cinética macroscópica da interna e conserva a hipótese de massa fixa; a seção energia inclui a base de balanço em escoamento. O destino da ficha 42 é a seção geral, não âncora de fórmula específica. A base COP mantém trabalho líquido total positivo, calor frio e rejeição quente na mesma fronteira e período. Essa leitura não aprova integralmente os dois contêineres modificados ou os demais.

`verificar.mjs` SHA `9e6062685bbc4cefedc6d9082741c8bdbbaa2b36e29e2c1996895276ae5347a7`, executado por `node auditoria/termodinamica/evidencias/QA-09/fichas-unidades-reconciliacao-r26-20261030/verificar.mjs`, passou: fotos, posições/hashes dos cartões e contextos, existência de 12 destinos de links e contas. O teste é somente leitura e não interpreta MathML nem avalia navegação ou o mérito físico automaticamente. Dados abaixo são sintéticos.

## Expressões e domínios

| Fichas | Exame e conta |
|---|---|
| 03–04 | Prefixo k=1000, 1 kPa·m³=1 kJ, L=10⁻³ m³, mm=10⁻³ m e cm³=10⁻⁶ m³; caloria **termoquímica** é 4,184 J. T/K=t/°C+273,15 e intervalos coincidem em °C e K: 27 °C=300,15 K. Não usar °C em razões absolutas. |
| 10 | Aumento relativo a X₁>0 é (X₂/X₁−1)100%, redução é seu oposto; 80→100 dá aumento 25%, redução −25%. Base de referência é inicial. |
| 11–12 | Fração volumétrica 1000 ppmv=0,001; 10 pessoas a 0,02 m³/h geram 0,2 m³/h quando taxa por pessoa é igual ou média apropriada e condições de referência de vazão são coerentes. Para m=0,028 kg, M=0,028 kg/mol, n=1 mol e R≈8,314/0,028=296,929 J/(kg K); usar mesma base de quantidade em Ru/M. |
| 19 | Modelo cinético clássico de gás ideal, três graus translacionais: média por molécula 3kBT/2. A 300 K e kB=1,380649×10⁻²³ J/K, 6,2129205×10⁻²¹ J; não é toda energia interna molecular. |
| 25 | Ar úmido ideal aproximado sem intensificação: φ=pv/psat(T). Com pv=1,2 kPa e psat=3 kPa, φ=0,4; à mesma temperatura e fase de referência, 0,6/0,4=1,5 é a razão das pressões parciais, com denominador não nulo. |
| 30 | Para massa fixa, movimento translacional não relativístico e g aproximadamente uniforme: ΔEc=m(v₂²−v₁²)/2 e ΔEp=mgΔz. m=2 kg, v=3→5 m/s e Δz=3 m com g=10 m/s² dão 16 e 60 J. |
| 42 e 57 | Volume de controle fixo, uma entrada e saída representativas, permanente, q entrando e trabalho não fluxo w saindo: q−w=Δh+Δv²/2000+gΔz/1000 em kJ/kg. Δh=100, velocidades 100→200 m/s, g=9,81 e Δz=20 m dão 115,1962 kJ/kg. No bocal adiabático sem trabalho e Δz desprezível, v₁=50 m/s e h₁−h₂=40 kJ/kg dão v₂≈287,228 m/s; raiz precisa argumento não negativo e não exige reversibilidade. |
| 60 | Ciclo acionado somente por trabalho líquido total recebido Win>0, QL frio e QH quente, mesma fronteira/período e sem outras interações energéticas relevantes. COPBC=QH/Win=COPR+1, com COPR=QL/Win. Se Win=80, QL=300 e QH=380 kJ, COPBC=4,75 e COPR=3,75; valores líquidos evitam confundir entrada bruta com desempenho do ciclo. |

## Fontes e pedido de auditoria

[NIST, fatores SI](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9); [NIST, geração de CO₂](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920870); [NIST, ar úmido e intensificação](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=921756); [MIT, equipartição](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/a48f66f75209c904d98e034be688ebe2_BTNsoSNR5B0.pdf); [MIT, balanço de escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm); [DOE/FEMP, COP por trabalho líquido](https://www.energy.gov/cmei/femp/incorporate-minimum-efficiency-requirements-heating-and-cooling-products-federal). Não são origem dos dados sintéticos.

Não identifiquei divergência no escopo descrito. Solicita-se Auditor distinto para texto, MathML, cálculos e contextos r26, incluindo duas regiões alteradas. Não houve navegador, leitor de tela, estudantes ou revisão humana; não se avalia a íntegra dos contextos, outras fichas ou a aprendizagem.
