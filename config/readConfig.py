import configparser
import os
import sys

'''
origin: config.read('config.ini', encoding='UTF-8')

I found that if I run this code, it will read file from oracle2mysql dir rather than config dir,
so I use abs path to read config.ini file.
'''
exepath = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(exepath, 'config.ini')
config = configparser.ConfigParser()
res = config.read(config_file, encoding='UTF-8')

class ReadConfig:
    def get_mysql(self, name):
        value = config.get('mysql', name)  # By using config.get to get name field in 'mysql' section in config.ini
        return value

    def get_oracle(self, name):
        value = config.get('oracle', name)  # By using config.get to get name field in 'oracle' section in config.ini
        return value
