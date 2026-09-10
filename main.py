import re
from funcao import *

def responder(mensagem):

    mensagem = mensagem.lower().strip()

        # Verificar se a mensagem é uma operação matemática
    calculo = re.match(r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)\s*$", mensagem
    )

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

    else:
        return "Não entendi a pergunta."