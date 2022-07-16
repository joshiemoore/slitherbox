"""
rm

Remove a file, or a directory with the -r flag.
"""

import os
import shutil
import argparse


def main(args):
    parser = argparse.ArgumentParser(description='Remove a file or directory.')
    parser.add_argument('file', type=str)
    parser.add_argument('-r', action='store_true',
        help='Remove a directory recursively')
    _args = parser.parse_args(args=args)

    if os.path.isdir(_args.file):
        if not _args.r:
            print(_args.file + ' is a directory')
            return 1
        shutil.rmtree(_args.file)
    else:
        os.remove(_args.file)

    return 0
