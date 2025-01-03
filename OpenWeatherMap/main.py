from open_weather import OpenWeather

class Main:

    def __init__(self):
        self.ow = OpenWeather()

    def main_function(self):
        self.ow.geocoding()
        self.ow.current_weather()

main = Main()
main.main_function()

