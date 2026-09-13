from datetime import datetime
import sqlite3
import urllib.request
import urllib.parse
import json


def conectar_bd():
    conexao = sqlite3.connect("ada.db")
    return conexao


def criar_bd():
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chave TEXT NOT NULL,
            valor TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

def guardar_memoria(chave, valor):
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM memoria WHERE chave = ?",
        (chave,)
    )

    resultado = cursor.fetchone()

    if resultado:
        cursor.execute(
            "UPDATE memoria SET valor = ? WHERE chave = ?",
            (valor, chave)
        )
    else:
        cursor.execute(
            "INSERT INTO memoria (chave, valor) VALUES (?, ?)",
            (chave, valor)
        )

    conexao.commit()
    conexao.close()

    return "Informação guardada com sucesso."

def buscar_memoria(chave):
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT valor FROM memoria WHERE chave = ?",
        (chave,)
    )

    resultado = cursor.fetchone()

    conexao.close()

    if resultado:
        return resultado[0]

    return None

def apagar_memoria(chave):
    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM memoria WHERE chave = ?",
        (chave,)
    )

    conexao.commit()

    apagado = cursor.rowcount

    conexao.close()

    if apagado > 0:
        return True

    return False

def dizer_hora():
    hora_atual = datetime.now()
    hora = hora_atual.strftime("%H:%M")
    return f"\nAgora são {hora}.\n"

def dizer_data():
    data_atual = datetime.now()
    data = data_atual.strftime("%d/%m/%Y")
    return f"Hoje é {data}.\n"

def calcular(x, operador, y):

    while True:
        try:
            a = float(x)
            break  # Sai do laço se a conversão para float der certo
        except ValueError:
            return "Número inválido! Por favor, digite apenas números."

    while True:
        try:
            b = float(y)
            break  # Sai do laço se a conversão para float der certo
        except ValueError:
            return "Número inválido! Por favor, digite apenas números."

    if operador == "+":
        return f"O resultado da soma é {a + b}."

    elif operador == "-":
        return f"O resultado da subtração é {a - b}."

    elif operador == "*":
        return f"O resultado da multiplicação é {a * b}."

    elif operador == "/":
        if b == 0:
            return "Não é possível dividir por zero."
        return f"O resultado da divisão é {a / b}."

    else:
        return "Operador inválido."

def pesquisar_internet(pergunta):

    try:

        # Preparar a pergunta
        pergunta_codificada = urllib.parse.quote(pergunta)

        # Pesquisa com região/idioma português
        url = (
            "https://api.duckduckgo.com/"
            f"?q={pergunta_codificada}"
            "&format=json"
            "&no_html=1"
            "&skip_disambig=1"
            "&kl=pt-pt"
        )

        # Fazer o pedido à Internet
        resposta = urllib.request.urlopen(
            url,
            timeout=5
        )

        # Ler os dados recebidos
        dados = json.loads(
            resposta.read().decode("utf-8")
        )

        # Procurar uma resposta direta
        resumo = dados.get("AbstractText")

        if resumo:

            fonte = dados.get(
                "AbstractSource",
                "DuckDuckGo"
            )

            return (
                f"Encontrei esta informação:\n\n"
                f"{resumo}\n\n"
                f"Fonte: {fonte}"
            )

        # Procurar resultados relacionados
        topicos = dados.get(
            "RelatedTopics",
            []
        )

        for topico in topicos:

            if isinstance(topico, dict):

                texto = topico.get("Text")

                if texto:

                    return (
                        "Encontrei esta informação:\n\n"
                        f"{texto}\n\n"
                        "Fonte: DuckDuckGo"
                    )

        # Não encontrou resposta
        return (
            "Não encontrei uma resposta adequada "
            "em português para essa pesquisa."
        )

    except urllib.error.URLError:

        return (
            "Não consigo pesquisar na Internet "
            "porque não existe ligação à Internet "
            "neste momento."
        )

    except TimeoutError:

        return (
            "A pesquisa demorou demasiado tempo. "
            "Verifica a tua ligação à Internet "
            "e tenta novamente."
        )

    except Exception as erro:

        print("Erro na pesquisa:", erro)

        return (
            "Ocorreu um problema ao tentar "
            "pesquisar na Internet."
        )   