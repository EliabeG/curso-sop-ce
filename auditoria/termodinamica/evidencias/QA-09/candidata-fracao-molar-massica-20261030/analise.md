# QA-09 — candidata para conversão molar/mássica de vapor

Data: 30/10/2026. Proponente `/root/qa_teoria`, agente automatizado. **Candidata isolada, não aplicada e aguardando revisão independente.** Relacionada ao achado do parecer `QA-09-teoria-fundamentos-lote-2-auditoria-independente-20261030`, na posição r7 102479 da aula.

## Falha e contramodelo

A frase atual diz que as frações molar e mássica de vapor coincidem apenas para substância pura. Considere mistura de dois componentes fictícios distintos com massas molares iguais a 28 g/mol, fases de composições diferentes, 6 mol de líquido e 4 mol de vapor. Então β=4/(6+4)=0,4 e x=(4×28)/(6×28+4×28)=0,4. Há uma mistura, logo a afirmação de exclusividade não vale. A igualdade também ocorre nos limites de vapor nulo ou de líquido nulo, quando se interpretam as frações nos limites apropriados.

Para quantidades de matéria totais por fase nᵥ,nₗ e massas molares médias positivas M̄ᵥ,M̄ₗ, β=nᵥ/(nᵥ+nₗ), mᵥ=nᵥ M̄ᵥ e mₗ=nₗ M̄ₗ, portanto x=βM̄ᵥ/[(1−β)M̄ₗ+βM̄ᵥ]. Com 0<β<1, x=β se e somente se M̄ᵥ=M̄ₗ. O texto candidato fornece essa expressão e afirma a igualdade para massas médias iguais e nos dois limites, preservando a distinção entre xA da composição líquida e x do título mássico. Trata-se de álgebra a partir das definições das frações, sem pressupor mistura real específica; massas molares iguais e quantidades são dados didáticos postulados.

## Identidade e limites

Fragmento original completo `original.html`, candidato `candidata.html`; ambos possuem quebra final no arquivo, excluída dos hashes de fragmento no `manifesto.json`. Origem `modulos/e1-termodinamica.html`, seção `fun01-estado-equilibrio`, posição UTF-16 102479–103112 e ocorrência r7 `modulos/e1-termodinamica.html:102479:texto`. HTML SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`, r7 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`; original encontrado uma vez e candidata ausente na fotografia. Mantidos os demais trechos do elemento. Codificações `&lt;` representam `<` visível.

O Auditor deve reexaminar a fórmula, as condições de igualdade e os limites, além do alcance da alteração sobre FUN-01 e textos ligados. Aplicação futura exige nova fotografia, reconciliação do inventário e das referências, preservação dos 197 artigos e auditoria da versão efetiva. Não se declara QA-09 concluído.
