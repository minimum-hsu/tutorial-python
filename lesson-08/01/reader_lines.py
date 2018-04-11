#!/usr/bin/env python3

with open('fruit.txt', 'r') as myfile:
    lines = myfile.readlines()
    for line in lines:
        print(line, end = '')
