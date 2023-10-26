#!/usr/bin/python3
"""Represents a node of a singly linked list."""


class Node:

    """Initializes a Node instance."""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    """Retrieves the data value of the node."""

    @property
    def data(self):
        return self.__data

    """Sets the data value of the node."""

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    """Retrieves the next node in the linked list."""

    @property
    def next_node(self):
        return self.__next_node

    """Sets the next node in the linked list."""

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


"""Represents a singly linked list."""


class SinglyLinkedList:
    """Initializes an empty SinglyLinkedList instance."""

    def __init__(self):
        self.__head = None

    """Inserts a new Node into the correct sorted position in linked list."""

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (
                    current.next_node is not None and
                    current.next_node.data < value
                    ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    """Returns a string representation of the linked list."""

    def __str__(self):
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
