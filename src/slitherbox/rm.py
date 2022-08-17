"""
rm

Remove a file, or a directory with the -r flag.
"""

import os
import shutil
import argparse


def main(*args):
    parser = argparse.ArgumentParser(description='Remove a file or directory.')
    parser.add_argument('files', type=str, nargs='+')
    parser.add_argument('-r', action='store_true',
        help='Remove a directory recursively')
    _args = parser.parse_args(args=args)

    for file in _args.files:
        if os.path.isdir(file):
            if not _args.r:
                print(file + ' is a directory')
                return 1
            shutil.rmtree(file)
        else:
            os.remove(file)

    return 0
