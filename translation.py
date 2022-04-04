import streamlit as st
from googletrans import Translator
translator = Translator()
word = True
while word != "nothing":
  word = st.text_input("gimme a word or phrase ")
  langaugeis = translator.translate(word, dest = "it")
  st.write(langaugeis)


#import json, requests 
#from pprint import pprint

