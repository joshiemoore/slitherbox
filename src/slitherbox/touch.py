"""
touch

Create a file, or update an existing file's accessed and modified timestamps.
"""

import os
import argparse


def main(*args):
    parser = argparse.ArgumentParser(description='Create a file, or update a file\'s timestamps.')
    parser.add_argument('file', type=str)
    _args = parser.parse_args(args=args)

    try:
        os.utime(_args.file, None)
    except OSError:
        open(_args.file, 'a').close()

    return 0
