
import streamlit as st
from PIL import Image
from googletrans import Translator
from gtts import gTTS

import pytesseract
import shutil
import os
import random

st.title("Import an image and I will translate it for you!")
urlfoto = "https://raw.githubusercontent.com/MartinaTebaldini/Tebaldini_CP/main/lingue-straniere.jpg"
st.image(urlfoto)
st.write("This app converts images into texts, more specifically it reads and recognises texts in images, it detects the language and then the text can be translated into the language of the user's choice. As output, it will give both the translated text and audio")

with st.expander("How to use"):
     st.write("""
         - Import an image
         - Select the language you want translate the text into
     """)


option = st.selectbox(
     'how would you like to import your image? Please select either browser or camera',
     ('browser', 'camera'))

#st.write('You selected:', option)

if option == "browser":
     picture = st.file_uploader("Please upload an Image file")
else:
     picture = st.camera_input("take a picture!")
  
if picture is not None:
     extractedInformation = pytesseract.image_to_string(Image.open(picture), lang='jpn+eng+hrv+ara+it') #???????? how can i call the uploaded file in a general way?
     st.markdown("**Here is the text extracted from the image**")
     st.write(extractedInformation)

     translator = Translator()
     detectedLanguage = translator.detect(extractedInformation)
     st.write(detectedLanguage) #to detect the language of the image

     st.markdown("**here is a link with the language codes, please, pick one!**")
     url = "https://cloud.google.com/translate/docs/languages"
     st.write(url)
     tar_lang = st.text_input("in which language do you want to translate the text?")
    #st.write("you selected", tar_lang)
     
     if tar_lang != "":
          if tar_lang == detectedLanguage:
               st.write("the language you selected is the same as the detected one! Pick another one")
          else:
               tra_text = translator.translate(extractedInformation, dest = tar_lang)
               st.write("here is the translation in", tar_lang)
               st.write(tra_text.text)
               st.write("here is the pronunciation!", tra_text.pronunciation)
               ttmp3=gTTS(tra_text.text, lang =tar_lang, tld="com")
               ttmp3.save("lang.mp3")
               audio_file = open("lang.mp3", "rb")
               st.audio(data=audio_file, format="audio/mp3", start_time=0)
          with st.expander("See credits"):
               st.write("""
               - for the language codes: https://cloud.google.com/translate/docs/languages
               - for the initial logo: google
               - for streamlit documentation: https://docs.streamlit.io/
               """)          
           
          


