from configparser import ConfigParser
import configparser
def read_configuration(category,key):
    global basic_info
    config = configparser.ConfigParser()
    try:
        config.read("config.ini")
        basic_info = config['basic info']
    except KeyError:
        print("the basic info' section does not exists in the configuration file")
