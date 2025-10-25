#!/usr/bin/env python3

from configparser import ConfigParser
from pathlib import Path

workdir = Path(__file__).parent
config = ConfigParser()
config.read(workdir / 'config.ini')

for section in config.sections():
    for key in config[section]:
        print('section: {}, key: {}, value: {}'.format(section, key, config[section][key]))
