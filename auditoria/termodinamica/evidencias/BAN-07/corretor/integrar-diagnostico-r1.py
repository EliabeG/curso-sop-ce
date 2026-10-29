"""Integra diagnósticos sem alterar arquivos do produto."""
import collections
import copy
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[5]
BASE = ROOT / "auditoria/termodinamica/evidencias/BAN-07"


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


sources = [
    "diagnostico-30-q-coordenador-r1.json",
    "corretor/diagnostico-87-cr-abertos-r1.json",
    "apoio/diagnostico-80-av-r1.json",
]
origin = []
indexed = {}
normalizations = []
for filename in sources:
    path = BASE / filename
    document = read(path)
    origin.append({"arquivo": "auditoria/termodinamica/evidencias/BAN-07/" + filename, "sha256": sha(path), "registros": len(document["registros"])})
    for original in document["registros"]:
        record = copy.deepcopy(original)
        item_id = record["id"]
        assert item_id not in indexed, item_id
        for ref in record["fontes_e_evidencias"]:
            if isinstance(ref, dict) and re.fullmatch(r"av-e\s+1-\d{2}", ref.get("localizador", "")):
                normalizations.append({"id": item_id, "campo": "fontes_e_evidencias.localizador", "antes": ref["localizador"], "depois": item_id})
                ref["localizador"] = item_id
        indexed[item_id] = record

selections = {
    "av-e1-08": "Substituir D por 180 °C. Explicar que 20 + 2 × 80 = 180 °C trata o alcance/span como semiamplitude, duplicando indevidamente o intervalo antes de somar o limite inferior. A definição correta é LS = LI + span = 100 °C.",
    "av-e1-10": "Substituir D por 0,18 kg/m³ e extensiva. Explicar que 12 × 0,015 = 0,18 é o produto indevido em vez de m/V; o produto teria unidade kg·m³, não kg/m³. A classificação extensiva também é falsa; a massa específica é intensiva.",
}
for item_id, proposal in selections.items():
    previous = indexed[item_id]["diagnostico"]["proposta_minima"]
    indexed[item_id]["diagnostico"]["proposta_minima"] = proposal
    normalizations.append({"id": item_id, "campo": "diagnostico.proposta_minima", "antes": previous, "depois": proposal, "motivo": "Escolha integradora concreta entre variantes; proposta ainda não implementada."})

extract = read(BASE / "extrato-197-antes.json")
assert sha(ROOT / "modulos/e1-termodinamica.html") == extract["html_sha256"]
assert set(indexed) == {item["id"] for item in extract["itens"]}
records = [indexed[item["id"]] for item in extract["itens"]]
for record, item in zip(records, extract["itens"]):
    assert record["sha256_artigo"] == item["sha256_artigo"]
    expected = list(dict.fromkeys(re.findall(r'<input\b[^>]*\bvalue="([A-E])"', item["html"])))
    if item["banco"] == "inicial":
        expected = re.findall(r'<li\b[^>]*\bdata-letra="([A-E])"', item["html"].split('class="q-resolucao"')[0])[:5]
    assert [option["opcao"] for option in record["alternativas"]] == expected, record["id"]

changed = [record["id"] for record in records if record["diagnostico"]["decisao"] in ["corrigir", "esclarecer"]]
assert len(changed) == 25
new_identity = ["q-e1-02", "q-e1-09", "q-e1-15", "q-e1-16", "q-e1-19", "q-e1-24", "q-e1-26", "q-e1-28", "av-e1-08", "av-e1-10", "av-e1-33", "av-e1-35", "av-e1-37", "av-e1-38", "av-e1-45", "av-e1-48", "av-e1-50", "av-e1-57", "av-e1-58", "av-e1-73"]
comments_only = [item_id for item_id in changed if item_id not in new_identity]
document = {
    "id": "BAN-07", "rodada": 1, "data": "2026-10-28",
    "integrador": "/root/corretor_aaa", "estado": "diagnostico_integrado_pre_edicao",
    "produto_modificado": False, "html_sha256": extract["html_sha256"],
    "fontes_diagnostico": origin, "normalizacoes_e_escolhas": normalizations,
    "cobertura": {"registros": len(records), "ids_unicos": len(indexed), "bancos": collections.Counter(record["banco"] for record in records), "alternativas_individuais": sum(len(record["alternativas"]) for record in records), "decisoes": collections.Counter(record["diagnostico"]["decisao"] for record in records)},
    "implementacao_proposta": {"artigos": changed, "novas_digitais": new_identity, "somente_comentarios": comments_only, "chaves_alteradas": [], "cr_alterados": [], "abertos_alterados": []},
    "registros": records,
    "limites": [
        "Diagnóstico e plano não são implementação nem parecer de aprovação.",
        "Apoio e integrador pertencem ao Corretor; o Auditor permanece independente.",
        "Erros dos distratores têm plausibilidade teórica, sem aplicação com estudantes.",
        "Cálculos necessários ao gabarito/unicidade incluídos, sem concluir BAN-08 global.",
        "Originais dos três diagnósticos preservados; correções documentais e escolhas rastreadas acima."
    ]
}
output = BASE / "diagnostico-197-integrado-r1.json"
output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"arquivo": str(output), "sha256": sha(output), "cobertura": document["cobertura"], "artigos": len(changed), "novas_digitais": len(new_identity), "somente_comentarios": comments_only}, ensure_ascii=False))
