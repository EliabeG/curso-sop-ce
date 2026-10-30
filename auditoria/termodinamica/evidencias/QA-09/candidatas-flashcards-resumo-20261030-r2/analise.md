# QA-09 — candidatas isoladas de flashcards e resumo, r2

Data: 30/10/2026. Corretor automatizado `/root/qa_oficina`. **Candidatas não aplicadas, aguardando novo parecer independente.** Esta rodada responde à revisão preliminar do Auditor `/root/qa_diagnosticos` e conserva a r1 em `../candidatas-flashcards-resumo-20261030/`. HTML fonte, inventário, artigos e registros de produto não foram editados. QA-09 não foi encerrado.

## Base, delta e motivo

A fotografia é a mesma r8: `modulos/e1-termodinamica.html` SHA-256 `57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c`; inventário `auditoria/termodinamica/evidencias/QA-09/inventario-r8.json` SHA-256 `ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687`. O manifesto relaciona documento, seções, posições UTF-16, hashes, arquivos e substituições. Os hashes de elemento não incluem a quebra final presente nos arquivos isolados. O hash do nó de texto direto do resumo no inventário omite descendentes e é diferente do hash do elemento completo.

- **COP:** delimita a ciclos de refrigeração ou bomba de calor **por compressão cujo acionamento é somente trabalho**, com o calor útil da fonte fria ou entregue à fonte quente, respectivamente. Isso evita estender a definição à entrada térmica de sistemas por absorção e restringe a interpretação de sistema híbrido. A resposta se refere ao calor útil e trabalho na mesma base e fronteira do ciclo; auxiliares fora da fronteira não são automaticamente cobertos.
- **Pressão intermediária:** ambos os cartões agora explicitam compressões adiabáticas em regime permanente, uma entrada e uma saída por estágio, mesmo gás ideal e calores específicos constantes, **mesma eficiência isentrópica constante nos dois estágios**, mesma vazão e ausência de separação de massa. Mantêm resfriamento perfeito até a temperatura de entrada, pressões extremas absolutas fixas com saída maior e ausência de quedas de pressão e variações cinética/potencial relevantes. Essas premissas são necessárias para apresentar a raiz geométrica como minimização do trabalho total nesse modelo; eficiências distintas ou resfriamento imperfeito podem deslocar o ótimo. Esse refinamento decorre da ressalva do parecer, não da descoberta de erro na conta geométrica.
- **Válvula, compressor, trocador e resumo:** candidatas byte a byte idênticas às da r1. Permanecem propostas para os quatro ajustes obrigatórios identificados no parecer e não constituem aprovação da versão aplicada.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/candidatas-flashcards-resumo-20261030-r2/verificar.py` retornou `ok=true` e verificou as sete substituições, cada original único na fotografia e hashes. O hash do resultado **hipotético** se as sete forem aplicadas exatamente à base r8 é `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`; não é hash do produto atual. O script é somente leitura e não demonstra sozinho mérito físico, comportamento, acessibilidade ou validade de aceites anteriores.

A análise deve ser repetida por Auditor independente sobre esta r2. Após eventual parecer favorável, a aplicação exige conferir a fotografia vigente, aplicar precisamente o delta aprovado, reconciliar os inventários e fotografias com posições deslocadas, confirmar preservação dos 197 artigos e registros e solicitar auditoria independente da versão efetivamente aplicada. Não houve revisão humana, uso com estudantes ou teste de navegador nesta rodada.

SHA-256: manifesto `dc906da64802545f62c4c7e232b16ca9737bb25abb1ae3d044c2fdad2dd76808`; script `de986570cb2227ed50b927921931126ea35130eee5588f5d2ad36225de93d32a`. A análise anterior r1 contém justificativas detalhadas para válvula, compressor, trocador e resumo.
