
import streamlit as st
from PIL import Image
from googletrans import Translator
#from gtts import GTTS

import pytesseract
import shutil
import os
import random


    
#pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
uploaded_file = st.file_uploader("Please upload an Image file")
extractedInformation = pytesseract.image_to_string(Image.open(uploaded_file))
st.write(extractedInformation)
