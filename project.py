
import streamlit as st
from PIL import Image
from googletrans import Translator
#from gtts import gTTS

import pytesseract
import shutil
import os
import random

urlfoto = "https://raw.githubusercontent.com/MartinaTebaldini/Tebaldini_CP/main/lingue-straniere.jpg
st.image(urlfoto)

st.header("import an image and i will translate it for you!")
uploaded_file = st.file_uploader("Please upload an Image file")
if uploaded_file is not None:
    
    extractedInformation = pytesseract.image_to_string(Image.open(uploaded_file)) #???????? how can i call the uploaded file in a general way?
    st.write("here is the text extracted from the image")
    st.write(extractedInformation)

    translator = Translator()
    #detectedLanguage = translator.detect(extractedInformation)
    #st.write(detectedLanguage) #to detect the language of the image

    st.write("here is a link with the language codes, pick one!")
    url = "https://cloud.google.com/translate/docs/languages"
    st.write(url)
    tar_lang = st.text_input("in which language do you want to translate the text?")
    #st.write("you selected", tar_lang)

    if tar_lang != "":
        tra_text = translator.translate(extractedInformation, dest = tar_lang)
        st.write("here is the translation in", tar_lang)
        st.write(tra_text.text)


