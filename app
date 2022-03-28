import streamlit as st
keyword=input('plz give me a keyword')

synonims = 'https://api.datamuse.com/words?rel_syn='+ keyword + '&max=4'
antonyms = 'https://api.datamuse.com/words?rel_ant='+ keyword + '&max=4'

option = st.selectbox('What would you like to know about this word?', ('synonims', 'antonyms')
st.write('You selected:', option):
