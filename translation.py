#import streamlit as st
from googletrans import Translator
translator = Translator()
word = st.text_input("gimme a word or phrase")
langaugeis = translator.translate(word, dest = "it")
s.write(langaugeis.text)

