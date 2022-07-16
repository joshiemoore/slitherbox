"""
sb_list

List available snakebox utilities.
"""

def main(args):
    args.sort()
    for util in args:
        print(util)
