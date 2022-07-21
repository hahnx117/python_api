from pprint import pprint
import requests
from bs4 import BeautifulSoup
import json
import datetime

## First, grab the object to get the hourly forecast URL from
# baseurl = https://api.weather.gov
# response = requests.get(f'{baseurl}/points/44.981944,-93.269167')

## Assign the returned value as the new URL
# url = response.json()['properties']['forecastHourly']
# response = requests.get(url)

baseurl = "https://www.ncei.noaa.gov/cdo-web/api/v2"
url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast/hourly'

response=requests.get(url)
#grabbing the temperature - nowstemp - and the temperature unit -tempunit- from noaa
#assigning nowstime as a datetime object
nowstemp = response.json()["properties"]["periods"][0]["temperature"]
nowstempunit = response.json()["properties"]["periods"][0]["temperatureUnit"]
nowstime=datetime.datetime.now().strftime("%I:%M %p, %B %d, %Y")

#print out "The temperature is: nowstemp nowstempunit - nowstime"
print ("The temperature is: " + str(nowstemp)+ " " + str(nowstempunit)+" - "+str(nowstime) )


