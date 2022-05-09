
import streamlit as st
from PIL import Image
from googletrans import Translator
#from gtts import GTTS

import pytesseract
import shutil
import os
import random


    
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
uploaded_file = st.file_uploader("Please upload an Image file")
extractedInformation = pytesseract.image_to_string(Image.open(uploaded_file))
st.write(extractedInformation)

translator = Translator()
detectedLanguage = translator.detect(extractedInformation)
st.write(detectedLanguage)

tar_language = st.text_input("give me your target language ")
text_to_translate = (extractedInformation)
langaugeis = translator.translate(text_to_translate, dest = tar_language)
st.write(langaugeis.text)
