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
   - Log levels: debug, info, warning, error, critical

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
    def __init__(self, name, parent = None):
        """
        Constructor to create a new Node

        Parameters:
            name (string):  the name of this node
            parent (Node):  the parent node of the node being created
        Returns:
            NA
        """

        self.name = name
        self.parent = parent
        if (parent is not None):
            self.parent.__addChild(self)
        self.children = [] # initialize with an empty list of children

    def setParent(self, parent):
        """
        Set the parent of this node. 

        Details: Use this in case you need to change the parent, as the original parent should always be 
        set when you construct the Node.#############

        Parameters:
            parent (Node):  the parent node of the node being created
        Returns:
            None
        """

        self.parent = parent

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

    def __addChild(self, child):
        """
        Add a child to this node's list of children. 

        Details: This is a private method because the children should never be added externally. Rather, they
        are only added internally to a parent when a parent is set.

        Parameters:
            child (Node):  a child node to add to this node's list of children
        Returns:
            None
        """

        self.children.append(child)
# end of class Node

class Tree:

    def __init__(self):
        """
        Constructor

        Parameters:
            None
        Returns:
            NA
        """
        # List of all nodes
        self.nodes = []
        # A dictionary to map from a node name to a node
        self.nodeMap = {}

    def addNode(name, parentName = None):
        """
        Create a new node and add it to the tree; note that a parent MUST be created before a child or else 
        an error will occur

        Parameters:
            name (string):        the name of this node; must be a unique name from all other nodes!
            parentName (string):  the *name* of the parent node for the node being created; this node must 
                                  already exist in the tree! In other words, add all parent nodes FIRST, and
                                  *then* their children! ########### NEED TO COME BACK TO THIS--MAY NOT WORK FOR MY
                                  INTENDED git-tree USAGE!
        Returns:
            NA
        """
        
        # Obtain the parent node using the parent node name if the parent node exists
        parentNode = None
        if (parentName is not None):
            if (not parentName in self.nodeMap):
                logging.error('Error: parent node must be created first!')
                return
            else:
                parentNode = self.nodeMap[parentName]
        newNode = Node(name, parentNode)
        self.nodes.append(newNode)

    def printTree(self):
        pass

    def cascade(self):
        pass
# end of class GitTree

def tests():
    """
    Run some tests to ensure my classes (Node, Tree, etc) are working
    """
    
    # See if I can duplicate this: https://anytree.readthedocs.io/en/latest/
    # WORKS!
    print('=== Test 1 ===')
    
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
    
    print('\n=== Test 2 ===')
    
    tree = Tree()
    tree.addNode("Udo", parentName)

def main():
    logging.debug('Running main.')
    tests()

# If this file is called directly, as opposed to imported, do this:
if __name__ == '__main__':
    main()
