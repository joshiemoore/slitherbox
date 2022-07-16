"""
which

Search the user's environment for specified executables.
"""

import shutil
import argparse


def main(args):
    parser = argparse.ArgumentParser(description='Search the user\'s environment for specified executables.')
    parser.add_argument('args', type=str, nargs='+', help='Executable(s) to search for')
    _args = parser.parse_args(args=args)

    for arg in _args.args:
        path = shutil.which(arg)
        if path:
            print(path)

    return 0
