# 🤖 ADA — Assistente Digital Autónoma

A **ADA (Assistente Digital Autónoma)** é um chatbot desenvolvido em **Python**, criado para responder a perguntas simples, realizar cálculos, guardar informações, pesquisar na Internet e manter o histórico das conversas.

O projeto começou como um chatbot simples no terminal e foi evoluindo para uma aplicação web com **Flask**, **SQLite**, reconhecimento de voz, síntese de voz e uma interface gráfica moderna.

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
* 🎤 Reconhecimento de voz
* 🗣️ Transformar voz em texto
* 🔊 Responder por voz
* 💬 Enviar automaticamente mensagens reconhecidas por voz
* 🖥️ Interface web
* 🌙 Modo escuro
* ☀️ Modo claro
* 📱 Interface adaptada para diferentes tamanhos de ecrã
* 🗄️ Base de dados SQLite para armazenamento das informações

---

## 🎤 Reconhecimento de Voz

A ADA consegue receber mensagens através do microfone.

O funcionamento é:

```text
🎤 Utilizador fala
       ↓
📝 Voz convertida em texto
       ↓
⏳ ADA espera o utilizador terminar
       ↓
📤 Mensagem enviada automaticamente
       ↓
🤖 ADA processa a mensagem
```

Por exemplo, o utilizador pode dizer:

```text
Quanto é vinte por cento de quinhentos?
```

A ADA transforma a fala em texto e envia automaticamente a mensagem depois de o utilizador terminar de falar.

O reconhecimento de voz utiliza as funcionalidades de voz disponíveis no navegador.

---

## 🔊 Resposta por Voz

A ADA também consegue transformar as suas respostas em voz.

O funcionamento é:

```text
🤖 ADA gera resposta
       ↓
💬 Resposta aparece no chat
       ↓
🔊 Resposta é lida em voz alta
```

A velocidade, idioma e voz utilizada dependem das funcionalidades de síntese de voz disponíveis no navegador e no sistema operativo.

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

---

## 🌐 Pesquisa na Internet

A ADA consegue realizar pesquisas na Internet através da API do **DuckDuckGo**.

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

Desta forma, as conversas podem continuar disponíveis mesmo depois de a aplicação ser fechada.

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

---

## ❓ Sistema de Ajuda

A ADA possui um comando de ajuda que apresenta os principais comandos e funcionalidades disponíveis.

Para consultar a ajuda, basta escrever:

```text
ajuda
```

A ADA apresenta exemplos relacionados com:

* conversação;
* data e hora;
* calculadora;
* pesquisa na Internet;
* outros comandos disponíveis.

---

## 🖥️ Interface Web

A ADA possui uma interface web desenvolvida com:

* HTML
* CSS
* JavaScript
* Flask

A interface possui:

* barra lateral;
* lista de conversas;
* área de chat;
* mensagens da ADA;
* mensagens do utilizador;
* campo de texto;
* botão de envio;
* botão de microfone;
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

Responsável pelo funcionamento da aplicação web utilizando Flask.

Controla as rotas da aplicação e faz a ligação entre a interface, o chatbot e a base de dados.

### `main.py`

Responsável pela lógica principal da ADA.

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

Controla a interação da interface com a ADA, o envio das mensagens, o reconhecimento de voz e a síntese de voz.

### `ada.db`

Base de dados SQLite utilizada para guardar as informações da aplicação.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Flask**
* **SQLite**
* **HTML**
* **CSS**
* **JavaScript**
* **Web Speech API**
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

Depois de executar o programa, abrir no navegador:

```text
http://127.0.0.1:5000
```

---

## 📌 Objetivo do projeto

O objetivo da ADA é desenvolver progressivamente um assistente digital utilizando conceitos de programação, desenvolvimento web, bases de dados, APIs e tecnologias de voz.

O projeto serve também como forma de praticar e aplicar conhecimentos de:

* Python;
* programação modular;
* expressões regulares;
* bases de dados SQL;
* desenvolvimento web;
* APIs;
* JavaScript;
* HTML e CSS;
* reconhecimento e síntese de voz;
* Git e GitHub.

---

## 🔮 Próximas funcionalidades

Algumas funcionalidades que podem ser adicionadas futuramente:

* 🔢 Fatorial
* 📐 Seno, cosseno e tangente
* 📊 Logaritmos
* 🧮 Expressões matemáticas mais complexas
* 🎙️ Melhorias no reconhecimento de voz
* 🔊 Controlo para ativar/desativar respostas por voz
* 🗣️ Seleção de diferentes vozes
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
