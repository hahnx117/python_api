from pprint import pprint
import requests
from bs4 import BeautifulSoup
import json
import datetime


baseurl = "https://www.ncei.noaa.gov/cdo-web/api/v2"
url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast/hourly'

response=requests.get(url)
response.json()["properties"]["periods"][0]

