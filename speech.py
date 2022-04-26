from googletrans import Translator
import streamlit as st
translator = Translator()
st.header("here is your translation and its pronunciation!")

text_user = st.text_input("give a me text to translate ")
tar_lang = st.text_input("give me a target language ")

langaugeis = translator.translate(text_user, dest = tar_lang)

tts1=gTTS(langaugeis.text, tar_lang)
tts1.save("lang.mp3")
#ipd.display(ipd.Audio("lang.mp3")
st.audio("lang.mp3", autoplay=False)
