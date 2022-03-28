import streamlit as st
import json, requests 
from pprint import pprint

keyword=st.text_input('plz give me a keyword')


option = st.selectbox('What would you like to know about this word?', ('synonims', 'antonyms', 'meaning'))
st.write('You selected:', option)


if option == "synonims":
  Url = 'https://api.datamuse.com/words?rel_syn='+ keyword + '&max=4'
elif option == "meaning":
  url = 'https://api.datamuse.com/words?ml='+ keyword + '&max=4'
else:
  url = 'https://api.datamuse.com/words?rel_ant='+ keyword + '&max=4'
  
response = requests.get(url)   


dataFromDatamuse = json.loads(response.text) 
pprint(dataFromDatamuse[0:10]
  





#st.header("hello world")  
#st.text("from Brixen")

#st.write('The current movie title is', title)
