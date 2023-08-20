import streamlit as st
import time
from PIL import Image

st.set_page_config(
    page_title="About",
    page_icon=":scissors:",
)

st.markdown("# About 🧑🏼‍💻")
st.sidebar.markdown("# About")

image = Image.open('ucm_fct.jpeg')

st.image(image, caption='Facultad de Comercio y Turismo - Universidad Complutense de Madrid')
st.markdown('**Synopsis** es el proyecto para el Trabajo Final de Máster propuesto por el Grupo 3 del **Master en Big Data y Data Science** de la Universidad Complutense de Madrid.')
st.markdown('Desarrolladores del proyecto:')
