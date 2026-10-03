import re
from funcao import *

# ==========================================================
# RESPOSTAS DE CONVERSAÇÃO
# ==========================================================

def resposta_saudacao():

    respostas = [
        "Olá! 👋 Como posso ajudar?",
        "Oi! 😊 Em que posso ajudar?",
        "Olá! É bom falar contigo. 😄",
        "Hey! 👋 O que vamos fazer hoje?",
        "Olá! Tudo pronto por aqui. O que precisas?"
    ]

    # Escolhe uma resposta aleatória
    import random

    return random.choice(respostas)


def resposta_tudo_bem():

    respostas = [
        "Estou bem! 😊 E contigo?",
        "Tudo ótimo por aqui! 😄",
        "Estou muito bem, obrigado por perguntares!",
        "Tudo tranquilo por aqui. Como posso ajudar?"
    ]

    import random

    return random.choice(respostas)


def resposta_como_estou():

    respostas = [
        "Estou bem! 😊 Obrigado por perguntares.",
        "Estou ótima e pronta para ajudar! 🤖",
        "Tudo bem por aqui! O que precisas?"
    ]

    import random

    return random.choice(respostas)

def responder(mensagem):

    mensagem = mensagem.lower().strip()

    # ==========================================================
    # PESQUISA NA INTERNET
    # ==========================================================

    comandos_pesquisa = [
        "pesquisa ",
        "pesquisar ",
        "procura ",
        "procurar ",
        "procure "
    ]

    for comando in comandos_pesquisa:

        if mensagem.startswith(comando):

            pergunta = mensagem[len(comando):].strip()

            # Remove "sobre" ou "informações sobre"
            if pergunta.startswith("sobre "):

                pergunta = pergunta.replace(
                    "sobre ",
                    "",
                    1
                ).strip()

            elif pergunta.startswith("informações sobre "):

                pergunta = pergunta.replace(
                    "informações sobre ",
                    "",
                    1
                ).strip()

            if not pergunta:

                return (
                    "🔎 O que gostarias que eu pesquisasse?"
                )

            return pesquisar_internet(pergunta)

        # Verificar se a mensagem é uma operação matemática
    calculo = re.match(r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/^])\s*(-?\d+(?:\.\d+)?)\s*$", mensagem)

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

    calculo = re.match(r"^\s*(-?\d+(?:\.\d+)?)\s*([+\-*/^])\s*(-?\d+(?:\.\d+)?)\s*$", mensagem)

    if calculo:
        numero1 = calculo.group(1)
        operador = calculo.group(2)
        numero2 = calculo.group(3)

        return calcular(numero1, operador, numero2)

    # ==========================================================
    # PERCENTAGEM
    # ==========================================================

    calculo_percentagem = re.match(
        r"^(-?\d+(?:\.\d+)?)%\s+de\s+(-?\d+(?:\.\d+)?)$",
        mensagem
    )

    if calculo_percentagem:

        percentagem = calculo_percentagem.group(1)

        numero = calculo_percentagem.group(2)

        return calcular_percentagem(
            percentagem,
            numero
        )

    # ==========================================================
    # RAIZ QUADRADA
    # ==========================================================

    if mensagem.startswith("raiz de "):

        numero = mensagem.replace(
            "raiz de ",
            "",
            1
        ).strip()

        return calcular_raiz(numero)


    elif mensagem.startswith("raiz quadrada de "):

        numero = mensagem.replace(
            "raiz quadrada de ",
            "",
            1
        ).strip()

        return calcular_raiz(numero)

    elif mensagem.startswith("√"):

        numero = mensagem.replace(
            "√",
            "",
            1
        ).strip()

        return calcular_raiz(numero)

        # ==========================================================
    # CONVERSAÇÃO
    # ==========================================================

    # DESPEDIDA
    elif re.fullmatch(
        r"(adeus|tchau|até logo|ate logo|até breve|ate breve|xau)[!.]?",
        mensagem
    ):
        return "Até logo! 👋"


    # SAUDAÇÕES
    elif re.fullmatch(
        r"(oi|olá|ola|oie|hey|hello|hi)[!.]?",
        mensagem
    ):
        return resposta_saudacao()


    # SAUDAÇÃO + ADA
    elif re.fullmatch(
        r"(oi|olá|ola|oie|hey|hello|hi)\s+ada[!.]?",
        mensagem
    ):
        return resposta_saudacao()


    # BOM DIA / BOA TARDE / BOA NOITE
    elif re.fullmatch(
        r"(bom dia|boa tarde|boa noite)[!.]?",
        mensagem
    ):
        if mensagem.startswith("bom dia"):
            return "Bom dia! ☀️ Como posso ajudar?"

        elif mensagem.startswith("boa tarde"):
            return "Boa tarde! 😊 Em que posso ajudar?"

        else:
            return "Boa noite! 🌙 Como posso ajudar?"


    # E AÍ
    elif re.fullmatch(
        r"e\s+a[ií][!.]?",
        mensagem
    ):
        return "E aí! 😄 O que precisas?"


    # TUDO BEM / TUDO BOM
    elif re.fullmatch(
        r"(tudo bem|tudo bom)[?!.]?",
        mensagem
    ):
        return resposta_tudo_bem()


    # COMO ESTÁS
    elif re.fullmatch(
        r"(como estás|como estas|estás bem|estas bem|como vai)[?!.]?",
        mensagem
    ):
        return resposta_como_estou()

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
        return ajuda()
    
    else:
        return (
            "Ainda não sei responder a isso. 🤔\n"
            "Podes tentar perguntar de outra forma ou escrever "
            "'ajuda' para veres o que consigo fazer."
        )

