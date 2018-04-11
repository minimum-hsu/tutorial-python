#!/usr/bin/env python3

with open('fruit.txt', 'r') as myfile:
    while True:
        line = myfile.readline()
        if not line:
            break
        print(line, end = '')
