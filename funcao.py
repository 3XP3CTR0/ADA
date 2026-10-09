from datetime import datetime
import sqlite3
import urllib.request
import urllib.parse
import urllib.error
import json
import math
import os
import subprocess
from pathlib import Path

# ==========================================================
# BASE DE DADOS
# ==========================================================

def conectar_bd():
    conexao = sqlite3.connect("ada.db")

    # Permite apagar mensagens automaticamente
    # quando uma conversa é apagada.
    conexao.execute("PRAGMA foreign_keys = ON")

    return conexao


def criar_bd():

    conexao = conectar_bd()
    cursor = conexao.cursor()

    # -----------------------------
    # Tabela de memória
    # -----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chave TEXT NOT NULL,
            valor TEXT NOT NULL
        )
    """)

    # -----------------------------
    # Tabela de conversas
    # -----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            data_criacao TEXT NOT NULL,
            data_atualizacao TEXT NOT NULL
        )
    """)

    # -----------------------------
    # Tabela de histórico
    # -----------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversa_id INTEGER NOT NULL,
            mensagem TEXT NOT NULL,
            resposta TEXT NOT NULL,
            data_hora TEXT NOT NULL,

            FOREIGN KEY (conversa_id)
            REFERENCES conversas(id)
            ON DELETE CASCADE
        )
    """)

    conexao.commit()
    conexao.close()


# ==========================================================
# MEMÓRIA DA ADA
# ==========================================================

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


# ==========================================================
# CONVERSAS
# ==========================================================

def criar_conversa(titulo="Nova conversa"):

    conexao = conectar_bd()
    cursor = conexao.cursor()

    agora = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO conversas
        (titulo, data_criacao, data_atualizacao)
        VALUES (?, ?, ?)
    """, (
        titulo,
        agora,
        agora
    ))

    conversa_id = cursor.lastrowid

    conexao.commit()
    conexao.close()

    return conversa_id


def listar_conversas():

    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, titulo, data_criacao, data_atualizacao
        FROM conversas
        ORDER BY data_atualizacao DESC
    """)

    resultados = cursor.fetchall()

    conexao.close()

    conversas = []

    for conversa in resultados:

        conversas.append({
            "id": conversa[0],
            "titulo": conversa[1],
            "data_criacao": conversa[2],
            "data_atualizacao": conversa[3]
        })

    return conversas


def gerar_titulo(mensagem):

    titulo = mensagem.strip()

    # Limitar o tamanho do título
    if len(titulo) > 35:
        titulo = titulo[:35].strip() + "..."

    return titulo


def guardar_historico(conversa_id, mensagem, resposta):

    conexao = conectar_bd()
    cursor = conexao.cursor()

    agora = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Guardar mensagem e resposta
    cursor.execute("""
        INSERT INTO historico
        (conversa_id, mensagem, resposta, data_hora)
        VALUES (?, ?, ?, ?)
    """, (
        conversa_id,
        mensagem,
        resposta,
        agora
    ))

    # Verificar se esta é a primeira mensagem
    cursor.execute("""
        SELECT COUNT(*)
        FROM historico
        WHERE conversa_id = ?
    """, (conversa_id,))

    quantidade = cursor.fetchone()[0]

    # Se for a primeira mensagem,
    # usar a mensagem como título.
    if quantidade == 1:

        titulo = gerar_titulo(mensagem)

        cursor.execute("""
            UPDATE conversas
            SET titulo = ?,
                data_atualizacao = ?
            WHERE id = ?
        """, (
            titulo,
            agora,
            conversa_id
        ))

    else:

        cursor.execute("""
            UPDATE conversas
            SET data_atualizacao = ?
            WHERE id = ?
        """, (
            agora,
            conversa_id
        ))

    conexao.commit()
    conexao.close()


def buscar_historico(conversa_id):

    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT mensagem, resposta, data_hora
        FROM historico
        WHERE conversa_id = ?
        ORDER BY id ASC
    """, (conversa_id,))

    resultados = cursor.fetchall()

    conexao.close()

    historico = []

    for item in resultados:

        historico.append({
            "mensagem": item[0],
            "resposta": item[1],
            "data_hora": item[2]
        })

    return historico


def apagar_conversa(conversa_id):

    conexao = conectar_bd()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM conversas WHERE id = ?",
        (conversa_id,)
    )

    apagado = cursor.rowcount

    conexao.commit()
    conexao.close()

    return apagado > 0


# ==========================================================
# HORA E DATA
# ==========================================================

def dizer_hora():

    hora_atual = datetime.now()
    hora = hora_atual.strftime("%H:%M")

    return f"\nAgora são {hora}.\n"


def dizer_data():

    data_atual = datetime.now()
    data = data_atual.strftime("%d/%m/%Y")

    return f"Hoje é {data}.\n"


# ==========================================================
# CALCULADORA
# ==========================================================

