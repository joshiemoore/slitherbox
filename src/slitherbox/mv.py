"""
mv

Move or rename a file.
"""

import shutil
import argparse


def main(*args):
    parser = argparse.ArgumentParser(description='Move or rename a file.')
    parser.add_argument('source', type=str)
    parser.add_argument('destination', type=str)
    _args = parser.parse_args(args=args)

    shutil.move(_args.source, _args.destination)
    return 0
