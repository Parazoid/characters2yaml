# characters2yaml by Paradox
# Special thanks to longbyte1/oldmud0 for some code snippets and inspiration.
"""

This script extracts character names from each character folder in the /base/characters directory of AO2 
and compiles it into a 'characters.yaml' file for quick tsuserver3 configuration.

To use it, simply place the script in the characters folder you wish to extract 
names from and run it, it will output a 'characters.yaml' file after finishing. 
If a 'characters.yaml' yaml file already exists in the current directory the script 
will add any new characters to the "Uncategorized" category at the bottom of the file.

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

import os, sys, subprocess, yaml
from msvcrt import getwch

cwd = os.getcwd() # Current working directory

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
check_depend()

files = os.listdir()
def dump_characters(charyaml):
    for folder in files:
        if os.path.isdir(folder):
            try: 
                os.chdir(folder)
                try: # Check if folder has a ini, dump the folder's name to the yaml if yes.
                    open('char.ini', 'r')
                    print("Adding " + folder)
                    # TODO: Add yaml dumping code here
                    os.chdir('..')
                    continue
                except Exception as e:
                    print(e)
                    print("Warning! The folder '" + folder + "' does not contain a valid 'char.ini'. Skipping...")
                    os.chdir('..')
                    continue
            except:
                print("Warning! The directory '" + folder + "' is no longer valid.")
                continue # Just in case the directory list changes and something goes wrong.
        else:
            continue
    else:
        print("Done dumping the character names to '" + os.path.basename(charyaml.name) + "'.")
        print("Press any key to exit.")
        if getwch():
            print("Exiting....")
            sys.exit(1)

# Handling a bunch of cases before dumping.
def main():
    if "characters.yaml" in files:
        choice = input("Found a 'characters.yaml' file in current directory. Add new characters? (Y/N/Q): ")
        while choice.upper() not in {"Y", "N", "Q"}:
            print("Invalid input. Please try again.")
            choice = input("Found a 'characters.yaml' file in current directory. "
            "Add new characters? (Y/N/Q): ")
        if choice.upper() == "Q":
            print("Exiting....")
            sys.exit(1)
        elif choice.upper() == "Y":
            print("Adding new characters to 'Uncategorized'...")
            charyaml = open('characters.yaml', 'r+')
            dump_characters(charyaml)
        elif choice.upper() == "N":
            print("Creating seperate 'characters.yaml' as 'characters-new.yaml'")
            newyaml = open('characters-new.yaml', 'w+')
            dump_characters(newyaml)
    else:
        print("No 'characters.yaml' found, creating a new one...")
        newyaml = open('characters.yaml', 'w+')
        dump_characters(newyaml)

# Forcing user input, just for the sake of people who don't know how to open the script in a command prompt.
print("Press any key to start (or Q to exit).")
while True:
    cmd = getwch() # Instantly passes the user's input without needing to press enter.
    if cmd.upper() == "Q":
        print("Exiting....")
        sys.exit(1)
    elif os.path.basename(cwd) != "characters": # Checks that we're in /base/characters folder.
        print("Error: This script only works in the 'characters' folder.")
        print("Exiting....")
        sys.exit(1)
    else:
        main()
        