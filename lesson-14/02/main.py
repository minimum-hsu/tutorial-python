#!/usr/bin/env python3

'''
Usage:
    main.py [--file=<file>] [-v] [--number=<number>] <output>

A simple example to demonstrate how argparse works.

positional arguments:
    <output>                Name of the output file.

options:
    -h, --help              Show this help message.
    -f, --file=<file>       Path to the input file.
    -v, --verbose           Enable verbose output.
    -n, --number=<number>   A number to process [default: 1].
'''

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.0')

    # Use the parsed arguments
    if args['--verbose']:
        print('Verbose mode is ON.')
        print(f'Input file: {args["--file"]}')
        print(f'Number: {args["--number"]}')
        print(f'Output file: {args["<output>"]}')
    else:
        print(f'Processing {args["<output>"]}...')
