from googletrans import Translator
import streamlit as st
translator = Translator()

st.header("here is your translation!")
word = st.text_input("gimme a word or phrase", "")
if word != "":
 #tar_language = st.text_input("give me a target language, it should be a two letter word, like es or de: ")
 languaget = translator.translate(word, dest = "it")

st.write("the translation of your word is", languaget.text)
 
