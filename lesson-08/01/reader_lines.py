#!/usr/bin/env python3

from pathlib import Path

workdir = Path(__file__).parent

with open(workdir / 'fruit.txt', 'r') as myfile:
    lines = myfile.readlines()
    for line in lines:
        print(line, end='')
