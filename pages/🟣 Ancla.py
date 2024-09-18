import streamlit as st

st.title("Casa 'Ancla'")


col1, col2, col3 = st.columns(3)


col1.image("image_ancla_churrasqueira.jpeg", 
         caption="Churrasqueira Casa Ancla")

col2.image("image_ancla.jpeg", 
         caption="Ancla do ano 1982")

col3.image("imagen_patio_ancla.jpeg", 
         caption="Pátio de 'El Ancla' ")

