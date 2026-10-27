# -*- coding: utf-8 -*-
"""
Cria a pasta de um cliente novo no padrão do sistema (docs/sistema.md §3), a partir de templates/cliente/.

    uv run --with pyyaml python scripts/novo_cliente.py la-plata "La Plata"

Copia cliente.md e contexto/00..09 trocando <slug> e <Nome>, e cria as pastas vazias do padrão. Não sobrescreve
nada: se a pasta do cliente já existe, para. Depois: preencher o cliente.md (contas, motores) com o Claude.
"""
import argparse, datetime as dt, io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELO = os.path.join(RAIZ, "templates", "cliente")
PASTAS = ["planos", "projetos", "testes", "midia", "reunioes/sprint", "reunioes/checkin", "metricas/serie",
          "diagnosticos", "checkin"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="minúsculas e hífen, igual ao compartilhado/carteira.yaml")
    ap.add_argument("nome")
    a = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug):
        sys.exit("slug inválido: use minúsculas, números e hífen")
    destino = os.path.join(RAIZ, "clientes", a.slug)
    if os.path.exists(destino):
        sys.exit("já existe: %s (nada foi alterado)" % os.path.relpath(destino, RAIZ))
    hoje = dt.date.today().isoformat()
    criados = []
    for raiz, _, arquivos in os.walk(MODELO):
        for nome in arquivos:
            origem = os.path.join(raiz, nome)
            alvo = os.path.join(destino, os.path.relpath(origem, MODELO))
            os.makedirs(os.path.dirname(alvo), exist_ok=True)
            txt = io.open(origem, encoding="utf-8").read()
            txt = txt.replace("<slug>", a.slug).replace("<Nome>", a.nome).replace("AAAA-MM-DD", hoje)
            io.open(alvo, "w", encoding="utf-8", newline="\n").write(txt)
            criados.append(os.path.relpath(alvo, RAIZ))
    for p in PASTAS:
        os.makedirs(os.path.join(destino, p), exist_ok=True)
        io.open(os.path.join(destino, p, ".gitkeep"), "w").close()
    print("criado clientes/%s/ com %d arquivos e %d pastas" % (a.slug, len(criados), len(PASTAS)))
    print("próximo: preencher cliente.md (contas e motores) e conferir o slug em compartilhado/carteira.yaml")


if __name__ == "__main__":
    main()
