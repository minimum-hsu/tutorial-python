#!/usr/bin/env python3

import argparse

def main():
    # Create a parser
    parser = argparse.ArgumentParser(
        description='A simple example to demonstrate how argparse works.'
    )

    # Add command-line arguments
    parser.add_argument('-f', '--file', type=str, help='Path to the input file.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output.')
    parser.add_argument('-n', '--number', type=int, default=1, help='A number to process (default: 1).')
    # Positional argument (required, no '-' or '--' prefix)
    parser.add_argument('output', type=str, help='Name of the output file.')

    # Parse the arguments
    args = parser.parse_args()

    # Use the parsed arguments
    if args.verbose:
        print('Verbose mode is ON.')
        print(f'Input file: {args.file}')
        print(f'Number: {args.number}')
        print(f'Output file: {args.output}')
    else:
        print(f'Processing {args.output}...')

if __name__ == '__main__':
    main()
