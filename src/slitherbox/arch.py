"""
arch

Print the hardware architecture to standard output.
"""

import platform


def main(*args):
    if len(args) != 0:
        print('Usage: arch')
        return 1

    print(platform.machine())
    return 0
