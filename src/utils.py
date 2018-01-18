from os.path import dirname, realpath
from logging import warning
from json import load
from sys import exit

def load_config():
    try:
        path = "{0}/bot_config.json".format(dirname(realpath(__file__)))
		with open(path, 'r') as conf:
			return load(conf)
	except:
		warning('Configuration not found')
		exit()

def store_config():
    pass