# 🤖 ADA — Assistente Digital Autónoma

A **ADA (Assistente Digital Autónoma)** é um chatbot desenvolvido em Python com o objetivo de criar um assistente virtual simples, capaz de responder a perguntas, realizar cálculos, consultar informações guardadas numa base de dados e pesquisar informações na Internet.

O projeto está em desenvolvimento e novas funcionalidades serão adicionadas progressivamente.

---

## 📌 Sobre o projeto

A ADA começou como um chatbot simples executado no terminal e evoluiu para uma aplicação web utilizando Flask.

Atualmente, a ADA consegue:

* Responder a saudações;
* Informar a hora atual;
* Informar a data atual;
* Dizer o seu nome e significado;
* Realizar cálculos matemáticos;
* Guardar informações na memória;
* Consultar informações guardadas;
* Atualizar informações existentes;
* Apagar informações da memória;
* Pesquisar informações na Internet;
* Informar quando não existe ligação à Internet;
* Funcionar através de uma interface web.

---

## ✨ Funcionalidades

### 💬 Conversação

A ADA reconhece algumas mensagens básicas, como:

```text
Olá
Oi
Bom dia
Tudo bem?
Quem és?
Qual é o teu nome?
```

---

### 🧮 Calculadora

A ADA consegue realizar operações matemáticas básicas.

Exemplos:

```text
20 + 10
50 - 15
8 * 5
100 / 4
```

Também consegue interpretar algumas operações escritas:

```text
quanto é 20 mais 10
calcula 50 menos 20
10 vezes 5
100 dividido por 4
```

A divisão por zero também é tratada para evitar erros.

---

### 🕐 Hora e data

A ADA consegue informar a hora e a data atuais.

Exemplos:

```text
Que horas são?
Que horas são agora?
Que dia é hoje?
Qual é a data de hoje?
```

---

### 🧠 Memória com SQLite

A ADA possui uma base de dados SQLite chamada:

```text
ada.db
```

A tabela utilizada atualmente é:

```text
memoria
```

A ADA pode guardar informações utilizando comandos como:

```text
guardar nome como Danilo
```

Também consegue utilizar formas mais naturais:

```text
Meu nome é Danilo
Eu sou Danilo
```

Para consultar uma informação:

```text
qual é nome
```

Também é possível apagar uma informação:

```text
apagar nome
```

Se uma informação já existir, a ADA atualiza o seu valor em vez de criar uma duplicada.

---

### 🌐 Pesquisa na Internet

A ADA também possui uma funcionalidade de pesquisa na Internet.

O utilizador pode escrever:

```text
pesquisar Python
```

ou:

```text
pesquisa inteligência artificial
```

ou:

```text
procura Cabo Verde
```

A pesquisa utiliza preferência de região/idioma português.

A ADA tenta obter uma resposta através da Internet e apresentar a informação encontrada.

#### 📡 Sem Internet

A pesquisa também possui tratamento para problemas de ligação.

Se o computador estiver sem Internet, a ADA não deverá fechar nem apresentar um erro técnico ao utilizador.

Em vez disso, apresenta uma mensagem informando que não foi possível realizar a pesquisa.

As restantes funcionalidades locais continuam disponíveis, como:

* Cálculos;
* Hora;
* Data;
* Memória;
* Conversação básica.

---

## 🌐 Interface Web

A ADA possui uma interface web desenvolvida com Flask.

A interface apresenta:

* Menu lateral;
* Área de conversação;
* Mensagens da ADA;
* Mensagens do utilizador;
* Campo para escrever mensagens;
* Botão de envio;
* Botão para iniciar uma nova conversa;
* Indicador de estado da ADA.

A comunicação entre o navegador e o Python é feita através de uma rota Flask:

```text
POST /chat
```

---

## 🛠️ Tecnologias utilizadas

