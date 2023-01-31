#!/usr/bin/python3
"""
Node class
"""

class Node:
    """
    Creates a Node
    """
    def __init__(self, data, next_node=None):
        """
        Instantiates the Node class

        Args:
        @data: element in node
        @next_node: pointer to next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (isinstance(value, Node) or isinstance(value, None)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value



    class SinglyLinkedList:
        """
        Singly Linked List class
        """
        def __init__(self):
            return self.__head
            

    
