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

'''
def swapNodeInPairs(head):
    if(head == None or head.next == None): return head

    tmp = head.next.next
    head.next.next = head
    head = head.next 
    head.next.next = swapNodeInPairs(tmp)

    return head
'''

'''
def swapNodePairs(head): #(1 - 2) - 4 - 6 - 8
    result = Node(-1)
    # -1
    current = result
    #true
    while head and head.next:
        # -1 -> 2 -> 1 -> 6 -> 4
        current.next = head.next
        current.next.next = head
        # 4
        current = current.next.next
        # None 
        head = head.next.next.next
        # 8
        head.next = head.next.next
    
    if head.next:
        current.next = head.next
    # -1 -> 2 -> 1 -> 6 -> 4 -> 8

    return result.next
'''

#1 - 2 - 4 - 6 - 8
def swapPairNode(head):
    # 0 - 1 
    dummy = Node(0, head)
    # 0 
    prev = dummy 
    # 1
    curr = head

    #true 
    while curr and curr.next:
        # 4 | 8
        nxtPair = curr.next.next
        # 2 | 6
        second = curr.next

        # 1 | 4
        second.next = curr
        # 4 | 8
        curr.next = nxtPair
        # 2 | 6
        prev.next = second

        # 1 | 4 
        prev = curr
        # 4 | 8
        curr = nxtPair

    return dummy.next

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)
list1.next.next.next = Node(6)
list1.next.next.next.next = Node(8)
list1.next.next.next.next.next = Node(3)

print(mostrarNodos(swapPairNode(list1)))
