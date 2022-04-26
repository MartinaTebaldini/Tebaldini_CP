import streamlit as st
from googletrans import Translator
from gtts import gTTS
 

st.header("here is your translation and its pronunciation!")

text_user = st.text_input("give a me text to translate ")
tar_lang = st.text_input("give me a target language ")

translator = Translator()
tra_text = translator.translate(text_user, dest = tar_lang)

tts1=gTTS(tra_text.text, tar_lang)
tts1.save("lang.mp3")
#ipd.display(ipd.Audio("lang.mp3")
st.audio("lang.mp3")
