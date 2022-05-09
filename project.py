import streamlit as st
from googletrans import Translator
from gtts import GTTS

import pytesseract
import shutil
import os
import random
try:
    from PIL import Image
except ImportError:
    import Image

uploaded_file = st.file_uploader("Choose a file")
extractedInformation = pytesseract.image_to_string(Image.open(uploaded_file))
st.write(extractedInformation)
