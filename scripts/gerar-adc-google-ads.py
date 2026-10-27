r"""Gera o refresh token do Google Ads e escreve o arquivo ADC que o MCP oficial consome.

O servidor MCP oficial (googleads/google-ads-mcp) NAO le google-ads.yaml: ele usa
Application Default Credentials. Este script faz o fluxo OAuth com o Client ID/Secret
do Google Cloud e grava o JSON no formato "authorized_user" que a ADC entende.

Como rodar (PowerShell, na pasta do projeto):

    # cliente OAuth do tipo Desktop app (porta aleatoria)
    uv run --with google-auth-oauthlib python scripts/gerar-adc-google-ads.py

    # cliente OAuth do tipo Web application (porta fixa, tem que estar cadastrada)
    uv run --with google-auth-oauthlib python scripts/gerar-adc-google-ads.py --port 8080

O navegador abre, voce autoriza com a conta que tem acesso as contas de anuncio,
e o arquivo e escrito em:

    %USERPROFILE%\.config\google-ads\adc.json

O Client ID e o Secret podem vir de variavel de ambiente
(GOOGLE_OAUTH_CLIENT_ID / GOOGLE_OAUTH_CLIENT_SECRET) ou serem digitados no prompt.
Nada e enviado para fora: o unico destino do token e o arquivo local.

Levantado em 10/09/2026. Ver docs/integracoes/google-ads.md
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Unico escopo necessario. O Google Ads nao publica escopo separado de leitura --
# a restricao a leitura vem das ferramentas que o servidor MCP expoe.
SCOPES = ["https://www.googleapis.com/auth/adwords"]

DESTINO_PADRAO = Path(os.path.expanduser("~")) / ".config" / "google-ads" / "adc.json"


def pedir(nome: str, env_var: str) -> str:
    valor = os.environ.get(env_var, "").strip()
    if valor:
        print(f"  {nome}: lido de {env_var}")
        return valor
    try:
        valor = input(f"  Cole o {nome}: ").strip()
    except EOFError:
        sys.exit(
            f"ERRO: {nome} nao informado. Rode num terminal interativo, ou "
            f"defina a variavel de ambiente {env_var} antes de rodar."
        )
    if not valor:
        sys.exit(f"ERRO: {nome} vazio. Abortado.")
    return valor


def avisar_sobre_redirect(port: int) -> None:
    """Explica o redirect_uri antes de abrir o navegador.

    redirect_uri_mismatch e o erro mais comum aqui, e ele acontece no navegador --
    o script nao consegue captura-lo. Por isso o aviso vem antes.
    """
    print()
    if port == 0:
        print("  Porta: aleatoria.")
        print("  Isso funciona com cliente OAuth do tipo 'Desktop app', que aceita")
        print("  qualquer porta em localhost.")
        print()
        print("  Se o navegador mostrar 'Erro 400: redirect_uri_mismatch', o cliente")
        print("  e do tipo 'Web application'. Duas saidas:")
        print("    a) criar um cliente novo do tipo Desktop app (recomendado), ou")
        print("    b) rodar de novo com --port 8080 e cadastrar a URI no Cloud Console")
    else:
        print(f"  Porta fixa: {port}")
        print("  A URI abaixo precisa estar cadastrada no cliente OAuth, em")
        print("  'URIs de redirecionamento autorizados':")
        print()
        print(f"      http://localhost:{port}/")
        print()
        print("  Cadastre TAMBEM a versao sem barra final, por seguranca:")
        print(f"      http://localhost:{port}")
        print()
        print("  Alteracao de URI no Cloud Console pode levar alguns minutos para valer.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gera a credencial ADC do Google Ads para o servidor MCP oficial."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("GOOGLE_OAUTH_PORT", "0")),
        help=(
            "porta local do redirect. 0 (padrao) = aleatoria, para cliente OAuth "
            "do tipo Desktop app. Use 8080 para cliente do tipo Web application, "
            "cadastrando http://localhost:8080/ no Cloud Console."
        ),
    )
    parser.add_argument(
        "--destino",
        default=str(DESTINO_PADRAO),
        help=f"caminho do arquivo ADC de saida (padrao: {DESTINO_PADRAO})",
    )
    args = parser.parse_args()

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit(
            "ERRO: google-auth-oauthlib nao encontrado. Rode assim: "
            "uv run --with google-auth-oauthlib python scripts/gerar-adc-google-ads.py"
        )

    print()
    print("=== Gerar credencial ADC para o Google Ads MCP ===")
    print()
    client_id = pedir("Client ID", "GOOGLE_OAUTH_CLIENT_ID")
    client_secret = pedir("Client Secret", "GOOGLE_OAUTH_CLIENT_SECRET")

    # O bloco "installed" serve tanto para cliente Desktop quanto para Web -- o que
    # muda entre eles nao e este dicionario, e sim se o Google exige que a URI de
    # redirecionamento esteja previamente cadastrada.
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [f"http://localhost:{args.port}/"],
        }
    }

    flow = InstalledAppFlow.from_client_config(client_config, scopes=SCOPES)

    avisar_sobre_redirect(args.port)

    print()
    print("  Abrindo o navegador. Autorize com a conta que tem acesso as contas")
    print("  de anuncio dos clientes (a que enxerga a MCC).")
    print()

    # prompt="consent" forca a tela de autorizacao; sem isso o Google pode devolver
    # a sessao sem refresh_token quando o app ja foi autorizado antes.
    creds = flow.run_local_server(
        port=args.port,
        access_type="offline",
        prompt="consent",
        open_browser=True,
    )

    if not creds.refresh_token:
        sys.exit(
            "ERRO: o Google nao devolveu refresh_token. Causa usual: o app ja "
            "estava autorizado nesta conta. Remova o acesso em "
            "https://myaccount.google.com/permissions e rode de novo."
        )

    # Formato "authorized_user" -- o que google.auth.default() espera de uma ADC
    # de usuario. Nao inclui developer token nem MCC: esses vao por env var.
    adc = {
        "type": "authorized_user",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": creds.refresh_token,
    }

    destino = Path(args.destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(adc, indent=2) + "\n", encoding="utf-8")

    # "granted_scopes" e o que o Google concedeu; "scopes" e o que foi pedido.
    # Ler o campo errado da um falso negativo -- acontece.
    concedidos = getattr(creds, "granted_scopes", None) or creds.scopes or []
    escopos = " ".join(concedidos)
    print()
    print("OK. Credencial escrita em:")
    print(f"  {destino}")
    print()
    print(f"Escopos concedidos: {escopos}")
    if "adwords" not in escopos:
        print()
        print("ATENCAO: o escopo adwords NAO aparece na lista. A credencial vai")
        print("autenticar e falhar na primeira consulta. Rode de novo.")
    print()
    print("Proximo passo: o claude mcp add da Parte C do")
    print("docs/integracoes/google-ads.md")
    print()


if __name__ == "__main__":
    main()
