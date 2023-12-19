import requests
import json
from bs4 import BeautifulSoup

location_count = int(input("Enter the amount of locations you want to find: "))
locations = []

gooyat = [locations.append(input(f"enter location #{i + 1}: ")) for i in range(location_count)]
weather = [None for _ in range(location_count)]
pairs = { k:v for (k,v) in zip(locations, weather)}  
 
def main():
    for place in pairs:
        assign_temp(place)

def assign_temp(place):
    if(" " in place): #parsing/formatting the users input into a usable URL
        place = place.replace(" ", "+")
    api_url = f"https://geocode.maps.co/search?q={place}"

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

    temperature = soup.find('p', class_ = "myforecast-current-lrg").text #scrapes weather.gov's html for the current tempature
    #location = soup.find('h2', class_ = "panel-title").text
    print(temperature)

main()
