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
#---------------------------------------------
import json, requests 
#from pprint import pprint

APIkey = '629e7883de074fc948b601e927640e29'
#location = st.text_input("give me a city name ")
location = st.text_input("give me a city name between milan, bolzano and palermo")

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'

# Download the JSON data from OpenWeatherMap.org's API.
response = requests.get(url)  
# Uncomment to see the raw JSON text:
#print(response.text)  


#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Uncomment to see the raw JSON text:
#st.text(str(weatherData))

#pprint(weatherData)

#-----------------------

weather = st.radio("Choose one of the following citys",('Milan', 'Bolzano', 'Palermo'), help = "clik one of the three options")
if weather == 'Milan':
     st.text(str(weatherData))
elif weather == 'Bolzano':
     st.write(weatherData)
else:
     st.write(weatherData)
