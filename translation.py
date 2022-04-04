import streamlit as st
#import json,requests
from googletrans import Translator
#import json, requests 
#from pprint import pprint
translator = Translator()
word = st.text_input("gimme a word or phrase")
langaugeis = translator.translate(word, dest = "it")

st.write(langaugeis.text)
 
