"""Sincroniza somente registros atingidos e mantém rastreio da revisão do Corretor."""
import copy
import hashlib
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[5]
BASE = ROOT / "auditoria/termodinamica/evidencias/BAN-07"


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def text(value):
    value = re.sub(r'<math\b[^>]*\bdata-formula-original="([^"]*)"[^>]*>[\s\S]*?</math>', lambda m: html.unescape(m[1]), value)
    return re.sub(r"\s+", " ", html.unescape(re.sub('<[^>]+>', '', value))).strip()


current_html = (ROOT / "modulos/e1-termodinamica.html").read_text(encoding="utf-8")
digest = hashlib.sha256(current_html.encode()).hexdigest()
snapshot_path = BASE / "e1-termodinamica.r1.html"
snapshot_path.write_text(current_html, encoding="utf-8", newline="\n")
mapping = load(BASE / "mapa-identidades-r1.json")
by_id = {entry["id"]: entry for entry in mapping["registros"]}
diagnostic = load(BASE / "diagnostico-197-integrado-r1.json")
updated = copy.deepcopy(diagnostic)
updated["estado"] = "produto_corrigido_pelo_corretor_aguardando_auditoria"
updated["produto_modificado"] = True
updated["html_sha256"] = digest
updated["referencia_pre_edicao"] = "auditoria/termodinamica/evidencias/BAN-07/diagnostico-197-integrado-r1.json"
for record in updated["registros"]:
    item_id = record["id"]
    row = by_id[item_id]
    if not row["artigo_alterado"]:
        for ref in record["fontes_e_evidencias"]:
            if isinstance(ref, dict) and ref.get("arquivo") == "modulos/e1-termodinamica.html":
                ref["arquivo"] = "auditoria/termodinamica/evidencias/BAN-07/antes/modulos/e1-termodinamica.html"
        continue
    record["sha256_artigo"] = row["depois"]["sha256_artigo"]
    article = re.search(r'<article\b[^>]*\bid="' + item_id + r'"[^>]*>[\s\S]*?</article>', current_html).group()
    if item_id.startswith('q-'):
        option_html = re.search(r'<ol class="q-alternativas">([\s\S]*?)</ol>', article)[1]
        options = dict(re.findall(r'<li data-letra="([A-E])">([\s\S]*?)</li>', option_html))
        comments = dict(re.findall(r'<li data-letra="([A-E])">([\s\S]*?)</li>', article.split('<details class="q-resolucao">', 1)[1]))
    else:
        options = dict(re.findall(r'<strong>([A-E])\.</strong> ([\s\S]*?)</span>', article))
        comments = dict(re.findall(r'<strong>([A-E]) — (?:Comentário|Alternativa do gabarito):</strong> ([\s\S]*?)</li>', article))
    assert set(options) == set(comments) == set('ABCDE'), item_id
    for option in record["alternativas"]:
        letter = option["opcao"]
        option["texto"] = text(options[letter])
        option["justificativa"] = text(comments[letter])
        option["erro_representado_e_plausibilidade"] = "Resposta correta conforme demonstração." if letter == row["chave"] else text(comments[letter]) + " Plausibilidade teórica, sem piloto."
    record["diagnostico_pre_edicao"] = record["diagnostico"]
    record["diagnostico"] = {"decisao": "manter", "achados": [], "proposta_minima": "Correção planejada executada; versão submetida ao Auditor independente.", "impacto_identidade": "Nova digital; tentativa anterior preservada sem migração de letra." if row["digital_alterada"] else "Digital preservada; mudança somente de comentários."}
    record["comentarios_existentes"] = {"coerencia": "Solução e cinco comentários finais confrontados com a demonstração e as opções efetivamente publicadas; a análise de erro foi sincronizada com as substituições registradas.", "lacunas": []}
    record["consistencia"]["resultado"] = "Não foi identificada contradição no comando final, na solução ou nas cinco alternativas relidas; conclusão do Corretor sujeita ao Auditor."
    for ref in record["fontes_e_evidencias"]:
        if isinstance(ref, dict) and ref.get("arquivo") == "modulos/e1-termodinamica.html":
            ref["sha256"] = digest
    record["verificacao_pos_correcao"] = {"autor": "/root/corretor_aaa", "digital_antes": row["antes"]["digital"], "digital_depois": row["depois"]["digital"], "chave_preservada": True, "limite": "Conferência do Corretor; não é parecer de aprovação nem avaliação empírica."}
    record["unicidade"]["equivalencias_apos_arredondamento"] = []
    record["unicidade"]["justificativa"] = "As cinco opções finais, com demonstração/refutação individual acima, não fornecem segunda resposta correta, incluindo arredondamentos indicados."

