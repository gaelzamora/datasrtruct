class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value + self.next.value

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def appendToTail(self, value):
        if(self.head == None):
            self.head = Node(value)
            return
        current = self.head
        
        while current.next != None:
            current = current.next
        
        current.next = Node(value)
    
    def deleteNode(self, value):
        if(self.head == None): return
        if(self.head.value == value):
            self.head = self.head.next
            return
        
        current = self.head

        while current.next != None:
            if(current.next.value == value):
                current.next = current.next.next
                return
            current = current.next
        
    def viewNodes(self):
        view = ""
        current = self.head
        
        while current != None:
            view += str(current.value)
            if(current.next != None): view+=","
            current = current.next
            
        print(view)

'''listNodes = SingleLinkedList()
print(listNodes.viewNodes())
listNodes.appendToTail(5)
listNodes.appendToTail(6)
listNodes.appendToTail(8)
listNodes.appendToTail(9)
print(listNodes.viewNodes())
listNodes.deleteNode(8)
print(listNodes.viewNodes())
'''


'''def mergeTwoLists(list1, list2):
    # 2 4 7 10
    # 2 3 6
    aux = Node(-1) # -1 
    current = aux # -1

    while list1 != None and list2 != None:#True
        if(list1.value <= list2.value):# 7 <= 6
            current.next = list1 # -1 2 2 3 4
            list1 = list1.next # 7
        else:
            current.next = list2 # -1 2 2 3 4 6
            list2 = list2.next # None
        current = current.next # 6


    if(list1 == None): current.next = list2
    else: current.next = list1

    return aux.next'''

# 2 4 7 10, 2

'''def getTargetNode(head, target):
    p1 = head # 2
    p2 = head # 2

    for i in range(0,target): # 0 < 1
        if p1 == None: return None
        p1 = p1.next # 4

    while(p1 != None):
        p1 = p1.next # None
        p2 = p2.next # 10

    return p2.value'''

def mostrarNodos(listNode):
    current = listNode
    string = ""
    while current != None:
        string += str(current.value)
        if current.next != None:
            string+=" -> "
        current = current.next

    print(string)


# 2 -> 4 -> 1 | 6 -> 9 -> 1 -> 7
# 142 + 7196
# 7338
# 8 -> 3 -> 3 -> 7

def addTwoNumbers(list1, list2):
    result = Node(-1)
    current = result 
    carry = 0

    while list1 != None or list2 != None:
        # -1 -> 8 -> 3 -> 3 -> 7
        current.next = Node(-1)
        # -1
        current = current.next 
        # 0
        digit = carry 

        if list1 != None:
            # 2
            digit += list1.value 
            # None
            list1 = list1.next 

        if list2 != None:
            # 7
            digit += list2.value
            # None
            list2 = list2.next 

        # 0
        carry = digit // 10
        # 7
        digit = digit % 10 
        # 7
        current.value = digit  
    
    if carry > 0:
        current.next = Node(carry)
    
    return result.next

list1 = Node(2)
list1.next = Node(4)
list1.next.next = Node(1)

list2 = Node(6)
list2.next = Node(9)
list2.next.next = Node(1)
list2.next.next.next = Node(7)

print(mostrarNodos(addTwoNumbers(list1, list2)))

'''list2 = Node(2)
list2.next = Node(3)
list2.next.next = Node(6)'''

#print(getTargetNode(list1, 2))

#print(mostrarNodos(mergeTwoLists(list1, list2)))
