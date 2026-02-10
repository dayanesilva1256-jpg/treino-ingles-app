import streamlit as st
import json
import os
import difflib

st.set_page_config(
    page_title="Treino de Inglês",
    page_icon="🇺🇸",
    layout="centered"
)

frases = [
    ("Eu gosto de estudar inglês todos os dias.", "I like to study English every day."),
    ("Ela trabalha em um hospital.", "She works in a hospital."),
    ("Nós vamos viajar amanhã.", "We are going to travel tomorrow."),
    ("Eu estou aprendendo algo novo.", "I am learning something new."),
    ("Ele mora perto do trabalho.", "He lives near his job."),
    ("Eu acordei cedo hoje.", "I woke up early today."),
    ("Eles gostam de assistir filmes.", "They like to watch movies."),
    ("Eu preciso praticar mais.", "I need to practice more."),
    ("Ela está muito cansada.", "She is very tired."),
    ("Nós almoçamos juntos ontem.", "We had lunch together yesterday.")
]

TOTAL = len(frases)
ARQUIVO = "progresso.json"

def similaridade(a, b):
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {"indice": 0, "notas": []}

def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f)

if "tela" not in st.session_state:
    st.session_state.tela = "menu"

if "dados" not in st.session_state:
    st.session_state.dados = carregar()

# MENU
if st.session_state.tela == "menu":
    st.title("🇺🇸 Treino de Tradução")

    indice = st.session_state.dados["indice"]
    notas = st.session_state.dados["notas"]

    st.write(f"📍 Progresso: **{indice}/{TOTAL}**")

    if notas:
        media = round(sum(notas) / len(notas), 1)
        st.write(f"📊 Média: **{media}**")

    if st.button("▶️ Começar / Continuar"):
        st.session_state.tela = "treino"
        st.experimental_rerun()

    if st.button("🔄 Reiniciar"):
        st.session_state.dados = {"indice": 0, "notas": []}
        salvar(st.session_state.dados)
        st.success("Progresso reiniciado!")

    st.stop()

# TREINO
indice = st.session_state.dados["indice"]

if indice >= TOTAL:
    st.success("🎉 Você terminou todas as frases!")
    if st.button("⬅️ Voltar ao menu"):
        st.session_state.tela = "menu"
    st.stop()

frase_pt, frase_ref = frases[indice]

st.markdown(f"### Frase {indice + 1}/{TOTAL}")
st.info(frase_pt)

resposta = st.text_area("Digite sua tradução em inglês:")

if st.button("✅ Corrigir"):
    if resposta.strip() == "":
        st.warning("Digite uma tradução.")
    else:
        nota = max(1, round(similaridade(resposta, frase_ref) * 10))
        st.session_state.dados["notas"].append(nota)
        st.session_state.dados["indice"] += 1
        salvar(st.session_state.dados)

        st.success(f"⭐ Nota: {nota}/10")
        st.caption(f"Tradução de referência: {frase_ref}")

        if st.button("➡️ Próxima"):
            st.experimental_rerun()

st.progress((indice + 1) / TOTAL)
