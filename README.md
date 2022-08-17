# slitherbox
slitherbox is a drop-in Python replacement for common shell utilities, as an incremental addition to the
[Snakeware Project](https://github.com/joshiemoore/snakeware). The goal is to implement a useful 
set of utilities with no runtime dependencies beyond a standard Python 3 installation, in furtherance
of the pursuit of Python-based computing environments.

In addition to a re-implementation of common shell utilities, slitherbox is also a platform for easily implementing
your own custom shell commands in Python. See the `Utilities` section for more information.

slitherbox is primarily intended for use with [xonsh](https://xon.sh/), though the installed commands
will work with any shell.

slitherbox is free software licensed under the terms of GPLv3 or later.

## Installation from PyPI
Installation and uninstallation of slitherbox is simple, and will not overwrite any existing utilities on your system.
slitherbox uses the same trick as BusyBox, in that symbolic links representing different commands are made to
the main slitherbox script. The main script is aware of what name it was run with and executes the corresponding utility.

You only need Python 3 and pip to install slitherbox.

1. Run `python3 -m pip install slitherbox`.

2. Open a Python interpreter and run the following:
   ```
   >>> from slitherbox.slitherbox import sb_main
   >>> sb_main('sb_install')
   ```

   This will create symlinks in the installation directory.

3. Add the installation directory to the *beginning* of your `$PATH` so your shell finds slitherbox
   commands before it finds your native system commands. For example, you could do this by adding
   `$PATH = ['/path/to/slitherbox'] + $PATH` to your `.xonshrc` if you use xonsh.

   The installation directory is displayed at the end of the `sb_install` command you ran in step 2.

   **NOTE:** You may need to also run `chmod +x slitherbox.py` inside the install directory to make
   the main script executable, or the commands won't work properly in your shell. 

4. Verify the installation was successful by running `$ which echo` and observing that the resulting
   path is inside the installation directory.

5. You can now run all slitherbox utilities from your shell. If you run a command that is not
   implemented in slitherbox, but does exist elsewhere in your path, then the existing native
   utility will still be run.

The slitherbox symlinks can be removed by running `$ sb_uninstall`, restoring use of your native utilities.
To re-enable slitherbox, do step 2 again.

You can view a list of available commands by running `$ sb_list`.

slitherbox commands can also be run without installing the symlinks by running the slitherbox script
directly: `$ ./slitherbox.py <command> [args...]`.

### Security Note
Of course, it would be trivial for a user on your system to modify slitherbox utility scripts to
cause the commands to act maliciously against other users that run them. If this is a concern for you,
it is recommended to permission the slitherbox installation directory such that users have read and
execute access, but no write access.

## Utilities

All slitherbox commands are implemented in the `src/slitherbox/` directory. See these files for examples of how
slitherbox commands work.

In the future, we may add more directories to host non-core contrib/miscellaneous/fun commands to keep
them separate from the core utilities and allow them to be optionally installed.

### Creating new commands
Adding commands to slitherbox is very simple, even for Python beginners. Many core utilities are just
wrappers for one line calls to the Python standard library.

To create a new command, first create a Python file in the `src/utilities/` directory corresponding to your
command's name. For example, if you want to run your command as `$ mycoolcmd`, name the file `mycoolcmd.py`.

The basic structure of a slitherbox utility is as follows:

```
def main(*args):
    # DO STUFF
    return 0
```

Replace `# DO STUFF` with the functionality that you want your command to implement.
`args` is the list of arguments that were passed to your command from the shell.

Your main function must be named `main`. Your main function must return an integer status
code, where 0 is success and non-zero is failure. If an integer status code is not returned
from your main function, an exception will be raised.

Once you have created your command, run `$ sb_install` to install a symlink for it. You will then be able to run
your command from your shell. You don't need to re-create the symlink every time you make changes,
any subsequent changes you make will automatically work the next time your command is run.

## Contributing/TODOs
If you would like to contribute to slitherbox, be sure to uninstall the symlinks before you do a git commit,
or otherwise avoid adding the symlinks to your commits.

slitherbox is early in development, so there is still much to do. Below is a list of some todos/plans.

* Implement more commands, to at least approximate a useful replacement for the GNU Core Utilities.
* Add more features to existing commands, including various flags and options which would be expected
  to exist in established implementations of that command.
* Add more comprehensive exception handling to command implementations. Incorrect inputs or other
  issues will often cause the Python library functions to throw exceptions, and we should display
  graceful error messages instead of showing the actual exception to the user running the command.
* ... 