* **Python** — lógica principal da ADA;
* **Flask** — criação da aplicação web;
* **SQLite** — armazenamento da memória;
* **HTML** — estrutura da interface;
* **CSS** — aparência da interface;
* **JavaScript** — interação com o chatbot;
* **urllib / JSON** — comunicação com o serviço de pesquisa;
* **Git** — controlo de versões;
* **GitHub** — armazenamento e publicação do projeto;
* **Visual Studio Code** — ambiente de desenvolvimento.

---

## 📁 Estrutura do projeto

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

---

## 📄 Função dos principais ficheiros

### `app.py`

É responsável por iniciar a aplicação Flask e criar as rotas da aplicação web.

A principal rota de comunicação com a ADA é:

```text
/chat
```

---

### `main.py`

Contém a lógica principal da ADA.

É responsável por:

* Interpretar as mensagens;
* Identificar comandos;
* Chamar funções;
* Processar cálculos;
* Consultar a memória;
* Solicitar pesquisas na Internet;
* Gerar as respostas.

---

### `funcao.py`

Contém várias funções utilizadas pela ADA.

Entre elas:

```text
conectar_bd()
criar_bd()
guardar_memoria()
buscar_memoria()
apagar_memoria()
dizer_hora()
dizer_data()
calcular()
pesquisar_internet()
```

A separação das funções ajuda a manter o projeto organizado.

---

### `app.py`

Faz a ligação entre o Python e a interface web.

---

### `templates/index.html`

Contém a estrutura HTML da interface da ADA.

---

### `static/style.css`

Contém os estilos visuais da aplicação.

---

### `static/script.js`

Controla a interação da página com a ADA.

É responsável por:

* Enviar mensagens;
* Receber respostas;
* Mostrar mensagens na interface;
* Limpar uma conversa;
* Comunicar com o Flask através de `fetch()`.

---

### `ada.db`

É a base de dados SQLite utilizada para armazenar as informações da memória da ADA.

---

## ▶️ Como executar o projeto

### 1. Abrir o projeto no VS Code

Abra a pasta:

```text
ADA
```

### 2. Abrir o terminal

No VS Code:

```text
Terminal → New Terminal
```

### 3. Executar a aplicação

Digite:

```bash
python app.py
```

### 4. Abrir no navegador

Depois de iniciar o Flask, abra o endereço apresentado no terminal, normalmente:

```text
http://127.0.0.1:5000
```

---

## 🗄️ Base de dados

A ADA utiliza SQLite porque é uma solução simples e adequada para este projeto.

A tabela atual possui:

```text
memoria
│
├── id
├── chave
└── valor
```

Exemplo:

```text
id    chave    valor
1     nome     Danilo
2     linguagem favorita    Python
```

A base de dados pode ser visualizada através de ferramentas como **SQLite Viewer** no VS Code ou **DB Browser for SQLite**.

---

## 🚧 Estado atual

**Em desenvolvimento.**

A ADA ainda é um projeto em evolução. O objetivo é adicionar novas funcionalidades gradualmente e melhorar a capacidade de compreensão e interação do chatbot.

---

## 🔮 Próximas funcionalidades

Algumas funcionalidades planeadas para versões futuras:

* 🧠 Memória mais inteligente;
* 📜 Histórico das conversas;
* 🗃️ Interface para visualizar e gerir a memória;
* 🌐 Pesquisa na Internet mais avançada;
* 🔗 Apresentação das fontes das pesquisas;
* 💻 Abrir aplicações e ficheiros do computador;
* 📂 Abrir pastas;
* 🎤 Reconhecimento de voz;
* 🔊 Respostas através de voz;
* 👤 Sistema de utilizadores;
* 🤖 Integração com modelos de Inteligência Artificial;
* ⚙️ Mais comandos e automações.

---

## 👨‍💻 Autor

**Danilo Alex Alves Lopes**

Estudante de Engenharia Informática e Sistemas Computacionais.

GitHub:

**3XP3CTR0**

---

## 📌 Projeto

**ADA — Assistente Digital Autónoma**

Projeto pessoal desenvolvido para aprendizagem e evolução prática em:

* Programação Python;
* Desenvolvimento Web;
* Bases de dados;
* APIs;
* Automação;
* Inteligência Artificial.
