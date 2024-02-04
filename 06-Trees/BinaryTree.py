class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.value
    

def inOrderTraversal(node: Node):
    # 1 / 2 / 4 / 7
    if node != None:
        # 2 / 4 / 7  
        inOrderTraversal(node.left)
        print(node.value, " ")
        '''
        7
        4
        2
        8
        5
        1
        3
        6
        '''
        inOrderTraversal(node.right)

    return

def preOrderTraversal(node: Node):
    if node != None:
        print(node.value, " ")
        preOrderTraversal(node.left)
        '''
        1
        2
        4
        7
        5
        8
        3
        6
        '''
        preOrderTraversal(node.right)
    
    return

def postOrderTraversal(node: Node):
    if node != None:
        postOrderTraversal(node.left)
        '''
        7
        4
        8
        5
        2
        6
        3
        1
        '''
        postOrderTraversal(node.right)
        print(node.value, " ")

    return

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)

root.left.left.left = Node(7)
root.left.right.left = Node(8)

print("IN ORDER TRAVERSAK")
inOrderTraversal(root)

print("PRE ORDER TRAVERSAL")
preOrderTraversal(root)

print("POST ORDER TRAVERSAL")
postOrderTraversal(root)
