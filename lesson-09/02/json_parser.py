#!/usr/bin/env python3

from json import load
from pathlib import Path

workdir = Path(__file__).parent
with open(workdir / 'config.json', 'r') as myfile:
    config = load(myfile)
    print(config)

    for index, account in enumerate(config['account']):
        print('account', index)
        for key, value in account.items():
            print('{}: {}'.format(key, value))

# you can re-run to see the property of dict
