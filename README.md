# 🤖 ADA — Assistente Digital Autónoma

A **ADA (Assistente Digital Autónoma)** é um chatbot desenvolvido em Python com o objetivo de criar um assistente virtual simples, capaz de responder a perguntas, realizar cálculos, guardar informações, manter o histórico de conversas e pesquisar informações na Internet.

O projeto começou como um chatbot executado no terminal e evoluiu para uma aplicação web utilizando Flask, SQLite, HTML, CSS e JavaScript.

O projeto encontra-se em desenvolvimento e novas funcionalidades serão adicionadas progressivamente.

---

## 📌 Sobre o projeto

A ADA foi criada como um projeto de aprendizagem prática na área de programação e desenvolvimento de sistemas.

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
* Criar novas conversas;
* Guardar o histórico das conversas;
* Recuperar conversas anteriores;
* Apagar conversas;
* Funcionar através de uma interface web.

---

## ✨ Funcionalidades

### 💬 Conversação

A ADA reconhece algumas mensagens básicas, como:

```text
Olá
Oi
Bom dia
Boa tarde
Boa noite
Tudo bem?
Quem és?
Qual é o teu nome?
```

A ADA processa a mensagem através da função principal `responder()` localizada no ficheiro `main.py`.

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

A ADA também trata situações de divisão por zero para evitar erros.

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

A hora é obtida através do módulo `datetime` do Python.

---

### 🧠 Memória com SQLite

A ADA possui uma base de dados SQLite chamada:

```text
ada.db
```

A tabela `memoria` é utilizada para guardar informações fornecidas pelo utilizador.

Por exemplo:

```text
guardar nome como Danilo
```

A ADA pode posteriormente consultar essa informação:

```text
qual é nome
```

Também é possível apagar uma informação:

```text
apagar nome
```

Se uma informação já existir, a ADA atualiza o valor existente em vez de criar uma nova informação duplicada.

A memória funciona de forma independente do histórico das conversas.

---

### 📜 Histórico de conversas

A ADA possui agora um sistema de **histórico de conversas utilizando SQLite**.

Cada conversa possui:

* Um identificador;
* Um título;
* Data de criação;
* Data da última atualização;
* As mensagens enviadas pelo utilizador;
* As respostas da ADA.

Quando o utilizador inicia uma conversa, ela é guardada na base de dados.

O título da conversa é criado automaticamente a partir da primeira mensagem.

Por exemplo:

```text
💬 Como funciona Python?
```

As conversas podem ser:

* Criadas;
* Consultadas;
* Carregadas novamente;
* Apagadas.

As conversas continuam disponíveis mesmo depois de fechar e voltar a abrir a aplicação.

---

### 🌐 Pesquisa na Internet

A ADA possui uma funcionalidade de pesquisa na Internet.

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

A pesquisa utiliza o serviço **DuckDuckGo Instant Answer API** através das bibliotecas `urllib` e `json` do Python.

A ADA tenta encontrar uma resposta direta ou um resultado relacionado à pesquisa.

#### 📡 Sem Internet

A pesquisa possui tratamento para problemas de ligação.

Se o computador estiver sem Internet, a ADA apresenta uma mensagem informando que não foi possível realizar a pesquisa.

As funcionalidades locais continuam disponíveis, como:

* Cálculos;
* Hora;
* Data;
* Memória;
* Histórico de conversas;
* Conversação básica.

---

## 🌐 Interface Web

A ADA possui uma interface web desenvolvida com **Flask**.

A interface apresenta:

* Menu lateral;
* Botão para criar uma nova conversa;
* Lista de conversas;
* Área de conversação;
* Mensagens da ADA;
* Mensagens do utilizador;
* Campo para escrever mensagens;
* Botão de envio;
* Indicador de estado da ADA;
* Opção para carregar conversas anteriores;
* Opção para apagar conversas.

A comunicação entre o navegador e o Python é feita através de rotas Flask e JavaScript utilizando `fetch()`.

Principais rotas utilizadas:

```text
/
```

Página principal.

```text
/chat
```

Envia uma mensagem para a ADA e recebe a resposta.

```text
/conversas
```

Obtém a lista de conversas.

```text
/conversa
```

Cria uma nova conversa.

```text
/conversa/<id>
```

Carrega ou apaga uma conversa específica.

---

## 🛠️ Tecnologias utilizadas

* **Python** — lógica principal da ADA;
* **Flask** — criação da aplicação web;
* **SQLite** — armazenamento da memória e histórico;
* **HTML** — estrutura da interface;
* **CSS** — aparência da interface;
* **JavaScript** — interação da interface com o chatbot;
* **urllib** — comunicação com a Internet;
* **JSON** — processamento dos dados da pesquisa;
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

É responsável pela aplicação Flask e pela comunicação entre a interface web e a lógica da ADA.

Também possui as rotas responsáveis por:

* Iniciar a aplicação;
* Receber mensagens;
* Criar conversas;
* Listar conversas;
* Carregar conversas;
* Apagar conversas;
* Inicializar a base de dados.

