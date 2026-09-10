from flask import Flask, render_template, request, jsonify
from main import responder

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    dados = request.get_json()

    mensagem = dados.get("mensagem", "")

    resposta = responder(mensagem)

    return jsonify({
        "resposta": resposta
    })


if __name__ == "__main__":
    app.run(debug=True)