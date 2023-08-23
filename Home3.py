# Instalación de librerías
import streamlit as st
import pytube
import os
import whisper
from pytube import YouTube
from functools import lru_cache
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Cache para el modelo ASR
@lru_cache(maxsize=1)
def load_asr_model():
    return whisper.load_model('small')

def main():
    st.title("YouTube Video Transcriber")

    # Ingreso de URL del vídeo de YouTube
    url = st.text_input("Ingrese la URL del vídeo de YouTube:")
    if url:
        st.write("URL del video:", url)

        # Descargar audio y transcribir
        download_and_transcribe(url)

def download_and_transcribe(url):
    # Cargar modelo ASR
    asr_model = load_asr_model()

    # Descargar audio
    st.text("Descargando el audio del video...")
    yt = YouTube(url=url)
    audio_streams = yt.streams.filter(only_audio = True)
    audio_streams[0].download(filename='tmp.mp4')

    result = asr_model.transcribe('tmp.mp4')
    transcription = result['text']
    st.write(transcription)


if __name__ == "__main__":
    main()