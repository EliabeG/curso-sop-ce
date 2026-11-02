# QA-09 — auditoria independente EX-041–046, EX-048 e EX-050

Data: 30/10/2026. Revisor automatizado independente `/root/qa_oficina`. **Veredito: APROVADO no alcance dos oito blocos e modelos examinados**. EX-047 e EX-049 não foram reexaminados neste parecer; QA-09 integral e a passagem ao próximo ID permanecem bloqueados.

## Identidade e limite

Examinei `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`, e inventário r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. As oito ocorrências são identificadas individualmente no resultado do Corretor por seção, posição UTF-16 e hash bruto. Comparei cada fragmento extraído da fotografia com o hash do inventário; as correspondências estão em `resultado.json`. Números de posição não são duráveis sob edição. Nessa mesma fotografia eu havia produzido antes da entrega deste Corretor um recálculo independente que abrange esses oito blocos: `auditoria/termodinamica/evidencias/QA-09/laboratorio-oficina-amostra-20261030/entrega.md`, script `verificar.py` SHA-256 `c403760df81815a395ab8486669170911ce0aca5f721912d9e31b9086ff21c18`. Reexaminei os textos e as hipóteses no contexto da aula para este parecer. O relatório do Corretor não foi minha única fonte de cálculos.

## Contas e hipóteses

- **EX-041:** fluxo Fourier `−5×(−30)=+150 W/m²`; a área de 2 m² com fluxo uniforme dá `300 W`. Sinal positivo é na direção +x.
- **EX-042:** `400×8×25=80 kW`; `300×8×25=60 kW`, queda de 25%. A comparação mantém área e diferença média efetiva, que podem mudar num equipamento real.
- **EX-043:** resistências comuns `0,002` e `0,001 m²·K/W` resultam em `U₁=500` e `U₂=333,333… W/(m²·K)`; relação de taxas `2/3` para mesma área e diferença média. Base em série sob modelo plano indicado.
- **EX-044:** razão de emissividades `0,30/0,60=0,5` reduz pela metade a parcela radiativa com temperaturas, área e geometria fixas e diferença radiativa não nula, para superfície pequena cinza com grande entorno aproximadamente negro. Outras perdas não estão incluídas.
- **EX-045:** `10×10⁻⁶×10×80=0,008 m=8 mm` para dilatação livre, aquecimento uniforme e coeficiente aproximadamente constante; não calcula tensão de restrição.
- **EX-046:** bloco `V=3×2×1=6 m³`; apenas face `A=3×2=6 m²`; `Q̇ger=200×6=1200 W`, `ΔT=1200/(20×6)=10 K`, `Ts=30 °C`. Balanço estacionário com as demais faces isoladas e ausência das outras perdas explicitadas na aula.
- **EX-048:** `150(0,30−0,10)=30 kJ` para pressão externa constante; `[(200+100)/2](0,30−0,10)=30 kJ` para variação linear quase estática. `kPa·m³=kJ`; a coincidência não faz W ser propriedade de estado.
- **EX-050:** `QL=1000−600=400 kJ`, `η=600/1000=0,60`, limite `1−300/600=0,50`, `Sger=400/300−1000/600=−1/3≈−0,333 kJ/K`. O ciclo entre as duas fontes não atende a segunda lei, mesmo com energia conservada. O erro de arredondamento é inferior a `0,0005 kJ/K`.

Os resultados são nominais e condicionados às hipóteses, sem precisão de instrumentos fornecida. A referência de trabalho de fronteira [OpenStax 3.2](https://openstax.org/books/university-physics-volume-2/pages/3-2-work-heat-and-internal-energy) e o limite de [Carnot/OpenStax 4.5](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle) sustentam os modelos examinados; [DOE, handbook vol. 2](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf) é referência de condução e trocadores, não fonte dos números didáticos. Os exemplos usam dados criados para treino.

Inspecionei `conferir.py` e executei em saída temporária: o resultado reproduz semanticamente o JSON registrado. O teste checa identidade e contas, mas não lê automaticamente os dados semânticos nem substitui análise dos trechos. A análise de figuras e objetos ancestrais como ocorrências separadas segue pendente.

| Critério da amostra | Resultado |
|---|---|
| Correspondência dos oito fragmentos com a versão identificada | Atendido; posição, seção e hash conferem. |
| Unidades, hipótese e valores nos blocos | Atendido no modelo e com os limites descritos. |
| Reprodução e fontes | Atendido na extensão de aritmética, identidade e modelos citados; não há validação experimental. |
| QA-09 integral e próximo ID | Não atendido nesta amostra; seguem pendentes e bloqueados. |

Nenhum ajuste obrigatório identificado neste alcance. Não houve teste de navegador, revisão humana, ensaio com estudantes ou certificação externa.

## SHA-256

- Relatório do Corretor: `216ad31dde8a98e51a3817c192bdbf9c3e4edbeaa6b88b10a509ada4c58c947c`.
- Resultado: `37970162c9173506ad2597665d2d37fae037c5493001b2bf11f306a4e32f933b`.
- Script: `9e1c9e6a9de05bcdfeb7cb4de5dfaa90eeefa3294fe40d608e3c9f1997355ed6`.
