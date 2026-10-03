const input = document.getElementById("mensagem");

const botaoEnviar = document.getElementById("enviar");

const mensagens = document.getElementById("mensagens");

const novaConversa =
    document.getElementById("nova-conversa");

const listaConversas =
    document.getElementById("lista-conversas");

const microfone = document.getElementById("microfone");


// ==========================================================
// BOTÃO DO TEMA
// ==========================================================

const temaToggle =
    document.getElementById("tema-toggle");


// ID da conversa que está aberta neste momento

let conversaAtual = null;


// ==========================================================
// TEMA CLARO / ESCURO
// ==========================================================

function atualizarBotaoTema() {

    if (!temaToggle) {
        return;
    }

    if (
        document.body.classList.contains("claro")
    ) {

        temaToggle.textContent =
            "☀️ Modo claro";

    } else {

        temaToggle.textContent =
            "🌙 Modo escuro";

    }
}


function carregarTema() {

    const tema =
        localStorage.getItem("tema");

    if (tema === "claro") {

        document.body.classList.add("claro");

    } else {

        document.body.classList.remove("claro");

    }

    atualizarBotaoTema();
}


function alternarTema() {

    document.body.classList.toggle("claro");

    if (
        document.body.classList.contains("claro")
    ) {

        localStorage.setItem(
            "tema",
            "claro"
        );

    } else {

        localStorage.setItem(
            "tema",
            "escuro"
        );

    }

    atualizarBotaoTema();
}


if (temaToggle) {

    temaToggle.addEventListener(
        "click",
        alternarTema
    );

}


// Carregar o tema guardado

carregarTema();


// ==========================================================
// ADICIONAR MENSAGEM NA INTERFACE
// ==========================================================

function adicionarMensagem(texto, tipo) {

    const mensagem =
        document.createElement("div");


    mensagem.classList.add("message");


    if (tipo === "ada") {

        mensagem.classList.add(
            "ada-message"
        );

    } else {

        mensagem.classList.add(
            "user-message"
        );
    }


    const avatar =
        document.createElement("div");


    avatar.classList.add(
        "message-avatar"
    );


    avatar.textContent =
        tipo === "ada"
            ? "🤖"
            : "👤";


    const conteudo =
        document.createElement("div");


    conteudo.classList.add(
        "message-content"
    );


    conteudo.textContent = texto;


    mensagem.appendChild(avatar);

    mensagem.appendChild(conteudo);

    mensagens.appendChild(mensagem);


    mensagens.scrollTop =
        mensagens.scrollHeight;
}


// ==========================================================
// MENSAGEM INICIAL
// ==========================================================

function mostrarMensagemInicial() {

    mensagens.innerHTML = "";


    adicionarMensagem(
        "Olá! Eu sou a ADA. Como posso ajudar-te hoje?",
        "ada"
    );
}


// ==========================================================
// CARREGAR LISTA DE CONVERSAS
// ==========================================================

async function carregarConversas() {

    try {

        const resposta =
            await fetch("/conversas");


        const conversas =
            await resposta.json();


        listaConversas.innerHTML = "";


        conversas.forEach(
            conversa => {

                adicionarConversaNaLista(
                    conversa
                );

            }
        );


        // Se já existem conversas,
        // abrir a mais recente.

        if (
            conversas.length > 0 &&
            conversaAtual === null
        ) {

            await carregarConversa(
                conversas[0].id
            );

        }


        // Se não existem conversas,
        // criar uma automaticamente.

        if (
            conversas.length === 0
        ) {

            await criarNovaConversa();

        }

    } catch (erro) {

        console.error(
            "Erro ao carregar conversas:",
            erro
        );

    }
}


// ==========================================================
// ADICIONAR CONVERSA À SIDEBAR
// ==========================================================

function adicionarConversaNaLista(conversa) {

    const item =
        document.createElement("div");


    item.classList.add(
        "conversa-item"
    );


    // Botão da conversa

    const botao =
        document.createElement("button");


    botao.classList.add(
        "conversa-btn"
    );


    botao.textContent =
        "💬 " + conversa.titulo;


    botao.dataset.id =
        conversa.id;


    if (
        conversa.id === conversaAtual
    ) {

        botao.classList.add(
            "ativa"
        );

    }


    botao.addEventListener(
        "click",
        function() {

            carregarConversa(
                conversa.id
            );

        }
    );


    // Botão apagar

    const apagar =
        document.createElement("button");


    apagar.classList.add(
        "apagar-conversa"
    );


    apagar.textContent = "🗑️";


    apagar.title =
        "Apagar conversa";


    apagar.addEventListener(
        "click",
        function(event) {

            event.stopPropagation();


            apagarConversa(
                conversa.id
            );

        }
    );


    item.appendChild(botao);

    item.appendChild(apagar);

    listaConversas.appendChild(item);
}


// ==========================================================
// CRIAR NOVA CONVERSA
// ==========================================================

async function criarNovaConversa() {

    try {

        const resposta =
            await fetch(
                "/conversa",
                {
                    method: "POST"
                }
            );


        const conversa =
            await resposta.json();


        conversaAtual =
            conversa.id;


        mostrarMensagemInicial();


        await carregarConversas();

    } catch (erro) {

        console.error(
            "Erro ao criar conversa:",
            erro
        );

    }
}


// ==========================================================
// CARREGAR CONVERSA
// ==========================================================

