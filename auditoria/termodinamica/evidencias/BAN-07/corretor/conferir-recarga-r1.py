"""Conferência reproduzível dos diagnósticos salvos; não edita produto."""
import collections
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[5]
BASE = ROOT / "auditoria/termodinamica/evidencias/BAN-07"
OUT = BASE / "corretor/conferencia-recarga-r1.json"


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def article(text, item_id):
    match = re.search(r'<article\b[^>]*\bid="' + re.escape(item_id) + r'"[^>]*>[\s\S]*?</article>', text)
    assert match, item_id
    return match.group()


extract = read(BASE / "extrato-197-antes.json")
items = {item["id"]: item for item in extract["itens"]}
contract = read(BASE / "CONTRATO_DIAGNOSTICO-r1.json")["modelo_registro"]
source_text = (ROOT / "modulos/e1-termodinamica.html").read_text(encoding="utf-8")
report = {
    "id": "BAN-07", "rodada": 1, "data": "2026-10-28",
    "autor": "/root/corretor_aaa", "estado": "conferencia_pre_edicao",
    "html_sha256": sha(ROOT / "modulos/e1-termodinamica.html"),
    "html_base_esperado": extract["html_sha256"], "diagnosticos": [],
    "herancas_abertas_reconferidas": [], "falhas": [],
    "limites": [
        "Conferência do próprio Corretor; não substitui o parecer independente do Auditor.",
        "Presença de campo e demonstração não é prova automática de correção científica.",
        "Os 30 Q do coordenador serão incorporados antes de qualquer edição material.",
        "CR79/80 são estudos críticos de múltipla escolha; há cinco opções, não duas.",
        "Nenhum produto é modificado pelo script."
    ]
}
if report["html_sha256"] != report["html_base_esperado"]:
    report["falhas"].append("HTML corrente diverge da base pré-edição")

for relative in ["corretor/diagnostico-87-cr-abertos-r1.json", "apoio/diagnostico-80-av-r1.json"]:
    path = BASE / relative
    records = read(path)["registros"]
    d = {
        "arquivo": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha(path),
        "registros": len(records), "ids_unicos": len({r["id"] for r in records}),
        "tipos_de_formato": collections.Counter(), "decisoes": collections.Counter(),
        "alternativas_individuais": 0, "campos_ausentes": [], "campos_vazios_indevidos": [],
        "identidades_divergentes": [], "opcoes_incompletas": [],
        "observacoes_documentais": []
    }
    for r in records:
        item_id = r["id"]
        src = items[item_id]
        current = article(source_text, item_id)
        if r["sha256_artigo"] != src["sha256_artigo"] or hashlib.sha256(current.encode()).hexdigest() != r["sha256_artigo"]:
            d["identidades_divergentes"].append(item_id)
        missing = [key for key in contract if key not in r]
        for key, value in contract.items():
            if isinstance(value, dict) and isinstance(r.get(key), dict):
                missing.extend(key + "." + sub for sub in value if sub not in r[key])
        if missing:
            d["campos_ausentes"].append({"id": item_id, "campos": missing})
        required_text = [
            ("autor_leitura", r.get("autor_leitura")),
            ("suficiencia.conclusao", r["suficiencia"].get("conclusao")),
            ("demonstracao.passos", r["demonstracao"].get("passos")),
            ("demonstracao.conclusao", r["demonstracao"].get("conclusao")),
            ("unicidade.justificativa", r["unicidade"].get("justificativa")),
            ("diagnostico.proposta_minima", r["diagnostico"].get("proposta_minima")),
        ]
        for key, value in required_text:
            if not value:
                d["campos_vazios_indevidos"].append({"id": item_id, "campo": key})
        values = re.findall(r'<input\b[^>]*\bvalue="([A-E])"', current)
        expected = list(dict.fromkeys(values))
        actual = [option["opcao"] for option in r["alternativas"]]
        if actual != expected:
            d["opcoes_incompletas"].append({"id": item_id, "esperado": expected, "encontrado": actual})
        for option in r["alternativas"]:
            if not all(option.get(key) for key in ["opcao", "valor_logico", "justificativa", "erro_representado_e_plausibilidade"]):
                d["opcoes_incompletas"].append({"id": item_id, "opcao": option})
        kind = "aberto" if not expected else "CE" if expected == ["C", "E"] else "MC5"
        d["tipos_de_formato"][kind] += 1
        d["decisoes"][r["diagnostico"]["decisao"]] += 1
        d["alternativas_individuais"] += len(actual)
        for ref in r["fontes_e_evidencias"]:
            if isinstance(ref, dict) and re.fullmatch(r"av-e\s+1-\d{2}", ref.get("localizador", "")):
                d["observacoes_documentais"].append({
                    "id": item_id, "campo": "fontes_e_evidencias.localizador",
                    "salvo": ref["localizador"], "localizador_correto": item_id,
                    "efeito": "Erro textual de localização; o registro e o SHA de artigo identificam corretamente a evidência. Corrigir na integração, preservando o diagnóstico original do apoio."
                })
    for key in ["campos_ausentes", "campos_vazios_indevidos", "identidades_divergentes", "opcoes_incompletas"]:
        if d[key]:
            report["falhas"].append({"arquivo": relative, "campo": key, "ocorrencias": len(d[key])})
    report["diagnosticos"].append(d)

heritage = read(BASE / "corretor/heranca-abertos-r1.json")
for entry in heritage["artigos"]:
    copied = (ROOT / entry["copia"]).read_text(encoding="utf-8")
    got = hashlib.sha256(article(copied, entry["id"]).encode()).hexdigest()
    ok = got == entry["sha256_aceito"] == items[entry["id"]]["sha256_artigo"]
    report["herancas_abertas_reconferidas"].append({"id": entry["id"], "sha256": got, "identico": ok})
    if not ok:
        report["falhas"].append({"heranca": entry["id"]})
for entry in heritage["recursos"]:
    got = sha(ROOT / entry["arquivo"])
    ok = got == entry["sha256_aceito"]
    report["herancas_abertas_reconferidas"].append({"arquivo": entry["arquivo"], "sha256": got, "identico": ok})
    if not ok:
        report["falhas"].append({"heranca": entry["arquivo"]})

report["totais"] = {
    "registros": sum(d["registros"] for d in report["diagnosticos"]),
    "alternativas_individuais": sum(d["alternativas_individuais"] for d in report["diagnosticos"]),
    "observacoes_documentais": sum(len(d["observacoes_documentais"]) for d in report["diagnosticos"]),
    "herancas_abertas_confirmadas": sum(h["identico"] for h in report["herancas_abertas_reconferidas"])
}
OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"arquivo": str(OUT), "totais": report["totais"], "falhas": report["falhas"]}, ensure_ascii=False))
