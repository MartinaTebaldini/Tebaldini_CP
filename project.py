
import streamlit as st
from PIL import Image
from googletrans import Translator
from gtts import gTTS

import pytesseract
import shutil
import os
import random

urlfoto = "https://raw.githubusercontent.com/MartinaTebaldini/Tebaldini_CP/main/lingue-straniere.jpg"
st.image(urlfoto)

st.title("Import an image and I will translate it for you!")
uploaded_file = st.file_uploader("Please upload an Image file")
if uploaded_file is not None:
    
    extractedInformation = pytesseract.image_to_string(Image.open(uploaded_file), lang='jpn') #???????? how can i call the uploaded file in a general way?
    st.subheader("Here is the text extracted from the image")
    st.write(extractedInformation)

    translator = Translator()
    #detectedLanguage = translator.detect(extractedInformation)
    #st.write(detectedLanguage) #to detect the language of the image

    st.subheader("here is a link with the language codes, pick one!")
    url = "https://cloud.google.com/translate/docs/languages"
    st.write(url)
    tar_lang = st.text_input("in which language do you want to translate the text?")
    #st.write("you selected", tar_lang)

    if tar_lang != "":
        tra_text = translator.translate(extractedInformation, dest = tar_lang)
        st.subheader("here is the translation in", tar_lang)
        st.write(tra_text.text)
        st.subheader("here is the pronunciation!", tra_text.pronunciation)
        tts1=gTTS(tra_text.text, tar_lang)
        tts1.save("lang.mp3")
        audio_file = open("lang.mp3", "rb")
        st.audio(data=audio_file, format="audio/mp3", start_time=0)


