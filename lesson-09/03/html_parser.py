#!/usr/bin/env python3

from html.parser import HTMLParser


with open('config.json', 'r') as myfile:
    config = load(myfile)
    print(config)

    for index, account in enumerate(config['account']):
        print('account', index) 
        for key, value in account.items():
            print('{}: {}'.format(key, value))

## you can re-run to see the property of dict
