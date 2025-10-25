#!/usr/bin/env python3

from pathlib import Path
import shutil
from tempfile import TemporaryDirectory

def prepare_files(dir: str):
    '''
    Prepare some files and folders in the given directory.

    Args:
        dir (str): The directory where files and folders will be created.
    '''

    tempfolder = Path(dir)
    (tempfolder / 'file1.txt').touch()
    (tempfolder / 'folder2').mkdir()
    (tempfolder / 'folder2' / "file2.txt").touch()

def list_files(dir: str):
    '''
    List all files and folders in the given directory.

    Args:
        dir (str): The directory to list files and folders from.
    '''

    tempfolder = Path(dir)
    for path in tempfolder.rglob('*'):
        print(path)

def remove_files(dir: str):
    '''
    Remove all files and folders in the given directory.

    Args:
        dir (str): The directory to remove files and folders from.
    '''

    shutil.rmtree(dir)

if __name__ == '__main__':
    with TemporaryDirectory() as myfolder:
        print('temp folder is', myfolder)
        prepare_files(myfolder)
        list_files(myfolder)
        remove_files(myfolder)

    print('folder is removed after closed')