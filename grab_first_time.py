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

#assign sunset datetime object
#loop until user inputs 'exit' command
requesteddate = input('Please enter the date you would like to retrieve temperatures for (YYYY-MM-DD), or type "exit" to leave: ')
while requesteddate != "exit":
    
    baseurl2 = 'http://api.sunrise-sunset.org/json'
    data = {'lat':44.9778,'lng':'-93.2650','date':requesteddate}
    response2=requests.get(baseurl2,params=data)
    mspdusk = response2.json()['results']['sunset']
    mspduskdate = datetime.datetime.strptime(f'{requesteddate} {mspdusk}',"%Y-%m-%d %H:%M:%S %p") - datetime.timedelta(hours=5) + datetime.timedelta(days=1)

    #assign temperature object
    baseurl = "https://www.ncei.noaa.gov/cdo-web/api/v2"
    url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast/hourly'


    response=requests.get(url)

    #grabbing the temperature - nowstemp - and the temperature unit -tempunit- from noaa
    #assigning nowstime as a datetime object
    nowstemp = response.json()["properties"]["periods"][0]["temperature"]
    nowstempunit = response.json()["properties"]["periods"][0]["temperatureUnit"]
    nowstime=datetime.datetime.now().strftime("%I:%M %p, %B %d, %Y")
    #nowsdusk=response2.json()["results"]["sunset"]

    #print out "The temperature is: nowstemp nowstempunit - nowstime"
    print(f'The dusk time on {requesteddate} is {mspduskdate}')
    print ("The temperature is: " + str(nowstemp)+ " " + str(nowstempunit)+" - "+str(nowstime) )
    #print ("Dusk today is at "+nowsdusk)
    requesteddate = input('Please enter the date you would like to retrieve temperatures for (YYYY-MM-DD), or type "exit" to leave: ')

