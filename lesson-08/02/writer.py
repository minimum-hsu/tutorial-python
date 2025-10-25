#!/usr/bin/env python3

names = ['Alice', 'Bob', 'Charlie']

with open('/tmp/names.txt', 'w') as myfile:
    for user in names:
        myfile.write(user + '\n')
