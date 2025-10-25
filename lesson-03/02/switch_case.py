#!/usr/bin/env python3

from random import randint

def get():
    print('you get data from database')


def delete():
    print('you delete data in database')


def insert():
    print('you insert data to database')


action = {
    0: get,
    1: delete,
    2: insert
}


if __name__ == '__main__':
    index = randint(0, 2)  # simulate user choice
    action[index]()
