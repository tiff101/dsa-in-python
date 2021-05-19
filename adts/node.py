
class Node:
    """
    Nodes have 2 properties: what's inside them (data) + a reference to the next node in sequence
    Useful for holding more than just basic data types
    Self-contained
    """
    def __init__(self, first_data):
        self.contents = first_data
        self.next = None

    # set
    def setContents(self, data):
        self.contents = data

    def setNext(self, ref):
        self.next = ref

    # getters
    def getNext(self):
        return self.next

    def getContents(self):
        return self.contents