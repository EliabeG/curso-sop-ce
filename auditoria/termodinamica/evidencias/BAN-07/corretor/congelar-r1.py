"""Congela produto e evidências já verificados; não altera conteúdo de produto."""
import difflib
import hashlib
import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parents[5]
BASE = ROOT / "auditoria/termodinamica/evidencias/BAN-07"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


snapshot = read(BASE / "snapshot-antes.json")
products = [entry["arquivo"] for entry in snapshot["arquivos"]]
changed = [filename for filename in products if sha(ROOT / filename) != next(e["sha256"] for e in snapshot["arquivos"] if e["arquivo"] == filename)]
assert len(changed) == 5
assert read(BASE / "corretor/verificacao-produto-r1.json")["falhas"] == []
assert read(BASE / "corretor/testes-persistencia-r1.json")["falhas"] == []
assert read(BASE / "conferencia-coordenador-r1.json")["falhas"] == []
assert read(BASE / "persistencia-q-coordenador-r1.json")["falhas"] == []
assert all(v["ok"] for v in read(BASE / "navegador-coordenador-r1.json")["verificacoes"])
assert read(BASE / "corretor/verificacao-cientifica-25-r1.json")["artigos"] == 25
diff = []
for filename in changed:
    before = (BASE / "antes" / filename).read_text(encoding="utf-8").splitlines(keepends=True)
    after = (ROOT / filename).read_text(encoding="utf-8").splitlines(keepends=True)
    diff.extend(difflib.unified_diff(before, after, fromfile="antes/" + filename, tofile="depois/" + filename))
(BASE / "corretor/delta-produto-r1.patch").write_text("".join(diff), encoding="utf-8", newline="\n")

table = "\n".join("| `" + filename + "` | `" + sha(ROOT / filename) + "` |" for filename in changed)
delivery = f"""# BAN-07 r1 — entrega congelada para auditoria

Data: 28/10/2026. Corretor: agente automatizado `/root/corretor_aaa`. Escopo exclusivo: enunciados e alternativas dos197itens de E1. A entrega não é aprovação independente e não libera outro ID.

O [diagnóstico integrado antes da edição](../evidencias/BAN-07/diagnostico-197-integrado-r1.json) registra197IDs únicos e731juízos individuais de opções:117múltipla escolha×5 e73C/E×2, além de sete problemas abertos com solução/rubrica e família de respostas admissíveis. Os três diagnósticos originais permanecem preservados e identificados por hash. O [plano](../evidencias/BAN-07/PLANO_DIAGNOSTICO-r1.md) foi confirmado pelo coordenador antes da edição.

Foram corrigidos25artigos autorais: Q02/09/13/15/16/18/19/24/26/28 e AV08/10/17/18/33/35/37/38/45/48/50/57/58/64/73. Quatro comandos explicitam condições antes da tentativa; os demais ajustes relacionam alternativas a erros concretos e sincronizam comentários. Nenhuma chave foi trocada. Os80CR, sete abertos e demais85artigos autorais permanecem idênticos, totalizando172artigos preservados. Os nove estudos críticos continuam fora da nota com documento, chave e análise técnica distinguidos.

O [diagnóstico após a correção](../evidencias/BAN-07/diagnostico-pos-correcao-197-r1.json) associa cada registro ao artigo examinado. A [releitura científica dos25](../evidencias/BAN-07/corretor/verificacao-cientifica-25-r1.json) registra125opções,16casos numéricos e nove conceituais. Os distratores novos têm operações ou confusões identificáveis; equivalências após arredondamento foram confrontadas. AV10B/E repetem800kg/m³ com classificações distintas, e somenteB fornece o par pedido. Q09 distingue trabalho produzido e consumido pelo sinal físico, apesar da mesma magnitude.

O [mapa dos197itens](../evidencias/BAN-07/mapa-identidades-r1.json) confirma20novasdigitais(oitoQ e12AV) e cinco mudanças somente de comentários(Q13/18,AV17/18/64). Nenhuma letra antiga foi migrada. Q E1 conserva respostas/erros/marcações de versões anteriores e conta somente digitais atuais; AV mantém seu mapa de histórico. Avisos aparecem quando pertinentes. JSON ilegível E1 não é sobrescrito: tentativas novas ficam na página com aviso. O comportamento dos demais módulos e o registro fora de E1 foram preservados.

## Verificações executadas e atribuição

- Corretor: [264verificações estruturais](../evidencias/BAN-07/corretor/verificacao-produto-r1.json), sem falhas;58substituições reproduzem integralmente oHTML;734elementosMathML preservados; apenas cinco arquivos e25registros de inventário alterados.
- Corretor: [15casos de persistência](../evidencias/BAN-07/corretor/testes-persistencia-r1.json), sem falhas, executando funções reais e a camada real de armazenamento em Node/VM com DOM/localStorage controlados. Não é teste de navegador.
- Validador canônico: [197registros,29recursos e1261links locais](../evidencias/BAN-07/corretor/validacao-inventario-r1.json), sem erro ou aviso. Isso verifica estrutura/rastreabilidade, não certifica ciência ou aprendizagem.
- Coordenador, apoio separado: [376verificações de preservação](../evidencias/BAN-07/conferencia-coordenador-r1.json), [59verificações de reconstrução](../evidencias/BAN-07/reconstrucao-coordenador-r1.json) e [15testes de funções Q](../evidencias/BAN-07/persistencia-q-coordenador-r1.json), sem falhas.
- Coordenador, navegador CUA: [nove verificações antes/depois](../evidencias/BAN-07/navegador-coordenador-r1.json). Q24/AV08 revisadas exigiram nova tentativa; Q23 preservou sua resposta; avisos apareceram; novas respostas persistiram após recarga. Há captura de Q24. Esse apoio não foi apresentado como execução do Auditor e o DOM não prova sozinho todos os bytes do histórico.

## Versão e arquivos

| Arquivo alterado | SHA-256 |
|---|---|
{table}

O [delta completo dos cinco arquivos](../evidencias/BAN-07/corretor/delta-produto-r1.patch), o [manifesto](../evidencias/BAN-07/manifesto-r1.json) e nove cópias finais em `evidencias/BAN-07/pacote-r1` identificam a versão. O HTML anterior, as fontes e os pacotes aceitos usados por herança permanecem identificados por hash. Hash diferente não foi tratado como identidade integral.

Não houve piloto com estudantes, revisão humana, certificação externa, auditoria integral de acessibilidade ou fechamento de BAN-08/QA globais. A plausibilidade dos erros é teórica. Inventário usa `verificado` para a conferência do Corretor dos25registros atingidos, explicitamente sujeita ao parecer independente.

Entrega para o Auditor independente designado pelo coordenador. O próximo ID permanece bloqueado até parecer explícito `APROVADO` sobre esta versão e liberação pelo coordenador.
"""
delivery_path = ROOT / "auditoria/termodinamica/entregas/BAN-07-r1.md"
delivery_path.write_text(delivery, encoding="utf-8", newline="\n")