async function carregarConversa(id) {

    try {

        const resposta =
            await fetch(
                `/conversa/${id}`
            );


        const dados =
            await resposta.json();


        conversaAtual = id;


        mensagens.innerHTML = "";


        // Se a conversa estiver vazia

        if (
            dados.historico.length === 0
        ) {

            mostrarMensagemInicial();

        } else {

            // Mostrar histórico

            dados.historico.forEach(
                item => {

                    adicionarMensagem(
                        item.mensagem,
                        "user"
                    );


                    adicionarMensagem(
                        item.resposta,
                        "ada"
                    );

                }
            );

        }


        // Atualizar conversa ativa

        await carregarListaSemAbrir();


    } catch (erro) {

        console.error(
            "Erro ao carregar conversa:",
            erro
        );

    }
}


// ==========================================================
// ATUALIZAR SIDEBAR
// ==========================================================

async function carregarListaSemAbrir() {

    try {

        const resposta =
            await fetch("/conversas");


        const conversas =
            await resposta.json();


        listaConversas.innerHTML = "";


        conversas.forEach(
            conversa => {

                adicionarConversaNaLista(
                    conversa
                );

            }
        );

    } catch (erro) {

        console.error(
            "Erro ao atualizar lista:",
            erro
        );

    }
}


// ==========================================================
// ENVIAR MENSAGEM
// ==========================================================

async function enviarMensagem() {

    const texto =
        input.value.trim();


    if (texto === "") {

        return;

    }


    // Se por algum motivo
    // ainda não existir conversa,
    // criar uma.

    if (conversaAtual === null) {

        await criarNovaConversa();

    }


    // Mostrar mensagem do utilizador

    adicionarMensagem(
        texto,
        "user"
    );


    // Limpar campo

    input.value = "";


    try {

        const resposta =
            await fetch(
                "/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        mensagem: texto,

                        conversa_id:
                            conversaAtual

                    })
                }
            );


        const dados =
            await resposta.json();


        // Atualizar ID da conversa

        conversaAtual =
            dados.conversa_id;


        // Mostrar resposta da ADA

        adicionarMensagem(
            dados.resposta,
            "ada"
        );
        falar(dados.resposta);


        // Atualizar lista

        await carregarListaSemAbrir();


    } catch (erro) {

        adicionarMensagem(

            "Ocorreu um erro ao comunicar com a ADA.",

            "ada"

        );


        console.error(erro);

    }
}


// ==========================================================
// APAGAR CONVERSA
// ==========================================================

async function apagarConversa(id) {

    const confirmar =
        confirm(
            "Tens a certeza que queres apagar esta conversa?"
        );


    if (!confirmar) {

        return;

    }


    try {

        await fetch(
            `/conversa/${id}`,
            {
                method: "DELETE"
            }
        );


        // Se apagámos a conversa atual

        if (id === conversaAtual) {

            conversaAtual = null;

            mensagens.innerHTML = "";

            await carregarConversas();

        } else {

            await carregarListaSemAbrir();

        }


    } catch (erro) {

        console.error(
            "Erro ao apagar conversa:",
            erro
        );

    }
}


// ==========================================================
// BOTÃO NOVA CONVERSA
// ==========================================================

novaConversa.addEventListener(
    "click",
    criarNovaConversa
);


// ==========================================================
// BOTÃO ENVIAR
// ==========================================================

botaoEnviar.addEventListener(
    "click",
    enviarMensagem
);


// ==========================================================
// TECLA ENTER
// ==========================================================

input.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            enviarMensagem();

        }

    }
);

// ==========================================================
// VOZ DA ADA - TEXT TO SPEECH
// ==========================================================

function falar(texto) {

    // Verifica se o navegador suporta voz
    if (!("speechSynthesis" in window)) {

        console.log(
            "O navegador não suporta síntese de voz."
        );

        return;
    }

    // Para qualquer fala anterior
    window.speechSynthesis.cancel();

    const fala = new SpeechSynthesisUtterance(texto);

    // Define o idioma
    fala.lang = "pt-PT";

    // Velocidade da fala
    fala.rate = 1;

    // Tom da voz
    fala.pitch = 1;

    // Volume
    fala.volume = 1;

    window.speechSynthesis.speak(fala);
}


// ==========================================================
// RECONHECIMENTO DE VOZ COM ENVIO AUTOMÁTICO
// ==========================================================

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

if (SpeechRecognition) {

    const reconhecimento = new SpeechRecognition();

    reconhecimento.lang = "pt-PT";
    reconhecimento.continuous = false;
    reconhecimento.interimResults = false;

    let textoReconhecido = "";
    let ouvindo = false;

    microfone.addEventListener("click", () => {

        if (ouvindo) {
            return;
        }

        textoReconhecido = "";
        ouvindo = true;

        microfone.classList.add("ouvindo");
        microfone.textContent = "🔴";

        try {
            reconhecimento.start();
        } catch (erro) {
            ouvindo = false;
            microfone.classList.remove("ouvindo");
            microfone.textContent = "🎤";
            console.error("Erro ao iniciar o microfone:", erro);
        }
    });

    reconhecimento.onresult = (evento) => {

        textoReconhecido =
            evento.results[0][0].transcript.trim();

    };

    reconhecimento.onerror = (evento) => {

        console.error("Erro no reconhecimento:", evento.error);

        textoReconhecido = "";
        ouvindo = false;

        microfone.classList.remove("ouvindo");
        microfone.textContent = "🎤";
    };

    reconhecimento.onend = () => {

        ouvindo = false;

        microfone.classList.remove("ouvindo");
        microfone.textContent = "🎤";

        if (textoReconhecido !== "") {

            input.value = textoReconhecido;

            // Envia a mensagem usando a função
            // de envio que a ADA já utiliza.
            botaoEnviar.click();
        }
    };

} else {

    microfone.disabled = true;
    microfone.textContent = "🚫";

    console.log(
        "O reconhecimento de voz não é suportado neste navegador."
    );
}




// ==========================================================
// INICIAR A APLICAÇÃO
// ==========================================================

carregarConversas();