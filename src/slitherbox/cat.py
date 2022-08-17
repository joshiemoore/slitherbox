"""
cat

Open a file and print its contents to standard output.
"""

import sys
import argparse


def main(*args):
    parser = argparse.ArgumentParser(description='Print the contents of a file to stdout.')
    parser.add_argument('file', type=str)
    _args = parser.parse_args(args=args)

    with open(_args.file, 'rb') as f:
        sys.stdout.buffer.write(f.read())

    return 0
