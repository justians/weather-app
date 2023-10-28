import requests
from bs4 import BeautifulSoup
#url = 'https://www.youtube.com/watch?v=xjA1HjvmoMY'
#url = 'https://www.wunderground.com/weather/us/md/baltimore'
url = 'https://forecast.weather.gov/MapClick.php?lat=39.290580000000034&lon=-76.60925999999995'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser') 

tempature = soup.find('p', class_ = "myforecast-current-lrg").text

message = f"The current tempature in Baltimore Maryland is {tempature}!"

print(message)
