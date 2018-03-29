#!/usr/bin/env python3

import sys

assert sys.version_info >= (3, 5)

from tempfile import TemporaryFile, TemporaryDirectory


def tempfile_demo():
    myfile = TemporaryFile(mode = 'w+')
    print('hello', file = myfile)
    myfile.seek(0)
    print(myfile.readline(), end = '')
    myfile.close()
    print('file is removed after closed')


def tempfolder_demo():
    with TemporaryDirectory() as myfolder:
        print('temp folder is', myfolder)
    print('folder is removed after closed')


if __name__ == '__main__':
    tempfile_demo()
    tempfolder_demo()
