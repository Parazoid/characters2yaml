# **CHARACTERS2YAML**
### This is a script that turns AO2 character folders into usable YAML files.
***The backgrounds version of this script can be found [here](https://github.com/Parazoid/characters2yaml/tree/bgs2yaml).***

It works by extracting character names from each character folder in the /base/characters directory of [Attorney Online 2](https://aceattorneyonline.com)
and compiles it into a 'characters.yaml' file for quick [tsuserver3](https://github.com/AttorneyOnline/tsuserver3) configuration.
It is the characters.yaml equivalent of the [music2yaml](https://gist.github.com/oldmud0/4af137512e6419a161218f705ceee16f) script made by oldmud1 a while ago. 

To use it, simply place the script in the characters folder you wish to extract 
names from and run it, it will output a 'characters.yaml' file after finishing. 
If a 'characters.yaml' file already exists in the current directory the script 
will ask if you wish to overwrite.
***(Overwriting will erase everything in your YAML file.)***


**This script requires the pyYAML module and Python 3.6 or higher. (Automatic pyYAML installation is an option.)**


#### TODO:
- Add a way to insert new characters into an existing YAML file non-disruptingly.
- Add a way to preserve YAML comments.

If I screwed anything up or if you found a typo somewhere, feel free to contact me!
Discord Contact: __Paradox#1001__

## LICENSE
Copyright **(c)** 2020 Paradox

This script is licensed under the MIT license. In short you're free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of it as long as it includes this copyright notice.
For the full license terms check the [LICENSE](https://github.com/Parazoid/characters2yaml/blob/master/LICENSE.txt) file.

Special thanks to anyone who helped me cobble this thing up.
