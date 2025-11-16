# ----------------------------------------------
# 🤖 PITOKO WEB - Atendente Virtual da Pit Shop
# Flask + OpenAI + Google Docs
# ----------------------------------------------

from flask import Flask, render_template, request, jsonify
import openai
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# ----------------------------------------------
# CONFIGURAÇÕES INICIAIS
# ----------------------------------------------

app = Flask(__name__)

# 🔹 Sua chave da OpenAI (no Replit, coloque em Secrets)
openai.api_key = os.getenv("OPENAI_API_KEY")

import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import os

# 🔹 Credenciais do Google (armazenadas em variável de ambiente)
GOOGLE_CRED_JSON = os.getenv("GOOGLE_CRED_JSON")
GOOGLE_DOC_ID = "1mrT9TV560XuHaYx329vtWLhoI0mG6hnIC-IBEYZWoF4"

# ----------------------------------------------
# FUNÇÃO: Ler o conteúdo do documento do Google Docs
# ----------------------------------------------
def ler_documento_google_docs(document_id):
    # Converte o JSON em dicionário Python
    cred_info = json.loads(GOOGLE_CRED_JSON)

    creds = service_account.Credentials.from_service_account_info(
        cred_info,
        scopes=["https://www.googleapis.com/auth/documents.readonly"]
    )

    service = build("docs", "v1", credentials=creds)
    document = service.documents().get(documentId=document_id).execute()

    conteudo = ""
    for elemento in document.get("body", {}).get("content", []):
        if "paragraph" in elemento:
            for item in elemento["paragraph"].get("elements", []):
                if "textRun" in item:
                    conteudo += item["textRun"].get("content", "")

    return conteudo


# ----------------------------------------------
# FUNÇÃO: Gerar resposta do Pitoko via OpenAI
# ----------------------------------------------
def gerar_resposta_pitoko(pergunta, contexto_documento):
    sistema = (
        "Você é Pitoko, o atendente virtual simpático e alegre da Pit Shop, "
        "uma clínica veterinária e pet shop especializada em produtos para animais domésticos. "
        "Você sempre fala de forma acolhedora e gentil, incentivando o cuidado e o amor pelos pets. "
        "Use as informações abaixo sobre os produtos, preços, horários e localização para responder de forma útil e simpática. "
        "Se a pergunta não estiver relacionada à Pit Shop, responda brevemente e traga a conversa de volta aos cuidados com os animais."
    )

    prompt = f"""
Informações da Pit Shop (extraídas do Google Docs):
{contexto_documento}

Pergunta do cliente:
{pergunta}
"""

    resposta = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": sistema},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return resposta.choices[0].message.content.strip()

# ----------------------------------------------
# ROTAS FLASK
# ----------------------------------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/pitoko', methods=['POST'])
def api_pitoko():
    dados = request.get_json()
    pergunta = dados.get('pergunta', '')

    try:
        contexto = ler_documento_google_docs(GOOGLE_DOC_ID)
        resposta = gerar_resposta_pitoko(pergunta, contexto)
        return jsonify({'resposta': resposta})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# ----------------------------------------------
# EXECUTAR APLICAÇÃO
# ----------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
