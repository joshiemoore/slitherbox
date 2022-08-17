"""
sb_list

List available slitherbox utilities.
"""

def main(*args):
    args.sort()
    for util in args:
        print(util)

    return 0
