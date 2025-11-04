#!/usr/bin/env python3

'''
Usage:
    animal dog --name=<name> --kind=<kind>

options:
    -h, --help          Show this help message.
    --name=<name>       Name of the dog.
    --kind=<kind>       Kind/Breed of the dog.
'''

import rich_click as click
from animal.mammalia import Dog

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='Name of the dog.')
@click.option('--kind', required=True, help='Kind/Breed of the dog.')
def dog(name: str, kind: str):
    instance = Dog(name=name, kind=kind)
    instance.hello()
    instance.run()

if __name__ == '__main__':
    cli()
