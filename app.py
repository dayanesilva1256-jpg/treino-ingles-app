import streamlit as st

st.set_page_config(page_title="Treino de Inglês", layout="centered")

# ===== 100 FRASES =====
frases = [
("Eu gosto de aprender inglês", "I like to learn English"),
("Hoje está um dia bonito", "Today is a beautiful day"),
("Eu preciso estudar todos os dias", "I need to study every day"),
("Ela trabalha em casa", "She works from home"),
("Nós vamos viajar amanhã", "We will travel tomorrow"),
("Eu estou com fome", "I am hungry"),
("Ele gosta de música", "He likes music"),
("Eu moro no Brasil", "I live in Brazil"),
("Está chovendo hoje", "It is raining today"),
("Nós precisamos descansar", "We need to rest"),
("Eu acordei cedo hoje", "I woke up early today"),
("Ela gosta de ler livros", "She likes to read books"),
("Nós estamos aprendendo inglês", "We are learning English"),
("Eu tenho dois irmãos", "I have two siblings"),
("Ele trabalha muito", "He works a lot"),
("Hoje é segunda-feira", "Today is Monday"),
("Eu gosto de café", "I like coffee"),
("Ela mora perto daqui", "She lives near here"),
("Nós saímos ontem à noite", "We went out last night"),
("Eu estou cansado", "I am tired"),
("Ele estuda à noite", "He studies at night"),
("Ela fala inglês muito bem", "She speaks English very well"),
("Eu preciso de ajuda", "I need help"),
("Nós estamos atrasados", "We are late"),
("Hoje faz calor", "It is hot today"),
("Eu quero aprender mais", "I want to learn more"),
("Ela gosta de cozinhar", "She likes to cook"),
("Nós vamos sair agora", "We are going out now"),
("Eu esqueci minha senha", "I forgot my password"),
("Ele está dormindo", "He is sleeping"),
("Ela chegou cedo", "She arrived early"),
("Nós estamos felizes", "We are happy"),
("Eu gosto de viajar", "I like to travel"),
("Ele mora sozinho", "He lives alone"),
("Ela trabalha muito bem", "She works very well"),
("Nós precisamos estudar", "We need to study"),
("Eu estou aprendendo rápido", "I am learning fast"),
("Ele gosta de esportes", "He likes sports"),
("Ela está esperando", "She is waiting"),
("Nós chegamos em casa", "We arrived home"),
("Eu quero descansar", "I want to rest"),
("Ele está ocupado", "He is busy"),
("Ela gosta de música", "She likes music"),
("Nós estamos prontos", "We are ready"),
("Eu perdi meu celular", "I lost my phone"),
("Ele chegou tarde", "He arrived late"),
("Ela saiu cedo", "She left early"),
("Nós estamos trabalhando", "We are working"),
("Eu gosto de estudar", "I like to study"),
("Ele precisa de ajuda", "He needs help"),
("Ela está feliz hoje", "She is happy today"),
("Nós vamos aprender juntos", "We will learn together"),
("Eu estou com sono", "I am sleepy"),
("Ele gosta de viajar", "He likes to travel"),
("Ela mora longe", "She lives far away"),
("Nós estamos estudando agora", "We are studying now"),
("Eu quero melhorar meu inglês", "I want to improve my English"),
("Ele trabalha em casa", "He works from home"),
("Ela gosta de filmes", "She likes movies"),
("Nós vamos começar agora", "We will start now"),
("Eu estou feliz hoje", "I am happy today"),
("Ele precisa estudar mais", "He needs to study more"),
("Ela gosta de aprender", "She likes to learn"),
("Nós estamos cansados", "We are tired"),
("Eu cheguei agora", "I just arrived"),
("Ele saiu agora", "He just left"),
("Ela gosta de conversar", "She likes to talk"),
("Nós estamos melhorando", "We are improving"),
("Eu gosto de desafios", "I like challenges"),
("Ele está aprendendo inglês", "He is learning English"),
("Ela trabalha de manhã", "She works in the morning"),
("Nós vamos conseguir", "We will succeed"),
("Eu estou confiante", "I am confident"),
("Ele gosta de estudar", "He likes to study"),
("Ela está animada", "She is excited"),
("Nós estamos quase lá", "We are almost there"),
("Eu terminei agora", "I just finished"),
("Ele começou cedo", "He started early"),
("Ela gosta de ajudar", "She likes to help"),
("Nós estamos focados", "We are focused"),
("Eu quero continuar", "I want to continue"),
("Ele está feliz", "He is happy"),
("Ela gosta de inglês", "She likes English"),
("Nós aprendemos muito", "We learned a lot")
]

# ===== ESTADO =====
if "indice" not in st.session_state:
    st.session_state.indice = 0

if "historico" not in st.session_state:
    st.session_state.historico = []

st.title("🇧🇷 ➜ 🇺🇸 Treino de Tradução")

# ===== FINAL =====
if st.session_state.indice >= len(frases):
    notas = [h["nota"] for h in st.session_state.historico]
    media = sum(notas) / len(notas)

    st.success("🎉 Treino finalizado!")
    st.write(f"📊 Média final: **{media:.1f}/10**")

    st.subheader("📜 Histórico")
    for h in st.session_state.historico:
        st.write(f"{h['pt']} ➜ {h['user']} | ⭐ {h['nota']}/10")

    if st.button("Recomeçar"):
        st.session_state.clear()

    st.stop()

# ===== FRASE ATUAL =====
pt, correta = frases[st.session_state.indice]

st.write(f"### Frase {st.session_state.indice + 1}/100")
st.write(f"**{pt}**")

resposta = st.text_input("Digite em inglês:")

if st.button("Verificar"):
    if resposta.strip() == "":
        st.warning("Digite algo antes de continuar.")
    else:
        user_words = resposta.lower().split()
        correct_words = correta.lower().split()

        acertos = sum(1 for w in user_words if w in correct_words)
        nota = round((acertos / len(correct_words)) * 10)
        nota = max(nota, 1)

        st.session_state.historico.append({
            "pt": pt,
            "user": resposta,
            "nota": nota
        })

        st.success(f"⭐ Nota: {nota}/10")
        st.info(f"Resposta correta: {correta}")

        st.session_state.indice += 1
