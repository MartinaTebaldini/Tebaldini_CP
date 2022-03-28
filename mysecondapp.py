import streamlit as st
keyword=st.text_input('plz give me a keyword')

synonims = 'https://api.datamuse.com/words?rel_syn='+ keyword + '&max=4'
antonyms = 'https://api.datamuse.com/words?rel_ant='+ keyword + '&max=4'

option = st.selectbox('What would you like to know about this word?', ('synonims', 'antonyms'))
st.write('You selected:', option)


#st.header("hello world")  
#st.text("from Brixen")

#st.write('The current movie title is', title)
