#!/usr/bin/env python3

from pathlib import Path
import tomllib

def parser_toml(file_: str) -> dict:
    with open(file_, 'rb') as f:
        return tomllib.load(f)

if __name__ == '__main__':
    workdir = Path(__file__).parent
    data = parser_toml(workdir / 'pyproject.toml')
    print(data)