package = BASE / "pacote-r1"
for filename in products:
    target = package / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / filename, target)

paths = set(ROOT / filename for filename in products)
for directory in [BASE / "antes", BASE / "corretor", BASE / "apoio"]:
    paths.update(path for path in directory.rglob('*') if path.is_file() and '__pycache__' not in path.parts)
paths.update(path for path in BASE.iterdir() if path.is_file() and path.name != 'manifesto-r1.json')
paths.update(path for path in package.rglob('*') if path.is_file())
paths.add(delivery_path)
paths.update(ROOT / filename for filename in ["auditoria/termodinamica/PROTOCOLO_AAA.md", "auditoria/termodinamica/pareceres/BAN-07-preparacao.md", "auditoria/termodinamica/pareceres/BAN-07-preparacao.json"])
entries = []
for path in sorted(paths):
    relative = path.relative_to(ROOT).as_posix()
    entry = {"arquivo": relative, "bytes": path.stat().st_size, "sha256": sha(path)}
    if relative in products:
        entry["copia"] = (package / relative).relative_to(ROOT).as_posix()
    entries.append(entry)
manifest = {"id": "BAN-07", "rodada": 1, "data": "2026-10-28", "estado": "congelado_para_auditoria", "autor": "/root/corretor_aaa", "escopo": "197itens examinados;25artigos autorais corrigidos;20novasdigitais;nenhuma chave alterada. Cinco arquivos de produto editados; outros produtos no pacote são cópias preservadas.", "arquivos": entries, "arquivos_produto_alterados": changed, "copias_finais": len(products), "limite": "Manifesto não aprova ciência, não inclui o controle mutável do coordenador e não substitui parecer independente."}
manifest_path = BASE / "manifesto-r1.json"
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
assert all(sha(ROOT / row['arquivo']) == row['sha256'] for row in entries)
assert all(sha(ROOT / row['arquivo']) == sha(ROOT / row['copia']) for row in entries if 'copia' in row)
print(json.dumps({"manifesto": manifest_path.relative_to(ROOT).as_posix(), "sha256_manifesto": sha(manifest_path), "arquivos": len(entries), "copias_finais": len(products), "entrega": delivery_path.relative_to(ROOT).as_posix(), "sha256_entrega": sha(delivery_path)}, ensure_ascii=False))
