#!/usr/bin/env python3

from csv import DictReader
from pathlib import Path

def parse_weather(file_: str):
    with open(file_, 'r') as f:
        reader = DictReader(f)
        for row in reader:
            print(row['SiteName'],row['Temperature'],row['Weather'])

if __name__ == '__main__':
    workdir = Path(__file__).parent
    parse_weather(workdir / 'weather.csv')
