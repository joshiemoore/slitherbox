"""
sb_install

Install snakebox by creating symbolic links to the
main snakebox script.
"""

import os


def main(args):
    SNAKEBOX_ROOT = args[0]
    utilities = args[1:]

    sb_main = SNAKEBOX_ROOT + '/snakebox'

    install_count = 0
    for util in utilities:
        symlink_path = SNAKEBOX_ROOT + '/' + util
        if not os.path.exists(symlink_path):
            print(f'Linking {util}...')
            os.symlink(sb_main, symlink_path)
            install_count += 1

    print(f'\nLinked {install_count} utilities')
    return 0
