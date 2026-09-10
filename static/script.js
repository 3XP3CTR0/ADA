const input = document.getElementById("mensagem");
const botaoEnviar = document.getElementById("enviar");
const mensagens = document.getElementById("mensagens");
const novaConversa = document.getElementById("nova-conversa");


function adicionarMensagem(texto, tipo) {

    const mensagem = document.createElement("div");

    mensagem.classList.add("message");

    if (tipo === "ada") {
        mensagem.classList.add("ada-message");
    } else {
        mensagem.classList.add("user-message");
    }


    const avatar = document.createElement("div");

    avatar.classList.add("message-avatar");

    avatar.textContent = tipo === "ada" ? "🤖" : "👤";


    const conteudo = document.createElement("div");

    conteudo.classList.add("message-content");

    conteudo.textContent = texto;


    mensagem.appendChild(avatar);
    mensagem.appendChild(conteudo);

    mensagens.appendChild(mensagem);


    mensagens.scrollTop = mensagens.scrollHeight;
}


async function enviarMensagem() {

    const texto = input.value.trim();


    if (texto === "") {
        return;
    }


    // Mostrar mensagem do utilizador

    adicionarMensagem(texto, "user");


    // Limpar campo

    input.value = "";


    try {

        const resposta = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                mensagem: texto
            })

        });


        const dados = await resposta.json();


        // Mostrar resposta da ADA

        adicionarMensagem(dados.resposta, "ada");


    } catch (erro) {

        adicionarMensagem(
            "Ocorreu um erro ao comunicar com a ADA.",
            "ada"
        );

        console.error(erro);
    }
}


botaoEnviar.addEventListener(
    "click",
    enviarMensagem
);


input.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            enviarMensagem();

        }

    }
);


novaConversa.addEventListener(
    "click",
    function() {

        mensagens.innerHTML = "";

        adicionarMensagem(
            "Olá! Eu sou a ADA. Como posso ajudar-te hoje?",
            "ada"
        );

    }
);