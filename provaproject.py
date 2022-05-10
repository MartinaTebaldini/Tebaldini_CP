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
  
