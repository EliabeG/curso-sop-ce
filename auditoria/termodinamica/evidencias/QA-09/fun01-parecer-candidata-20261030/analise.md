# QA-09 — candidata isolada para parecer v e ρ

Data: 30/10/2026. Corretor automatizado `/root/qa_oficina`. **Candidata não aplicada**, aguardando exame independente. O HTML, os 197 artigos e os inventários oficiais não foram modificados nesta preparação. Não conclui QA-09 nem FUN-01.

## Achado e correção proposta

No mini parecer da âncora `fun01-parecer`, o produto `0,004 m³/kg × 250 kg/m³=1` confirma a compatibilidade dos valores centrais com `ρ=1/v`, para a mesma amostra e instante. A identidade também torna as propriedades dependentes; não constituem duas coordenadas independentes de estado. Contudo, números recíprocos **não demonstram como cada medição foi obtida**: poderiam derivar do mesmo dado ou ter sido obtidos por medições separadas. O texto atualmente afirma que uma medida foi obtida por inversão da outra sem documentar essa origem.

Substituição proposta, mantendo o resultado e o modelo: de “porém uma medida foi obtida por inversão da outra e o par é redundante” para “porém as duas grandezas estão vinculadas por ρ=1/v e não fornecem duas propriedades independentes”. Medidas separadas podem servir à verificação de consistência, desde que se considerem suas incertezas; isso não as transforma em propriedades independentes de estado. O exemplo não declara tolerâncias, portanto o teste da igualdade central não estabelece acordo metrológico certificado.

## Identidade e verificação

Base HTML `modulos/e1-termodinamica.html` SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`, âncora `fun01-parecer`, nó em posição UTF-16 `114112` na fotografia r7. Trecho original e candidato isolados em `original.html` e `candidata.html`; o `manifesto.json` informa substituição, hashes e contexto. Cada arquivo isolado termina com uma quebra de linha; os hashes de fragmento registrados excluem essa quebra. A conferência de identidade requer localização por documento, contexto, posição e hash, não apenas pela impressão de igualdade textual.

`ρv=250×0,004=1` é exato para números nominais; não foi inferida precisão instrumental. A candidata preserva a estrutura do parágrafo e os demais textos, apenas altera a frase indicada. Sua suficiência científica, a fidelidade literal e a análise do impacto em FUN-01, BAN-02, BAN-07 e BAN-08 exigem revisão independente. A efetiva aplicação exigirá conferir o hash do HTML então vigente, reconciliar e atualizar as fotografias/inventários deslocados, verificar preservação dos artigos e auditar a versão aplicada; não é autorizada automaticamente por este registro. O trabalho QA-09 restante permanece aberto.
