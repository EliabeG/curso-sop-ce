# QA-09 — reconciliação das fichas de entropia e exergia r22

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente.** As fichas 64–69 e 73–78 já foram examinadas e auditadas na r9; a 67 foi corrigida na r10. Esta rodada reconcilia e reexamina a r22, sem tratá-las como inéditas ou aprovar automaticamente contextos e outras versões. Produto não alterado; QA-09 permanece aberto.

## Versão e método

Formulário r22 SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`, aula r22 `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f`, inventário r22 `6e68d5a9e5cfec73aa2a5ce24121ede1c3a155ca2a5783cf6f17ca95eee8061b`. Formulários preservados r9 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb` e r10 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`: 11 artigos idênticos r9/r22; 67 mudou na r10 para declarar massa fixa e destino pertinente; todos 12 idênticos aos da r10. Parecer de fichas r9 SHA `1c54a5775a0c10e87aac24f6b19363455590d73ebce65587edd5155c1f16eacc`; auditoria da aplicação r10 `26a166c526f7b2be922ba90bb13870c90e2b4a6066213fabfbf39affd7c60ffc`.

`identidades.json` SHA `d15ef85f09953a9285a83c606e0ffb089a315b5ddf95163013df1432391eb406` fixa IDs, hashes e offsets UTF-16 em cada versão. `verificar.mjs` SHA `6c66dd321cbf421f84ea3f5bb2fb087bd3e7c22816890fcc4883999bc411c447` é somente leitura, confirma fotos, fragmentos, existência das 12 âncoras e contas; `node auditoria/termodinamica/evidencias/QA-09/fichas-entropia-reconciliacao-r22-20261030/verificar.mjs` retornou `ok=true`. A existência de âncora não comprova navegação nem adequação integral; o script não interpreta MathML ou pressupostos. Os valores abaixo são hipotéticos, não propriedades medidas.

## Relações e condições

| Ficha | Revisão |
|---|---|
| 64 | Sistema fechado, calor positivo entrando e temperatura absoluta uniforme na fronteira de cada contato: ΔS=∫δQ/Tb+Sger, Sger≥0; para vários contatos ou temperaturas distribuídas, somar/integrar localmente. ΔS=0,2 kJ/K, Q=30 kJ a 300 K dão Sger=0,1 kJ/K. Reversibilidade interna implica Sger=0, não exige ΔS=0. |
| 65–66 | Sistema isolado ΔS=Sger≥0; conjunto sistema+vizinhança só tem garantia de soma não negativa se o conjunto for isolado. −0,1+0,3=+0,2 kJ/K; uma parte pode diminuir sua entropia. |
| 67 | Sistema fechado de massa fixa em trajetória reversível de referência: δqrev=T ds e qrev=∫T ds, com T da fronteira igual à do sistema nesse caminho. Para T=300 K e Δs=0,2 kJ/(kg K), qrev=60 kJ/kg. Não confundir essa integral com calor da trajetória real irreversível. |
| 68–69 | Gás ideal de composição fixa e cp/cv constantes: Δs=cp ln(T₂/T₁)−R ln(p₂/p₁)=cv ln(T₂/T₁)+R ln(v₂/v₁). Para cp=1,005, cv=0,718, R=0,287 kJ/(kg K), T₂/T₁=2, p₂/p₁=2 e v₂/v₁=1: ambas dão 0,4976797 kJ/(kg K). Razões de temperaturas e pressões absolutas devem ser positivas e adimensionais. |
| 73 | Volume de controle estacionário, s e ṁ de todas as correntes e Q̇j positivo entrando a Tj de fronteira uniforme: Ṡger=Σsaída ṁs−Σentrada ṁs−ΣQ̇j/Tj≥0. Vazão 1 kg/s, s₁=0,4, s₂=0,5 e operação adiabática dão 0,1 kW/K. Em transiente incluir acumulação. |
| 74 | Com referência ambiental T₀ constante e Sger da fronteira considerada, exergia destruída=T₀Sger. T₀=300 K e Ṡger=0,1 kW/K dão Ẋdest=30 kW; Sger não é sempre ΔS do sistema. |
| 75–76 | Substância simples compressível de composição fixa, estados de equilíbrio: du=Tds−pdv, dh=Tds+vdp. Diferenciais ilustrativos T=300, ds=0,1, p=100, dv=0,2, v=0,2, dp=100 em unidades da ficha dão du=10 e dh=50 kJ/kg; não afirmam integração finita dessas grandezas variáveis. Isentrópica com v≈0,001 m³/kg e Δp=1000 kPa dá Δh≈1 kJ/kg; caso v varie integrar v dp na isentrópica. Não é automaticamente trabalho de um equipamento real. |
| 77 | Transferência infinitesimal de um componente f→g em conjunto fechado, T,p fixas e hipóteses da ficha: dG=(μg−μf)dn. Diferença 1 J/mol e dn=0,001 mol dão 0,001 J; fases presentes em equilíbrio com troca permitida exigem μg=μf, sem provar estabilidade global apenas por igualdade. |
| 78 | Gás ideal de composição fixa com cp(T) variável: ∫cp(T)/T dT−R ln(p₂/p₁). cp=0,8+0,001T kJ/(kg K), 300→400 K e mesma pressão dão 0,8 ln(4/3)+0,1≈0,33014566 kJ/(kg K); coeficiente de T tem unidade kJ/(kg K²). |

## Fontes e limitações

[MIT, reversibilidade e entropia](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_7.htm); [Stanford, tese sobre exergia, apêndice A.3](https://web.stanford.edu/group/peec/cgi-bin/docs/systems/research/AdamPSimpson_PhDThesis_Final_Draft.pdf), relação de Gouy–Stodola; [MIT, equilíbrio de fases e potencial químico](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/b312114e4e885b69b5746dcad660cc4f_lec_18.pdf), p. 1. Fontes consultadas em 30/10/2026 e não fonte dos números sintéticos. A fonte OSTI citada na entrega r9 retornou 502 nesta tentativa; não se infere falha universal e utiliza-se aqui a fonte de Stanford acessível.

Não identifiquei divergência neste recorte. Solicita-se Auditor distinto para confrontar fotos, MathML, hipóteses, fontes e cálculos, especialmente 67, 73 e 77. Não houve navegador real, leitor de tela, alunos, revisão humana ou certificação externa; demais fórmulas, figuras e destinos não são automaticamente validados.
