"""
sb_uninstall

Uninstall slitherbox by removing utility symlinks.
"""

import os


def main(*args):
    SLITHERBOX_ROOT = args[0]
    utilities = args[1:]

    uninstall_count = 0
    for util in utilities:
        symlink_path = SLITHERBOX_ROOT + '/' + util
        if os.path.exists(symlink_path):
            print(f'Unlinking {util}...')
            os.unlink(symlink_path)
            uninstall_count += 1

    print(f'\nUnlinked {uninstall_count} utilities from {SLITHERBOX_ROOT}')
    return 0
