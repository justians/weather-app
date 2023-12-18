import requests
import json
import time
from bs4 import BeautifulSoup

weather_count = range(int(input("Number of locations you would like to find the weather for: ")))
locations = {}
for i in weather_count:
    locations["location{0}".format(i)] = input(f"Enter location #{i}: ")
    print(locations)

"""def location_finder(target_location):

    if(" " in target_location): #parsing/formatting the users input into a usable URL
        target_location = target_location.replace(" ", "+")
    global api_url
    api_url = f"https://geocode.maps.co/search?q={target_location}"

#location_finder(input("Hello, enter target location for current tempature to be displayed: "))

def api_pulling():
    api_request = requests.get(api_url)
    api_data = json.loads(api_request.text)
    latitude = api_data[0]['lat'] #sifting through GEOCODE JSON file to find necessary attributes of the dict
    longitude = api_data[0]["lon"]
    #location = api_data[0]["display_name"]
    #lat_and_lon = str(api_data[0]['lat']) + str(api_data[0]['lon'])
    #print(lat_and_lon, sep = ", ")
    url = f'https://forecast.weather.gov/MapClick.php?lat={latitude}&lon={longitude}'

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')#initial html parse

    tempature = soup.find('p', class_ = "myforecast-current-lrg").text #scrapes weather.gov's html for the current tempature
    #location = soup.find('h2', class_ = "panel-title").text
    print(tempature)

def main_loop():
    for i in weather_count:
        location_finder(input("Hello, enter target location for current tempature to be displayed: "))
        api_pulling()

main_loop()"""
