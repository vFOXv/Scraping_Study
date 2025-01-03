import yaml


class YamlWorked:

    def yaml_reader(self):
        with open("../config_ow/list_cities.yaml", 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data


    def yaml_writer(self, list_weather):
        # serialization
        with open("../config_ow/list_weather.yaml", 'w') as file:
            yaml.dump(list_weather, file)

