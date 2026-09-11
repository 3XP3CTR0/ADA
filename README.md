# 🤖 ADA — Assistente Digital Autónoma

## 📌 Sobre o projeto

A **ADA (Assistente Digital Autónoma)** é um chatbot desenvolvido em **Python**, com uma interface web criada com **Flask, HTML, CSS e JavaScript**.

O objetivo do projeto é desenvolver, de forma gradual, uma assistente digital capaz de conversar com o utilizador, realizar tarefas e guardar informações através de uma base de dados.

O projeto também serve como forma de aprendizagem e prática de **Python, desenvolvimento web, bases de dados e Inteligência Artificial**.

---

## ✨ Funcionalidades atuais

Atualmente, a ADA consegue:

* 💬 Responder a saudações;
* 🕐 Informar a hora atual;
* 📅 Informar a data atual;
* 🤖 Informar o seu nome e significado;
* 🧮 Realizar operações matemáticas básicas;
* 🌐 Funcionar através de uma interface web;
* 🗄️ Utilizar uma base de dados SQLite;
* 💾 Guardar informações na memória;
* 🔎 Consultar informações guardadas;
* ✏️ Atualizar informações existentes;
* 🗑️ Apagar informações da memória.

### 🧠 Sistema de memória

A ADA possui uma memória baseada em **SQLite**, permitindo guardar informações através de comandos como:

```text
guardar nome como Danilo
```

Consultar:

```text
qual é o nome
```

Atualizar:

```text
guardar nome como João
```

E apagar:

```text
apagar nome
```

A base de dados é armazenada no ficheiro:

```text
ada.db
```

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🌐 Flask
* 🗄️ SQLite
* 🌎 HTML
* 🎨 CSS
* ⚡ JavaScript
* 🔧 Git
* 🐙 GitHub
* 💻 Visual Studio Code

---

## 📂 Estrutura do projeto

```text
ADA/

│
├── README.md
├── app.py
├── main.py
├── funcao.py
├── ada.db
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

### 📄 Descrição dos principais ficheiros

**`app.py`**

Responsável pelo servidor Flask e pela comunicação entre a interface web e o código Python.

**`main.py`**

Contém a lógica principal de conversação da ADA e determina como a assistente deve responder às mensagens do utilizador.

**`funcao.py`**

Contém as funções utilizadas pela ADA, incluindo:

* Hora;
* Data;
* Cálculos;
* Ligação à base de dados;
* Guardar informações;
* Consultar informações;
* Atualizar informações;
* Apagar informações.

**`ada.db`**

Base de dados SQLite utilizada pelo sistema de memória da ADA.

**`index.html`**

Define a estrutura da interface web do chatbot.

**`style.css`**

Define o design e o estilo visual da interface.

**`script.js`**

Controla a interação entre o utilizador e a interface, enviando as mensagens para o servidor Flask e apresentando as respostas da ADA.

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_TEU_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd ADA
```

### 3. Instalar o Flask

```bash
pip install flask
```

### 4. Executar o projeto

```bash
python app.py
```

### 5. Abrir no navegador

Aceda a:

```text
http://127.0.0.1:5000
```

> A base de dados `ada.db` é criada automaticamente quando a aplicação é executada pela primeira vez.

---

## 🧠 Base de dados

A ADA utiliza **SQLite** para armazenar a sua memória.

A tabela principal utilizada atualmente é:

```text
memoria
```

Com os campos:

| Campo   | Descrição             |
| ------- | --------------------- |
| `id`    | Identificador único   |
| `chave` | Nome da informação    |
| `valor` | Informação armazenada |

Exemplo:

| id | chave     | valor  |
| -: | --------- | ------ |
|  1 | nome      | Danilo |
|  2 | linguagem | Python |

O sistema também consegue atualizar uma informação existente em vez de criar vários registos iguais.

---

## 🔮 Futuras funcionalidades

Algumas funcionalidades planeadas para futuras versões:

* 🧠 Melhor compreensão de linguagem natural;
* 🗣️ Compreensão de diferentes formas de escrever a mesma frase;
* 🌐 Pesquisas na Internet;
* 📂 Abertura de ficheiros, pastas e aplicações;
* 🎙️ Reconhecimento de voz;
* 🔊 Respostas por voz;
* 🧠 Sistema de memória mais avançado;
* 💬 Histórico das conversas;
* 🤖 Integração com modelos de Inteligência Artificial;
* 🧠 Processamento de linguagem natural mais avançado;
* 🔐 Sistema de utilizadores e autenticação;
* 📊 Interface para visualizar e gerir a memória da ADA.

---

## 📌 Estado do projeto

🚧 **Em desenvolvimento**

A ADA é um projeto de aprendizagem e desenvolvimento contínuo.

O projeto está a ser utilizado para praticar e aprofundar conhecimentos em:

* Programação em Python;
* Desenvolvimento web;
* Flask;
* JavaScript;
* Bases de dados e SQL;
* Integração entre frontend e backend;
* Estruturação de projetos;
* Inteligência Artificial.

Novas funcionalidades serão adicionadas progressivamente.

---

## 👨‍💻 Autor

**Danilo Alex Alves Lopes**

GitHub: **3XP3CTR0**
