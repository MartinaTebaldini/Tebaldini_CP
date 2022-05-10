import streamlit as st
from PIL import Image
from googletrans import Translator
from gtts import gTTS

import pytesseract
import shutil
import os
import random


option = st.selectbox(
     'how would you like to import your image?',
     ('browser', 'camera'))

st.write('You selected:', option)

if browser:
     uploaded_file = st.file_uploader("Please upload an Image file")
else:
     picture = st.camera_input("take a picture!)
  
