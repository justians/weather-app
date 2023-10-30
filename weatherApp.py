import requests
import json
import time
from bs4 import BeautifulSoup

target_location = input("Hello, enter target location for current tempature to be displayed: ")

if(" " in target_location): #parsing/formatting the users input into a usable URL
    target_location = target_location.replace(" ", "+")

api_url = f"https://geocode.maps.co/search?q={target_location}"

api_request = requests.get(api_url)
api_data = json.loads(api_request.text)
latitude = api_data[0]['lat'] #sifting through GEOCODE JSON file to find necessary attributes of the dict
longitude = api_data[0]["lon"]
location = api_data[0]["display_name"]
#lat_and_lon = str(api_data[0]['lat']) + str(api_data[0]['lon'])
#print(lat_and_lon, sep = ", ")


url = f'https://forecast.weather.gov/MapClick.php?lat={latitude}&lon={longitude}'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')#initial html parse

tempature = soup.find('p', class_ = "myforecast-current-lrg").text #scrapes weather.gov's html for the current tempature
#location = soup.find('h2', class_ = "panel-title").text

message = f"The current tempature in {location} is {tempature}!"


print(message)
