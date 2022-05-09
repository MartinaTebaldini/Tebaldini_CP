
import speech_recognition as sr
import streamlit as st
import requests

r = sr.Recognizer()
#AUDIO_FILE = "sample_audio_short.wav"   #mp3 files are not supported
AUDIO_FILE = "sample_audio_long.wav"    #these files are in files-section of Class08 folder, on MS Teams.

AUDIO_FILE= st.file_uploader("choose a file") 
if AUDIO_FILE is not None:
  st.write("you uploaded this file")
  st.audio(AUDIO_FILE, format = "audio/wav")
  with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file


  recognised_text= r.recognize_google(audio)

  st.write('the text recognized from the audio seems to be: ')
  st.write( recognised_text)
