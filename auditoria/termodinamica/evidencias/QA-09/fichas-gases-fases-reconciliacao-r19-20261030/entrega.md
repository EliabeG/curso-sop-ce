# QA-09 — reconciliação de fichas de gases e fases na r19

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente.** As fichas 13–18 e 20–22 já haviam recebido exame de relações e parecer na r9; esta é uma reconciliação e nova revisão localizada, não um lote histórico inédito. O levantamento de lotes anteriores identifica todas as fichas por número em algum recorte, mas isso não estabelece aceite integral ou cobertura uniforme. Não se alterou produto nem se encerrou QA-09.

## Fotografia, identidade e vínculos

Formulário r19 SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`, aula r19 `9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65`, inventário r19 `ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f`. Formulário r9 preservado `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`. Os nove artigos são byte a byte idênticos; identidades r9/r19 e offsets UTF-16 estão em `identidades.json` SHA `93eee99a4326cbd56695226d7a79c6f2b84b15a0c73ea627fa5c1455174488fc`. Parecer anterior `QA-09-fichas-gases-fases-r9-auditoria-independente-20261030.md` SHA `5df2181f6b56d634a5fa226b6ab0cd2f16dcb8fe173abac0540d75f2fdc2dd3c`. Identidade do cartão não transfere automaticamente conclusões para contexto, recursos, outras versões ou a seção toda.

`verificar.mjs` SHA `7ecbbdeea3764cae3d670c8721ce62d01c408a7742444a717a78c86b0948d860` lê ambos os cartões, confere hashes, unicidade dos nove destinos de retomada na aula r19 e reproduz as contas; executado da raiz com `node auditoria/termodinamica/evidencias/QA-09/fichas-gases-fases-reconciliacao-r19-20261030/verificar.mjs` retornou `ok=true`. Não interpreta MathML nem prova adequação pedagógica do destino. Li os quatro destinos: 13–16 apontam a `#base-gas-modelo`, 17–18 a `#base-gas-energia`, 20 a `#base-calor-variavel` e 21–22 à seção `#substancias`, onde o tema aparece; links a seção geral não são prova de foco exato no trecho. Os destinos não recebem aprovação integral por esta leitura.

## Expressões e testes

Valores abaixo são artificiais, não medições de fluidos reais.

| Fichas | Domínio e recálculo |
|---|---|
| 13 | Para gás ideal de composição fixa, pV=mRT=nRuT, pv=RT, p e T absolutos. Com m=1 kg, R=0,287 kJ/(kg K), T=300 K e V=0,861 m³, p=100 kPa. |
| 14–15 | Para mesma massa/composição ideal, pV/T constante entre estados. Para p₂=200 kPa e T₂=400 K, V₂=0,574 m³; isolando V, T ou p constantes obtêm-se as três relações do cartão. Não são restrições simultâneas. |
| 16 | Z=pv/(RT), adimensional; com p=90 kPa e demais dados anteriores, Z=0,9. A igualdade Z=1 num estado não assegura comportamento ideal global nem de derivadas. |
| 17–18 | Mesmo gás ideal: cp−cv=R, k=cp/cv; cp=1,005 e cv=0,718 dão k≈1,39972. Para capacidades constantes em ΔT=100 K, m=2 kg, Δu=71,8 kJ/kg, Δh=100,5 kJ/kg e ΔU=143,6 kJ. Não confundir temperatura absoluta com intervalo. |
| 20 | Gás ideal de composição fixa com capacidades variáveis exige integrar em T. Para cp(T)=0,8+0,001T kJ/(kg K), 300→400 K: Δh=115 kJ/kg. O coeficiente de T tem unidade kJ/(kg K²); não é valor de tabela. |
| 21–22 | Substância pura em equilíbrio líquido–vapor subcrítico, frações mássicas: x=mg/(mf+mg), y=(1−x)yf+xyg; inversão só para yg≠yf. Com mg=1 e mf=3 kg, x=0,25; hf=500, hg=2500 kJ/kg dão h=1000, vf=0,001 e vg=1 m³/kg dão v=0,25075. Não usar título como fração volumétrica ou além da região bifásica. |

Consultei [NASA Glenn, equação de estado](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/equation-of-state-ideal-gas-2/), [NIST, fator de compressibilidade](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir86-3057.pdf), [MIT, energia do gás ideal](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/mud/T6newmud.html) e [DOE, fundamentos de termodinâmica](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), capítulos de propriedades e saturação. Os dados sintéticos não provêm das fontes. A URL DOE utilizada aqui é a consultada nesta rodada, distinta do endereço antigo da entrega r9.

Solicita-se Auditor distinto para examinar versão, hipóteses, MathML, links e contas sem generalizar o parecer. Não houve navegador real, leitor de tela, alunos, revisão humana ou certificação externa.
