# QA-09 — parecer independente das candidatas de pressão e entalpia

Data: 30/10/2026. Auditor automatizado `/root/next_formulas`, independente do Corretor `/root/next_theory`. **Veredito: APROVADAS as duas propostas isoladas no alcance examinado**; não estão aplicadas e não aprovam QA-09, nem liberam o próximo ID.

## Escopo e identidade

O critério integral QA-09 exige conferência do conteúdo numérico além das questões, incluindo explicações. Este parecer examina somente os dois fragmentos propostos em combustão e vaporização, seus pressupostos e vínculos; sua aplicação efetiva e o restante do curso continuam pendentes.

- Aula r9 SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`.
- [Entrega](../evidencias/QA-09/teoria-pressao-entalpia-r9-20261030/entrega.md) SHA-256 `28ceea6e676adb05ff22070957d7def8df9703fae4f80306e84d55b6e3ff43fb`; manifesto SHA-256 `02c70956250a209aae22d4fc0a46d13ee33e4f61a8d2ba8c10d0817214cd98e0`; verificador SHA-256 `eb9f61a00531617acbb99707452d96e248483ed3fdfe26eb4fffedb9b99d5621`.
- Combustão: posição UTF-16 199954–200230; original SHA `6b0690f2cc7a68ed2c8d7d98d96cb65a3ffbb96d1e2f8f252c4fda062cac5d9e`; candidata `8de3b4d51c7ee7b3c55b4379526741a86a95f4ce14f5ca00fe0ad178a1c53bb5`.
- Vaporização: posição UTF-16 405901–406892; original SHA `f54d7722c520f14cf734a7308366e8efe9c15c2954e7aa2727a8fbc2f95ad5d3`; candidata `04d26bdf44bfacbbaceff77f777a94f9b9ae8eaf825fb518f0dcec2ccaafc45a`.

Os hashes de fragmentos excluem a quebra de linha final dos arquivos isolados. Reconstituí por comandos independentes a ocorrência única, as posições, hashes e substituições literais em ambos os elementos; cada candidata resulta do delta declarado. O verificador do Corretor foi inspecionado e executado sem gravar produto: passou. Não houve aplicação ao HTML.

## Mérito científico e limites

No sistema fechado, sem variações relevantes de energia cinética/potencial, a primeira lei estabelece `Q=ΔU+Wb` quando não há outros trabalhos. Se os estados delimitados usam a mesma pressão p na entalpia e `Wb=p(V₂−V₁)`, então `Q=ΔU+pΔV=ΔH`. A candidata de combustão enuncia pressão termodinâmica constante, apenas trabalho de fronteira e identidade de pressões; a candidata de vaporização explicita pressão termodinâmica constante e o trabalho pΔV. Ambas são suficientes para a redução apresentada sem afirmar que reversibilidade é universalmente necessária. As restrições não alteram massa ou estequiometria da reação e não excluem reações; para mudança de fase, `ΔH=m(hg−hf)` usa a mesma massa de substância pura entre os estados saturados.

O contraste da entrega é aritmético: p dos estados 100 kPa, ΔV=1 m³, ΔU=400 kJ e Wb=80 kJ dão ΔH=500 kJ e Q=480 kJ. Esse contraste identifica a necessidade da igualdade entre pΔV e Wb; **não constitui por si só trajetória física validada com pressão termodinâmica uniforme constante**. Uma condição suficiente usual é processo isobárico quase estático. A formulação proposta também abrange qualquer processo cujo trabalho satisfaça explicitamente a identidade exigida.

Para vaporizador em escoamento permanente, o texto preservado diferencia massa fechada do volume de controle: com mesma vazão de entrada e saída, termos cinético/potencial desprezíveis e sem trabalho de eixo ou elétrico não associado ao escoamento, `Q̇=ṁ(hg−hf)`. Se houver resistência elétrica dentro da fronteira, `Q̇−Ẇnão-fluxo=ṁhfg`, trabalho saindo positivo; sistema externamente adiabático pode receber trabalho elétrico. O texto não transforma essa interação em calor através da fronteira.

Comparei a candidata da [ficha 40](../evidencias/QA-09/candidatas-fichas-40-67-r9-20261030/40-candidata.html): ela exige as mesmas condições de p e Wb. A concordância é conceitual entre **propostas**, não prova de que tenham sido aplicadas em conjunto nem revalidação da ficha ou do arquivo efetivo. Qualquer aplicação deve reconciliar o vínculo de retomada e versões.

Confrontei [MIT, derivação de Q=ΔH no caso reversível isobárico e trabalho pV](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html) e [MIT, trabalho quase estático](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html). A primeira mostra um caso suficiente; a generalização explicitada para qualquer trajetória com `Wb=pΔV` segue do balanço, sem extrapolar a fonte para afirmar reversibilidade necessária.

| Critério localizado | Resultado |
|---|---|
| Identidade e delta das candidatas | Atendidos na fotografia r9. |
| Condições para Q=ΔH e unidades | Atendidas nas duas propostas, no domínio descrito. |
| Massa fechada, fase e escoamento permanente | Distintos; texto de escoamento preservado. |
| Compatibilidade com candidata da ficha 40 | Conceitualmente compatível; aplicação e vínculo efetivo pendentes. |
| Versão aplicada e QA-09 integral | Não examinados; bloqueados até entrega e auditoria posteriores. |

Não houve ensaio em navegador, revisão humana, piloto com estudantes ou certificação externa. A aplicação requer nova fotografia/mapa, preservação dos 197 artigos e reavaliação dos aceites afetados; este parecer não substitui a auditoria da versão efetivamente alterada.
