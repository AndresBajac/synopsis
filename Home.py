import streamlit as st
import time # agregar barra de carga
from pytube import YouTube 
import whisper
import numpy as np
from io import BytesIO

st.set_page_config(
    page_title="Home",
    page_icon=":scissors:",
)

st.title('Synopsis.io')
st.markdown("### Your Deep Learning tool for video summarization 📹")
st.sidebar.markdown("# Synopsis.IA")

with st.form(key='form_1'):
    url = st.text_input('Enter Youtube video URL:')
    st.form_submit_button('Transcribe')
    
    if url:
    
        # Open AI's Whisper model
        asr_model = whisper.load_model('small')

        # URL del video seleccionado
        yt = YouTube(url=url)

        # Descarga del audio
        audio_streams = yt.streams.filter(only_audio = True)
        audio_streams[0].download(filename='tmp.mp4')

        result = asr_model.transcribe('tmp.mp4')
        transcription = result['text']
        st.write(transcription)

        st.toast('Audio transcribed!')

    else:
        st.markdown('or')        

with st.form(key='form_2'):
    file_uploader = st.file_uploader('Upload your audio file')
    st.form_submit_button('Transcribe')

    if file_uploader:

        st.toast('Audio transcribed!')

    else:

        st.markdown("Supported audio formats:")
        st.markdown("- .mp3")
        st.markdown("- .mp4")
        st.markdown("- .wav")