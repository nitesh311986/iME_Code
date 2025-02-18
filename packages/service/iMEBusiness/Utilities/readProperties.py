import configparser

config = configparser.RawConfigParser()
config.read('.\\Configuration\\Config.ini')


class ReadConfig:
    @staticmethod
    def getURl():
        url = config.get('common data', 'base_url')
        return url
