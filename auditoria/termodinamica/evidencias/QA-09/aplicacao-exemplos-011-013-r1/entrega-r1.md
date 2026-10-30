# QA-09 — aplicação localizada dos exemplos EX-011 e EX-013, r1

Data: 30/10/2026. Autor: agente automatizado `/root/corretor`. Estado: **aguardando auditoria independente da versão efetiva**. Esta entrega é uma parcela de QA-09, não encerra o ID, nem libera o seguinte.

## Base, alterações e recálculo

A base é o commit `ee5da2588b799cc62bf85c5146ab8bb4982d2352`, com HTML SHA-256 `dd47dc9dbc5c22f6f74a4fa67bd28b495cff775ff8ca04cec2c76c405dfefd1a` e inventário QA-09 r6 `a38b60799c23cf88fb0085e7c9bd82b4f22f58a4c7f89b6b418f8b3f5ae5d1aa`. As duas candidatas foram examinadas em [revisão independente anterior](../../../pareceres/QA-09-exemplos-011-013-revisao-candidatas-independente-r1.md); esse parecer não audita a aplicação presente. Cada original foi localizado uma vez por documento, contexto, posição e hash e substituído pela candidata correspondente. A reconstrução pelas duas substituições reproduz o HTML resultante byte a byte.

- EX-011: calor líquido perdido de 40 kJ e eixo como único trabalho; na convenção de calor para o sistema e trabalho pelo sistema positivos, Q = −40 kJ, W = −250 kJ, ΔU = 210 kJ. Sistema fechado e rígido; desprezam-se variações de energia cinética e potencial conforme a base didática.
- EX-013: pressão constante de 200 kPa, ΔV = −0,020 m³, trabalho de fronteira único: W = −4 kJ; Q líquido = −7 kJ e ΔU = −3 kJ. No segundo caso inalterado, 35/(1 × 0,70) = 50 K para o modelo de gás ideal com cᵥ constante ou representativo da faixa. Resultados para dados nominais, sem precisão instrumental declarada.

## Verificações e limites

`node auditoria/termodinamica/evidencias/QA-09/aplicacao-exemplos-011-013-r1/verificar-aplicacao-r1.mjs` confirmou a identidade de originais e candidatas, reconstrução e fotografia efetiva, 197 artigos íntegros e na mesma ordem, 197 registros individuais do inventário idênticos e alteração apenas de `fonte` no topo do JSON. O Markdown do inventário recebeu seção histórica desta entrega. As fotografias anteriores dos três documentos estão em `antes/`.

`node auditoria/termodinamica/inventario/validar-inventario.mjs` retornou `ok=true`, 197 itens/artigos, 29 recursos, 1.263 links locais, nenhum erro ou aviso. A verificação é estrutural e documental; não certifica mérito científico ou aprendizagem. O teste `auditoria/termodinamica/evidencias/BAN-08/aplicacao-av42-av45-av52-r1/testar-persistencia.mjs`, inspecionado antes da execução para não regravar evidências, passou nos seis cenários informados; usa funções reais de `curso.js` com DOM e armazenamento simulados, não um navegador real.

O inventário estrutural r7 foi produzido por cópia do gerador r6 com destino novo, sem regravar r6. O mapa r6→r7 registra 11.396 pares, 11.391 hashes iguais, cinco alterados (seção ancestral, dois exemplos e dois parágrafos), 5.484 IDs deslocados e nenhum erro de correspondência. O mapeamento usa documento, ordem, tipo, tag, seção, âncora e deslocamentos UTF-16. Não mapeia listas separadas de referências e recursos; hash igual não comprova dependências e não transfere aceite automaticamente.

Os dois blocos são exemplos fora dos artigos pontuados. A preservação dos artigos e dos scripts sustenta ausência de impacto identificado sobre BAN-02/07/08, mas a revalidação localizada da versão aplicada cabe ao Auditor independente. Não houve teste em navegador real, revisão humana, aplicação com alunos ou certificação externa. QA-09 exige ainda inventário e recálculo de todo o restante do conteúdo numérico; as contagens estruturais não são contagens de cálculos conferidos.

## SHA-256

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` e fotografia posterior | `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `c240148429da2f2a295e6a97bce2f466a255fdc5f5fef1858aaed2fc2a687e89` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `939b865b200f20061b56cd5f4e0163948d8b8d48fbf9fd30c68322a392ea2e4b` |
| `auditoria/termodinamica/evidencias/QA-09/inventario-r7.json` | `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a` |
| `auditoria/termodinamica/evidencias/QA-09/inventariar-r7.mjs` | `4c1831efad100c171fb699e07f28a8d7282fbd36c1e1d251027957c5f34c7201` |
| `auditoria/termodinamica/evidencias/QA-09/mapa-correspondencia-inventario-r6-r7-r1.json` | `21fc816ecb3e5191463a089a3a23ab76b4b9aa42431b14f8e48f35f7f7200c26` |
| `auditoria/termodinamica/evidencias/QA-09/mapear-r6-r7-r1.mjs` | `92b8dbf10b64e976ddd53dbb4247993bf3ae1d745ff2957957a57ee6bbb9b555` |
| `verificar-aplicacao-r1.mjs` nesta pasta | `7ded49d1cf3919b30437add6ef9c2dfce9fd402c79012355d8854bf391268825` |
| `assets/curso.js` | `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` |
| `assets/registro.js` | `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c` |
| `formulas/termodinamica.html` | `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0` |
