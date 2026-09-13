import re
from funcao import *

def responder(mensagem):

    mensagem = mensagem.lower().strip()

        # Verificar se a mensagem é uma operação matemática
    calculo = re.match(r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$", mensagem)

    if calculo:
        numero1 = calculo.group(1)
        operador = calculo.group(2)
        numero2 = calculo.group(3)

        return calcular(numero1, operador, numero2)

        # Detectar cálculos escritos por extenso
    mensagem = mensagem.replace("quanto é", "")
    mensagem = mensagem.replace("quanto e", "")
    mensagem = mensagem.replace("calcula", "")
    mensagem = mensagem.replace("calcule", "")

    mensagem = mensagem.replace("mais", "+")
    mensagem = mensagem.replace("menos", "-")
    mensagem = mensagem.replace("vezes", "*")
    mensagem = mensagem.replace("multiplicado por", "*")
    mensagem = mensagem.replace("dividido por", "/")

    mensagem = mensagem.replace("?", "")
    mensagem = mensagem.strip()

    calculo = re.match(r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$", mensagem)

    if calculo:
        numero1 = calculo.group(1)
        operador = calculo.group(2)
        numero2 = calculo.group(3)

        return calcular(numero1, operador, numero2)

    if mensagem == "sair":
        return "Até logo!"

    elif mensagem in ["olá", "ola", "oi", "bom dia", "boa tarde", "boa noite"]:
        return "Olá! Como estás?"

    elif mensagem in [
        "estas bem?",
        "estás bem?",
        "tudo bem?",
        "tudo ótimo?",
        "tudo otimo?"
    ]:
        return "Estou bem, obrigado!"

    elif mensagem in [
        "que horas são",
        "que horas são agora",
        "me diga as horas",
        "me diga as horas agora"
    ]:
        return dizer_hora()

    elif mensagem in [
        "que dia é hoje",
        "qual é a data de hoje",
        "me diga a data de hoje"
    ]:
        return dizer_data()

    elif mensagem in [
        "quem es",
        "quem és",
        "qual e o teu nome",
        "qual é o teu nome",
        "quem és tu",
        "quem é você"
    ]:
        return (
            "O meu nome é ADA. "
            "ADA significa Assistente Digital Autónoma. "
            "Estou em desenvolvimento e vou aprender "
            "novas funcionalidades ao longo do tempo."
        )

    elif mensagem.startswith("guardar "):
        dados = mensagem.replace("guardar ", "", 1)

        if " como " in dados:
            chave, valor = dados.split(" como ", 1)

            chave = chave.strip()
            valor = valor.strip()

            guardar_memoria(chave, valor)

            return f"Guardei que {chave} é {valor}."

        return "Para guardar uma informação, escreva por exemplo: guardar nome como Danilo."

    elif mensagem.startswith("qual é "):
        chave = mensagem.replace("qual é ", "", 1).strip()

        valor = buscar_memoria(chave)

        if valor:
            return f"O {chave} é {valor}."

        return f"Não tenho nenhuma informação guardada sobre {chave}."

    elif mensagem.startswith("apagar "):
        chave = mensagem.replace("apagar ", "", 1).strip()

        if apagar_memoria(chave):
            return f"Apaguei a informação sobre {chave}."

        return f"Não encontrei nenhuma informação sobre {chave}."

    elif mensagem.startswith("pesquisar "):

        pergunta = mensagem.replace(
            "pesquisar ",
            "",
            1
        ).strip()

        if pergunta == "":
            return "O que queres que eu pesquise?"

        return pesquisar_internet(pergunta)


    elif mensagem.startswith("pesquisa "):

        pergunta = mensagem.replace(
            "pesquisa ",
            "",
            1
        ).strip()

        if pergunta == "":
            return "O que queres que eu pesquise?"

        return pesquisar_internet(pergunta)


    elif mensagem.startswith("procura "):

        pergunta = mensagem.replace(
            "procura ",
            "",
            1
        ).strip()

        if pergunta == "":
            return "O que queres que eu pesquise?"

        return pesquisar_internet(pergunta)


    else:
        return "Não entendi a pergunta."


criar_bd()  # Chama a função para criar o banco de dados ao iniciar o programa