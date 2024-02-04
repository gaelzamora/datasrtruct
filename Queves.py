class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def __str__(self):
        return self.value
    
class MyQueve:
    first = None
    last = None

    def add(value):
        newLast = Node(value)
        if last:
            