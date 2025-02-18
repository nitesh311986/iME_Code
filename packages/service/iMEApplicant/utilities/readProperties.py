import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join('.', 'Configurations', 'config.ini')
config.read(config_path)


class ReadConfig:
    @staticmethod
    def getURl():
        url = config.get('common data', 'base_url')
        return url
