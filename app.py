from flask import Flask, render_template, request, jsonify

from main import responder

from funcao import (
    criar_bd,
    criar_conversa,
    listar_conversas,
    buscar_historico,
    guardar_historico,
    apagar_conversa
)


app = Flask(__name__)


# Criar as tabelas quando a aplicação iniciar
criar_bd()


# ==========================================================
# PÁGINA PRINCIPAL
# ==========================================================

@app.route("/")
def inicio():

    return render_template("index.html")


# ==========================================================
# CHAT
# ==========================================================

@app.route("/chat", methods=["POST"])
def chat():

    dados = request.get_json()

    mensagem = dados.get(
        "mensagem",
        ""
    )

    conversa_id = dados.get(
        "conversa_id"
    )

    # Se não existir uma conversa,
    # criar automaticamente.
    if not conversa_id:

        conversa_id = criar_conversa()

    # ADA responde
    resposta = responder(mensagem)

    # Guardar no histórico
    guardar_historico(
        conversa_id,
        mensagem,
        resposta
    )

    return jsonify({
        "resposta": resposta,
        "conversa_id": conversa_id
    })


# ==========================================================
# CRIAR NOVA CONVERSA
# ==========================================================

@app.route("/conversa", methods=["POST"])
def nova_conversa():

    conversa_id = criar_conversa()

    return jsonify({
        "id": conversa_id,
        "titulo": "Nova conversa"
    })


# ==========================================================
# LISTAR CONVERSAS
# ==========================================================

@app.route("/conversas", methods=["GET"])
def conversas():

    return jsonify(
        listar_conversas()
    )


# ==========================================================
# CARREGAR UMA CONVERSA
# ==========================================================

@app.route("/conversa/<int:conversa_id>", methods=["GET"])
def carregar_conversa(conversa_id):

    historico = buscar_historico(
        conversa_id
    )

    return jsonify({
        "historico": historico
    })


# ==========================================================
# APAGAR CONVERSA
# ==========================================================

@app.route(
    "/conversa/<int:conversa_id>",
    methods=["DELETE"]
)
def eliminar_conversa(conversa_id):

    apagada = apagar_conversa(
        conversa_id
    )

    return jsonify({
        "sucesso": apagada
    })


# ==========================================================
# INICIAR SERVIDOR
# ==========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )