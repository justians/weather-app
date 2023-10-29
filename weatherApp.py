import requests
import datetime
import geocoder
import time
from bs4 import BeautifulSoup
#url = 'https://www.youtube.com/watch?v=xjA1HjvmoMY'
#url = 'https://www.wunderground.com/weather/us/md/baltimore'



url = 'https://forecast.weather.gov/MapClick.php?lat=39.29&lon=-76.61'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser') 

tempature = soup.find('p', class_ = "myforecast-current-lrg").text


message = f"The current tempature in Baltimore Maryland is {tempature}!"


print(message)
