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

# add your own APIkey
APIkey = '629e7883de074fc948b601e927640e29'
location = 'london'

# check API documentation to see what structure of URL is needed to access the data
# http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey
# print(url)


# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
# print(response.text)  


# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
# print(weatherData) 
# from pprint import pprint 
# pprint(weatherData) 

print(weatherData['main']['temp_max']) 
# more???????????'
