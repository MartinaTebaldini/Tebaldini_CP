import streamlit as st
from googletrans import Translator

translator = Translator()
word = st.text_input("gimme a word or phrase")
tar_language = input("give me a target language, it should be a two letter word, like es or de: ")
languaget = translator.translate(word, dest = tar_language)

st.write("the translation of youe word is", languaget.text)
 
