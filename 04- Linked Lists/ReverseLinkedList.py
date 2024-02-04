# input: 2 -> 4 -> 6 -> 1 -> None
# output: 1 -> 6 -> 4 -> 2

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    prev = None
    current = head 
    while current:
        # None
        nxt = current.next
        # 6
        current.next = prev
        # 1
        prev = current
        # None
        current = nxt
        # 1 -> 6 -> 4 -> 2
    return prev

def printLinkedList(head):
    string = ""
    while head:
        string += str(head.value)
        if head.next:
            string+=" -> "
        head = head.next

    return string

node = Node(2)
node.next = Node(4)
node.next.next = Node(6)
node.next.next.next = Node(1)

print(printLinkedList(reverseLinkedList(node)))
