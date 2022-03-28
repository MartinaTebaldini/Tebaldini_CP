import streamlit as st
import json, requests 
keyword=st.text_input('plz give me a keyword')

synonims = 'https://api.datamuse.com/words?rel_syn='+ keyword + '&max=4'
antonyms = 'https://api.datamuse.com/words?rel_ant='+ keyword + '&max=4'
meaning = 'https://api.datamuse.com/words?ml'+ keyword + '&max=4'

option = st.selectbox('What would you like to know about this word?', ('synonims', 'antonyms', 'meaning'))
st.write('You selected:', option)


response1 = requests.get(synonims)
response2 = requests.get(meaning)
response3 = requests.get(antonyms)
dataFromDatamuse1 = json.loads(response1.text)
dataFromDatamuse2 = json.loads(response2.text)
dataFromDatamuse3 = json.loads(response3.text)

if option == "synonims":
  st.write(dataFromDatamuse1)
elif option == "meaning":
  st.write(dataFromDatamuse2)
else:
  st.write(dataFromDatamuse3)
  





#st.header("hello world")  
#st.text("from Brixen")

#st.write('The current movie title is', title)
