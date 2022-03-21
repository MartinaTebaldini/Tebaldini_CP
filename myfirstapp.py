import streamlit as st
st.header("hello world")  
st.text("from Brixen")
title = st.text_input('Gimme a movie title', 'enter a movie title here',  max_chars= 10)
st.write('The current movie title is', title)

genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'), help = "clik one of the three options")
if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")
     
import json, requests 

APIkey = '629e7883de074fc948b601e927640e29'
location = 'london'

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'


response = requests.get(url)   

weatherData = json.loads(response.text)

st.header(weatherData['main']['temp_max']) 

