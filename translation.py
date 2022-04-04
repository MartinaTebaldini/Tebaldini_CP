import streamlit as st
from googletrans import Translator

translator = Translator()
word = st.text_input("gimme a word or phrase")
languaget = translator.translate(word, dest = "it")

st.write(languaget.text)
 
