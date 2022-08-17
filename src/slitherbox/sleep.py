"""
sleep

Delay execution by a specified number of seconds.
"""

import time
import argparse


def main(*args):
    parser = argparse.ArgumentParser(description='Delay execution by a specified number of seconds.')
    parser.add_argument('delay', type=float)
    _args = parser.parse_args(args=args)

    time.sleep(_args.delay)
    return 0
