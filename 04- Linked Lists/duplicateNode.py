# Realiza una funcion que retorne una linked list de nodos ordenada con valores no duplicados Ejemplo:
# Input
# 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4 -> 4 
# Output
# 1 -> 2 -> 3 -> 4


class Node:
    def __init__(self, value, nxt = None):
        self.value = value
        self.next = nxt

    def __str__(self):
        self.value + self.nxt

def viewNodes(head):
    string = ""
    while head:
        string += str(head.value)
        if head.next:
            string += " -> "
        head = head.next

    return string

'''
p1 = head

    while p1:
        tmp = p1.next
        while p1.value == tmp.value:
            tmp = tmp.next
        p1.next = tmp
        p1 = p1.next

    return p1
'''

def duplicateNode(head):
    cur = head

    while cur:
        while cur.next and cur.value == cur.next.value:
            cur.next = cur.next.next
        cur = cur.next
        print(cur.value)

    return cur


list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(2)
list1.next.next.next = Node(3)
list1.next.next.next.next = Node(3)
list1.next.next.next.next.next = Node(3)
list1.next.next.next.next.next.next = Node(4)
list1.next.next.next.next.next.next.next = Node(4)
list1.next.next.next.next.next.next.next.next = Node(4)
list1.next.next.next.next.next.next.next.next.next = Node(5)

print(viewNodes(duplicateNode(list1)))