def calcular(x, operador, y):

    while True:

        try:
            a = float(x)
            break

        except ValueError:
            return "Número inválido! Por favor, digite apenas números."

    while True:

        try:
            b = float(y)
            break

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

    elif operador == "^":

        return f"O resultado da potência é {a ** b}."

    else:

        return "Operador inválido."

def calcular_raiz(numero):

    try:

        numero = float(numero)

    except ValueError:

        return "Número inválido! Por favor, digite apenas números."

    if numero < 0:

        return "Não é possível calcular a raiz quadrada de um número negativo."

    resultado = math.sqrt(numero)

    return f"A raiz quadrada de {numero} é {resultado}."

def calcular_percentagem(percentagem, numero):

    try:

        percentagem = float(percentagem)
        numero = float(numero)

    except ValueError:

        return "Número inválido! Por favor, digite apenas números."

    resultado = (percentagem / 100) * numero

    return f"{percentagem}% de {numero} é {resultado}."

# ==========================================================
# PESQUISA NA INTERNET
# ==========================================================

def pesquisar_internet(pergunta):

    try:

        pergunta_codificada = urllib.parse.quote(
            pergunta
        )

        url = (
            "https://api.duckduckgo.com/"
            f"?q={pergunta_codificada}"
            "&format=json"
            "&no_html=1"
            "&skip_disambig=1"
            "&kl=pt-pt"
        )

        resposta = urllib.request.urlopen(
            url,
            timeout=5
        )

        dados = json.loads(
            resposta.read().decode("utf-8")
        )

        resultados = []

        # ==================================================
        # RESULTADO PRINCIPAL
        # ==================================================

        resumo = dados.get("AbstractText")

        if resumo:

            fonte = dados.get(
                "AbstractSource",
                "DuckDuckGo"
            )

            url_fonte = dados.get(
                "AbstractURL",
                ""
            )

            resultados.append({
                "titulo": fonte,
                "descricao": resumo,
                "url": url_fonte
            })

        # ==================================================
        # RESULTADOS RELACIONADOS
        # ==================================================

        topicos = dados.get(
            "RelatedTopics",
            []
        )

        for topico in topicos:

            if len(resultados) >= 5:
                break

            if isinstance(topico, dict):

                texto = topico.get("Text")
                url_topico = topico.get("FirstURL", "")

                if texto:

                    resultados.append({
                        "titulo": "Resultado relacionado",
                        "descricao": texto,
                        "url": url_topico
                    })

        # ==================================================
        # VERIFICAR RESULTADOS
        # ==================================================

        if not resultados:

            url_pesquisa = (
                "https://duckduckgo.com/?q="
                + pergunta_codificada
            )

            return (
                "🔎 Não encontrei uma resposta direta "
                "para essa pesquisa.\n\n"
                "Podes consultar os resultados completos "
                "da pesquisa aqui:\n"
                f"🔗 {url_pesquisa}"
            )

        # ==================================================
        # ORGANIZAR RESPOSTA
        # ==================================================

        resposta_final = (
            f"🔎 Encontrei {len(resultados)} "
            "resultado(s):\n\n"
        )

        for numero, resultado in enumerate(
            resultados,
            start=1
        ):

            resposta_final += (
                f"{numero}. {resultado['titulo']}\n"
                f"{resultado['descricao']}\n"
            )

            if resultado["url"]:

                resposta_final += (
                    f"🔗 {resultado['url']}\n"
                )

            resposta_final += "\n"

        return resposta_final

    except urllib.error.URLError:

        return (
            "🌐 Não consigo pesquisar na Internet "
            "porque não existe ligação à Internet "
            "neste momento."
        )

    except TimeoutError:

        return (
            "⏳ A pesquisa demorou demasiado tempo. "
            "Verifica a tua ligação à Internet "
            "e tenta novamente."
        )

    except Exception as erro:

        print("Erro na pesquisa:", erro)

        return (
            "Ocorreu um problema ao tentar "
            "pesquisar na Internet."
        )

# ==========================================================
# AJUDA
# ==========================================================

def ajuda():

    return """
🤖 O QUE POSSO FAZER

👋 Conversar
- oi / olá
- bom dia / boa tarde / boa noite
- tudo bem?
- como estás?

🕐 Data e hora
- que horas são
- que dia é hoje

🧮 Calcular
- 10 + 5
- 20 - 8
- 6 * 7
- 50 / 5
- raiz de 25
- 20% de 500

🧠 Memória
- guardar nome como Danilo
- qual é nome
- apagar nome

🌐 Pesquisar
- pesquisar Python
- pesquisar sobre Cabo Verde

❓ ajuda
"""


# ==========================================================
# CONTROLO DO COMPUTADOR
# ==========================================================


