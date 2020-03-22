#!/bin/bash

# This file is part of git-tree: https://github.com/ElectricRCAircraftGuy/git-tree
# Author: Gabriel Staples

# Installation:
# Add a symbolic link to this program in ~/bin
#       cd path/to/this/dir
#       mkdir -p ~/bin
#       ln -si "$PWD/git-tree.sh" ~/bin/git-tree

# Run the python program
THIS_PATH="$(realpath $0)"
# echo "THIS_PATH = \"$THIS_PATH\"" # for debugging
THIS_DIR="$(dirname "$THIS_PATH")"
# echo "THIS_DIR = \"$THIS_DIR\"" # for debugging 
python3 "$THIS_DIR/git-tree.py" "$@"
