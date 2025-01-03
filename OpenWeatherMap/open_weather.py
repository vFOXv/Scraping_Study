
import requests
from OpenWeatherMap.yaml_worked import YamlWorked

# обращаться к переменным из папок на одном уровне(из config_ow)
import sys
sys.path.append("..")
#from config_ow.global_config import API_KEY
# если импорт всего -> from config_ow.global_config import *
# если импорт всего -> import config_ow.global_config as gc (обращение к переменной gc.API_KEY)
import config_ow.global_config as gc

class OpenWeather:

    cities = None
    limit: int
    list_coordinates = None

    def __init__(self):
        self.yw = YamlWorked()
        self.cities = self.yw.yaml_reader()
        self.limit = gc.LIMIT
        self.list_coordinates = []

    # Geocoding API
    def geocoding(self):
        for this_city in self.cities:
            params = {'q':this_city, 'limit':self.limit, 'appid':gc.API_KEY}
            #http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
            response = requests.get(gc.G_URL, params=params)
            result = response.json()

            for item in result:
                coordinates = {}
                coordinates['lat'] = item.get("lat")
                coordinates['lon'] = item.get("lon")
                self.list_coordinates.append(coordinates)

    # Current weather data
    def current_weather(self):
        list_weather = []

        for item in self.list_coordinates:
            weather = {}
            lat = item.get('lat')
            lon = item.get('lon')
            params = {'lat': lat, 'lon': lon, 'units': 'metric', 'appid': gc.API_KEY}
            #c_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={str(gc.API_KEY)}'
            response = requests.get(gc.C_URL, params=params)
            result = response.json()
            weather['city'] = result.get('name')
            weather['country'] = result.get('sys').get('country')
            weather['temp'] = int(result.get('main').get('temp'))
            weather['main'] = result.get('weather')[0].get('main')
            weather['wind'] = result.get('wind').get('speed')
            list_weather.append(weather)
        self.yw.yaml_writer(list_weather)
        for city in list_weather:
            print(city)



