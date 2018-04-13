#!/usr/bin/env python3

import yaml


def parser_yaml(file_: str) -> dict:
    with open(file_, 'r') as f:
        return yaml.load(f)


if __name__ == '__main__':
    data = parser_yaml('docker-compose.yml')
    print(data)
