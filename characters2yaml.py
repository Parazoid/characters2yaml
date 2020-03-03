# characters2yaml by Paradox
"""

This script extracts character names from each character folder in the /base/characters directory of AO2 
and compiles it into a 'characters.yaml' file for quick tsuserver3 configuration.

To use it, simply place the script in the characters folder you wish to extract 
names from and run it, it will output a 'characters.yaml' file after finishing. 
If a 'characters.yaml' yaml file already exists in the current directory the script 
will add any new characters to the "Uncategorized" category at the bottom of file.

This requires the pyYAML module and Python 3.6 or higher.

"""

# ISC License
#
# Copyright (c) 2020 Paradox <https://github.com/Parazoid>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import os, sys, subprocess

# Installs pyYAML in case it's missing.
def check_depend():
    py_version = sys.version_info
    if py_version.major < 3 or (py_version.major == 3 and py_version.minor < 6):
        print("This script requires at least Python 3.6! Your version is: {}.{}"
            .format(py_version.major, py_version.minor))
        sys.exit(1)

    try:
        import yaml
    except ModuleNotFoundError:
        print('Installing pyYAML for you...')
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '--user','pyYAML'])
        except subprocess.CalledProcessError:
            print(
                'Couldn\'t install it for you, because you don\'t have pip, '
                'or another error occurred.'
            )

def main():
    check_depend()
    return

main()
