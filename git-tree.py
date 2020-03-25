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
    """
    Nodes in a tree. Each node consists of a *single parent* and a *list of children*. It has no limit on the number
    of children it can have. 
    """
    
    def __init__(self, name, parent = None):
        """
        Constructor to create a new Node

        Parameters:
            name (string):  the name of this node
            parent (Node):  the parent node of the node being created; note: obviously the parent node must already
                            exist in order to be passed in as a parameter here
            
        Returns:
            NA
        """

        self.name = name
        self.children = [] # initialize with an empty list of children
        self.setParent(parent)

    def setParent(self, parent):
        """
        Set or update the parent of this node

        Parameters:
            parent (Node):  the parent node of this node
        Returns:
            None
        """
        
        self.parent = parent
        if (parent is not None):
            self.parent.__addChild(self)

    def printChildren(self):
        """
        Print the names of the children this node has

        Parameters:
            None
        Returns:
            None
        """

        print("Printing {}'s children:".format(self.name))
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
    """
    A Tree consists of one or more Nodes (ideally 2+ or it's not really a tree) linked together via parent/child
    relationships. No circular relationships are allowed: ie: a node's parent cannot be its child, grandchild, 
    great grandchild, etc.
    """

    def __init__(self):
        """
        Constructor

        Parameters:
            None
        Returns:
            NA
        """
        # List of all nodes in the tree
        self.allNodes = []
        # List of all nodes in the tree *in the order* the nodes were added via `addNode()`; this is different from
        # the nodes contained in self.allNodes, and the order of the nodes in self.allNodes, because 
        # self.allNodes also includes *parent nodes* that were added consequently since they were specified as 
        # parameters passed to `addNode()` but they didn't already exist in the tree
        self.orderedNodes = []
        # A dictionary to map from a node name string to a node object; all nodes in the tree are in this
        # dict, so you may use it to determine whether or not a node with a given name exists in the tree
        self.nodeMap = {}

    def addOrUpdateNode(self, name, parent = None):
        """
        Add or update a node and its parent node, as required, to the tree.
        
        Details: If a node named "name" isn't already in the tree, create it and add it to the tree, setting its 
        parent node as well. If the specified parent node doesn't exist in the tree, also create it, setting its 
        parent node to `None`. If a node named "name" *is* already in the tree, simply update its parent node as
        specified. 
        
        Parameters:
            name (string):      the name of this node; note that only one node by any given name can exist in the 
                                tree at one time
            parent (string):    the *name* of the parent node for the node being created; the parent node will be
                                created if it doesn't already exist in the tree; see "Details" just above
        Returns:
            None
        """
        
        ############ PICK BACK UP HERE!
        
        # Each node name can only exist *once* in the tree, so first check to make sure this node name isn't already
        # in the tree!
        if (name in self.nodeMap):
            logging.error('Error: this node is already in the tree! name = {}; parent = {}'.format(name, parent))
            return
        
        # Create the parent node if it doesn't exist
        
        # Obtain the parent node using the parent node name if the parent node exists
        parentNode = None
        if (parent is not None):
            if (not parent in self.nodeMap):
                logging.error('Error: parent node must be created first! name = {}; parent = {}'.format(name, parent))
                return
            else:
                parentNode = self.nodeMap[parent]
        newNode = Node(name, parentNode)
        # add the newly-created node to the node map and node list
        self.nodeMap[name] = newNode 
        self.allNodes.append(newNode)

    def printChildren(self):
        """
        Print the names of all of the children of each node in this tree
        
        Parameters:
            None
        Returns:
            None
        """
        for node in self.allNodes:
            node.printChildren()

    def printTree(self):
        """
        Graphically print the tree
        
        Parameters:
            None
        Returns:
            None
        """
        pass

    def cascade(self):
        pass
# end of class GitTree

def tests():
    """
    Run some tests to ensure my classes (Node, Tree, etc) are working
    """
    
    # See if I can duplicate this behavior: https://anytree.readthedocs.io/en/latest/
    
    print('=== Test 1 ===') # WORKS!
    
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
    
#     print('\n=== Test 2 ===') # WORKS! OUTPUT IS IDENTICAL TO TEST 1!
#     
#     tree = Tree()
#     tree.addOrUpdateNode("Udo")
#     tree.addOrUpdateNode("Marc", parent="Udo")
#     tree.addOrUpdateNode("Lian", parent="Marc")
#     tree.addOrUpdateNode("Dan", parent="Udo")
#     tree.addOrUpdateNode("Jet", parent="Dan")
#     tree.addOrUpdateNode("Jan", parent="Dan")
#     tree.addOrUpdateNode("Joe", parent="Dan")
#     tree.printChildren()

def main():
    logging.debug('Running main.')
    tests()

# If this file is called directly, as opposed to imported, do this:
if __name__ == '__main__':
    main()
