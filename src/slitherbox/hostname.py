"""
hostname

Print the name of the host to standard output.
"""

import platform


def main(*args):
    if len(args) != 0:
        print('Usage: hostname')
        return 1

    print(platform.node())
    return 0
