# QA-09 — auditoria independente dos exemplos 001–005 e diagnósticos 26–28 em r9

Data: 30/10/2026. Revisor: agente automatizado independente `/root/next_graphics`. **Veredito: APROVADO exclusivamente no alcance localizado abaixo.** Não se aprova QA-09 integral, não se libera o próximo ID e não se atribui revisão humana ou aprendizagem demonstrada.

## Critério e versão

QA-09 exige inventário e recálculo de todo conteúdo numérico, incluindo exemplos, oficinas, diagnósticos, fichas, figuras e explicações, com referência verificável e resultado conferido. A presente revisão examina oito blocos, seus enunciados, bases de hipóteses e números descritos na entrega; não abrange as demais ocorrências, todos os nós subordinados como objetos separados, apresentação dinâmica ou o curso inteiro.

- Aula `modulos/e1-termodinamica.html` SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; inventário `inventario-r9.json` SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`.
- Entrega do Corretor: `auditoria/termodinamica/evidencias/QA-09/exemplos001-005-diagnosticos26-28-r9-20261030/entrega.md`, SHA-256 `fb917cc55164f2803a5047e97c4a05c5b8c95ad37993681299d49c54273ef0f1`; verificador do Corretor SHA-256 `371edbd7a58df9e2e65b36a660a188bec6901200d0eba0173f3ddd118b77e6fe`.
- Verificador independente `auditoria/termodinamica/evidencias/QA-09/auditoria-exemplos001-005-diagnosticos26-28-r9/verificar.py`, SHA-256 `4ceda05715619e21f6660f6693ec1655eebd1ad859c44aa2e63597cd212fde0f`; execução passou. Reextrai os oito intervalos UTF-16 e seus hashes, confronta títulos e registros r9 e recalculei os valores usando frações exatas. Li diretamente os enunciados e as bases `base-medidas`, `base-instrumentos`, `base-gas-modelo`, `base-misturador-correntes` e `base-balanco-co2` da aula. Identificações e hashes individuais constam da entrega e da fonte do script independente.

## Conferência científica independente

1. **EX-001.** Para amostra homogênea dividida nas mesmas condições, base imediatamente anterior à caixa, 9/0,010 = 900 kg/m³ e 4,5/0,005 = 900 kg/m³. Massa, volume e energia total se reduzem à metade; a energia específica permanece sob a mesma condição. O resultado não se aplica a uma partição arbitrária não homogênea.
2. **EX-002.** A definição de alcance é limite superior menos inferior. Com limite −10 °C e span 120 °C, limite superior 110 °C. Intervalo 120 °C equivale em magnitude a 120 K; não se interpreta span como incerteza do instrumento.
3. **EX-003.** A base declara interpolação afim. `10 + (30−0)/(40−0) × (90−10) = 70`, consistente com o ganho 2. Não implica que as escalas tenham a mesma origem nem que um instrumento real esteja calibrado.
4. **EX-004.** Para mistura líquido–vapor de substância pura em equilíbrio, `x=(900−400)/(2400−400)=0,25`, logo 25% de vapor em massa. Entalpias pressupõem mesma referência; os valores fictícios não identificam fluido real e título não é fração de volume.
5. **EX-005.** `1×0,082×320/26,24 = 1 atm`, com as unidades dadas e a constante aproximada fornecida em `base-gas-modelo`. Recalculei com R = 8,31446261815324 J/(mol·K), 1 atm = 101325 Pa e V = 0,02624 m³: 1,000699586 atm, cerca de 0,070% maior. A diferença decorre de usar uma aproximação mais curta de R; não configura discrepância para os dados adotados.
6. **Diagnóstico 26.** O texto especifica todos os trabalhos e todo calor externo recebido na mesma base de massa, e uma única rejeição restante. `w=600+900−20=1480 kJ/kg`, `q_in=2400+800=3200 kJ/kg`, `η=1480/3200=46,25%` e `q_out=1720 kJ/kg`. O balanço não prova viabilidade de segunda lei sem temperaturas dos reservatórios.
7. **Diagnóstico 27.** Nas hipóteses da base do misturador (permanente, adiabático, sem trabalho e variações cinética/potencial desprezíveis, referências compatíveis), `y=(700−300)/(2300−300)=0,20`. De 10 kg/s, sobram 8 kg/s e a turbina posterior, nos limites do enunciado, fornece `8×250=2000 kW`.
8. **Diagnóstico 28.** No modelo diluído, bem misturado, com volume e densidade aproximadamente constantes, fluxos equilibrados, mesma referência de condições e sem outras fontes/sumidouros, `dC_i/dt=[0,20+500(0,0004−0,0006)]/200=0,0005 h⁻¹ = 500 ppm/h` no instante inicial. O limite estacionário para condições mantidas é `400 + (0,20/500)×10⁶ = 800 ppm`; não é condição instantânea nem a taxa fica constante durante o transiente.

As igualdades são para dados nominais e o modelo da aula; dados de incerteza experimental não foram fornecidos. Não há alegação de substância real ou validação de edifício.

## Referências e decisão

Verifiquei o [DOE Fundamentals Handbook, p. 34](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf) para a definição mássica do título e a [EPA APEX v5.2 vol. II, §8.2.2](https://www.epa.gov/sites/default/files/2019-12/documents/apex52_usersguide_vol2_october2019.pdf) para o modelo de volume bem misturado com balanço de espécie. A [tabela NIST CODATA 2022](https://physics.nist.gov/cuu/Constants/Table/allascii.txt) confirma a constante molar dos gases e o [NIST SP 811, capítulo 8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8) trata unidades SI; dados dos exercícios são autorais. A URL inicial NIST da entrega retornou erro na auditoria e foi substituída pelo Corretor antes do parecer; confirmei a tabela e o hash final da entrega.

| Critério localizado | Decisão |
|---|---|
| Identidade dos oito fragmentos na versão r9 | Atendido: offsets, hashes e contexto conferidos. |
| Dados, unidades, contas e hipóteses | Atendido para os modelos e limites acima. |
| Fontes de modelo e referência da constante | Atendido no escopo descrito; valores fictícios não atribuídos a fontes externas. |
| Critério integral QA-09 e liberação do próximo ID | Não atendido: restante do inventário e recálculo permanece pendente. |

**APROVADO apenas para os oito blocos e alcance explicitado.** Uma mudança posterior no conteúdo, contexto ou fonte exige reconciliação e reavaliação, sem transferência automática. Não houve navegador, leitor de tela, teste com estudantes, revisão humana ou certificação externa nesta revisão.
