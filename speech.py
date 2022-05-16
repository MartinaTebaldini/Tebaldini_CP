import streamlit as st
from googletrans import Translator
from gtts import gTTS

urlfoto = "https://raw.githubusercontent.com/MartinaTebaldini/Tebaldini_CP/main/rs7352_thinkstockphotos-493800479-low.jpg"
st.image(urlfoto)

st.header("here is your translation and its pronunciation!")

text_user = st.text_input("give me a text to translate ")

if text_user != "":
 #tar_lang = st.selectbox("choose one of the following languages", ("it", "de", "se", "hr", "et", "en", "hu"))
 st.write("here is a link with the language codes")
 url = "https://cloud.google.com/translate/docs/languages"
 st.write(url)
 #if you dont want the selectbox write simply as follows:
 tar_lang = st.text_input("in which language do you want to translate the text?")
 st.write("you selected", tar_lang)
 translator = Translator()
 if tar_lang != "":
  tra_text = translator.translate(text_user, dest = tar_lang)
  st.write(tra_text.text)
  st.write("here is the pronunciation!", tra_text.pronunciation)
  ttmp3=gTTS(tra_text.text, lang=tar_lang, tld="com")
  ttmp3.save("lang.mp3")
#ipd.display(ipd.Audio("lang.mp3")
#st.audio("lang.mp3")
  audio_file = open("lang.mp3", "rb")

  st.audio(data=audio_file, format="audio/mp3", start_time=0)
