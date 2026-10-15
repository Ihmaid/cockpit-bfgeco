#!/usr/bin/env python3
"""
Confere o HTML gerado antes de entregar.

Pega os erros que passam despercebidos na leitura: tag aberta e nao fechada,
link do menu apontando para uma secao que nao existe, marcador de template
esquecido, imagem que nao foi embutida.

Uso:
    python3 conferir.py saida.html
"""
import re
import sys


def main(caminho):
    h = open(caminho, encoding="utf-8").read()
    erros, avisos = [], []

    ids = re.findall(r'<section id="([^"]+)"', h)
    alvos = set(re.findall(r'href="#([^"]+)"', h))
    orfaos = sorted(a for a in alvos if a not in ids)
    if orfaos:
        erros.append("links do menu sem secao correspondente: %s" % ", ".join(orfaos))

    for tag in ("div", "section", "table", "tbody", "thead", "tfoot", "ul"):
        d = len(re.findall(r"<%s[\s>]" % tag, h)) - h.count("</%s>" % tag)
        if d:
            erros.append("tag <%s> desbalanceada (%+d)" % (tag, d))

    for marcador in ("__TITULO__", "<!--__BODY__-->", "__IMG", "IMG:"):
        if marcador in h:
            erros.append("marcador nao substituido no arquivo: %s" % marcador)

    if not h.rstrip().endswith("</html>"):
        erros.append("arquivo nao termina em </html> — o bloco <script> pode ter se perdido")

    if 'data:image/jpeg;base64' not in h and '<img' in h:
        avisos.append("ha <img> mas nenhuma imagem embutida em base64")

    tam = len(h.encode()) / 1024 / 1024
    if tam > 16:
        erros.append("arquivo com %.1f MB — acima do limite de 16 MB" % tam)

    print("Secoes (%d): %s" % (len(ids), ", ".join(ids)))
    print("Tamanho: %.2f MB" % tam)
    for a in avisos:
        print("AVISO  " + a)
    for e in erros:
        print("ERRO   " + e)
    print("\n%s" % ("FALHOU" if erros else "OK"))
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
