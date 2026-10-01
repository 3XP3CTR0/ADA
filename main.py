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

    elif mensagem in [
        "olá",
        "ola",
        "oi",
        "oie",
        "hey",
        "hello",
        "hi",
        "bom dia",
        "boa tarde",
        "boa noite",
        "e aí",
        "e ai",
        "tudo bem",
        "tudo bom"
    ]:
        return "Olá! 👋 Como estás?"

    elif mensagem in [
        "estas bem?",
        "estás bem?",
        "tudo bem?",
        "tudo ótimo?",
        "tudo otimo?"
    ]:
        return "Estou bem, obrigado!"

    elif any(palavra in mensagem for palavra in [
        "hora",
        "horas",
        "que horas",
        "diz-me as horas",
        "diga-me as horas",
        "sabes que horas",
        "qual é a hora",
        "qual a hora"
    ]):
        return dizer_hora()

    elif any(frase in mensagem for frase in [
        "que dia é hoje",
        "qual é a data",
        "qual a data",
        "data de hoje",
        "diz-me a data",
        "diga-me a data",
        "que dia estamos",
        "em que dia estamos"
    ]):
        return dizer_data()

    elif mensagem in [
        "quem es",
        "quem és",
        "quem és tu",
        "quem e voce",
        "quem é você",
        "qual e o teu nome",
        "qual é o teu nome",
        "como te chamas",
        "como você se chama",
        "qual é o teu nome?",
        "qual e o teu nome?",
        "o que é a ada",
        "o que e a ada",
        "o que significa ada"
    ]:
        return (
            "O meu nome é ADA. "
            "ADA significa Assistente Digital Autónoma. "
            "Estou em desenvolvimento e vou aprender "
            "novas funcionalidades ao longo do tempo."
        )

    elif mensagem.startswith("guardar "):

        dados = mensagem.replace(
            "guardar ",
            "",
            1
        ).strip()

        if " como " in dados:

            chave, valor = dados.split(
                " como ",
                1
            )

            chave = chave.strip()
            valor = valor.strip()

            guardar_memoria(
                chave,
                valor
            )

            return f"Guardei que {chave} é {valor}."

        return (
            "Para guardar uma informação, "
            "escreve por exemplo: "
            "guardar nome como Danilo."
        )


    elif mensagem.startswith("lembra-te que "):

        dados = mensagem.replace(
            "lembra-te que ",
            "",
            1
        ).strip()


        if " é " in dados:

            chave, valor = dados.split(
                " é ",
                1
            )

            chave = chave.strip()
            valor = valor.strip()

            guardar_memoria(
                chave,
                valor
            )

            return f"Vou lembrar-me que {chave} é {valor}."

        return (
            "Diz-me o que queres que eu memorize. "
            "Por exemplo: lembra-te que o meu nome é Danilo."
        )

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

    elif mensagem in ["ajuda", "help", "o que podes fazer", "o que você pode fazer"]:
        return """
        🤖 Posso ajudar-te com:

        💬 Conversação
        - olá
        - como estás?
        - quem és?

        🧮 Calculadora
        - 10 + 5
        - 20 * 4
        - quanto é 50 dividido por 2?

        🕐 Hora e Data
        - que horas são?
        - que dia é hoje?

        🧠 Memória
        - guardar nome como Danilo
        - qual é nome
        - apagar nome

        🌐 Internet
        - pesquisar Python
        - pesquisar notícias sobre tecnologia
        - procura informações sobre Flask

        💾 Conversas
        - As conversas são guardadas automaticamente.

        💡 Experimenta escrever uma das opções acima!
        """

    else:
        return "Não entendi a pergunta."

