#!/usr/bin/python3
"""
This module defines a SinglyLinkedList class that represents a singly linked list.
"""

class Node:
    """
    A class representing a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node with a given data and next_node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for next_node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
