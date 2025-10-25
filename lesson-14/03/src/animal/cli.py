#!/usr/bin/env python3

'''
Usage:
    animal dog --name=<name> --kind=<kind>

options:
    -h, --help          Show this help message.
    --name=<name>       Name of the dog.
    --kind=<kind>       Kind/Breed of the dog.
'''

from docopt import docopt
from animal.mammalia import Dog

def main():
    args = docopt(__doc__, version='0.1.0')

    # Use the parsed arguments
    if args['dog']:
        dog = Dog(name=args['--name'], kind=args['--kind'])
        dog.hello()
        dog.run()
