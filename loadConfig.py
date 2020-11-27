import configparser
config = configparser.ConfigParser()
config.read('D:\\Projects\\BadWeatherBot\\badWeatherBot\\config.ini')

tg_bot_token = config['Telegram Bot']['tg_bot_token']
db_path = config['Database']['db_path']
db_type = config['Database']['db_type']