#!/usr/bin/env python3

from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

for section in config.sections():
    for key in config[section]:
        print('section: {}, key: {}, value: {}'.format(section, key, config[section][key]))
