
class Deque:
    """
    Standard double ended queue, implemented w/ array
    """
    def __init__(self):
        self.items = []

    # add to 'front'
    def addTop(self, item):
        self.items.insert(0, item)

    # rm from 'front'
    def addTail(self, item):
        self.items.append(item)

    def rmTop(self, item):
        return self.items.pop(0)

    def rmTail(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)