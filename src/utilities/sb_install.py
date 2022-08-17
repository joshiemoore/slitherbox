"""
sb_install

Install slitherbox by creating symbolic links to the
main slitherbox script.
"""

import os


def main(args):
    SLITHERBOX_ROOT = args[0]
    utilities = args[1:]

    sb_main = SLITHERBOX_ROOT + '/slitherbox'

    install_count = 0
    for util in utilities:
        symlink_path = SLITHERBOX_ROOT + '/' + util
        if not os.path.exists(symlink_path):
            print(f'Linking {util}...')
            os.symlink(sb_main, symlink_path)
            install_count += 1

    print(f'\nLinked {install_count} utilities')
    return 0
