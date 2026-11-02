# QA-09 — reexame de EX-031–040 na r27 e achado adicional EX-028

30/10/2026. Responsável `/root/next_examples`. **Reexame técnico localizado; aguarda auditor distinto antes de integração.** Fui também autor da reconciliação r18 deste lote, posteriormente auditada por `/root/planning` em `QA-09-exemplos-031-040-r18-auditoria-independente-20261030.md`; portanto não apresento este trabalho como auditoria independente da minha própria entrega anterior. Recalculei a fotografia r27 e confrontei os modelos, sem transferir aceite automático. Produto e controles não alterados.

## Identidades e rastreio

Aula r27 SHA `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; inventário `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`. Fotografia r18 `7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca`; inventário `717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc`. O verificador somente leitura `auditoria/termodinamica/evidencias/QA-09/exemplos-r28-031-040-r27-next-examples-20261030/verificar.mjs`, SHA `477fcabd2902f986c060bc0707cb1ee0dce958eb80236997741baf83a85aa165`, reextrai os dez exemplos por seção e hash do registro r18, verifica offsets, contêineres e contas. Sua saída preservada `resultado.json` SHA `71e3367e7c378f579270fd29e65e73e970e6ad76ed7800580f0280e30322804f` registra as duas identidades. Todos os dez trechos e seus contêineres imediatos são idênticos em r18/r27; isso confirma identidade, não a validade automática do modelo ou de dependências externas.

## Modelos e recálculo

- **031:** mesmo kg, sem extração, permanente, turbinas e bomba adiabáticas, caldeira/reaquecedor/condensador sem trabalho não-fluxo e ΔEc/ΔEp desprezíveis: turbinas 1600, bomba 10, entrada térmica 3590 e rejeição 2000 kJ/kg; Wlíq=1590 e η≈44,29%. A base adverte que os dados didáticos não provam estados fisicamente realizáveis nem satisfazem automaticamente a segunda lei.
- **032:** aquecedor aberto permanente e adiabático sem trabalho, duas entradas e uma saída, h compatíveis: y=(500−210)/(2700−210)=29/249≈0,11646586. Fração extraída ≈11,65% e restante ≈88,35%. A verificação com y exato dá 500; substituir o arredondado 0,1165 dá 500,085. O texto declara y=290/2490≈0,1165, portanto a igualdade para y exato é correta; é possível reforçar que a verificação utiliza o valor não arredondado, sem classificá-la como erro aritmético.
- **033:** referência à sucção e ao mesmo ciclo: 3,5/5=0,70. Eficiência volumétrica não é eficiência isentrópica.
- **034:** carga útil 20 kW, efeito refrigerante didático 1000 kJ/kg → 0,020 kg/s; número não validado como propriedade real da amônia.
- **035:** 16×250 mL/min=0,24 m³/h e excesso 400 ppm=0,0004; vazão exterior 600 m³/h. Usa zona única, CO₂ diluído, regime estacionário e bases volumétricas coerentes, não padrão normativo.
- **036:** 0,20/500=0,0004=400 ppm, somados a 450 ppm exteriores → 850 ppm, na mesma hipótese de zona estacionária.
- **037:** 54 m³/h=0,015 m³/s, Ph=1000×10×0,015×20=3000 W, ηb=3000/5000=0,60; H é carga total e eficiência não inclui motor.
- **038:** (230−200)/(300−200)=0,30; h≈2800+0,30×200=2860 kJ/kg. Tabela sintética, mesma pressão e região de fase; interpolação não fornece erro experimental.
- **039:** duas correntes de 1 kg/s, permanente e sem calor externo: Ṡger=−0,20+0,30=0,10 kW/K. Calor entre correntes não é calor através da fronteira total. Os dados isolados de entropia não validam todos os estados e o balanço energético.
- **040:** mesmo gás ideal, dois estágios adiabáticos de vazões e eficiências constantes iguais, sem perdas de pressão ou separação, resfriamento de volta a T1: pi=√(1×16)=4 bar absolutos e razões 4/4. Mudanças de eficiência, temperatura ou perdas podem alterar o ótimo do sistema real.

## EX-028: fronteira do trabalho

A leitura adicional de EX-028 r27 identificou ambiguidade localizada: “retira 600 kJ consumindo 200 kJ de trabalho” não explicita se 200 é entrada bruta ou trabalho líquido total na fronteira, embora a base de ciclo simples permita a interpretação do cálculo apresentado. Se 200 forem entrada bruta com outra saída de trabalho de 20 kJ, o líquido é 180, COPR≈3,333 e QH=780; temperaturas de reservatórios 300/350 K dariam Sger≈0,22857 kJ/K, logo os balanços do contramodelo são consistentes. Isso não prova falha do cálculo sob o modelo pretendido, mas sustenta proposta de explicitação local. Candidata isolada `auditoria/termodinamica/evidencias/QA-09/exemplos-r28-candidata-ex028-r27-next-examples-20261030/analise.md` SHA `c3e0759b373967428b7a45c75bde0fc2fdd9f65fc628bbf4dd56a8c9fe110a01`; manifesto `131ab1c9901cbbc991d84e293f915dd0a37bc2feba9bd5966bc2bac2138b037e`. Solicita-se Auditor distinto para julgar a necessidade e a candidata antes de aplicação.

## Fontes e limites

Foram consultados diretamente em 30/10/2026 [MIT, primeira lei em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm), [NIST, balanço de CO₂ em zona única](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=934011), [DOE, bombas](https://www.energy.gov/sites/default/files/2014/05/f16/pump.pdf), [Texas A&M, compressão em dois estágios](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/720949b2-1bd4-4884-9025-d39f685f11a5/content) e [MIT, ciclos inversos](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node25.html). Nenhuma é fonte dos dados sintéticos. Não foram revalidados visualmente figuras, navegação, leitor de tela, alunos ou fontes completas; não há revisão humana ou certificação externa de nível AAA.
