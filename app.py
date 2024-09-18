import streamlit as st
import pandas as pd
from datetime import date


def gravar_dados(nome, data_inicio, data_fin, casa_escolhida ):
    if nome and data_inicio and data_fin >= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {data_inicio.strftime(format='%d/%m/%Y')}, {data_fin.strftime(format='%d/%m/%Y')}, {casa_escolhida}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


st.set_page_config(
    page_title= "Alugel El Ancla",
    page_icon= "⚓",
    layout="wide")

st.title("Casas de alugel 'El Ancla' ")
st.title("Agenda de ferias!")
st.divider()


st.header(":violet[CALENDÁRIO] :sunglasses:")
st.write("Aqui você pode selecionar sua melhor data de férias! :smile:")


col1, col2 = st.columns(2)

data_inicio = col1.date_input(
    "Selecione sua data de entrada:",
    format="DD/MM/YYYY",
    value=None,
    key="dt_inicio"
)

data_fin = col2.date_input(
    "Selecione sua data de partida:",
    format="DD/MM/YYYY",
    value= None,
    key="dt_fin"
)

nome = st.text_input("Digite o seu nome",
                     key="nome_cliente")



casa_escolhida = st.selectbox("Casa Escolhida",
                              ["Ancla", "Timón", "Virazón"],
                              key="cs_escolhida")


btn_cadastrar = st.button("Cadastrar", 
                          on_click= gravar_dados,
                          args=[nome, data_inicio, data_fin, casa_escolhida])


if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Seus dias foram salvos com sucesso!",
                   icon="✔")
    else:
        st.error("Dias ocupados, tente novamente.",
                 icon="❌")


