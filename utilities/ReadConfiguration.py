import configparser
from configparser import ConfigParser
# def read_configuration(category,key):
#     config = configparser.ConfigParser()
#     config.read("ConfigFiles/config.ini")
#     return config.get('basic info', 'some_key')
    # config = ConfigParser()
    # config.read("ConfigFiles/config.ini")
    # return config.get(category,key)

    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # # if 'basic info' in config:
    # #     value1 = config['basic info'].get('browser')
    # #     value2 = config['basic info'].get('url')
    # #     print("Value 1:", value1)
    # #     print("Value 2:", value2)
    # # else:
    # #     print("The 'basic info' section ")


import configparser
from configparser import ConfigParser, NoSectionError

def read_configuration(category, key):
    config = ConfigParser()
    try:
        config = configparser.ConfigParser()
        config.read("config.ini")
        return config.get(category, key)
    except NoSectionError:
        return None