"""
mkdir

Create a directory.
"""

import os
import argparse


def main(*args):
    parser = argparse.ArgumentParser(description='Create a directory.')
    parser.add_argument('dir', type=str)
    _args = parser.parse_args(args=args)

    os.mkdir(_args.dir)
    return 0