def controlar_computador(comando):

    comando = comando.lower().strip()

    # Normalizar acentos
    comando = (
        comando.replace("á", "a")
        .replace("à", "a")
        .replace("ã", "a")
        .replace("â", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("õ", "o")
        .replace("ú", "u")
        .replace("ç", "c")
    )


    # Remover expressões usadas para dar ordens
    # Repetir até limpar todas as expressões iniciais
    while True:
        comando = comando.strip()
        comando = comando.rstrip(" .,!?")

        expressoes = [
            "ada, ",
            "ada ",
            "por favor, ",
            "por favor ",
            "podes ",
            "pode ",
            "abre ",
            "abrir ",
            "inicia ",
            "iniciar ",
            "executa ",
            "executar ",
            "a pasta ",
            "o pasta ",
            "pasta ",
            "a ",
            "o "
        ]

        removida = False

        for expressao in expressoes:
            if comando.startswith(expressao):
                comando = comando[len(expressao):].strip()
                removida = True
                break

        if not removida:
            break

    
    # ==========================================================
    # ABRIR PASTAS DO AMBIENTE DE TRABALHO
    # ==========================================================

    # Procurar o Ambiente de Trabalho do utilizador.
    # Também verificar a localização habitual do OneDrive.
    pasta_utilizador = Path.home()

    candidatos = [
        pasta_utilizador / "Desktop",
        pasta_utilizador / "OneDrive" / "Desktop"
    ]

    # Procurar também pastas OneDrive com outros nomes.
    candidatos.extend(pasta_utilizador.glob("OneDrive*/Desktop"))

    ambiente_trabalho = next(
        (pasta for pasta in candidatos if pasta.is_dir()),
        None
    )

    # Nomes que significam abrir o Ambiente de Trabalho.
    nomes_ambiente = [
        "ambiente de trabalho",
        "desktop",
        "area de trabalho",
        "meus projetos",
        "os meus projetos",
        "dos meus projetos"
    ]

    if comando in nomes_ambiente:

        if ambiente_trabalho is None:
            return (
                "Não consegui localizar o Ambiente de Trabalho. "
                "Verifica a localização da pasta no Windows."
            )

        try:
            os.startfile(str(ambiente_trabalho))
            return "Já estou a abrir o Ambiente de Trabalho. 😊"

        except OSError:
            return "Não consegui abrir o Ambiente de Trabalho."

    # Abrir uma subpasta pelo nome, dentro do Ambiente de Trabalho.
    if ambiente_trabalho is not None:

        for pasta in ambiente_trabalho.iterdir():

            if (
                pasta.is_dir()
                and pasta.name.casefold() == comando.casefold()
            ):
                try:
                    os.startfile(str(pasta))
                    return f"Já estou a abrir a pasta {pasta.name}. 😊"

                except OSError:
                    return f"Não consegui abrir a pasta {pasta.name}."

    # Aplicações autorizadas
    aplicacoes = {
        "chrome": ["cmd", "/c", "start", "", "chrome"],
        "google chrome": ["cmd", "/c", "start", "", "chrome"],
        "edge": ["cmd", "/c", "start", "", "msedge"],
        "microsoft edge": ["cmd", "/c", "start", "", "msedge"],
        "vs code": ["cmd", "/c", "start", "", "code"],
        "visual studio code": ["cmd", "/c", "start", "", "code"],
        "calculadora": ["calc.exe"],
        "explorador": ["explorer.exe"],
        "explorador de ficheiros": ["explorer.exe"],
        "word": ["cmd", "/c", "start", "", "winword"],
        "excel": ["cmd", "/c", "start", "", "excel"],
        "powerpoint": ["cmd", "/c", "start", "", "powerpnt"]
    }

    if comando in aplicacoes:
        try:
            subprocess.Popen(aplicacoes[comando])
            return f"Claro! Estou a abrir {comando}. 😊"

        except OSError:
            return (
                f"Não consegui abrir {comando}. "
                "Verifica se está instalado no computador."
            )

    # Abrir ficheiros ou pastas através de um caminho completo
    if comando.startswith("caminho "):

        caminho_texto = comando[len("caminho "):].strip()
        caminho = Path(caminho_texto)

        if not caminho.is_absolute():
            return "Indica o caminho completo do ficheiro ou da pasta."

        if not caminho.exists():
            return (
                "Não encontrei esse ficheiro ou pasta. "
                "Verifica o caminho indicado."
            )

        extensoes_bloqueadas = {
            ".exe", ".bat", ".cmd", ".ps1", ".msi", ".com"
        }

        if caminho.is_file() and caminho.suffix.lower() in extensoes_bloqueadas:
            return (
                "Por segurança, não vou executar programas "
                "ou scripts através deste comando."
            )

        try:
            os.startfile(str(caminho))
            return f"Já estou a abrir: {caminho.name}. 😊"

        except OSError:
            return (
                "Não consegui abrir esse caminho. "
                "Verifica se tens acesso ao ficheiro."
            )

    return None