---

### `main.py`

Contém a lógica principal da ADA.

É responsável por:

* Interpretar as mensagens;
* Identificar comandos;
* Processar cálculos;
* Consultar a memória;
* Apagar informações;
* Solicitar pesquisas na Internet;
* Gerar as respostas da ADA.

A função principal deste ficheiro é:

```python
responder(mensagem)
```

---

### `funcao.py`

Contém as funções utilizadas pela ADA.

Entre elas:

```text
conectar_bd()

criar_bd()

guardar_memoria()

buscar_memoria()

apagar_memoria()

criar_conversa()

listar_conversas()

gerar_titulo()

guardar_historico()

buscar_historico()

apagar_conversa()

dizer_hora()

dizer_data()

calcular()

pesquisar_internet()
```

A separação das funções ajuda a manter o projeto organizado e facilita a adição de novas funcionalidades.

---

### `templates/index.html`

Contém a estrutura HTML da interface da ADA.

É responsável pela estrutura da:

* Sidebar;
* Lista de conversas;
* Área de mensagens;
* Caixa de texto;
* Botão de envio.

---

### `static/style.css`

Contém os estilos visuais da aplicação.

É responsável pelo:

* Tema escuro;
* Menu lateral;
* Botões;
* Mensagens;
* Área de conversação;
* Campo de texto;
* Lista de conversas;
* Design responsivo.

---

### `static/script.js`

Controla a interação entre o utilizador e a interface.

É responsável por:

* Enviar mensagens;
* Receber respostas;
* Mostrar mensagens;
* Criar conversas;
* Listar conversas;
* Carregar conversas;
* Apagar conversas;
* Destacar a conversa atual;
* Comunicar com o Flask através de `fetch()`.

---

### `ada.db`

É a base de dados SQLite utilizada pela ADA.

Atualmente contém as tabelas:

```text
memoria
```

Responsável pelas informações guardadas pela ADA.

```text
conversas
```

Responsável pelos dados das conversas.

```text
historico
```

Responsável pelas mensagens e respostas de cada conversa.

A relação entre as tabelas de conversas e histórico é feita através do `conversa_id`.

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

A ADA utiliza **SQLite** porque é uma solução simples, leve e adequada para o projeto.

A base de dados é armazenada no ficheiro:

```text
ada.db
```

### Tabela `memoria`

```text
memoria

├── id
├── chave
└── valor
```

Exemplo:

```text
id    chave                 valor

1     nome                  Danilo
2     linguagem favorita    Python
```

### Tabela `conversas`

```text
conversas

├── id
├── titulo
├── data_criacao
└── data_atualizacao
```

### Tabela `historico`

```text
historico

├── id
├── conversa_id
├── mensagem
├── resposta
└── data_hora
```

O campo `conversa_id` permite relacionar cada mensagem com a conversa correspondente.

A base de dados pode ser visualizada através de ferramentas como **SQLite Viewer** no VS Code ou **DB Browser for SQLite**.

---

## 🔄 Funcionamento do histórico

O funcionamento básico é:

```text
Utilizador
    ↓
Escreve uma mensagem
    ↓
JavaScript
    ↓
Flask (/chat)
    ↓
main.py
    ↓
ADA gera uma resposta
    ↓
Flask
    ↓
SQLite
    ↓
Mensagem + resposta são guardadas
```

Quando o utilizador volta a abrir uma conversa:

```text
Utilizador
    ↓
Clica numa conversa
    ↓
JavaScript
    ↓
Flask (/conversa/<id>)
    ↓
SQLite
    ↓
Histórico recuperado
    ↓
Mensagens aparecem novamente
```

---

## 🚧 Estado atual

**Em desenvolvimento.**

A ADA já possui uma estrutura funcional de chatbot web com:

* Processamento de mensagens;
* Calculadora;
* Hora e data;
* Memória;
* Base de dados SQLite;
* Pesquisa na Internet;
* Histórico de conversas;
* Interface web;
* Gestão de múltiplas conversas.

O objetivo é continuar a melhorar a capacidade de compreensão, interação e automação da ADA.

---

## 🔮 Próximas funcionalidades

Algumas funcionalidades planeadas para versões futuras:

* 🧠 Memória mais inteligente;
* 🔎 Pesquisa dentro do histórico de conversas;
* 🗃️ Interface para visualizar e gerir a memória;
* 🌐 Pesquisa na Internet mais avançada;
* 🔗 Apresentação de fontes e links das pesquisas;
* 💻 Abrir aplicações e ficheiros do computador;
* 📂 Abrir pastas;
* 🎤 Reconhecimento de voz;
* 🔊 Respostas através de voz;
* 👤 Sistema de utilizadores;
* 🤖 Integração com modelos de Inteligência Artificial;
* ⚙️ Mais comandos e automações;
* 🎨 Melhorias na interface;
* 🔐 Sistema de autenticação;
* ☁️ Possibilidade de sincronizar dados.

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
* JavaScript;
* Automação;
* Inteligência Artificial.
