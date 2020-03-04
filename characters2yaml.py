# characters2yaml by Paradox
# Thanks to longbyte1/oldmud0 for inspiration and argoneus for suggestions.

"""

This script extracts character names from each character folder in the /base/characters directory of AO2 
and compiles it into a 'characters.yaml' file for quick tsuserver3 configuration.

To use it, simply place the script in the characters folder you wish to extract 
names from and run it, it will output a 'characters.yaml' file after finishing. 
If a 'characters.yaml' file already exists in the current directory the script 
will either add any new characters to the "Uncategorized" label at the bottom 
of the file, or create a 'characters-new.yaml' file.


This script requires the pyYAML module and Python 3.6 or higher.

"""
# MIT License
#
# Copyright (c) 2020 Paradox <https://github.com/Parazoid/>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os, sys, subprocess

cwd = os.getcwd() # Current working directory

# Installs pyYAML in case it's missing.
def check_depend():
    py_version = sys.version_info
    if py_version.major < 3 or (py_version.major == 3 and py_version.minor < 6):
        print("This script requires at least Python 3.6! Your version is: {}.{}"
            .format(py_version.major, py_version.minor))
        if input("Enter any key to exit: "):
            print("Quitting....")
            sys.exit(1)
    try:
        import yaml
    except ModuleNotFoundError:
        choice = input("Unable to find the required pyYAML module. Would you like to install it? (Y/N): ")
        while choice.upper() not in {"Y", "N"}:
            print("Invalid input. Please try again.")
            choice = input("Would you like to install pyYAML? (Y/N): ")
            if choice.upper() == "N":
                print("Quitting....")
                sys.exit(1)
            elif choice.upper() == "Y":
                print('Installing pyYAML for you...')
                try:
                    subprocess.check_call([
                        sys.executable, '-m', 'pip', 'install', '--user','pyYAML'])
                except subprocess.CalledProcessError:
                    print(
                        'Couldn\'t install it for you, because you don\'t have pip, '
                        'or another error occurred.'
                    )
                    if input("Enter any key to exit: ") or input("Enter any key to exit: ") == " ":
                        print("Quitting....")
                        sys.exit(1)
check_depend()
import yaml

files = os.listdir()
def yaml_parser(yamlhandle):
    data = yaml.load(yamlhandle, Loader=yaml.SafeLoader)
    print(data)
    for folder in files: #
        if os.path.isdir(folder): # Skips all non-folders.
            try: 
                inipath = os.path.join(cwd, folder, 'char.ini')
                if os.path.isfile(inipath): # Checking for valid ini files.
                    print("Adding " + folder)
                    data.append(folder)
                    continue
                else:
                    print("Warning! No valid 'char.ini' file found inside the " + folder + " directory. Skipping....")
                    continue
                
            except Exception as e: # Rare scenario, but just in case.
                print(e)
                print("Warning! The directory '" + folder + "' is no longer valid. Skipping....")
                continue 
        else:
            continue
    else:
        dump_yaml(data, yamlhandle)

def dump_yaml(chars, yamlhandle):
        print("Dumping....")
        yaml.safe_dump(chars, yamlhandle)
        print("Finished dumping the character names to the '" + os.path.basename(yamlhandle.name) + "' file.")
        if input("Enter any key to exit: "):
            print("Quitting....")
            sys.exit(1)


# Handling a bunch of cases before parsing.
def main():
    if "characters.yaml" in files:
        choice = input("Found a 'characters.yaml' file in current directory. Overwrite? (Y/N): ")
        while choice.upper() not in {"Y", "N"}:
            print("Invalid input. Please try again.")
            choice = input("Found a 'characters.yaml' file in current directory. "
            "Overwrite? (Y/N): ")
        if choice.upper() == "N":
            print("Quitting....")
            sys.exit(1)
        elif choice.upper() == "Y":
            print("Overwriting existing 'characters.yaml' file....")
            yamlhandle = open('characters.yaml', 'w+')
            yaml_parser(yamlhandle)
    else:
        print("Creating a 'characters.yaml' file....")
        yamlhandle = open('characters.yaml', 'w+')
        yaml_parser(yamlhandle)

# Forcing user input, just for the sake of people who don't know how to open the script in a command prompt.
print("Enter any key to start (or Q to exit).")
while True:
    cmd = input().upper()
    if cmd == "Q":
        print("Quitting....")
        sys.exit(1)
    elif os.path.basename(cwd) != "characters": # Checks that we're in /base/characters folder.
        print("Error: This script only works in the 'characters' folder.")
        print("Quitting....")
        sys.exit(1)
    else:
        main()
        