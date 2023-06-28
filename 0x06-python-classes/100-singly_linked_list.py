#!/usr/bin/python3
""" Singly link list module """


class Node:
    """ Creates a Node """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Created a singly linked list """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value, None)

        if self.__head is None:
            new.next_node = self.__head
            self.__head = new
            return

        curr = self.__head
        prev = None

        while curr.next_node is not None:
            if value < curr.data:
                if prev is None:
                    new.next_node = self.__head
                    self.__head = new
                else:
                    prev.next_node = new
                    new.next_node = curr
                return
            prev = curr
            curr = curr.next_node

        if value <= curr.data:
            if prev is None:
                new.next_node = self.__head
                self.__head = new
            else:
                prev.next_node = new
                new.next_node = curr
        else:
            curr.next_node = new

    def __str__(self):
        list = []
        tmp = self.__head
        while tmp is not None:
            list.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(list)
