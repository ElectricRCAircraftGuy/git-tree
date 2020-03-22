#!/usr/bin/env python3

"""
This file is part of git-tree: https://github.com/ElectricRCAircraftGuy/git-tree
Author: Gabriel Staples

REFERENCES:

Here's a few of my own Python code samples (previous projects) I am looking at to remind myself how to write
Python:
1. More C++-like (uses a class): https://github.com/ElectricRCAircraftGuy/LibreBulletin/blob/master/bulletin_find_and_replace.py
2. More C-like (does NOT use a class): https://github.com/ElectricRCAircraftGuy/eRCaGuy_PyTerm/blob/master/serial_terminal.py

Logging:
1. https://inventwithpython.com/blog/2012/04/06/stop-using-print-for-debugging-a-5-minute-quickstart-guide-to-pythons-logging-module/

"""

# Imports
import logging

# Globals
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')

class GitTree:

    def __init__(self):
        pass


    def tree(self):
        pass

    def cascade(self):
        pass

# end of class GitTree

def main():
    logging.debug('Running main.')


# If this file is called directly, as opposed to imported, do this:
if __name__ == '__main__':
    main()
