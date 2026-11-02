# QA-09 — recálculo localizado de fundamentos FUN-01/FUN-02

Data: 30/10/2026. Corretor automatizado `/root/qa_teoria`. **Lote preparado, pendente de Auditor independente.** Não libera próximo ID, nem reaprova automaticamente FUN-01/02, nem demonstra conclusão de QA-09. Os 17 trechos são explicações e preparações fora dos artigos de questões; não equivalem a cobertura integral de suas seções. Nenhum HTML ou arquivo histórico foi alterado por este lote. Alguns dados pedagógicos são os mesmos da unidade já aceita, mas este registro examina sua apresentação textual para QA-09, sem transferir automaticamente parecer anterior.

Fonte `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. As posições abaixo são UTF-16 de elementos `texto_direto` na fotografia, não IDs permanentes. Reconstruir como `modulos/e1-termodinamica.html:<posição>:texto`, consultando seção e hash da tabela final. O hash do campo corresponde ao texto bruto direto e não necessariamente ao texto visível total. Valores didáticos são nominais; cálculos sem arredondamento demonstrados com os dígitos fornecidos, não inferem precisão de instrumentos ou de tabelas. Limites de unidades e de modelos seguem cada linha.

| Posição | Recálculo e condições |
|---|---|
| 91881 | 0,012/4=0,003 m³/kg; ao dobrar massa e volume a razão permanece. Fração molar de A=3/(3+2)=0,60, não fração mássica. 1 cm³/g = 10⁻⁶/10⁻³ = 0,001 m³/kg. |
| 92203 | 12±3 com erro máximo significa intervalo [9,15], inclusive extremidades; 9 contradiz garantia de valor >10. Não há distribuição probabilística declarada. |
| 96357 | Para A⇌2B, ΔᵣG=2μB−μA=2×3−6=0 kJ por mol de extensão. Estacionariedade sob T,p fixos e reação permitida não demonstra estabilidade por si só. |
| 101326 | Regra F=C−P+2: (C,P)=(1,1)→2; (1,2)→1; (1,3)→0. Trata intensivos das fases em equilíbrio no modelo sem outras restrições; não determina as proporções das fases. |
| 102086 | A 0,10 MPa, NIST Table 2 lista 99,606 °C, hₗ=417,50, hᵥ=2674,9 kJ/kg e vₗ=1,04315, vᵥ=1693,9 cm³/g. Multiplicados por 0,001, vₗ=0,00104315 e vᵥ=1,6939 m³/kg. Para título mássico 0,20, v=0,33961452 m³/kg e h=868,98 kJ/kg a partir desses números arredondados. O número de casas resultante não representa precisão adicional. |
| 102479 | Regra F=2−2+2=2 para binária bifásica, nas hipóteses da unidade. Fração molar de vapor β e composições líquida/vapor usam bases molares; isso não é automaticamente título mássico. **Achado aberto:** a aula afirma incorretamente que só na substância pura β e título coincidem; massas molares médias iguais ou limites de fase única também permitem coincidência. A [candidata isolada](../candidata-fracao-molar-massica-20261030/analise.md) aguarda revisão e não foi aplicada. |
| 105052 | Modelo Raoult/Dalton ideal: para pressões de saturação 400 e 100 kPa, zA=0,25 → 0,25×400+0,75×100=175 kPa; zA=0,75 → 0,75×400+0,25×100=325 kPa. Dados fictícios, não tabela real. |
| 105534 | IAPWS R7-97(2012), §3, informa Tcr=647,096 K e pcr=22,064 MPa. A unidade do curso define supercrítico estritamente como T>Tcr e p>pcr. |
| 108659 | No modelo ideal à mesma T, 80×0,250=160×0,125=20 kPa; ln(1)=0 e ΔμA=0. Para mistura binária, pB são 80−20=60 e 160−20=140 kPa. A igualdade só de A não garante equilíbrio de B. |
| 114112 | 250 kg/m³×0,004 m³/kg=1; ρ=1/v logo o par é redundante para a mesma amostra e instante, não duas propriedades independentes. |
| 235496 | 80 kPa×0,006 m³ =0,480 kPa·m³=0,480 kJ; 1 Pa·m³=1 J. |
| 236866 | Para f=θν, ∂f/∂θ|ν=ν; na curva ν=θ², f=θ³ e df/dθ=3θ². A diferença 2θ² decorre de θ(dν/dθ), não de defeito da derivada parcial. |
| 239213 | Em ω=(−y dx+x dy)/(x²+y²), sobre x=cos t, y=sen t, o denominador é 1 e o numerador é (sen²t+cos²t)dt=dt; de 0 a 2π, ∮ω=2π. O domínio exclui a origem; derivadas cruzadas iguais não garantem potencial global em domínio com furo. |
| 239807 | Φ=θ³+θν: ∂Φ/∂θ=3θ²+ν e ∂Φ/∂ν=θ; derivadas cruzadas valem 1. No quadrante θ,ν>0, a forma descrita é exata. |
| 244208 | p(V)=p₀[1+2(V−V₀)/V₀]: p(1,5V₀)=2p₀. Integral na trajetória linear ou trapézio: W=(p₀+2p₀)/2×0,5V₀=0,75p₀V₀; usar p₀ constante daria 0,50p₀V₀. Válido como trabalho de fronteira em processo mecanicamente quase estático. |
| 249892 | Primitiva de ln x é x ln x−x para x>0; F(e)=0 e F(1)=−1, logo ∫₁ᵉ ln x dx=1. Argumentos dos logaritmos são adimensionais. |
| 251114 | Com ζ=T/(400 K), dζ/dT=1/(400 K); 240 J/mol por ζ dividido por 400 K =0,600 J/(mol·K), mantendo as demais coordenadas indicadas. |

Conferência de fonte: [NISTIR 5078, Table 2, p. 11](https://www.nist.gov/document/nistir5078-tab2pdf), linha 0,10 MPa; [IAPWS R7-97(2012), §3, p. 5](https://iapws.org/technical-guidance/release/IF97-Rev.download). Ambos consultados em 30/10/2026. Os demais dados quantitativos são do próprio enunciado e os modelos/condições estão no texto E1; a checagem numérica não constitui validação independente dos modelos físicos gerais.

Reprodução, pela raiz: `python3 auditoria/termodinamica/evidencias/QA-09/teoria-fundamentos-lote-2-20261030/verificar.py`. O script confirmou hashes dos dois arquivos, marcadores e posição dos 17 trechos, mais contas numéricas com frações exatas e a integral de ln numericamente; não reimplementa o gerador do hash de cada fragmento, não prova as derivações simbólicas nem verifica textos fora do lote. A inspeção e revisão científica independente ainda são necessárias. Alteração futura do HTML invalida a fotografia e exige reconciliação; nenhum teste com estudantes ou navegador foi feito.

## Identidades no inventário r7

| Posição UTF-16 | Seção | SHA-256 do campo `sha256_fragmento` do r7 |
|---:|---|---|
| 91881 | fun01-estado-equilibrio | `fad96cafcf88f056ff0a4e69d8fec891c08f407b953c0e692a0f3d69339aa915` |
| 92203 | fun01-estado-equilibrio | `965917bf4caf720957a9b406c4aecac6a7f7717cfe43e6293434c8f217388b5f` |
| 96357 | fun01-estado-equilibrio | `fea165532faadff44f4a29e76bc0daff6f7054b275cf607fedb20c793ed05314` |
| 101326 | fun01-estado-equilibrio | `7ff9c9769f7acbd491ac26b2270f81e0b13f59b4292ec4e111787e4251674d9d` |
| 102086 | fun01-estado-equilibrio | `681bee416847a9eebe2f7e7b8b70e366fe77c1e1699ecc87e256c24670922fe4` |
| 102479 | fun01-estado-equilibrio | `1d15dea75bd4e687abb16e7876566a8501413ea3797640c4fca0eb3402945508` |
| 105052 | fun01-estado-equilibrio | `6388e81079087cf2f378761bfca7a28f20fafc5a9760cef081fd56387e3eec11` |
| 105534 | fun01-estado-equilibrio | `34a8181ae2f69e502d28b0d52df65b602fbe7f5490d8432d499781e7ae1b08a7` |
| 108659 | fun01-preparacao-equilibrio | `d7035a6ada3765be275f56a31c02e851224fa769333e379b3f5e507d91e6e2ca` |
| 114112 | fun01-estado-equilibrio | `83069e3d23f6c8e2a5f1f1d98cdf4df71e23980a0aa6ef3ef192bec67097f6e4` |
| 235496 | fun02-diferenciais-caminhos | `de8df1a18ab0581005e9940f626857fa8400f4dce945ff5597acdb073129d06d` |
| 236866 | fun02-diferenciais-caminhos | `a2426e201bf80fdb04aed93aca9559473c97ebbb1007078e956eda60ae9b1cc3` |
| 239213 | fun02-diferenciais-caminhos | `52a5b10e05842451b785b911a1305be47c5ad730c309468f5c9648528d0fc7ac` |
| 239807 | fun02-diferenciais-caminhos | `742084c7aa28a2ba22b3a80e677162eb7e69ba511b9bae0f84ffa15de8755ea7` |
| 244208 | fun02-diferenciais-caminhos | `310f5bf948ec5293a61d33ad645456a3749ac6eeaf6111d15612a01e4f73f05e` |
| 249892 | fun02-preparacao-integrabilidade | `e15804e0d38e377e56bcc4fd9f5c9f50ba08d8a4726d63efd85be02fdeb78f3c` |
| 251114 | fun02-preparacao-integrabilidade | `d6b58dbce947930a0198604e9f61bcdaf214f44b9c3f41f57853187ce3226d74` |
