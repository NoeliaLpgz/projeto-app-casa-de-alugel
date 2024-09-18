import streamlit as st

st.title("Casa 'Virazón")


col1, col2, col3 = st.columns(3)

col1.image("image_virazon_sala.jpeg",
         caption="Sala da casa VIRAZON")

col2.image("image_garage_virazon.jpeg",
         caption="Garaje da VIRAZON")

col3.image("image_cocina_virazon.jpeg",
         caption="Cocina da VIRAZON")
