#import streamlit as st
from googletrans import Translator
translator = Translator()
word = True
word = st.input_("gimme a word or phrase")
langaugeis = translator.translate(word, dest = "it")
s.write(langaugeis.text)

