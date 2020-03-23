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

Python Docstrings:
1. https://www.geeksforgeeks.org/python-docstrings/
2. https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format


"""

# Imports
import argparse # TODO: use this
import logging

# Globals
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')

class Node:
    def __init__(self, name = None, parent = None):
        """
        Create a new Node

        Parameters:
            name (string):  the name of this node
            parent (Node):  the parent node of the node being created
        Returns:
            NA
        """

        self.name = name
        self.parent = parent
        if (parent is not None):
            self.parent.addChild(self)
        self.children = [] # initialize with an empty list of children

    def setParent(self, parent):
        """
        Set the parent of this node

        Parameters:
            parent (Node):  the parent node of the node being created
        Returns:
            None
        """

        self.parent = parent

    def addChild(self, child):
        """
        Add a child to this node's list of children

        Parameters:
            child (Node):  a child node to add to this node's list of children
        Returns:
            None
        """

        self.children.append(child)

    def printChildren(self):
        """
        Print the names of the children this node has

        Parameters:
            None
        Returns:
            None
        """

        logging.debug("Printing {}'s children:".format(self.name))
        if (self.children):
            for child in self.children:
                print(child.name)
        else:
            # no children
            print("NONE")

# end of class Node

class GitTree:

    def __init__(self):
        pass


    def printTree(self):
        pass

    def cascade(self):
        pass
# end of class GitTree

def main():
    logging.debug('Running main.')

    # See if I can duplicate this: https://anytree.readthedocs.io/en/latest/
    udo = Node("Udo")
    marc = Node("Marc", parent=udo)
    lian = Node("Lian", parent=marc)
    dan = Node("Dan", parent=udo)
    jet = Node("Jet", parent=dan)
    jan = Node("Jan", parent=dan)
    joe = Node("Joe", parent=dan)

    udo.printChildren()
    marc.printChildren()
    lian.printChildren()
    dan.printChildren()
    jet.printChildren()
    jan.printChildren()
    joe.printChildren()


# If this file is called directly, as opposed to imported, do this:
if __name__ == '__main__':
    main()
