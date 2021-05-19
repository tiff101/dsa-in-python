
from node import Node

class LinkedList:
    """
    An unordered list, with a 'head' reference, and a list chained by references to consecutive elements.
    Implemented using the Node class as an individual 'element'
    """

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        element = Node(data)
        element.setNext()