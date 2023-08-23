import streamlit as st
import time # agregar barra de carga
from pytube import YouTube 
import whisper
#from audio_recorder_streamlit import audio_recorder
from tempfile import NamedTemporaryFile

# https://www.youtube.com/shorts/xDNzz8yAH7I
# Open AI's Whisper model

asr_model = whisper.load_model('tiny')

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

        # URL del video seleccionado
        yt = YouTube(url=url)

        audio_streams = yt.streams.filter(only_audio=True)
        audio_file = NamedTemporaryFile(delete=False, suffix=".mp3")
        audio_streams[0].download(output_path=r'C:\Complutense\synopsis\synopsis', filename=audio_file.name)
        audio_file.close()

        result = asr_model.transcribe(audio_file.name)  # Transcribe the downloaded audio file
        transcription = result['text']
        st.write(transcription)

        st.toast('Audio transcribed!')