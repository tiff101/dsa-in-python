
class Stack:
    """
    classic FILO stack. implemented w/ an array such that the first element is 0, 'top' of the stack is at the end
    i.e. push / pop operations occur at the last element
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # look at the most recently-added element only
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)