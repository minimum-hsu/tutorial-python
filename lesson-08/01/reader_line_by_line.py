#!/usr/bin/env python3

from pathlib import Path

workdir = Path(__file__).parent

with open(workdir / 'fruit.txt', 'r') as myfile:
    while True:
        line = myfile.readline()
        if not line:
            break
        print(line, end='')
