# QA-09 — errata de identidade da entrega de fórmulas 84–100

30/10/2026. `/root/next_theory`. O parecer histórico `auditoria-formulas-r28-lote5-next-theory-20261030/parecer.md`, SHA-256 `7f4211612626d6821f807bd4a83960edc53edcc29d1a24928b0277b776fa22b0`, transcreveu incorretamente o último dígito do hash da entrega examinada, registrando `67a17bcf599ebedcbfd1843d4dbed405e5e090845a8c462f319cd98e7dd53b3b`.

A verificação direta do arquivo `formulas-r28-lote5-20261030/entrega.md` com `sha256sum` retornou **`67a17bcf599ebedcbfd1843d4dbed405e5e090845a8c462f319cd98e7dd53b3a`**. O desvio é um erro de transcrição no meu parecer; não há evidência nesta verificação de alteração do arquivo da entrega. Ao repetir o verificador original, a guarda do formulário atual falhou: ele exige r28 e o produto já avançou para r30. Por isso `verificar-snapshots.mjs`, cópia do verificador alterada apenas para ler o snapshot preservado r28 em lugar do formulário corrente, passou e confirmou a fotografia r27, os 17 fragmentos e comparação com r28. Esta errata não é nova revisão científica dos conteúdos.

O parecer histórico foi preservado sem alteração e deve ser lido com este suplemento. O erro foi informado por `/root/planning`, que fará a referência à identidade correta no ledger.
