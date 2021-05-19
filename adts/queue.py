
class Queue:
    """
    Standard fifo queue, implemented w/ array
    Items are appended to the front O(n)
    Removed from the end O(1)
    """
    def __init__(self):
        self.items = []

    # add to 'front'
    def enqueue(self, item):
        self.items.insert(0, item)

    # rm from 'front'
    def remove(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)