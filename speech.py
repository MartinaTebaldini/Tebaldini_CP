from googletrans import Translator
import streamlit as st
st.header("here is your translation and its pronunciation!")

text_user = st.input("give a me text to translate ")
tar_lang = st.input("give me a target language ")

langaugeis = translator.translate(text_user, dest = tar_lang)

tts1=gTTS(text = text_user, lang = tar_lang)
tts1.save("lang.mp3")
#ipd.display(ipd.Audio("lang.mp3")
st.audio("lang.mp3", autoplay=False))
