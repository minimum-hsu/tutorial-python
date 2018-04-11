#!/usr/bin/env python3

from tempfile import mkstemp, mkdtemp
import os


def tempfile_demo():
    _, temp_path = mkstemp()
    print('temp file is', temp_path)

    with open(temp_path, 'w') as myfile:
        myfile.write('hello')

    os.remove(temp_path)


def tempfolder_demo():
    temp_path = mkdtemp()
    print('temp folder is', temp_path)

    os.rmdir(temp_path)


if __name__ == '__main__':
    tempfile_demo()
    tempfolder_demo()
