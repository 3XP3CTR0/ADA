# chatbot.py
from datetime import datetime
from funcao import *

print("ADA iniciando....")
print("Olá! Eu sou a ADA. Como posso ajudar você hoje Danilo?")
print("Digite 'sair' para terminar.\n")

while True:
    mensagem = input("Você: ").lower()

    if mensagem == "sair":
        print("ADA: Até logo!")
        break

    elif mensagem in ["olá", "ola", "oi", "bom dia", "boa tarde", "boa noite"]:
        print("\nADA: Olá! Como estás?\n")

    elif mensagem in ["estas bem?", "estás bem?", "tudo bem?", "tudo ótimo?", "tudo otimo?"]:
        print("\nADA: Estou bem, obrigado!\n")

    elif mensagem in ["que horas são", "que horas são agora", "me diga as horas", "me diga as horas agora"]:
        print(dizer_hora())

    elif mensagem in ["que dia é hoje", "qual é a data de hoje", "me diga a data de hoje"]:
        print(dizer_data())

    elif mensagem in ["quem es", "quem és", "qual e o teu nome", "qual é o teu nome", "quem és tu", "quem é você"]:
        print("\nADA: O meu nome é ADA.")
        print("ADA: ADA significa Assistente Digital Autónoma.")
        print("ADA: Estou em desenvolvimento e vou aprender novas funcionalidades ao longo do tempo.\n")

    else:
        print("\nADA: Não entendi a pergunta.\n")