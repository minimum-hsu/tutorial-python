#!/usr/bin/env python3

from pathlib import Path
import yaml

def parser_yaml(file_: str) -> dict:
    with open(file_, 'r') as f:
        return yaml.safe_load(f)

if __name__ == '__main__':
    workdir = Path(__file__).parent
    data = parser_yaml(workdir / 'docker-compose.yml')
    print(data)
