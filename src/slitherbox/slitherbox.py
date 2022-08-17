#!/usr/bin/env python3

import os
import sys
import importlib.util

SLITHERBOX_ROOT = os.path.dirname(os.path.realpath(__file__))


__header__ = f"""
slitherbox - Drop-in Python replacement for common shell utilities
Usage: slitherbox <command> [args...]

To install slitherbox, run:

  $ ./slitherbox sb_install

Then add '{SLITHERBOX_ROOT}' to the beginning of your path
to run slitherbox commands directly from your shell.
"""

__copyright__ = """
Copyright (c) 2022, Joshua Moore

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


def run_utility(utility_name, *args):
    # load utility module
    utility_spec = importlib.util.spec_from_file_location(
        f'{utility_name}',
        f'{SLITHERBOX_ROOT}/{utility_name}.py'
    )
    utility = importlib.util.module_from_spec(utility_spec)

    try:
        utility_spec.loader.exec_module(utility)
    except FileNotFoundError:
        print(f'No such slitherbox utility: {utility_spec}')
        return 1
    
    # run utility
    return utility.main(*args)


def list_utilities():
    result = []
    for util in os.listdir(SLITHERBOX_ROOT):
        if '.py' not in util:
            continue
        result.append(util.replace('.py', ''))
    return result


def sb_main(*args):
    # clean up invoked name
    invoked_name = args[0].replace('./', '')
    invoked_name = os.path.basename(
        os.path.normpath(invoked_name)
    )

    if 'slitherbox' in invoked_name:
        if len(args) < 2:
            print(__header__)
            print(__copyright__)
            exit()
        invoked_name = args[1]
        _args = args[2:]
    else:
        _args = args[1:]

    # handle special slitherbox-internal commands
    if invoked_name == 'sb_install':
        _args = [SLITHERBOX_ROOT] + list_utilities()
    elif invoked_name == 'sb_uninstall':
        _args = [SLITHERBOX_ROOT] + list_utilities()
    elif invoked_name == 'sb_list':
        _args = list_utilities()

    status_code = run_utility(invoked_name, *_args)

    # exit with status code returned by utility
    if status_code is None or not isinstance(status_code, int):
        raise ValueError(
            'slitherbox utilities must return an integer status code, '\
            f'but {invoked_name} returned: {status_code}'
        )

    return status_code


if __name__ == '__main__':
    status_code = sb_main(*sys.argv)
    exit(status_code)
