"""
sb_uninstall

Uninstall snakebox by removing utility symlinks.
"""

import os


def main(args):
    SNAKEBOX_ROOT = args[0]
    utilities = args[1:]

    uninstall_count = 0
    for util in utilities:
        symlink_path = SNAKEBOX_ROOT + '/' + util
        if os.path.exists(symlink_path):
            print(f'Unlinking {util}...')
            os.unlink(symlink_path)
            uninstall_count += 1

    print(f'\nUnlinked {uninstall_count} utilities')
