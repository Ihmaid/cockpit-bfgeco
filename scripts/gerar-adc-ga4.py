r"""Gera o refresh token de LEITURA do GA4 e grava a credencial local que o scripts/ga4.py usa.

Copia adaptada de scripts/gerar-adc-google-ads.py. Mesmo cliente OAuth, mesmo projeto do
Cloud, outro escopo e outro arquivo -- para nao mexer na credencial do Google Ads, que o MCP
oficial usa e que esta funcionando desde 10/09.

Como rodar (PowerShell, na pasta do projeto):

    uv run --with google-auth-oauthlib python scripts/gerar-adc-ga4.py

Por padrao reaproveita o Client ID e o Secret de %USERPROFILE%\.config\google-ads\adc.json
(e o mesmo cliente OAuth). Para usar outro cliente: --cliente-de-env, com
GOOGLE_OAUTH_CLIENT_ID / GOOGLE_OAUTH_CLIENT_SECRET no ambiente, ou digitando no prompt.

O navegador abre, voce autoriza com a conta que tem acesso de Leitor na propriedade GA4,
e o arquivo e escrito em:

    %USERPROFILE%\.config\ga4\adc.json

Nada e enviado para fora: o unico destino do token e o arquivo local. Nada e impresso.

Levantado em 28/09/2026. Ver docs/25-ga4-credencial.md
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Somente leitura. Serve para a Data API (relatorios) e para a Admin API (listar propriedades).
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

HOME = Path(os.path.expanduser("~"))
ADC_GOOGLE_ADS = HOME / ".config" / "google-ads" / "adc.json"
DESTINO_PADRAO = HOME / ".config" / "ga4" / "adc.json"


def cliente_do_google_ads() -> tuple[str, str]:
    if not ADC_GOOGLE_ADS.exists():
        sys.exit(
            f"ERRO: nao achei {ADC_GOOGLE_ADS}. Rode com --cliente-de-env e informe o "
            "Client ID e o Secret do cliente OAuth do projeto do Cloud."
        )
    dados = json.loads(ADC_GOOGLE_ADS.read_text(encoding="utf-8"))
    cid, secret = dados.get("client_id", ""), dados.get("client_secret", "")
    if not cid or not secret:
        sys.exit(f"ERRO: {ADC_GOOGLE_ADS} nao tem client_id/client_secret. Use --cliente-de-env.")
    print(f"  Cliente OAuth: reaproveitado de {ADC_GOOGLE_ADS}")
    return cid, secret


def pedir(nome: str, env_var: str) -> str:
    valor = os.environ.get(env_var, "").strip()
    if valor:
        print(f"  {nome}: lido de {env_var}")
        return valor
    try:
        valor = input(f"  Cole o {nome}: ").strip()
    except EOFError:
        sys.exit(f"ERRO: {nome} nao informado. Defina {env_var} ou rode num terminal interativo.")
    if not valor:
        sys.exit(f"ERRO: {nome} vazio. Abortado.")
    return valor


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera a credencial de leitura do GA4.")
    parser.add_argument("--port", type=int, default=0,
                        help="porta do redirect. 0 (padrao) = aleatoria, para cliente Desktop app")
    parser.add_argument("--destino", default=str(DESTINO_PADRAO),
                        help=f"arquivo de saida (padrao: {DESTINO_PADRAO})")
    parser.add_argument("--cliente-de-env", action="store_true",
                        help="nao reaproveitar o cliente do Google Ads; ler de env ou do prompt")
    args = parser.parse_args()

    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit("ERRO: rode assim: uv run --with google-auth-oauthlib python scripts/gerar-adc-ga4.py")

    print()
    print("=== Gerar credencial de leitura do GA4 ===")
    print()
    if args.cliente_de_env:
        client_id = pedir("Client ID", "GOOGLE_OAUTH_CLIENT_ID")
        client_secret = pedir("Client Secret", "GOOGLE_OAUTH_CLIENT_SECRET")
    else:
        client_id, client_secret = cliente_do_google_ads()

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

    print()
    print("  Abrindo o navegador. Autorize com a conta que tem acesso de Leitor")
    print("  na propriedade GA4 do cliente.")
    print("  Se aparecer 'O Google nao verificou este app': Avancado > Acessar (app proprio).")
    print("  Se aparecer 'redirect_uri_mismatch': ver docs/17, secao do tipo do cliente OAuth.")
    print()

    # prompt="consent" forca a tela e garante o refresh_token (ver o script do Google Ads).
    creds = flow.run_local_server(port=args.port, access_type="offline",
                                  prompt="consent", open_browser=True)

    if not creds.refresh_token:
        sys.exit("ERRO: o Google nao devolveu refresh_token. Remova o acesso do app em "
                 "https://myaccount.google.com/permissions e rode de novo.")

    adc = {
        "type": "authorized_user",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": creds.refresh_token,
    }
    destino = Path(args.destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(adc, indent=2) + "\n", encoding="utf-8")

    concedidos = " ".join(getattr(creds, "granted_scopes", None) or creds.scopes or [])
    print()
    print("OK. Credencial escrita em:")
    print(f"  {destino}")
    print(f"Escopos concedidos: {concedidos}")
    if "analytics.readonly" not in concedidos:
        print()
        print("ATENCAO: analytics.readonly NAO aparece. A leitura vai falhar. Rode de novo.")
    print()
    print("Proximo passo: uv run python scripts/ga4.py --propriedades")
    print()


if __name__ == "__main__":
    main()