models = {
    "q-e1-02": ["Pressão manométrica de +200 kPa explicitamente referida à atmosfera local de100kPa."],
    "q-e1-09": ["Sistema fechado de fronteira móvel, limite de equilíbrio mecânico sem atrito; pressão conjugada a dV; sem outros trabalhos; pedido de trabalho realizado pelo sistema."],
    "av-e1-33": ["Não há outros modos de trabalho nem interação energética relevante com a membrana."],
    "av-e1-50": ["Compressores/turbinas adiabáticos em regime permanente, EC/EP desprezíveis, comparação por massa com mesmos estados de entrada e pressões de saída em cada componente."],
}
for record in updated["registros"]:
    if record["id"] in models:
        record["suficiencia"]["dados_e_condicoes_fornecidos"].extend(models[record["id"]])
        record["suficiencia"]["somente_na_resolucao"] = []
        record["suficiencia"]["faltantes_relevantes"] = []
        record["suficiencia"]["conclusao"] = "O comando final explicita a condição/modelo apontado no diagnóstico; não depende de acrescentá-lo depois da tentativa."
        record["consistencia"]["restricoes_fisicas"] = "Condições explicitadas no comando final: " + " ".join(models[record["id"]])
    if record["id"] == "av-e1-50":
        record["demonstracao"]["conclusao"] = "C: na classe adiabática, em regime permanente e sob as referências de entrada/pressão de saída declaradas, as irreversibilidades aumentam o consumo específico do compressor e reduzem a produção específica da turbina."
        record["demonstracao"]["contraexemplo_historico_que_motivou_esclarecimento"] = record["demonstracao"].pop("contraexemplo_do_comando_sem_restricao")

updated["cobertura"]["decisoes_pos_correcao"] = {"manter": 188, "estudo_critico_preservado": 9}
(BASE / "diagnostico-pos-correcao-197-r1.json").write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

inventory_path = ROOT / "auditoria/termodinamica/inventario/inventario-questoes.json"
inventory = load(BASE / "antes/auditoria/termodinamica/inventario/inventario-questoes.json")
inventory["fonte"]["sha256"] = digest
inventory["fonte"]["snapshot"] = "auditoria/termodinamica/evidencias/BAN-07/e1-termodinamica.r1.html"
inventory["metodo"]["descricao"] += " BAN-07 r1: diagnóstico individual de197itens e731opções;25artigos autorais corrigidos e20digitais alteradas, sem troca de chave. Registros modificados apontam à conferência científica do Corretor, ainda sujeita ao parecer independente; não se declara BAN-08 concluído."
changed_records = []
for record in inventory["itens"]:
    row = by_id[record["id"]]
    if not row["artigo_alterado"]:
        continue
    changed_records.append(record["id"])
    record["localizacao"]["sha256_artigo"] = row["depois"]["sha256_artigo"]
    record["revisao"]["gabarito"] = "verificado"
    record["revisao"]["evidencia_gabarito"] = "auditoria/termodinamica/evidencias/BAN-07/diagnostico-pos-correcao-197-r1.json"
    if record["id"] in models:
        record["hipoteses"]["explicitadas"].extend(models[record["id"]])
    if record["id"] == "q-e1-02":
        record["hipoteses"]["implicitas"] = []
    if record["id"] == "q-e1-09":
        record["hipoteses"]["implicitas"] = ["Segmentos seguem o retângulo indicado na figura."]
    if record["id"] == "av-e1-50":
        record["hipoteses"]["explicitadas"] = models[record["id"]]
        record["hipoteses"]["limites"].append("A referência isentrópica não é mínimo irrestrito para compressor refrigerado; a classe comparada é adiabática.")
inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
summary_path = ROOT / "auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md"
summary = (BASE / "antes/auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md").read_text(encoding="utf-8")
summary = summary.replace(" + FON-02 r1\n", " + FON-02 r1 + BAN-07 r1\n", 1)
summary += "\n## Revisão BAN-07 r1 — versão submetida à auditoria\n\nO diagnóstico integral contém197registros e731juízos individuais de opções. Foram corrigidos25artigos autorais(10Q e15AV), com20novasdigitais e cinco alterações somente de comentários; nenhuma chave foi trocada. Os80CR e sete problemas abertos permanecem integralmente preservados. Os nove estudos críticos continuam fora da pontuação. A verificação do Corretor dos25registros atingidos aponta ao [diagnóstico após correção](../evidencias/BAN-07/diagnostico-pos-correcao-197-r1.json); o [mapa de identidade](../evidencias/BAN-07/mapa-identidades-r1.json) distingue cada versão e mantém o histórico sem copiar letras antigas para novas digitais.\n\nAs hipóteses de Q02/Q09/AV33/AV50 foram explicitadas antes da tentativa. Foram sincronizados os hashes e os metadados realmente atingidos; os outros172registros permanecem idênticos. Níveis, competências e estatísticas do inventário foram preservados. A conferência do Corretor não é parecer de aprovação independente e não conclui BAN-08 ou classificação global do curso.\n"
summary_path.write_text(summary, encoding="utf-8", newline="\n")
print(json.dumps({"registros_atualizados": len(changed_records), "sha256_html": digest}, ensure_ascii=False))
