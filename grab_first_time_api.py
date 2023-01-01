"""Converting grab_first_time.py to API end points with POST and GET methods."""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
from datetime import datetime

class DuskTime(Resource):
    """The dusk-time end point for the API."""

    def __init__(self):
        self.baseurl = 'http://api.sunrise-sunset.org/json'
        self.msp_weather_url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast/hourly'
        self.lat = 44.9778
        self.lon = -93.2650


    def get_info(self, requesteddate = None):
        """Return a dict with the info for the users query."""

        if not requesteddate:
            requesteddate = datetime.now().strftime('%Y-%m-%d')
        
        data = {'lat': self.lat,'lon': self.lon,'date': requesteddate}
        return_dict = {}

        # First get sunset time
        response = requests.get(self.baseurl, params = data)

        if response.json()['status'] != 'OK':
            raise ValueError("There was a problem with a value inputted. PLease try again.")

        # Append sunset time to the return dictionary
        return_dict['dusk_time'] = {requesteddate: response.json()['results']['sunset'], 'lat': self.lat, 'lon': self.lon}

        # Get weather locally in MSP
        response=requests.get(self.msp_weather_url)

        # Append weather data to return dict
        return_dict['temp'] = {'nowstemp':response.json()["properties"]["periods"][0]["temperature"], 'nowstempunit': response.json()["properties"]["periods"][0]["temperatureUnit"], 'nowstime': datetime.now().strftime("%I:%M %p, %B %d, %Y")}

        return return_dict


    def get(self):
        """Define the get method for the dusk-time endpoint."""

        data_dict = self.get_info()

        return {'data': data_dict}, 200


    def post(self):
        """Set the date to run the get against."""

        parser = reqparse.RequestParser()

        parser.add_argument('date', required=True)

        args = parser.parse_args()

        print(args['date'])

        data_dict = self.get_info(requesteddate = args['date'])

        return {'data': data_dict}, 200

    pass

app = Flask(__name__)
api = Api(app)

api.add_resource(DuskTime, '/dusk-time')

if __name__ == '__main__':
    app.run()  # run our Flask app
