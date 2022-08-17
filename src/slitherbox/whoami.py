"""
whoami

Prints the current user's username to standard output.
"""

import os


def main(*args):
    if len(args) != 0:
        print('Usage: whoami')
        return 1

    print(os.getlogin())
    return 0
