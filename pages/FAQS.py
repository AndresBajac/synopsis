import streamlit as st
import time
from streamlit_extras.colored_header import colored_header

st.set_page_config(
    page_title="FAQS",
    page_icon=":scissors:",
)

colored_header(
    label="Preguntas Frecuentes 🤔",
    description="#FACTS",
    color_name="violet-10",
)

st.sidebar.markdown("# FAQs")

with st.expander("¿Qué es Synopsis?"):
    st.markdown('**Synopsis** es el proyecto para el Trabajo Final de Máster propuesto por el Grupo 3 del **Master en Big Data y Data Science** de la Universidad Complutense de Madrid.')

with st.expander("¿Como funciona?"):
    st.markdown("Se trata de una combinación de modelos de Deep Learning, alojados en el Hub de HuggingFace, disponibles en forma _open source_.") 
    st.markdown("- En primer lugar encontramos el modelo Whisper de _Automatic Speech Recognition_ de la empresa Open AI (la misma de ChatGPT).")
    st.markdown("- Luego encontramos al modelo DistilBART, utilizado para el proceso de resumen de la transcripción del audio.")
    st.markdown("- Finalmente encontramos el Tokenizador T5 de VoiceLab, dedicado a la obtención de _Keywords_ o palabras clave de la traducción para una visión rápida de los tópicos principales.")
    
with st.expander("¿Funciona en otros idiomas?"):
    st.markdown("Si! Tanto los modelos de transcripción como de resumen y palabras clave funcionan correctamente en los principales idiomas. Sin embargo, como estos modelos fueron entrenados en su mayoría por datasets en inglés, puede que tengan un mejor desempeño en dicho idioma.")    

with st.expander("¿Esto es inteligencia artificial?"):
    st.markdown("Esta web utiliza modelos de Deep Learning, es decir redes neuronales, y modelos tipo transformers, que son las bases de la Inteligencia Artificial (IA). El deep learning es un conjunto de algoritmos de aprendizaje automático que utiliza redes neuronales artificiales para modelar abstracciones de alto  y una de sus  aplicaciónes es el reconocimiento de patrones, como en este caso para el audio y en el modelo BART, para el encadenamiento sintático y semántico de oraciones en un contexto.")

with st.expander("¿Qué limitaciones esta herramienta?"):
    st.markdown("A mejor calidad de audio, mejor será el resultado de la transcripción, y por consiguiente, del resumen que provee el modelo. Es por esto que la herramienta funciona mejor con videos inferiores a una hora. Por otro lado, es útil para obtener transcripciones de letras de canciones, aunque dependerá de la modulación del artista para una mejor comprensión de la misma y su posterior resultado.")
