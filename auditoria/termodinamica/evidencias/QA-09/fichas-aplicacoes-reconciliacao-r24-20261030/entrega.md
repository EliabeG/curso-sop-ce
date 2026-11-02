# QA-09 — reconciliação das fichas de aplicações na r24

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente.** Recorte 87, 88, 91–95 e 97–100: fichas já examinadas na r12; 88/99 foram corrigidas na r13. Esta é revalidação na versão atual, não lote inédito ou aceite global. Produto não alterado; QA-09 aberto.

## Versões e método

Formulário r24 SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`, aula r24 `2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9`, inventário r24 `469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf`. Fotos do formulário r12 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756` e r13 `5f3f31a4801f96a2b78b40c75d37392f6b16d264901ac313ac00458901970285`: nove artigos r24 idênticos aos r12; 88/99 mudaram na r13; todos 11 coincidem com r13. Parecer de fichas r12 SHA `00e27bc4d916f5d7a6446e98ca07e6256c4e82d6cc1bc6cbd6fa35ba8ea4b316`; parecer da aplicação r13 SHA `79db2c1bfcd63971af7d5571fb726f415ab43a32e2c7d4e74b10ea925f1ecad1`. Os contextos e outras fichas não são automaticamente aceitos por igualdade de fragmentos.

`identidades.json` SHA `99776869f5b9c168d3990735290e12626fe49c5ecfab6c29862f0aca2cfd72c4` registra IDs, hashes e intervalos UTF-16. `verificar.mjs` SHA `7a7187af4e533071f73d62241d2ce86000dcf35b6cd19e839ba8bb2962c9c298` executa `node auditoria/termodinamica/evidencias/QA-09/fichas-aplicacoes-reconciliacao-r24-20261030/verificar.mjs`, confirmou fotos, 11 destinos existentes e contas (`ok=true`); somente leitura, sem interpretação automática de MathML ou hipótese. A existência de âncora não prova navegação nem revisão integral do destino. Valores seguintes são fictícios, não medições.

## Relações e pressupostos

| Ficha | Revisão |
|---|---|
| 87 | Eficiência volumétrica é volume fresco admitido referido às condições de sucção dividido pelo volume deslocado na mesma base e ciclo. 0,8/1=0,8; vazões equivalentes devem representar médias coerentes no mesmo período, não valores instantâneos arbitrários. Não é eficiência isentrópica. |
| 88 | Dois estágios adiabáticos estacionários de mesmo gás ideal, cp/cv constantes, mesma eficiência isentrópica constante, mesma vazão, sem mudança de fase, intercooler sem perda até T₁ e ΔEc/ΔEp desprezíveis. Para pressões absolutas 1 e 16 bar, pi=√(1×16)=4 bar e razão 4 em cada estágio. O ótimo de trabalho do modelo não inclui perdas e auxiliares do sistema real. |
| 91–93 | Fourier 1D q″x=−kt dT/dx: kt=2 W/(m K), gradiente −10 K/m dão +20 W/m² e, uniforme em 3 m², +60 W. Parede plana estacionária sem geração, k constante: kt=2, A=3, ΔT=50 K e L=0,5 m dão 600 W. Convecção com h=10 W/(m² K), A=2 m² e Ts−T∞=30 K dá 600 W da superfície ao fluido. Sinal e unidades são essenciais. |
| 94–95 | Para arranjo e perfis apropriados, U constante e mesma área de referência, Q̇=UA FΔTlm. Com U=200, A=10, F=0,8 e ΔTlm=25 K, Q̇=40000 W. Para parede plana 1D sem geração, resistências por área 1/100+0,02/2+1/200+0,001=0,026 m² K/W dão U=500/13≈38,462 W/(m² K). Resistências cilíndricas exigem geometria e áreas próprias. |
| 97 | No modelo da ficha 96 de corpo cinza pequeno perante entorno grande negro, com mesmas temperaturas, área/geometria e perda inicial não nula, ε₂/ε₁=0,8/0,4=2 é a razão das taxas radiativas. Não se estende automaticamente a superfícies com reflexões mútuas arbitrárias. |
| 98 | Dilatação livre aproximada e uniforme com α constante e |αΔT|≪1: α=12×10⁻⁶ K⁻¹, L₀=2 m, ΔT=50 K dão ΔL=0,0012 m. Não calcula tensões com restrição mecânica. |
| 99 | Balanço **térmico** permanente, geração total q‴ uniforme ou média, única perda convectiva relevante e nenhuma entrada independente não incluída em q‴. q‴=100000 W/m³, V=0,01 m³ e hA=10×2 W/K dão Ts−T∞=50 K. Geração pode representar conversão de energia suprida através da fronteira, por exemplo entrada elétrica que integralmente se converte em q‴V; não se somam duas vezes a entrada e sua conversão. A ficha não afirma que um sistema isolado gera energia continuamente. |
| 100 | Bloco 2×3×0,5 m tem V=3 m³ e face 2×3 m tem A=6 m²; profundidade entra no volume, não na face. |

## Fontes e pedido de revisão

[DOE, guia de ar comprimido](https://www1.eere.energy.gov/manufacturing/tech_assistance/pdfs/compressed_air_sourcebook.pdf), glossário de eficiência volumétrica; [Texas A&M, estudo de compressão em dois estágios](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/720949b2-1bd4-4884-9025-d39f685f11a5/content), limite do ótimo; [MIT, folha de relações de transferência de calor](https://ocw.mit.edu/courses/2-051-introduction-to-heat-transfer-fall-2015/e32f70f7e00f34953447b606cea0421f_MIT2_051F15_EqnSheet_Q2_v3.pdf); [NIST, métodos de medição de expansão térmica](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication960-11.pdf). A ficha 96 e a constante radiativa tiveram outro lote; aqui 97 é examinada apenas no modelo referenciado. As fontes não fornecem os números sintéticos.

Solicita-se Auditor distinto para identidade, MathML, fontes, cálculos e sobretudo fronteira energética da 99, sem assumir que fonte térmica é energia criada ou uma segunda entrada. Não houve navegador real, leitor de tela, alunos, revisão humana ou certificação externa; destinos e demais fichas não recebem aceite integral.
