#!/usr/bin/env python3
"""
Monta o HTML final do check-in.

Junta o template base (CSS + JS + shell) com o corpo escrito para o periodo e
embute as imagens dos criativos em base64, ja tratadas para caber no card
quadrado sem cortar o conteudo (fundo desfocado da propria peca).

Uso:
    python3 montar.py corpo.html saida.html --titulo "Check-in de Setembro — Cliente"

No corpo, referencie cada imagem assim:

    <img src="IMG:/caminho/para/print.png" alt="...">

O script troca isso por um data URI. Qualquer src que nao comece com "IMG:"
fica intacto.
"""
import argparse
import base64
import io
import os
import re
import sys

LADO = 620
QUALIDADE = 82


def preparar(caminho, lado=LADO, qualidade=QUALIDADE):
    """Transforma a imagem num quadrado: peca inteira centralizada sobre um
    fundo desfocado dela mesma. Prints de Stories (9:16) nao perdem conteudo."""
    from PIL import Image, ImageFilter

    im = Image.open(caminho).convert("RGB")
    w, h = im.size

    escala_fundo = max(lado / w, lado / h) * 1.25
    fundo = im.resize((int(w * escala_fundo), int(h * escala_fundo)), Image.LANCZOS)
    fundo = fundo.filter(ImageFilter.GaussianBlur(28))
    bw, bh = fundo.size
    esq, topo = (bw - lado) // 2, (bh - lado) // 2
    fundo = fundo.crop((esq, topo, esq + lado, topo + lado))
    fundo = Image.blend(fundo, Image.new("RGB", (lado, lado), (14, 14, 14)), 0.45)

    escala = min(lado / w, lado / h)
    frente = im.resize((int(w * escala), int(h * escala)), Image.LANCZOS)
    fundo.paste(frente, ((lado - frente.width) // 2, (lado - frente.height) // 2))

    buf = io.BytesIO()
    fundo.save(buf, "JPEG", quality=qualidade, optimize=True)
    return base64.b64encode(buf.getvalue()).decode()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("corpo", help="arquivo HTML com o corpo do check-in")
    p.add_argument("saida", help="caminho do HTML final")
    p.add_argument("--titulo", required=True, help="titulo da aba do navegador")
    p.add_argument(
        "--template",
        default=os.path.join(os.path.dirname(__file__), "..", "assets", "template-base.html"),
    )
    a = p.parse_args()

    with open(a.template, encoding="utf-8") as f:
        tpl = f.read()
    with open(a.corpo, encoding="utf-8") as f:
        corpo = f.read()

    faltando = []

    def troca(m):
        caminho = m.group(1)
        if not os.path.exists(caminho):
            faltando.append(caminho)
            return m.group(0)
        return 'src="data:image/jpeg;base64,%s"' % preparar(caminho)

    corpo, n = re.subn(r'src="IMG:([^"]+)"', troca, corpo)

    if faltando:
        sys.exit("Imagens nao encontradas:\n  " + "\n  ".join(faltando))

    html = tpl.replace("__TITULO__", a.titulo).replace("<!--__BODY__-->", corpo)

    if "__TITULO__" in html or "<!--__BODY__-->" in html:
        sys.exit("Template invalido: marcadores nao foram substituidos.")

    os.makedirs(os.path.dirname(os.path.abspath(a.saida)), exist_ok=True)
    with open(a.saida, "w", encoding="utf-8") as f:
        f.write(html)

    print("OK  %s  %.1f KB  %d imagem(ns) embutida(s)" % (a.saida, len(html) / 1024, n))


if __name__ == "__main__":
    main()
