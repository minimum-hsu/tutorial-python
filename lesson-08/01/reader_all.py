#!/usr/bin/env python3

from pathlib import Path

workdir = Path(__file__).parent
file = workdir / 'fruit.txt'
content = file.read_text()
print(content)
