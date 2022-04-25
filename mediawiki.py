import streamlit as st
import json, requests 
from pprint import pprint
#keyword = True
#while keyword != "nothing":
keyword = st.text_input("what you want to know about ")
url ='https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch='+keyword
st.write(url)
response = requests.get(url) 
dataFromWikipedia = json.loads(response.text)
# Uncomment to see the raw JSON text:
st.write(dataFromWikipedia) 
# Uncomment to see a better readable JSON text:
#pprint(dataFromWikipedia) #dont forget to import the correct library to make this work
#textwithHTMLtags = dataFromWikipedia["query"]["search"][0]["snippet"]
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(textwithHTMLtags)

 
#textwithoutHTMLtags = soup.get_text()
#st.write(textwithoutHTMLtags)
