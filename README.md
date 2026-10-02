# 🤖 ADA — Assistente Digital Autónoma

A **ADA (Assistente Digital Autónoma)** é um chatbot desenvolvido em **Python**, criado para responder a perguntas simples, realizar cálculos, guardar informações e manter o histórico das conversas.

O projeto começou como um chatbot simples no terminal e foi evoluindo para uma aplicação web com **Flask**, **SQLite**, interface gráfica e pesquisa na Internet.

---

## 🚀 Funcionalidades

Atualmente, a ADA possui as seguintes funcionalidades:

* 👋 Responder a saudações
* 🕐 Informar a hora atual
* 📅 Informar a data atual
* 🤖 Informar o seu nome e significado
* 🧮 Realizar cálculos matemáticos
* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão
* 🔢 Potências
* √ Calcular raiz quadrada
* 📊 Calcular percentagens
* 💾 Guardar informações na memória
* 🗑️ Apagar informações guardadas
* 🌐 Pesquisar informações na Internet
* 💬 Criar novas conversas
* 📚 Guardar o histórico das conversas
* 🔄 Carregar conversas anteriores
* 🗑️ Apagar conversas
* 📝 Criar automaticamente títulos para as conversas
* 🖥️ Interface web
* 🌙 Modo escuro
* ☀️ Modo claro
* 📱 Interface adaptada para diferentes tamanhos de ecrã
* 🗄️ Base de dados SQLite para armazenamento das informações

---

## 🧮 Calculadora

A ADA consegue realizar vários tipos de cálculos.

### Operações básicas

```text
10 + 5
20 - 8
6 * 7
50 / 5
```

Também é possível escrever de forma mais natural:

```text
quanto é 10 mais 5
calcula 20 menos 8
quanto é 6 vezes 7
quanto é 50 dividido por 5
```

### Potência

```text
2 ^ 3
```

Resultado:

```text
O resultado da potência é 8.0.
```

### Raiz quadrada

```text
raiz de 25
```

ou:

```text
raiz quadrada de 25
```

Também é possível utilizar:

```text
√25
```

### Percentagem

```text
20% de 500
```

Resultado:

```text
20.0% de 500.0 é 100.0.
```

---

## 🌐 Pesquisa na Internet

A ADA também consegue realizar pesquisas na Internet através da API do **DuckDuckGo**.

Exemplo:

```text
Quem é Albert Einstein?
```

Se existir uma resposta disponível, a ADA apresenta a informação encontrada e a respetiva fonte.

Caso não exista ligação à Internet, a ADA apresenta uma mensagem informando que não foi possível realizar a pesquisa.

---

## 💾 Base de Dados

A ADA utiliza **SQLite** para guardar informações.

A base de dados é armazenada no ficheiro:

```text
ada.db
```

A base de dados contém atualmente tabelas para:

### `memoria`

Guarda informações que a ADA deve recordar.

### `conversas`

Guarda as conversas criadas pelo utilizador.

### `historico`

Guarda as mensagens enviadas pelo utilizador e as respostas da ADA.

Desta forma, as conversas não desaparecem quando a aplicação é fechada.

---

## 💬 Sistema de Conversas

A ADA possui um sistema de conversas semelhante ao de aplicações modernas de chat.

É possível:

* criar uma nova conversa;
* enviar mensagens;
* guardar automaticamente o histórico;
* carregar conversas anteriores;
* apagar conversas;
* criar automaticamente um título baseado na primeira mensagem.

Exemplo:

```text
Nova conversa
    ↓
"Como funciona Python?"
    ↓
Título: "Como funciona Python?"
    ↓
Histórico guardado na base de dados
```

---

## 🖥️ Interface Web

A ADA possui uma interface web desenvolvida com:

* HTML
* CSS
* JavaScript
* Flask

A aplicação possui:

* barra lateral;
* lista de conversas;
* área de chat;
* mensagens da ADA;
* mensagens do utilizador;
* campo de texto;
* botão de envio;
* botão para criar nova conversa;
* modo claro e modo escuro.

---

## 📁 Estrutura do Projeto

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

### `app.py`

É responsável pelo funcionamento da aplicação web utilizando Flask.

Controla as rotas da aplicação e faz a ligação entre a interface, o chatbot e a base de dados.

### `main.py`

É responsável pela lógica principal da ADA.

Recebe as mensagens do utilizador, identifica o tipo de pedido e chama as funções necessárias.

### `funcao.py`

Contém as principais funções utilizadas pela ADA, incluindo:

* base de dados;
* memória;
* conversas;
* histórico;
* hora;
* data;
* cálculos;
* pesquisa na Internet.

### `index.html`

Define a estrutura da interface web.

### `style.css`

Define o visual da aplicação, incluindo os modos claro e escuro.

### `script.js`

Controla a interação da interface com a ADA e comunica com o servidor Flask.

### `ada.db`

É a base de dados SQLite utilizada para guardar as informações da aplicação.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Flask**
* **SQLite**
* **HTML**
* **CSS**
* **JavaScript**
* **Git**
* **GitHub**
* **VS Code**
* **DuckDuckGo Instant Answer API**

---

## ▶️ Como executar o projeto

### 1. Clonar o projeto

```bash
git clone https://github.com/3XP3CTR0/ADA.git
```

### 2. Entrar na pasta

```bash
cd ADA
```

### 3. Instalar o Flask

```bash
pip install flask
```

### 4. Executar a aplicação

```bash
python app.py
```

### 5. Abrir no navegador

Depois de executar o programa, abrir no navegador o endereço apresentado pelo Flask, normalmente:

```text
http://127.0.0.1:5000
```

---

## 📌 Objetivo do projeto

O objetivo da ADA é desenvolver progressivamente um assistente digital utilizando conceitos de programação, desenvolvimento web, bases de dados e integração com serviços externos.

O projeto também serve como forma de praticar e aplicar conhecimentos de:

* Python;
* programação modular;
* expressões regulares;
* bases de dados SQL;
* desenvolvimento web;
* APIs;
* JavaScript;
* HTML e CSS;
* Git e GitHub.

---

## 🔮 Próximas funcionalidades

Algumas funcionalidades que podem ser adicionadas futuramente:

* 🔢 Fatorial
* 📐 Seno, cosseno e tangente
* 📊 Logaritmos
* 🧮 Expressões matemáticas mais complexas
* 🗣️ Reconhecimento de voz
* 🔊 Respostas por voz
* 📷 Reconhecimento de texto através de imagens (OCR)
* 📂 Abrir aplicações, ficheiros e pastas
* 🔎 Pesquisa web mais avançada
* 🧠 Sistema de memória mais inteligente
* 🤖 Integração com modelos de Inteligência Artificial
* 🔐 Sistema de utilizadores

---

## 👨‍💻 Autor

**Danilo Alex Alves Lopes**

Projeto desenvolvido como forma de aprendizagem e evolução na área de **Informática e Desenvolvimento de Software**.
