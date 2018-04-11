#!/usr/bin/env python3

import sys

assert sys.version_info >= (3, 5)

from pathlib import Path


myfile = Path('fruit.txt')
content = myfile.read_text()
print(content)
