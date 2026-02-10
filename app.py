import streamlit as st

st.set_page_config(page_title="Treino de Inglês", layout="centered")

frases = [
    "Eu gosto de aprender inglês",
    "Hoje está um dia bonito",
    "Eu preciso estudar todos os dias",
    "Ela trabalha em casa",
    "Nós vamos viajar amanhã"
]

if "indice" not in st.session_state:
    st.session_state.indice = 0

st.title("🇧🇷 ➜ 🇺🇸 Treino de Tradução")

st.write("📌 Progresso:", st.session_state.indice, "/", len(frases))

frase_pt = frases[st.session_state.indice]
st.write("### Traduza a frase:")
st.write(f"**{frase_pt}**")

resposta = st.text_input("Digite em inglês:")

if st.button("Verificar"):
    if resposta.strip() == "":
        st.warning("Digite a tradução antes de continuar.")
    else:
        st.success("Resposta registrada! ⭐")
        st.session_state.indice += 1

        if st.session_state.indice >= len(frases):
            st.balloons()
            st.success("🎉 Parabéns! Você concluiu o treino.")
            st.session_state.indice = 0
