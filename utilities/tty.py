"""
tty

Print the current tty device to standard output.
"""

import os
import sys


def main(args):
    if len(args) != 0:
        print('Usage: tty')
            return 1

    print(os.ttyname(sys.__stdout__.fileno()))
    return 0
