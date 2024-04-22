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