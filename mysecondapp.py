import streamlit as st
keyword=st.text_input('plz give me a keyword')

synonims = 'https://api.datamuse.com/words?rel_syn='+ keyword + '&max=4'
antonyms = 'https://api.datamuse.com/words?rel_ant='+ keyword + '&max=4'

option = st.selectbox('What would you like to know about this word?', ('synonims', 'antonyms'))
st.write('You selected:', option)

response1 = requests.get(synonims)
response2 = requests.get(antonyms)
dataFromDatamuse1 = json.loads(response1.text)
dataFromDatamuse2 = json.loads(response2.text)

print("you give me the word", keyword, "the word its synonims are")
for eachentry in dataFromDatamuse2:
  print("--", eachentry['word'])
print("its antonyms are:")
for eachentry in dataFromDatamuse1:
  print("--", eachentry['word'])


#st.header("hello world")  
#st.text("from Brixen")

#st.write('The current movie title is', title)
