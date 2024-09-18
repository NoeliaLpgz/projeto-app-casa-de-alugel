import streamlit as st

st.title("Casa 'Timón'")


col1, col2 = st.columns(2)

col1.image("image_timon_sala.jpeg", 
         caption="Sala do Timon")

col2.image("image_timon_portao.jpeg",
         caption="Portao do Timón")

