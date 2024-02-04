class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value + self.next.value
    

def mostrarNodos(listNode):
    current = listNode
    string = ""
    while current != None:
        string += str(current.value)
        if current.next != None:
            string+=" -> "
        current = current.next

    print(string)

def sumNode(head):
    # 3 -> 5 -> 1 -> 8
    res = 0

    #true
    while head:
        # 17 
        res += head.value
        # None
        head = head.next

    return res

list1 = Node(3)
list1.next = Node(5)
list1.next.next = Node(1)
list1.next.next.next = Node(8)

print(sumNode(list1))