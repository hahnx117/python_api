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
nowstime = response.json()["properties"]["periods"][0]["startTime"]

print (nowstime)

