# -*- coding: utf-8 -*-
"""
Retorno do conector Meta Ads (claude.ai) -> metricas/serie/meta_ads.csv do cliente.

É o executor "Claude" do passo Meta (P2, executor trocável) enquanto o token de usuário de
sistema não é aprovado (docs/24). Quando o token sair, o metricas.py passa a buscar sozinho e
este script fica como plano B.

    uv run --with pyyaml python scripts/meta_cache.py --cliente atacadao-posto-13 --arquivo <dump.json>

O dump esperado: ads_get_ad_entities com level=campaign, time_increment=1 e os campos
id, objective, amount_spent, impressions, link_click, offsite_conversion_fb_pixel_purchase,
offsite_conversion_fb_pixel_purchase_values. TODAS as campanhas com gasto (sem filtro de objetivo):
a soma dá o total da conta e o filtro pelo objetivo declarado no cliente.md dá o *_venda.

Criado em 28/09/2026.
"""
import io, os, sys, json, argparse, datetime as dt, collections, importlib.util

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

spec = importlib.util.spec_from_file_location("metricas", os.path.join(RAIZ, "scripts", "metricas.py"))
metricas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metricas)


def num(v):
    if v is None:
        return 0.0
    if isinstance(v, dict):
        v = v.get("value")
    return float(v or 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--arquivo", required=True, help="JSON salvo pelo conector ({ad_entities: '<json>'})")
    a = ap.parse_args()

    base, cli, _, _ = metricas.carregar(a.cliente)
    objetivo = cli.get("meta_objetivo_ecommerce") or "OUTCOME_SALES"
    bruto = json.load(io.open(a.arquivo, encoding="utf-8"))
    if isinstance(bruto, dict) and bruto.get("pagination", {}).get("next_cursor"):
        sys.exit("O dump tem próxima página (next_cursor). Busque todas as páginas antes de importar.")
    linhas = json.loads(bruto["ad_entities"]) if isinstance(bruto.get("ad_entities"), str) else bruto["ad_entities"]

    novos = collections.defaultdict(lambda: collections.defaultdict(float))
    objetivos = collections.Counter()
    for r in linhas:
        d = dt.date.fromisoformat(r["date_start"])
        if r.get("date_stop") and r["date_stop"] != r["date_start"]:
            sys.exit("Linha não diária (%s a %s). Use time_increment=1." % (r["date_start"], r["date_stop"]))
        gasto, imp, clq = num(r.get("amount_spent")), num(r.get("impressions")), num(r.get("link_click"))
        comp, val = num(r.get("offsite_conversion_fb_pixel_purchase")), num(r.get("offsite_conversion_fb_pixel_purchase_values"))
        x = novos[d]
        x["investimento_meta"] += gasto
        x["impressoes_meta"] += imp
        x["cliques_meta"] += clq
        x["compras_meta"] += comp
        x["receita_meta"] += val
        objetivos[r.get("objective")] += gasto
        if r.get("objective") == objetivo:
            x["investimento_meta_venda"] += gasto
            x["compras_meta_venda"] += comp
            x["receita_meta_venda"] += val

    ini, fim = min(novos), max(novos)
    caminho = os.path.join(base, "metricas", "serie", "meta_ads.csv")
    dados = metricas.ler_serie(caminho)
    metricas.gravar_serie(caminho, dados, ini, fim, {d: dict(v) for d, v in novos.items()})
    print("Meta · %d linhas (campanha × dia) · %s a %s → %s" % (len(linhas), ini, fim, os.path.relpath(caminho, RAIZ)))
    print("gasto por objetivo:", {k: round(v, 2) for k, v in objetivos.items()})


if __name__ == "__main__":
    main()
