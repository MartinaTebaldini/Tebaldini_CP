import streamlit as st
from googletrans import Translator
from gtts import gTTS
 

st.header("here is your translation and its pronunciation!")

text_user = st.text_input("give a me text to translate ")

if text_user != "":
 tar_lang = st.text_input("give me a target language ")
 translator = Translator()
 if tar_lang != "":
  tra_text = translator.translate(text_user, dest = tar_lang)
  print(tra_text)
  tts1=gTTS(tra_text.text, tar_lang)
  tts1.save("lang.mp3")
#ipd.display(ipd.Audio("lang.mp3")
#st.audio("lang.mp3")
  audio_file = open("lang.mp3", "rb")

  st.audio(data=audio_file, format="audio/mp3", start_time=0)
