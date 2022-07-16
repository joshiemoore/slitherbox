"""
uname

Print system information to standard output.
"""

import platform
import argparse


def main(args):
    parser = argparse.ArgumentParser(description='Print system information to standard output.')
    parser.add_argument('-a', '--all', action='store_true', help='Print all information')
    parser.add_argument('-m', '--machine', action='store_true', help='Print the machine hardware name')
    parser.add_argument('-n', '--nodename', action='store_true', help='Print the network node hostname')
    parser.add_argument('-r', '--kernel-release', action='store_true', help='Print the kernel release')
    parser.add_argument('-s', '--kernel-name', action='store_true', help='Print the kernel name')
    parser.add_argument('-v', '--kernel-version', action='store_true', help='Print the kernel version')
    _args = parser.parse_args(args)

    uname = platform.uname()

    if _args.all:
        print(' '.join(uname))
        return 0

    result = []

    if _args.kernel_name or len(args) == 0:
        result.append(uname.system)
    if _args.nodename:
        result.append(uname.node)
    if _args.kernel_release:
        result.append(uname.release)
    if _args.kernel_version:
        result.append(uname.version)
    if _args.machine:
        result.append(uname.machine)

    if result:
        print(' '.join(result))

    return 0
